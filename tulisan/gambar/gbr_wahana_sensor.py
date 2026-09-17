"""(a) Tampak atas wahana dan (b) geometri estimasi lebar ruang w_e."""
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Arc, FancyArrowPatch
from gaya import SETENGAH, CM, GARIS, TIPIS, ABU, ABU_MUDA, PUTUS, FS, FS_KECIL, ukur, garis, simpan
import parameter as P

# ════════ (a) tampak atas wahana, satuan cm, berskala ════════
W, L, D = P.W_WAHANA*100, P.L_WAHANA*100, P.D_SALURAN*100
DX, DY = (W - D)/2, (L - D)/2
SPINE = 2*DX - D
TAG = P.PENANDA*100

fig, ax = plt.subplots(figsize=(SETENGAH, 6.4*CM))
for sx in (-1, 1):
    for sy in (-1, 1):
        ax.add_patch(Circle((sx*DX, sy*DY), D/2, fc="white", ec="black", lw=GARIS, zorder=2))
        ax.add_patch(Circle((sx*DX, sy*DY), D/2 - 1.0, fc="none", ec="black", lw=TIPIS, zorder=2))
ax.add_patch(Rectangle((-SPINE/2, -L/2 + 0.8), SPINE, L - 1.6, fc=ABU_MUDA, ec="black", lw=GARIS, zorder=3))
ax.add_patch(Rectangle((-TAG/2, -TAG/2), TAG, TAG, fc="none", ec="black", lw=GARIS, ls=PUTUS, zorder=4))
for sx in (-1, 1):
    px, py = sx*(W/2 - 2.0), L/2 - 2.0
    ax.add_patch(Rectangle((px - 0.8, py - 0.55), 1.6, 1.1, fc="black", ec="black", lw=0, zorder=5))
    ang = math.radians(90 - sx*45)
    garis(ax, [px, px + 6.5*math.cos(ang)], [py, py + 6.5*math.sin(ang)], lw=TIPIS, gaya=PUTUS)
ax.add_patch(FancyArrowPatch((0, L/2 + 1.2), (0, L/2 + 4.4), arrowstyle="-|>",
                             mutation_scale=7, lw=GARIS, color="black"))
ax.text(0.8, L/2 + 3.4, "arah maju", fontsize=FS_KECIL, va="center")

ukur(ax, (-W/2, -L/2), (W/2, -L/2), "25", offset=-3.4, celah=0.4)
ukur(ax, (W/2, -L/2), (W/2, L/2), "21", offset=2.6, celah=0.4)
ukur(ax, (-SPINE/2, -L/2 + 0.8), (SPINE/2, -L/2 + 0.8), "4", offset=-1.3, celah=0.2)

def penunjuk(xy, teks, xyt, ha):
    ax.annotate(teks, xy, xyt, fontsize=FS_KECIL, ha=ha, va="center",
                arrowprops=dict(arrowstyle="-", lw=TIPIS, shrinkA=1, shrinkB=0))
penunjuk((-DX - D/2*0.72, -DY - D/2*0.72), "saluran\npropeler", (-W/2 - 3.2, -L/2 + 1.0), "right")
penunjuk((TAG/2, -TAG/2 + 1.2), "penanda\n12 cm\n(bertiang)", (W/2 + 5.6, -5.6), "left")
penunjuk((-(W/2 - 2.0) - 0.8, L/2 - 2.0), "sensor\njarak", (-W/2 - 3.2, L/2 + 1.6), "right")

ax.set_xlim(-W/2 - 8.5, W/2 + 12.0); ax.set_ylim(-L/2 - 5.2, L/2 + 5.5)
ax.set_aspect("equal"); ax.axis("off")
simpan(fig, "wahana-atas")

# ════════ (b) geometri estimasi w_e, skematik ════════
fig, ax = plt.subplots(figsize=(SETENGAH, 6.4*CM))
XW, SX, SY, TH = 3.6, 0.9, 0.9, math.radians(45)
for s in (-1, 1):
    ax.add_patch(Rectangle((s*XW - (0.25 if s > 0 else 0) + (0 if s > 0 else -0.25) + (0.25 if s < 0 else 0) - (0 if s < 0 else 0), -1.6),
                           0.25, 5.4, fc="white", ec="black", lw=GARIS, hatch="////", zorder=1))
ax.add_patch(Rectangle((-SX, -0.9), 2*SX, 1.8, fc=ABU_MUDA, ec="black", lw=GARIS, zorder=3))
ax.text(0, -0.05, "wahana", fontsize=FS_KECIL, ha="center", va="center", zorder=4)
for s in (-1, 1):
    ax.add_patch(Rectangle((s*SX - 0.12, SY - 0.12), 0.24, 0.24, fc="black", ec="black", lw=0, zorder=5))
    hit = (s*XW, SY + (XW - SX)/math.tan(TH))
    garis(ax, [s*SX, hit[0]], [SY, hit[1]], lw=GARIS, gaya=PUTUS, z=2)
    garis(ax, [s*SX, s*SX], [SY, SY + 1.5], lw=TIPIS, warna=ABU, z=2)
    a0, a1 = (90, 135) if s < 0 else (45, 90)
    ax.add_patch(Arc((s*SX, SY), 1.5, 1.5, theta1=a0, theta2=a1, lw=TIPIS, zorder=3))
    ax.text(s*SX - s*0.28, SY + 0.95, r"$\beta$", fontsize=FS, ha="center", va="center")
    mid = ((s*SX + hit[0])/2, (SY + hit[1])/2)
    ax.text(mid[0] - s*0.32, mid[1] + 0.25, r"$d_{\mathrm{raw},%s}$" % ("l" if s < 0 else "r"),
            fontsize=FS, ha="center", va="center", rotation=-s*45,
            bbox=dict(fc="white", ec="none", pad=0.3))
    lo, hi = sorted([s*SX, s*XW])
    ax.add_patch(FancyArrowPatch((lo, SY), (hi, SY), arrowstyle="<|-|>", mutation_scale=6,
                                 lw=TIPIS, color="black", zorder=6))
    ax.text((lo + hi)/2, SY - 0.28, r"$d_%s$" % ("l" if s < 0 else "r"), fontsize=FS, ha="center", va="top")
ukur(ax, (-SX, -0.9), (SX, -0.9), r"$w_{\mathrm{body}}$", offset=-0.55, fs=FS)
ukur(ax, (-XW, -1.6), (XW, -1.6), r"$w_e$", offset=-0.5, fs=FS, bantu=False)
ax.add_patch(FancyArrowPatch((0, 1.05), (0, 2.3), arrowstyle="-|>", mutation_scale=7, lw=GARIS, color="black"))
ax.set_xlim(-XW - 0.5, XW + 0.5); ax.set_ylim(-2.5, 3.9)
ax.set_aspect("equal"); ax.axis("off")
simpan(fig, "geometri-we")
