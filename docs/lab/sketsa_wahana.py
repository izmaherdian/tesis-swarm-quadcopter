"""Sketsa skala wahana quadcopter (SpeedyBee Bee35 cinewhoop).

Menghasilkan tulisan/proposal/figures/sketsa-wahana.png. Satuan sentimeter.
Dimensi luar dari pengukuran lapangan (docs/lab/foto/06); tata letak komponen
dari foto 09 (tampak atas), 10 (tampak bawah), dan 11 (tampak samping).
"""
import os, math
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, FancyArrowPatch, Wedge

W, L, H = 25.0, 21.0, 8.0     # lebar, panjang, tinggi (dengan baterai)
DUCT_OD = 10.5
DX, DY  = (W-DUCT_OD)/2, (L-DUCT_OD)/2
SPINE_W = 2*DX - DUCT_OD      # celah bebas antara pasangan duct kiri & kanan
TAG     = 10.0

fig, (ax, bx) = plt.subplots(1, 2, figsize=(14.5, 7.4),
                             gridspec_kw={"width_ratios": [1.25, 1]})

# ══════════ TAMPAK ATAS ══════════
ax.add_patch(Rectangle((-W/2, -L/2), W, L, fc="none", ec="#999", lw=1.2, ls=(0,(5,4))))
for sx in (-1, 1):
    for sy in (-1, 1):
        cxd, cyd = sx*DX, sy*DY
        ax.add_patch(Circle((cxd, cyd), DUCT_OD/2, fc="#F2D24B", ec="#8A7420", lw=1.6, zorder=2))
        ax.add_patch(Circle((cxd, cyd), DUCT_OD/2-1.1, fc="#4A4A4A", ec="#333", lw=1, zorder=3))
        ax.add_patch(Circle((cxd, cyd), 1.5, fc="#222", ec="k", lw=1, zorder=4))

# spine tengah (satu-satunya area datar bebas duct)
ax.add_patch(Rectangle((-SPINE_W/2, -L/2+1), SPINE_W, L-2, fc="#2B2B2B",
                       ec="k", lw=1.2, zorder=5))
ax.add_patch(Rectangle((-1.6, -1.6), 3.2, 3.2, fc="#1B9AAA", ec="k", lw=1, zorder=6))
ax.text(0, 0, "FC\nESC", ha="center", va="center", fontsize=6, color="w",
        fontweight="bold", zorder=7)
ax.add_patch(Rectangle((-1.1, 3.4), 2.2, 1.8, fc="#EF476F", ec="k", lw=1, zorder=6))
ax.text(0, 4.3, "ESP32", ha="center", va="center", fontsize=5.2, color="w",
        fontweight="bold", zorder=7)
ax.add_patch(Rectangle((-1.6, -6.2), 3.2, 3.0, fc="#7B68EE", ec="k", lw=1, zorder=6))
ax.text(0, -4.7, "BAT", ha="center", va="center", fontsize=5.5, color="w",
        fontweight="bold", zorder=7)

# penanda AprilTag 10 cm -> menonjolkan tumpang tindih dengan duct
ax.add_patch(Rectangle((-TAG/2, -TAG/2), TAG, TAG, fc="#C1121F", alpha=.20,
                       ec="#C1121F", lw=2.4, ls=(0,(4,3)), zorder=8))
ax.annotate(f"AprilTag {TAG:.0f} cm\n(menumpang di atas duct)",
            (TAG/2, TAG/2), (W/2+3.2, L/2-1.5), fontsize=8.5, color="#C1121F",
            fontweight="bold", ha="left", va="center", zorder=10,
            arrowprops=dict(arrowstyle="->", color="#C1121F", lw=1.4))

# sensor jarak 45 derajat di dua sudut depan
for sx in (-1, 1):
    px, py = sx*(W/2-2.0), L/2-2.0
    ax.add_patch(Rectangle((px-0.9, py-0.7), 1.8, 1.4, fc="#06D6A0", ec="k",
                           lw=1, zorder=9))
    ang = math.radians(90 - sx*45)
    ax.add_patch(Wedge((px, py), 7.5, math.degrees(ang)-13, math.degrees(ang)+13,
                       fc="#06D6A0", alpha=.22, ec="none", zorder=1))
    ax.annotate("", (px+7.5*math.cos(ang), py+7.5*math.sin(ang)), (px, py),
                arrowprops=dict(arrowstyle="-|>", color="#06938C", lw=1.6))
ax.text(0, L/2+5.2, "2× sensor jarak, diagonal $\\theta = 45°$", ha="center",
        fontsize=8.5, color="#06938C", fontweight="bold")

ax.annotate("", (0, L/2+2.2), (0, L/2+0.4),
            arrowprops=dict(arrowstyle="-|>", color="k", lw=2.2, mutation_scale=18))
ax.text(1.0, L/2+1.4, "arah maju", fontsize=8, va="center")

