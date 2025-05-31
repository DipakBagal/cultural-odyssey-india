## 
import streamlit as st
import requests
import os

HF_TOKEN = os.getenv("HF_TOKEN") or st.secrets["hf"]["token"]
API_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"


headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}

def query_hf(prompt, history=[]):
    full_prompt = (
        "<|system|>You are a helpful assistant specialized in Indian culture, arts, history, and tourism planning.<|end|>\n"
    )
    for user, assistant in history:
        full_prompt += f"<|user|>{user}<|end|>\n<|assistant|>{assistant}<|end|>\n"
    full_prompt += f"<|user|>{prompt}<|end|>\n<|assistant|>"

    response = requests.post(API_URL, headers=headers, json={
        "inputs": full_prompt,
        "parameters": {"max_new_tokens": 256, "return_full_text": False}
    })

    if response.status_code != 200:
        return f"⚠️ Error: {response.status_code} - {response.text}"

    output = response.json()
    return output[0]['generated_text'].split("<|assistant|>")[-1].strip()

st.title("🧠 Cultural Chat Assistant (Hugging Face GenAI)")

if "history" not in st.session_state:
    st.session_state.history = []

for user, assistant in st.session_state.history:
    st.chat_message("user").markdown(user)
    st.chat_message("assistant").markdown(assistant)

query = st.chat_input("Ask about Indian art, a place, or plan a trip...")

if query:
    st.chat_message("user").markdown(query)

    with st.spinner("Asking the cultural oracle..."):
        reply = query_hf(query, st.session_state.history)

    st.chat_message("assistant").markdown(reply)
    st.session_state.history.append((query, reply))
