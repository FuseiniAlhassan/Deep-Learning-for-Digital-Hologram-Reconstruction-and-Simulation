import os
os.makedirs("outputs", exist_ok=True)
plt.savefig(os.path.join("outputs", "figure.png"))
