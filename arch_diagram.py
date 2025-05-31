# Re-run the architecture diagram generation after environment reset

import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Set up figure and axis
fig, ax = plt.subplots(figsize=(12, 8))
ax.set_xlim(0, 10)
ax.set_ylim(0, 12)
ax.axis('off')

# Draw components
components = {
    "Snowflake DB": (1, 10, 3, 1.5),
    "Streamlit App": (4, 8, 5, 3),
    "Prophet Forecasting": (4.2, 6, 2.5, 1),
    "Folium Maps": (6.8, 6, 2.5, 1),
    "Altair Charts": (5.5, 9, 3.3, 1),
    "HF GenAI API": (1, 5.5, 3, 1),
    "User Interface": (4, 2, 5, 1.2)
}

for label, (x, y, w, h) in components.items():
    ax.add_patch(patches.Rectangle((x, y), w, h, edgecolor='black', facecolor='#f2f2f2'))
    ax.text(x + w/2, y + h/2, label, ha='center', va='center', fontsize=10, fontweight='bold')

# Arrows from Snowflake
ax.annotate('', xy=(4, 10.75), xytext=(3.9, 10.75), arrowprops=dict(arrowstyle="->"))
ax.annotate('', xy=(5.5, 9), xytext=(3.9, 10.75), arrowprops=dict(arrowstyle="->"))
ax.annotate('', xy=(5, 8), xytext=(3.9, 10.75), arrowprops=dict(arrowstyle="->"))

# Arrows from Streamlit App
ax.annotate('', xy=(6.5, 8), xytext=(6.5, 7), arrowprops=dict(arrowstyle="->"))
ax.annotate('', xy=(5.3, 8), xytext=(5.3, 7), arrowprops=dict(arrowstyle="->"))
ax.annotate('', xy=(6.5, 8), xytext=(6.5, 3.2), arrowprops=dict(arrowstyle="->"))
ax.annotate('', xy=(2.5, 5.5), xytext=(5.5, 3.2), arrowprops=dict(arrowstyle="->"))

# Arrows into UI
ax.annotate('', xy=(6.5, 2), xytext=(6.5, 1), arrowprops=dict(arrowstyle="->"))
ax.text(5.5, 0.5, "User Interaction (Browser)", fontsize=9, ha='center')

plt.tight_layout()
image_path = "data/cultural_odyssey_architecture_diagram.png"
plt.savefig(image_path, dpi=300)
plt.show()

image_path