def d(x1,y1,x2,y2,t,rot=0,c="#C1121F"):
    ax.annotate("", (x2,y2), (x1,y1), arrowprops=dict(arrowstyle="<->", color=c, lw=1.6))
    ax.text((x1+x2)/2, (y1+y2)/2, t, ha="center", va="center", fontsize=9,
            color=c, fontweight="bold", rotation=rot,
            bbox=dict(fc="w", ec=c, lw=1, boxstyle="round,pad=0.2"))
d(-W/2, -L/2-2.6, W/2, -L/2-2.6, "25 cm")
d(W/2+2.6, -L/2, W/2+2.6, L/2, "21 cm", rot=90)
ax.annotate("", (SPINE_W/2, -L/2-0.8), (-SPINE_W/2, -L/2-0.8),
            arrowprops=dict(arrowstyle="<->", color="#8A0F16", lw=1.6))
ax.annotate(f"celah datar bebas duct\nhanya {SPINE_W:.0f} cm — tag {TAG:.0f} cm\ntidak muat tanpa tiang",
            (0, -L/2-0.8), (-W/2-4.5, -L/2-4.2), fontsize=8, color="#8A0F16",
            fontweight="bold", ha="left", va="center",
            arrowprops=dict(arrowstyle="->", color="#8A0F16", lw=1.4))

ax.set_xlim(-W/2-10, W/2+13); ax.set_ylim(-L/2-7.5, L/2+7)
ax.set_aspect("equal"); ax.axis("off")
ax.set_title("Tampak Atas", fontsize=12, fontweight="bold")

# ══════════ TAMPAK SAMPING ══════════
RISER = 7.0
bx.add_patch(Rectangle((-W/2, 0), W, 2.6, fc="#CFCFCF", ec="k", lw=1.4))
bx.text(0, 1.3, "rangka + duct", ha="center", va="center", fontsize=8)
bx.add_patch(Rectangle((-4, 2.6), 8, 2.2, fc="#1B9AAA", ec="k", lw=1.2))
bx.text(0, 3.7, "stack FC / ESC", ha="center", va="center", fontsize=7.5, color="w",
        fontweight="bold")
bx.add_patch(Rectangle((-5, 4.8), 10, 3.2, fc="#7B68EE", ec="k", lw=1.2))
bx.text(0, 6.4, "baterai LiPo", ha="center", va="center", fontsize=7.5, color="w",
        fontweight="bold")
for sx in (-1, 1):
    bx.plot([sx*3.5, sx*3.5], [H, H+RISER], color="#555", lw=3, solid_capstyle="round")
bx.add_patch(Rectangle((-TAG/2, H+RISER), TAG, 0.5, fc="#C1121F", ec="k", lw=1.4))
bx.text(0, H+RISER+1.6, f"pelat AprilTag {TAG:.0f} cm", ha="center", fontsize=9,
        color="#C1121F", fontweight="bold")
bx.annotate("", (-TAG/2-1.6, H), (-TAG/2-1.6, H+RISER),
            arrowprops=dict(arrowstyle="<->", color="#555", lw=1.5))
bx.text(-TAG/2-2.4, H+RISER/2, f"tiang\n±{RISER:.0f} cm", ha="right", va="center",
        fontsize=7.5, color="#555")
bx.annotate("", (W/2+1.8, 0), (W/2+1.8, H),
            arrowprops=dict(arrowstyle="<->", color="#C1121F", lw=1.6))
bx.text(W/2+2.6, H/2, "8 cm", fontsize=9, color="#C1121F", fontweight="bold",
        rotation=90, va="center")
bx.plot([-W/2-2, W/2+4], [0,0], color="#888", lw=1, ls=":")
bx.text(0, -1.4, "Tiang menaikkan penanda di atas mulut duct\nagar aliran udara masuk tidak tertutup.",
        ha="center", va="top", fontsize=8, color="#444", style="italic")

bx.set_xlim(-W/2-6, W/2+6); bx.set_ylim(-5, H+RISER+4)
bx.set_aspect("equal"); bx.axis("off")
bx.set_title("Tampak Samping", fontsize=12, fontweight="bold")

fig.suptitle("Wahana Uji — SpeedyBee Bee35 (cinewhoop ber-duct), gambar berskala, satuan cm",
             fontsize=13, fontweight="bold", y=0.985)
plt.tight_layout(rect=[0,0.02,1,0.955])
OUT = "tulisan/proposal/figures/sketsa-wahana.png"
os.makedirs(os.path.dirname(OUT), exist_ok=True)
plt.savefig(OUT, dpi=135, bbox_inches="tight", facecolor="w")
print(f"lebar x panjang x tinggi : {W} x {L} x {H} cm")
print(f"diameter duct            : {DUCT_OD} cm, pusat di (±{DX:.2f}, ±{DY:.2f})")
print(f"celah bebas antar-duct   : {SPINE_W:.1f} cm  <-- area datar satu-satunya")
print(f"tag dibutuhkan           : {TAG:.0f} cm  -> {TAG/SPINE_W:.1f}x lebih lebar dari celah")
