import pandas as pd
import matplotlib.pyplot as plt

# --- your existing data prep ---
df = pd.read_csv("iip_wrt_prevyr.csv")
df.columns = df.columns.str.strip()

df["Year"] = df["Year"].str[:4].astype(int)

cols = ["Mining", "Manufacturing", "Electricity", "General"]
df[cols] = df[cols].apply(pd.to_numeric, errors="coerce")

df = df.set_index("Year")

# --- colors (soft pastel like your image) ---
colors = ["#6baed6", "#e34a33", "#fc8d59", "#fdd49e"]

# --- plot ---
ax = df.plot(
    kind="bar",
    stacked=True,
    color=colors,
    alpha=0.85,
    figsize=(10, 5)
)

# --- styling ---
# floating axes
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# create that clean separation
ax.spines["left"].set_position(("outward", 9))
ax.spines["bottom"].set_position(("outward", 9))

# thin lines (important for that look)
ax.spines["left"].set_linewidth(0.8)
ax.spines["bottom"].set_linewidth(0.8)
# baseline at 0
plt.axhline(0, color="black", linewidth=0.8, linestyle="--", alpha=0.7)

# grid (only horizontal)
plt.grid(axis="y", linestyle="--", alpha=0.4)

# labels & title
plt.title("IIP GROWTH RATE FOR INDIA", fontsize=14)
plt.xlabel("Financial Year")
plt.ylabel("IIP Growth Rate\nw.r.t Prev. Year")

# rotate x labels
plt.xticks(rotation=90)

# legend inside
plt.legend(loc="upper left", frameon=True, ncols=2)

plt.tight_layout()
plt.show()
