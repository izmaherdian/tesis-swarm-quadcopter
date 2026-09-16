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

fig, ax = plt.subplots(figsize=(7.4, 4.5))

# lantai koridor
ax.add_patch(Rectangle((0, 0), L, W, fc="#f8fafc", ec="none", zorder=0))

# zona liputan kamera (transparan berwarna)
# Kamera 1 (biru langit lembut)
ax.add_patch(Rectangle((0, 0), 4.80, W, fc="#0284c7", alpha=0.08, ec="none", zorder=1))
# Kamera 2 (indigo lembut)
ax.add_patch(Rectangle((2.40, 0), 4.80, W, fc="#6366f1", alpha=0.08, ec="none", zorder=1))

# dinding koridor
for y in (0, W):
    ax.plot([0, L], [y, y], color="#0f172a", lw=TEBAL, solid_capstyle="butt", zorder=5)

# rintangan: kolom beton A (abu-abu beton dengan arsiran rapat)
ax.add_patch(Rectangle((KOL_X, W-KOL_D), KOL_W, KOL_D, fc="#cbd5e1", ec="#334155",
                       lw=TEBAL, hatch="/////", zorder=6))

# rintangan: dus kardus B (warna karton cokelat/oranye muda dengan arsiran)
for x0, w in ((CH_X0, KOL_X-CH_X0), (KOL_X+KOL_W, CH_X0+CH_L-KOL_X-KOL_W)):
    ax.add_patch(Rectangle((x0, W-KOL_D), w, KOL_D, fc="#fed7aa", ec="#c2410c",
                           lw=TEBAL, hatch="///", zorder=6))
ax.add_patch(Rectangle((CH_X0, 0), CH_L, BOX_D, fc="#fed7aa", ec="#c2410c",
                       lw=TEBAL, hatch="///", zorder=6))

# sumbu lintasan
ax.plot([0, L], [W/2, W/2], color="#94a3b8", lw=TIPIS, ls=(0,(8,3,1,3)), zorder=2)

# liputan kamera — kurung berwarna di atas denah
# Kamera 1
ax.plot([0, 0, 4.80, 4.80], [W+0.36, W+0.44, W+0.44, W+0.36], color="#0284c7", lw=TIPIS*1.2)
ax.text(2.40, W+0.48, "liputan kamera 1 (0,00 -- 4,80 m)", ha="center", va="bottom",
        fontsize=7.8, color="#0369a1", fontweight="semibold")

# Kamera 2
ax.plot([2.40, 2.40, 7.20, 7.20], [W+0.74, W+0.82, W+0.82, W+0.74], color="#4f46e5", lw=TIPIS*1.2)
ax.text(4.80, W+0.86, "liputan kamera 2 (2,40 -- 7,20 m)", ha="center", va="bottom",
        fontsize=7.8, color="#4338ca", fontweight="semibold")

# Panah tumpang tindih
ax.annotate("", (4.80, W+0.16), (2.40, W+0.16),
            arrowprops=dict(arrowstyle="<|-|>", mutation_scale=8, lw=TIPIS*1.2, color="#b45309"))
ax.text(3.60, W+0.19, "daerah tumpang tindih liputan (2,40 m)", ha="center", va="bottom",
        fontsize=7.5, color="#92400e", fontweight="semibold",
        bbox=dict(fc="#fffbeb", ec="#fcd34d", pad=1.2, lw=0.5, boxstyle="round,pad=0.2"))

# formasi V (biru)
cx, cy = 1.15, W/2
for i, (dx, dy) in enumerate(TOPO):
    x, y = cx+dx*k, cy+dy*k
    ax.add_patch(Circle((x, y), D/2, fc="#dbeafe", ec="#1d4ed8", lw=1.0, zorder=8))
    ax.text(x, y, str(i+1), ha="center", va="center", fontsize=7.0,
            fontweight="bold", color="#1e40af", zorder=9)

# tailgating / mengekor (hijau zamrud) — agen 1 memimpin di sisi kanan
ygap = BOX_D + CELAH/2
for i in range(5):
    x = CH_X0 + 0.18 + i*0.38
    ax.add_patch(Circle((x, ygap), D/2, fc="#d1fae5", ec="#059669", lw=1.0, zorder=8))
    ax.text(x, ygap, str(5-i), ha="center", va="center", fontsize=7.0,
            fontweight="bold", color="#065f46", zorder=9)

# arah gerak
ax.add_patch(FancyArrowPatch((0.25, W-0.20), (1.25, W-0.20), arrowstyle="-|>",
                             mutation_scale=9, lw=1.0, color="#0f172a"))
ax.text(1.34, W-0.20, "arah gerak", fontsize=8, va="center", fontweight="semibold", color="#0f172a")

# balon penunjuk
def balon(huruf, titik, dxy, fc_bg="#ffffff", ec_c="#000000", tc="#000000"):
    px, py = titik[0]+dxy[0], titik[1]+dxy[1]
    ax.annotate("", titik, (px, py),
                arrowprops=dict(arrowstyle="-", color=ec_c, lw=TIPIS,
                                shrinkA=0, shrinkB=7))
    ax.add_patch(Circle((px, py), 0.14, fc=fc_bg, ec=ec_c, lw=0.9, zorder=10))
    ax.text(px, py, huruf, ha="center", va="center", fontsize=7.5,
            fontweight="bold", color=tc, zorder=11)

balon("A", (KOL_X+KOL_W*0.65, W-KOL_D*0.45), (1.45, 0.15),
      fc_bg="#f1f5f9", ec_c="#334155", tc="#1e293b")
balon("B", (CH_X0+CH_L*0.25, BOX_D*0.72), (-1.28, 0.22),
      fc_bg="#ffedd5", ec_c="#c2410c", tc="#9a3412")
balon("C", (cx-0.55, cy-k*0.55),          (-0.95, -0.50),
      fc_bg="#eff6ff", ec_c="#1d4ed8", tc="#1e40af")
balon("D", (CH_X0+CH_L-0.20, ygap),       (1.25, -0.40),
      fc_bg="#ecfdf5", ec_c="#059669", tc="#065f46")

ket = ("A  kolom bangunan (beton), 0,60 × 0,79 m        "
       "B  dus rintangan (kardus), 1,80 × 1,01 m\n"
       "C  formasi V nominal, bentang lateral 2,05 m    "
       "D  formasi mengekor (transisi), agen 1 memimpin")
ax.text(L/2, -1.28, ket, ha="center", va="top", fontsize=8, linespacing=1.7)

# ukuran
ukur(ax, (0, 0), (L, 0), "7,20", offset=-0.78)
ukur(ax, (L, 0), (L, W), "2,70", offset=0.38)
ukur(ax, (CH_X0, 0), (CH_X0+CH_L, 0), "1,80", offset=-0.34)
ukur(ax, (CH_X0, BOX_D), (CH_X0, BOX_D+CELAH), "0,90", offset=-0.26)

ax.set_xlim(-1.35, L+1.15); ax.set_ylim(-2.15, W+1.32)
ax.set_aspect("equal"); ax.axis("off")
simpan(fig, "sketsa-arena")
