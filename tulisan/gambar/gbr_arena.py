"""Denah arena uji pada koridor PTIO ITB (satuan m, berskala)."""
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, FancyArrowPatch
from gaya import LEBAR, CM, GARIS, TIPIS, ABU, ABU_MUDA, PUTUS, FS, FS_KECIL, ukur, garis, simpan
import parameter as P

W, L = P.W_KORIDOR, P.L_SEGMEN
CH0 = (L - P.KANAL) / 2
KX = CH0 + (P.KANAL - P.KOLOM_W) / 2
DUS = W - P.KOLOM_D - P.CELAH
D, k = P.W_WAHANA, P.K_SKALA
g = P.liputan()["panjang"]          # liputan model lubang jarum
kam = (g / 2, L - g / 2)

fig, ax = plt.subplots(figsize=(LEBAR, 7.2 * CM))

# dinding dan rintangan
for y in (0, W):
    garis(ax, [0, L], [y, y], lw=1.6)
ax.add_patch(Rectangle((KX, W - P.KOLOM_D), P.KOLOM_W, P.KOLOM_D, fc=ABU, ec="black", lw=GARIS, zorder=4))
for x0, w in ((CH0, KX - CH0), (KX + P.KOLOM_W, CH0 + P.KANAL - KX - P.KOLOM_W)):
    ax.add_patch(Rectangle((x0, W - P.KOLOM_D), w, P.KOLOM_D, fc="white", ec="black", lw=GARIS, hatch="////", zorder=3))
ax.add_patch(Rectangle((CH0, 0), P.KANAL, DUS, fc="white", ec="black", lw=GARIS, hatch="////", zorder=3))
for huruf, (x, y) in (("A", (KX + P.KOLOM_W / 2, W - P.KOLOM_D / 2)), ("B", (CH0 + P.KANAL / 2, DUS / 2))):
    ax.text(x, y, huruf, ha="center", va="center", fontsize=FS, fontweight="bold", zorder=6,
            bbox=dict(boxstyle="circle,pad=0.15", fc="white", ec="black", lw=TIPIS))

# formasi V dan formasi mengekor (agen 1 memimpin ke kanan)
cx, cy = 1.15, W / 2
for i, (dx, dy) in enumerate(P.TOPOLOGI):
    x, y = cx + dx * k, cy + dy * k
    ax.add_patch(Circle((x, y), D / 2, fc="white", ec="black", lw=GARIS, zorder=5))
    ax.text(x, y, str(i + 1), ha="center", va="center", fontsize=FS_KECIL - 1, zorder=6)
yc = DUS + P.CELAH / 2
for i in range(5):
    x = CH0 + 0.18 + i * 0.36
    ax.add_patch(Circle((x, yc), D / 2, fc=ABU_MUDA, ec="black", lw=GARIS, zorder=5))
    ax.text(x, yc, str(5 - i), ha="center", va="center", fontsize=FS_KECIL - 1, zorder=6)
ax.add_patch(FancyArrowPatch((0.15, W - 0.22), (0.95, W - 0.22), arrowstyle="-|>", mutation_scale=7, lw=GARIS, color="black"))
ax.text(1.02, W - 0.22, "arah gerak", fontsize=FS_KECIL, va="center")

# kamera dan liputan minimum
for i, c in enumerate(kam, 1):
    ax.add_patch(Rectangle((c - 0.09, W + 0.30), 0.18, 0.13, fc="black", ec="black", zorder=5))
    ax.text(c, W + 0.47, f"K{i}", ha="center", va="bottom", fontsize=FS_KECIL)
    garis(ax, [c, c], [W + 0.30, W], lw=TIPIS, gaya=PUTUS, warna=ABU)
    y = W + (0.95 if i == 1 else 1.20)
    garis(ax, [c - g / 2, c - g / 2, c + g / 2, c + g / 2], [y - 0.06, y, y, y - 0.06], lw=TIPIS)

# ukuran
ukur(ax, (0, 0), (L, 0), f"{L:.2f}".replace(".", ","), offset=-0.72)
ukur(ax, (CH0, 0), (CH0 + P.KANAL, 0), f"{P.KANAL:.2f}".replace(".", ","), offset=-0.32)
ukur(ax, (L, 0), (L, W), f"{W:.2f}".replace(".", ","), offset=0.35)
ukur(ax, (CH0 + P.KANAL, DUS), (CH0 + P.KANAL, DUS + P.CELAH), f"{P.CELAH:.2f}".replace(".", ","), offset=0.30)

ax.set_xlim(-0.25, L + 0.65); ax.set_ylim(-1.05, W + 1.40)
ax.set_aspect("equal"); ax.axis("off")
simpan(fig, "arena")
print(f"liputan per kamera {g:.2f} m, kamera di x = {kam[0]:.2f} dan {kam[1]:.2f} m, tumpang tindih {2*g - L:.2f} m")
