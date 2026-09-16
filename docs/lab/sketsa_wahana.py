"""Wahana uji SpeedyBee Bee35. Tampak atas dan tampak samping, satuan cm."""
import sys, os, math; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, FancyArrowPatch
from gaya_gambar import ukur, simpan, TEBAL, TIPIS, PUTUS, ABU, ABU_MUDA

W, L, H   = 25.0, 21.0, 8.0
DUCT      = 10.5
DX, DY    = (W - DUCT) / 2, (L - DUCT) / 2
SPINE     = 2 * DX - DUCT
TAG       = 10.0
RISER     = 7.0

# Kanvas proporsional dan lapang
fig, (ax, bx) = plt.subplots(1, 2, figsize=(10.5, 5.2),
                             gridspec_kw={"width_ratios": [1.55, 1.0]})

def penunjuk_kotak(a, titik, teks, dxy, fs=8.0, ha="left", va="center"):
    """Garis penunjuk dengan kotak latar putih bersih berbayang tipis agar sangat jelas dibaca."""
    px, py = titik[0] + dxy[0], titik[1] + dxy[1]
    a.annotate(teks, xy=titik, xytext=(px, py),
               fontsize=fs, ha=ha, va=va, zorder=15,
               bbox=dict(boxstyle="round,pad=0.3", fc="#ffffff", ec="#64748b", lw=0.7),
               arrowprops=dict(arrowstyle="-|>", color="#1e293b", lw=0.9,
                               mutation_scale=9, shrinkA=0, shrinkB=2))

# ───────── TAMPAK ATAS ─────────
# Batas luar wahana
ax.add_patch(Rectangle((-W/2, -L/2), W, L, fc="#fafafa", ec=ABU, lw=TIPIS, ls=PUTUS, zorder=1))

# Saluran propeler (ducts)
for sx in (-1, 1):
    for sy in (-1, 1):
        c = (sx * DX, sy * DY)
        ax.add_patch(Circle(c, DUCT/2, fc="#f1f5f9", ec="#1e293b", lw=TEBAL, zorder=3))
        ax.add_patch(Circle(c, DUCT/2 - 1.2, fc="white", ec="#475569", lw=TIPIS, zorder=3))
        ax.add_patch(Circle(c, 1.4, fc=ABU_MUDA, ec="#1e293b", lw=TIPIS, zorder=4))

# Jalur bodi tengah (spine)
ax.add_patch(Rectangle((-SPINE/2, -L/2 + 1), SPINE, L - 2, fc="#ffffff", ec="#1e293b",
                       lw=TEBAL, zorder=5))

# Komponen pada jalur tengah
# Baterai LiPo (belakang)
ax.add_patch(Rectangle((-1.5, -7.5), 3.0, 3.8, fc="#fef08a", ec="#ca8a04", lw=1.0, zorder=6))
# Stack FC / ESC (tengah)
ax.add_patch(Rectangle((-1.6, -2.0), 3.2, 3.2, fc="#bae6fd", ec="#0284c7", lw=1.0, zorder=6))
# Companion computer XIAO ESP32-S3 (depan)
ax.add_patch(Rectangle((-1.2, 2.5), 2.4, 2.8, fc="#bbf7d0", ec="#16a34a", lw=1.0, zorder=6))

# Dudukan penanda AprilTag (proyeksi garis putus-putus 10x10 cm)
ax.add_patch(Rectangle((-TAG/2, -TAG/2), TAG, TAG, fc="#e2e8f0", ec="#334155",
                       lw=1.2, ls=(0, (4, 2.5)), alpha=0.5, zorder=7))

# Sensor jarak diagonal (kiri & kanan depan)
for sx in (-1, 1):
    px, py = sx * (W/2 - 2.2), L/2 - 2.2
    ax.add_patch(Rectangle((px - 0.9, py - 0.7), 1.8, 1.4, fc="#fed7aa", ec="#ea580c",
                           lw=1.0, zorder=9))
    ang = math.radians(90 - sx * 45)
    ax.plot([px, px + 6.0 * math.cos(ang)], [py, py + 6.0 * math.sin(ang)],
            color="#ea580c", lw=TIPIS, ls=(0, (4, 2)), zorder=8)

# Panah arah gerak maju (di atas saluran depan-kiri)
ax.add_patch(FancyArrowPatch((-DX, L/2 + 0.8), (-DX, L/2 + 4.2), arrowstyle="-|>",
                             mutation_scale=12, lw=1.5, color="#dc2626"))
ax.text(-DX, L/2 + 4.8, "Arah Maju", fontsize=8.5, fontweight="bold",
        color="#dc2626", ha="center", va="bottom")

