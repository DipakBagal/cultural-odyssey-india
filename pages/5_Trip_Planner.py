import streamlit as st

st.title("🧳 Cultural Trip Planner")

interest = st.selectbox("Choose your interest", ["Dance", "Craft", "Spiritual", "Festival"])
season = st.selectbox("Preferred season", ["Winter", "Monsoon", "Summer"])

recommendations = {
    "Dance": "Visit Tamil Nadu in December for the Natyanjali Dance Festival.",
    "Craft": "Explore Kutch, Gujarat in January for Rann Utsav and local artisans.",
    "Spiritual": "Try Rishikesh during spring for yoga and Ganga aarti.",
    "Festival": "Go to Assam in April for Bihu and cultural immersion."
}

st.success(recommendations[interest])
st.image(f"https://source.unsplash.com/800x400/?{interest},india", use_column_width=True)