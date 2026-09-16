"""Wahana uji SpeedyBee Bee35. Tampak atas dan tampak samping, satuan cm."""
import sys, os, math; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, FancyArrowPatch
from gaya_gambar import ukur, simpan, TEBAL, TIPIS, PUTUS, ABU, ABU_MUDA

W, L, H   = 25.0, 21.0, 8.0
DUCT      = 10.5
DX, DY    = (W-DUCT)/2, (L-DUCT)/2
SPINE     = 2*DX - DUCT
TAG       = 10.0
RISER     = 7.0

fig, (ax, bx) = plt.subplots(1, 2, figsize=(7.4, 3.7),
                             gridspec_kw={"width_ratios": [1.18, 1]})

def balon(a, huruf, titik, dxy, r=0.95):
    px, py = titik[0]+dxy[0], titik[1]+dxy[1]
    a.annotate("", titik, (px, py), arrowprops=dict(arrowstyle="-", color="black",
               lw=TIPIS, shrinkA=0, shrinkB=r*5.5))
    a.add_patch(Circle((px, py), r, fc="white", ec="black", lw=0.8, zorder=10))
    a.text(px, py, huruf, ha="center", va="center", fontsize=7.5,
           fontweight="bold", zorder=11)

# ───────── TAMPAK ATAS ─────────
ax.add_patch(Rectangle((-W/2, -L/2), W, L, fc="none", ec=ABU, lw=TIPIS, ls=PUTUS))
for sx in (-1, 1):
    for sy in (-1, 1):
        c = (sx*DX, sy*DY)
        ax.add_patch(Circle(c, DUCT/2, fc="white", ec="black", lw=TEBAL, zorder=3))
        ax.add_patch(Circle(c, DUCT/2-1.2, fc="white", ec="black", lw=TIPIS, zorder=3))
        ax.add_patch(Circle(c, 1.4, fc=ABU_MUDA, ec="black", lw=TIPIS, zorder=4))
ax.add_patch(Rectangle((-SPINE/2, -L/2+1), SPINE, L-2, fc="white", ec="black",
                       lw=TEBAL, zorder=5))
ax.add_patch(Rectangle((-1.5, -1.5), 3.0, 3.0, fc=ABU_MUDA, ec="black", lw=TIPIS, zorder=6))
ax.add_patch(Rectangle((-1.0, 3.5), 2.0, 1.7, fc=ABU_MUDA, ec="black", lw=TIPIS, zorder=6))
ax.add_patch(Rectangle((-1.5, -6.0), 3.0, 2.8, fc=ABU_MUDA, ec="black", lw=TIPIS, zorder=6))
ax.add_patch(Rectangle((-TAG/2, -TAG/2), TAG, TAG, fc="none", ec="black",
                       lw=1.1, ls=(0,(4,2.5)), zorder=8))
for sx in (-1, 1):
    px, py = sx*(W/2-2.2), L/2-2.2
    ax.add_patch(Rectangle((px-0.8, py-0.6), 1.6, 1.2, fc=ABU_MUDA, ec="black",
                           lw=TIPIS, zorder=9))
    ang = math.radians(90 - sx*45)
    ax.plot([px, px+7.0*math.cos(ang)], [py, py+7.0*math.sin(ang)],
            color=ABU, lw=TIPIS, ls=(0,(4,2)), zorder=2)
ax.add_patch(FancyArrowPatch((-W/2-7.6, -2.0), (-W/2-7.6, 2.0), arrowstyle="-|>",
                             mutation_scale=9, lw=0.9, color="black"))
ax.text(-W/2-8.2, 0, "arah maju", fontsize=8, rotation=90, va="center", ha="right")

ukur(ax, (-W/2, -L/2), (W/2, -L/2), "25,0", offset=-3.2, pad=0.7)
ukur(ax, (W/2, -L/2), (W/2, L/2), "21,0", offset=3.2, pad=0.7)
ukur(ax, (-SPINE/2, L/2-1), (SPINE/2, L/2-1), "4,0", offset=2.4, pad=0.5, fs=8)

# tampak atas: hanya geometri saluran, sensor, dan jejak penanda
balon(ax, "A", (DX+DUCT/2*0.70, DY+DUCT/2*0.70), (4.6, 3.2))
balon(ax, "E", (-(W/2-2.2), L/2-2.2), (-4.8, 3.0))
balon(ax, "F", (-TAG/2, -TAG/2), (-5.2, -4.4))
ax.set_xlim(-W/2-11, W/2+9); ax.set_ylim(-L/2-5.0, L/2+5.4)
ax.set_aspect("equal"); ax.axis("off")

# ───────── TAMPAK SAMPING ─────────
lapis = [(0.0, 2.6, "white", TEBAL),      # rangka + saluran
         (2.6, 2.2, ABU_MUDA, TIPIS),     # stack FC/ESC
         (4.8, 0.9, ABU_MUDA, TIPIS),     # companion computer
         (5.7, 2.3, ABU_MUDA, TIPIS)]     # baterai
lebar = [W, 8.0, 4.0, 10.0]
for (y0, h, fc, lw), lb in zip(lapis, lebar):
    bx.add_patch(Rectangle((-lb/2, y0), lb, h, fc=fc, ec="black", lw=lw))
for sx in (-1, 1):
    bx.plot([sx*3.5, sx*3.5], [H, H+RISER], color="black", lw=1.4)
bx.add_patch(Rectangle((-TAG/2, H+RISER), TAG, 0.6, fc="white", ec="black", lw=TEBAL))
bx.plot([-W/2-2, W/2+3], [0, 0], color=ABU, lw=TIPIS, ls=(0,(1,2)))

ukur(bx, (W/2, 0), (W/2, H), "8,0", offset=3.0, pad=0.6)
ukur(bx, (TAG/2, H), (TAG/2, H+RISER), "7,0", offset=2.2, pad=0.6)

balon(bx, "B", (-4.0, 3.7), (-8.2, -1.8))
balon(bx, "C", (-2.0, 5.25), (-10.2, 1.4))
balon(bx, "D", (-5.0, 6.8), (-9.6, 4.6))
balon(bx, "F", (TAG/2*0.55, H+RISER+0.6), (5.8, 2.2))
balon(bx, "G", (-3.5, H+RISER*0.55), (-7.6, 1.2))
bx.set_xlim(-W/2-13, W/2+9); bx.set_ylim(-3.6, H+RISER+5.4)
bx.set_aspect("equal"); bx.axis("off")

ax.text(0, -L/2-4.4, "(a) tampak atas", ha="center", va="top", fontsize=8.5)
bx.text(0, -3.4, "(b) tampak samping", ha="center", va="top", fontsize=8.5)

ket = ("A  saluran propeler (4×)     B  stack flight controller dan ESC     "
       "C  companion computer XIAO ESP32-S3     D  baterai LiPo\n"
       "E  sensor jarak (2×, diagonal 45°)     F  penanda AprilTag 10 × 10 cm     "
       "G  tiang penyangga penanda")
fig.text(0.5, 0.005, ket, ha="center", va="bottom", fontsize=7.8, linespacing=1.8)
plt.tight_layout(rect=[0, 0.13, 1, 1])
simpan(fig, "sketsa-wahana")
print(f"jalur datar bebas saluran = {SPINE:.1f} cm, penanda dibutuhkan {TAG:.0f} cm")