# Dimensi tampak atas
ukur(ax, (-W/2, -L/2), (W/2, -L/2), "25,0 cm", offset=-3.6, pad=0.7, fs=8.5)
ukur(ax, (W/2, -L/2), (W/2, L/2), "21,0 cm", offset=3.2, pad=0.7, fs=8.5)
ukur(ax, (-SPINE/2, L/2 - 1), (SPINE/2, L/2 - 1), "4,0 cm", offset=2.5, pad=0.5, fs=8.0)

# Keterangan Terdistribusi Bersih pada Tampak Atas (a)
# Sisi Kiri:
penunjuk_kotak(ax, (-(W/2 - 2.2), L/2 - 2.2),
               "Sensor jarak kiri\n(diagonal 45°)", (-5.2, 3.0), ha="right")
penunjuk_kotak(ax, (-1.2, 3.5),
               "Companion computer\n(Seeed XIAO ESP32-S3)", (-6.2, 1.0), ha="right")
penunjuk_kotak(ax, (-TAG/2, -1.0),
               "Penanda visual AprilTag\n(proyeksi 10 × 10 cm)", (-6.2, -2.0), ha="right")
penunjuk_kotak(ax, (-1.5, -6.5),
               "Baterai LiPo\n(4S / 1200 mAh)", (-6.2, -5.5), ha="right")

# Sisi Kanan:
penunjuk_kotak(ax, (DX + DUCT/2 * 0.707, DY + DUCT/2 * 0.707),
               "Saluran propeler\n(duct 4×, ⌀10,5 cm)", (5.0, 6.2), ha="left")
penunjuk_kotak(ax, (W/2 - 2.2, L/2 - 2.2),
               "Sensor jarak kanan\n(diagonal 45°)", (5.0, 1.0), ha="left")
penunjuk_kotak(ax, (1.6, -0.4),
               "Stack kontrol inti\n(SpeedyBee F405 & ESC)", (5.0, -3.2), ha="left")

ax.set_xlim(-W/2 - 20.0, W/2 + 18.0)
ax.set_ylim(-L/2 - 6.5, L/2 + 8.5)
ax.set_aspect("equal")
ax.axis("off")
ax.text(0, -L/2 - 5.2, "(a) Tampak Atas (Tata Letak Komponen Lengkap)", ha="center", va="top",
        fontsize=9.5, fontweight="bold")

# ───────── TAMPAK SAMPING ─────────
# Susunan lapis tampak samping
lapis = [
    (0.0, 2.6, "#f1f5f9", "Rangka & saluran", TEBAL),
    (2.6, 2.2, "#bae6fd", "Stack FC/ESC", TIPIS),
    (4.8, 0.9, "#bbf7d0", "ESP32-S3", TIPIS),
    (5.7, 2.3, "#fef08a", "Baterai LiPo", TIPIS)
]
lebar = [W, 8.0, 4.0, 10.0]
for (y0, h, fc, lbl, lw), lb in zip(lapis, lebar):
    bx.add_patch(Rectangle((-lb/2, y0), lb, h, fc=fc, ec="#1e293b", lw=lw, zorder=2))

# Tiang penyangga penanda (riser)
for sx in (-1, 1):
    bx.plot([sx * 3.5, sx * 3.5], [H, H + RISER], color="#1e293b", lw=1.6, zorder=3)

# Pelat AprilTag di puncak tiang
bx.add_patch(Rectangle((-TAG/2, H + RISER), TAG, 0.6, fc="#e2e8f0", ec="#1e293b", lw=TEBAL, zorder=4))
bx.plot([-W/2 - 2, W/2 + 3], [0, 0], color=ABU, lw=TIPIS, ls=(0, (1, 2)), zorder=1)

# Dimensi vertikal
ukur(bx, (W/2, 0), (W/2, H), "8,0 cm", offset=3.0, pad=0.6, fs=8.5)
ukur(bx, (TAG/2, H), (TAG/2, H + RISER), "7,0 cm", offset=2.2, pad=0.6, fs=8.5)

# Penunjuk tampak samping (minimalis untuk elevasi penanda)
penunjuk_kotak(bx, (0, H + RISER + 0.3),
               "Pelat penanda AprilTag\n(di atas mulut saluran)", (0, 3.2), ha="center")
penunjuk_kotak(bx, (-3.5, H + RISER * 0.5),
               "Tiang penyangga\n(riser 7,0 cm)", (-6.0, 0), ha="right")
penunjuk_kotak(bx, (-W/2 + 2, 1.3),
               "Rangka bodi & saluran", (-4.2, -2.8), ha="right")

bx.set_xlim(-W/2 - 11.5, W/2 + 8.5)
bx.set_ylim(-4.5, H + RISER + 6.0)
bx.set_aspect("equal")
bx.axis("off")
bx.text(0, -3.8, "(b) Tampak Samping (Profil Ketinggian)", ha="center", va="top",
        fontsize=9.5, fontweight="bold")

plt.tight_layout()
simpan(fig, "sketsa-wahana")
print("Berhasil generate sketsa-wahana.png tanpa overlap!")
