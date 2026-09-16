"""Denah arena uji pada koridor PTIO ITB. Satuan meter, gambar berskala."""
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, FancyArrowPatch
from gaya_gambar import ukur, penunjuk, simpan, TEBAL, TIPIS, PUTUS, ABU, ABU_MUDA

W, L          = 2.70, 7.20          # lebar koridor, panjang terliput
KOL_X, KOL_W, KOL_D = 3.30, 0.60, 0.79
CH_L, CELAH   = 1.80, 0.90
CH_X0         = (L - CH_L) / 2
BOX_D         = W - KOL_D - CELAH
D             = 0.25                # diameter wahana
k             = 0.90
TOPO          = [(1,0), (0,-0.5), (0,0.5), (-1,1), (-1,-1)]

fig, ax = plt.subplots(figsize=(7.2, 4.4))

# dinding koridor
for y in (0, W):
    ax.plot([0, L], [y, y], color="black", lw=TEBAL, solid_capstyle="butt", zorder=5)

# rintangan: kolom (arsiran rapat) dan dus (arsiran renggang)
ax.add_patch(Rectangle((KOL_X, W-KOL_D), KOL_W, KOL_D, fc="white", ec="black",
                       lw=TEBAL, hatch="/////", zorder=6))
for x0, w in ((CH_X0, KOL_X-CH_X0), (KOL_X+KOL_W, CH_X0+CH_L-KOL_X-KOL_W)):
    ax.add_patch(Rectangle((x0, W-KOL_D), w, KOL_D, fc="white", ec="black",
                           lw=TEBAL, hatch="///", zorder=6))
ax.add_patch(Rectangle((CH_X0, 0), CH_L, BOX_D, fc="white", ec="black",
                       lw=TEBAL, hatch="///", zorder=6))

# sumbu lintasan
ax.plot([0, L], [W/2, W/2], color=ABU, lw=TIPIS, ls=(0,(8,3,1,3)), zorder=2)

# liputan kamera — kurung tipis di atas denah
for x0, x1, y in ((0, 4.80, W+0.44), (2.40, 7.20, W+0.82)):
    ax.plot([x0, x0, x1, x1], [y-0.08, y, y, y-0.08], color="black", lw=TIPIS)
ax.text(2.40, W+0.48, "liputan kamera 1", ha="center", va="bottom", fontsize=8)
ax.text(4.80, W+0.86, "liputan kamera 2", ha="center", va="bottom", fontsize=8)
ax.annotate("", (4.80, W+0.16), (2.40, W+0.16),
            arrowprops=dict(arrowstyle="<|-|>", mutation_scale=7, lw=TIPIS, color=ABU))
ax.text(3.60, W+0.18, "tumpang tindih 2,40", ha="center", va="bottom",
        fontsize=7.5, color=ABU)

# formasi V
cx, cy = 1.15, W/2
for i, (dx, dy) in enumerate(TOPO):
    x, y = cx+dx*k, cy+dy*k
    ax.add_patch(Circle((x, y), D/2, fc="white", ec="black", lw=0.9, zorder=8))
    ax.text(x, y, str(i+1), ha="center", va="center", fontsize=6.5, zorder=9)

# tailgating — agen 1 memimpin di sisi kanan sesuai arah gerak
ygap = BOX_D + CELAH/2
for i in range(5):
    x = CH_X0 + 0.18 + i*0.38
    ax.add_patch(Circle((x, ygap), D/2, fc=ABU_MUDA, ec="black", lw=0.9, zorder=8))
    ax.text(x, ygap, str(5-i), ha="center", va="center", fontsize=6.5, zorder=9)

# arah gerak
ax.add_patch(FancyArrowPatch((0.25, W-0.20), (1.25, W-0.20), arrowstyle="-|>",
                             mutation_scale=9, lw=0.9, color="black"))
ax.text(1.34, W-0.20, "arah gerak", fontsize=8, va="center")

# balon penunjuk
def balon(huruf, titik, dxy):
    px, py = titik[0]+dxy[0], titik[1]+dxy[1]
    ax.annotate("", titik, (px, py),
                arrowprops=dict(arrowstyle="-", color="black", lw=TIPIS,
                                shrinkA=0, shrinkB=7))
    ax.add_patch(Circle((px, py), 0.135, fc="white", ec="black", lw=0.8, zorder=10))
    ax.text(px, py, huruf, ha="center", va="center", fontsize=7.5,
            fontweight="bold", zorder=11)

balon("A", (KOL_X+KOL_W/2, W-KOL_D*0.80), (1.62, -0.30))
balon("B", (CH_X0+CH_L*0.25, BOX_D*0.72), (-1.28, 0.22))
balon("C", (cx-0.55, cy-k*0.55),          (-0.95, -0.50))
balon("D", (CH_X0+CH_L-0.30, ygap+D/2),   (1.55,  0.62))

ket = ("A  kolom bangunan, 0,60 × 0,79 m        "
       "B  dus rintangan, 1,80 × 1,01 m\n"
       "C  formasi V, bentang lateral 2,05 m     "
       "D  formasi mengekor, agen 1 memimpin")
ax.text(L/2, -1.28, ket, ha="center", va="top", fontsize=8, linespacing=1.7)

# ukuran
ukur(ax, (0, 0), (L, 0), "7,20", offset=-0.78)
ukur(ax, (L, 0), (L, W), "2,70", offset=0.38)
ukur(ax, (CH_X0, 0), (CH_X0+CH_L, 0), "1,80", offset=-0.34)
ukur(ax, (CH_X0, BOX_D), (CH_X0, BOX_D+CELAH), "0,90", offset=-0.26)

ax.set_xlim(-1.35, L+1.15); ax.set_ylim(-2.15, W+1.32)
ax.set_aspect("equal"); ax.axis("off")
simpan(fig, "sketsa-arena")
