"""Sketsa skala arena uji di koridor PTIO ITB.

Menghasilkan docs/lab/sketsa-arena.png. Semua satuan meter.
Jalankan ulang bila geometri berubah: python3 docs/lab/sketsa_arena.py
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch, Circle

# ── Parameter arena ────────────────────────────────────────────────
W       = 2.70   # lebar bersih koridor (setelah sofa & banner disingkirkan)
L       = 7.20   # panjang terliput 2 kamera
KOL_X, KOL_W, KOL_D = 3.30, 0.60, 0.79   # kolom "tembok mencuil"
CH_L    = 1.80   # panjang kanal sempit
CELAH   = 0.90   # lebar celah
CH_X0   = (L - CH_L)/2
BOX_D   = W - KOL_D - CELAH              # kedalaman dus di sisi seberang
D_DRONE = 0.25
k       = 0.90                            # faktor skala formasi
TOPO    = [(1,0), (0,-0.5), (0,0.5), (-1,1), (-1,-1)]

fig, ax = plt.subplots(figsize=(15.5, 7.6))

# ── Liputan kamera ─────────────────────────────────────────────────
ax.add_patch(Rectangle((0,0), 4.80, W, fc="#2E86AB", alpha=.10, ec="none"))
ax.add_patch(Rectangle((2.40,0), 4.80, W, fc="#A23B72", alpha=.10, ec="none"))
ax.add_patch(Rectangle((2.40,0), 2.40, W, fc="#6A4C93", alpha=.13, ec="none"))
for x, lbl, c in ((2.40,"KAMERA 1","#2E86AB"), (4.80,"KAMERA 2","#A23B72")):
    ax.plot([x,x], [W, W+0.55], color=c, lw=1.2, ls=":", zorder=3)
    ax.plot(x, W+0.62, marker="v", ms=16, color=c, clip_on=False, zorder=10)
    ax.text(x, W+0.85, f"{lbl}\nliputan 4,80 m", ha="center", va="bottom",
            fontsize=10, fontweight="bold", color=c)
ax.annotate("", (4.80, W+0.30), (2.40, W+0.30),
            arrowprops=dict(arrowstyle="<->", color="#6A4C93", lw=1.6))
ax.text(3.60, W+0.36, "tumpang tindih 2,40 m", ha="center", fontsize=9,
        color="#6A4C93", style="italic", fontweight="bold")

# ── Dinding koridor ────────────────────────────────────────────────
for y in (0, W):
    ax.plot([0,L], [y,y], color="k", lw=4.5, solid_capstyle="butt", zorder=5)

# ── Rintangan ──────────────────────────────────────────────────────
ax.add_patch(Rectangle((KOL_X, W-KOL_D), KOL_W, KOL_D, fc="#4A4A4A", ec="k",
                       lw=1.5, hatch="///", zorder=7))
ax.text(KOL_X+KOL_W/2, W-KOL_D/2, "KOLOM", ha="center", va="center",
        fontsize=8, color="w", fontweight="bold", zorder=8, rotation=90)
ax.annotate("tembok mencuil\n60 × 79 cm", (KOL_X+KOL_W/2, W+0.02),
            (KOL_X+KOL_W/2-0.9, W+1.25), fontsize=8.5, ha="center", color="#4A4A4A",
            fontweight="bold", arrowprops=dict(arrowstyle="->", color="#4A4A4A", lw=1.3))

for x0, w in ((CH_X0, KOL_X-CH_X0), (KOL_X+KOL_W, CH_X0+CH_L-KOL_X-KOL_W)):
    ax.add_patch(Rectangle((x0, W-KOL_D), w, KOL_D, fc="#C89F5D", ec="k",
                           lw=1.3, alpha=.92, zorder=6))
ax.add_patch(Rectangle((CH_X0, 0), CH_L, BOX_D, fc="#C89F5D", ec="k",
                       lw=1.3, alpha=.92, zorder=6))
ax.text(CH_X0+CH_L/2, BOX_D/2, "DUS RINTANGAN\n1,80 × 1,01 m", ha="center",
        va="center", fontsize=9.5, fontweight="bold", zorder=7)

# ── Celah ──────────────────────────────────────────────────────────
ax.add_patch(Rectangle((CH_X0, BOX_D), CH_L, CELAH, fc="#F5D547", alpha=.38,
                       ec="#D4A017", lw=2.2, ls="--", zorder=4))

def dim(x1,y1,x2,y2,txt,c="#C1121F",fs=10,rot=0):
    ax.annotate("", (x2,y2), (x1,y1),
                arrowprops=dict(arrowstyle="<->", color=c, lw=1.8))
    ax.text((x1+x2)/2, (y1+y2)/2, txt, ha="center", va="center", fontsize=fs,
            color=c, fontweight="bold", rotation=rot,
            bbox=dict(fc="w", ec=c, lw=1.2, boxstyle="round,pad=0.25"))

dim(L+0.34, 0, L+0.34, W, "270 cm", rot=90)
dim(0, -0.92, L, -0.92, "7,20 m   (liputan 2 kamera)")
dim(CH_X0, -0.42, CH_X0+CH_L, -0.42, "kanal 1,80 m", c="#8B5E00", fs=9)
# celah: panah di dalam kanal, label digeser ke kanan agar bebas
ax.annotate("", (CH_X0+CH_L-0.22, BOX_D+CELAH), (CH_X0+CH_L-0.22, BOX_D),
            arrowprops=dict(arrowstyle="<->", color="#C1121F", lw=2.2))
ax.text(CH_X0+CH_L+0.52, BOX_D+CELAH/2, "CELAH\n90 cm", ha="center", va="center",
        fontsize=11, color="#C1121F", fontweight="bold",
        bbox=dict(fc="#FFF3B0", ec="#C1121F", lw=1.5, boxstyle="round,pad=0.3"))

# ── Formasi V saat mendekat ────────────────────────────────────────
cx, cy = 1.15, W/2
for i,(dx,dy) in enumerate(TOPO):
    x, y = cx+dx*k, cy+dy*k
    ax.add_patch(Circle((x,y), D_DRONE/2, fc="#1B9AAA", ec="k", lw=1.3, zorder=8))
    ax.text(x, y, str(i+1), ha="center", va="center", fontsize=7.5,
            color="w", fontweight="bold", zorder=9)
# bentang LATERAL = melintang koridor (sumbu y)
ax.annotate("", (cx-1.22, cy-0.9-D_DRONE/2), (cx-1.22, cy+0.9+D_DRONE/2),
            arrowprops=dict(arrowstyle="<->", color="#0B7285", lw=1.8))
for yy in (cy-0.9-D_DRONE/2, cy+0.9+D_DRONE/2):
    ax.plot([cx-1.32, cx-1.12], [yy,yy], color="#0B7285", lw=1.6)
ax.text(cx-1.42, cy, "2,05 m", rotation=90, ha="center", va="center",
        fontsize=9.5, fontweight="bold", color="#0B7285")
ax.text(cx, -0.42, "FORMASI V  (skala 0,9)\nbentang lateral 2,05 m", ha="center",
        va="center", fontsize=9.5, fontweight="bold", color="#0B7285",
        bbox=dict(fc="w", ec="#0B7285", lw=1.2, boxstyle="round,pad=0.25"))

# ── Tailgating di dalam kanal ──────────────────────────────────────
ygap = BOX_D + CELAH/2
for i in range(5):
    x = CH_X0 + 0.18 + i*0.38
    ax.add_patch(Circle((x, ygap), D_DRONE/2, fc="#EF476F", ec="k", lw=1.3, zorder=8))
    ax.text(x, ygap, str(i+1), ha="center", va="center", fontsize=7.5,
            color="w", fontweight="bold", zorder=9)
ax.text(CH_X0+CH_L/2, ygap-0.42, "TAILGATING", ha="center", fontsize=9.5,
        fontweight="bold", color="#EF476F")

for x0,x1,lbl in ((0.15, CH_X0-0.15, "ANCANG-ANCANG  →"),
                  (CH_X0+CH_L+0.15, L-0.15, "KELUAR & MENGEMBANG  →")):
    ax.text((x0+x1)/2, W-0.16, lbl, ha="center", fontsize=8.5, color="#555",
            style="italic")

ax.set_xlim(-1.15, L+1.1); ax.set_ylim(-1.35, W+1.85)
ax.set_aspect("equal"); ax.axis("off")
ax.set_title("Sketsa Arena Uji — Koridor PTIO ITB   (gambar berskala, satuan meter)",
             fontsize=13.5, fontweight="bold", pad=12)
plt.tight_layout()
plt.savefig("docs/lab/sketsa-arena.png", dpi=135, bbox_inches="tight", facecolor="w")
print(f"celah        = {CELAH:.2f} m")
print(f"dus menonjol = {BOX_D:.2f} m")
print(f"bentang V    = {2*k+D_DRONE:.2f} m, sisa {(W-(2*k+D_DRONE))/2*100:.1f} cm per sisi")
print(f"mengekor     : sisa {(CELAH-D_DRONE)/2*100:.1f} cm per sisi")
print(f"rasio bentang/celah = {(2*k+D_DRONE)/CELAH:.2f}  (simulator 2,40)")
