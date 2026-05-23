#!/usr/bin/env python3
"""
Generative art banner for sbookworm.github.io
Theme: "Flowing Embeddings" — abstract visualization of
high-dimensional vector fields projected to 2D, evoking LLM attention patterns.
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Circle as MplCircle
from matplotlib import font_manager as fm
from numpy.linalg import norm

# Chinese font
cjk_font = fm.FontProperties(
    fname="/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"
)
mono_font = fm.FontProperties(
    fname="/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"
)

np.random.seed(42)

W, H = 1400, 500

# ---------- perlin-like flow field ----------
def fbm(x, y, octaves=4):
    """Simple hash-based pseudo-Perlin noise."""
    val = 0
    amp = 1.0
    freq = 1.0
    norm_amp = 0.0
    for _ in range(octaves):
        val += amp * np.sin(freq * x * 0.017 + 1.3 * np.sin(freq * y * 0.013 + x * 0.009))
        val += amp * np.cos(freq * y * 0.019 + 0.7 * np.cos(freq * x * 0.011 + y * 0.008))
        norm_amp += amp
        amp *= 0.5
        freq *= 2.1
    return val / norm_amp

# ---------- figure ----------
fig = plt.figure(figsize=(14, 5), dpi=120)
ax = fig.add_axes((0, 0, 1, 1), frameon=False)
ax.set_xlim(0, W)
ax.set_ylim(0, H)
ax.axis('off')

# background gradient
bg = np.linspace(0, 1, 256).reshape(1, -1)
bg_cmap = LinearSegmentedColormap.from_list(
    "bg", ["#0d1117", "#161b22", "#1c2128"], N=256
)
ax.imshow(bg, extent=(0, W, 0, H), aspect="auto", cmap=bg_cmap, alpha=1.0, zorder=0)

# color palette — cyan/teal → orange → pink, evoking warmth+tech
PALETTE = [
    "#00d4ff",  # cyan
    "#0099cc",
    "#ff6b35",  # orange
    "#f7c59f",  # peach
    "#e84393",  # pink
    "#00cec9",  # teal
]

# ---------- flow field streamlines ----------
xs = np.linspace(0, W, 80)
ys = np.linspace(0, H, 40)
X, Y = np.meshgrid(xs, ys)

U = np.zeros_like(X)
V = np.zeros_like(Y)
for i in range(X.shape[0]):
    for j in range(X.shape[1]):
        nx = X[i, j] / W
        ny = Y[i, j] / H
        angle = fbm(nx * 3.5, ny * 3.5) * np.pi * 2
        strength = (fbm(nx * 2 + 5, ny * 2 + 5) + 1.5) * 0.5
        U[i, j] = np.cos(angle) * strength * 4
        V[i, j] = np.sin(angle) * strength * 4

stream_color = LinearSegmentedColormap.from_list(
    "stream", ["#00d4ff22", "#ff6b3522", "#e8439322"]
)
ax.streamplot(
    xs, ys, U, V,
    color=np.sqrt(U**2 + V**2),
    cmap=stream_color,
    linewidth=0.6,
    density=1.2,
    zorder=1,
)

# ---------- attention dot grid (like attention heads) ----------
n_heads = 12
head_positions = []
for h in range(n_heads):
    hx = W * (0.08 + 0.84 * (h % 4) / 3.0)
    hy = H * (0.15 + 0.70 * (h // 4) / 2.5)
    head_positions.append((hx, hy))

# draw "attention" arcs between heads
from numpy.random import uniform as rand
for _ in range(80):
    i1, i2 = np.random.randint(0, n_heads), np.random.randint(0, n_heads)
    if i1 == i2:
        continue
    x1, y1 = head_positions[i1]
    x2, y2 = head_positions[i2]
    alpha = 0.05 + 0.15 * np.random.rand()
    lw = 0.3 + 1.2 * np.random.rand()
    color = PALETTE[np.random.randint(0, len(PALETTE))]
    # bezier-ish arc
    mid_x = (x1 + x2) / 2 + (rand() - 0.5) * W * 0.3
    mid_y = (y1 + y2) / 2 + (rand() - 0.5) * H * 0.25 + H * 0.1
    t = np.linspace(0, 1, 80)
    bx = (1-t)**2*x1 + 2*(1-t)*t*mid_x + t**2*x2
    by = (1-t)**2*y1 + 2*(1-t)*t*mid_y + t**2*y2
    ax.plot(bx, by, color=color, alpha=alpha, lw=lw, zorder=2)

# draw head nodes
for i, (hx, hy) in enumerate(head_positions):
    r = 6 + 4 * np.sin(i * 1.3)
    circle = MplCircle(
        (hx, hy), r,
        color=PALETTE[i % len(PALETTE)], alpha=0.55, zorder=3
    )
    ax.add_patch(circle)
    ring = MplCircle(
        (hx, hy), r + 5 + 3 * np.sin(i * 0.9),
        color=PALETTE[i % len(PALETTE)], alpha=0.18, zorder=3
    )
    ax.add_patch(ring)

# ---------- floating particles / embedding vectors ----------
for _ in range(120):
    px = rand(0, W)
    py = rand(0, H)
    pr = 0.5 + rand(0, 2.5)
    color = PALETTE[np.random.randint(0, len(PALETTE))]
    alpha = 0.1 + rand(0, 0.35)
    circ = MplCircle((px, py), pr, color=color, alpha=alpha, zorder=4)
    ax.add_patch(circ)

# ---------- vertical subtle grid lines ----------
for gx in np.linspace(50, W - 50, 20):
    ax.axvline(gx, color="#ffffff", alpha=0.025, lw=0.5, zorder=0)

# ---------- title text ----------
ax.text(
    W / 2, H * 0.56,
    "Engineer's LLM Journey",
    ha="center", va="center",
    fontsize=28, fontweight="bold",
    color="#f0f6fc",
    fontfamily="monospace",
    zorder=10,
    alpha=0.92,
    fontproperties=mono_font,
)
ax.text(
    W / 2, H * 0.36,
    "读书  ·  编程  ·  思考",
    ha="center", va="center",
    fontsize=13,
    color="#8b949e",
    fontfamily="sans-serif",
    zorder=10,
    alpha=0.75,
    fontproperties=cjk_font,
)

# ---------- bottom tagline line ----------
ax.axhline(H * 0.18, xmin=0.05, xmax=0.95, color="#30363d", lw=0.8, alpha=0.6, zorder=5)

# ---------- output ----------
out_path = "/home/songli/sbookworm.github.io/assets/img/home-banner.png"
plt.savefig(out_path, dpi=150, bbox_inches="tight", pad_inches=0, facecolor="#0d1117")
plt.close()
print(f"Saved: {out_path}")
