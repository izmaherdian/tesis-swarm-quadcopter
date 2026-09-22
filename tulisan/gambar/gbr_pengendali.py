"""Pengontrol tingkat rendah kaskade pada flight controller (ArduPilot).

Koordinat sumbu dalam sentimeter cetak (lebar 14 cm).
"""
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from gaya import LEBAR, CM, GARIS, TIPIS, ABU, PUTUS, FS_KECIL, kotak, panah, garis, simpan

TINGGI = 7.3
fig = plt.figure(figsize=(LEBAR - 0.3 * CM, TINGGI * CM))   # sisakan pad simpan
ax = fig.add_axes([0, 0, 1, 1])
B = dict(fs=FS_KECIL)
R, H = 0.2, 0.8


def jumlah(x, y):
    ax.add_patch(Circle((x, y), R, fc="white", ec="black", lw=GARIS, zorder=4))
    ax.text(x - R - 0.03, y + 0.04, "+", fontsize=FS_KECIL, ha="right", va="bottom")
    ax.text(x + 0.08, y - R - 0.02, "$-$", fontsize=FS_KECIL, ha="left", va="top")


def teks(x, y, s, **kw):
    ax.text(x, y, s, fontsize=FS_KECIL, **{"ha": "center", "va": "center", **kw})


def umpan(x, y, s):
    panah(ax, (x, y - 0.9), (x, y - R))
    teks(x, y - 0.95, s, va="top")


SJ1, SJ2 = 1.25, 3.85           # posisi titik jumlah
# ── batas flight controller ─────────────────────────────────────────────
X0, X1 = 0.62, 9.75
garis(ax, [X0, X1, X1, X0, X0], [0.1, 0.1, 7.2, 7.2, 0.1], lw=TIPIS, gaya=PUTUS, warna=ABU)
teks(X1 - 0.1, 7.1, "flight controller", ha="right", va="top", style="italic", color="0.35")

# ── kalang translasi ────────────────────────────────────────────────────
Y1 = 5.85
jumlah(SJ1, Y1)
pp = kotak(ax, 1.75, Y1 - H/2, 1.5, H, "P posisi", **B)
jumlah(SJ2, Y1)
pv = kotak(ax, 4.35, Y1 - H/2, 2.45, H, "PID kecepatan", **B)
ak = kotak(ax, 7.75, Y1 - 0.5, 1.85, 1.0, "konversi\nakselerasi", **B)
panah(ax, (0.0, Y1), (SJ1 - R, Y1)); teks(0.32, Y1 + 0.1, "$\\mathbf{p}_{\\mathrm{ref}}$", va="bottom")
panah(ax, (SJ1 + R, Y1), pp["kiri"])
panah(ax, pp["kanan"], (SJ2 - R, Y1))
panah(ax, (SJ2 + R, Y1), pv["kiri"])
panah(ax, pv["kanan"], ak["kiri"]); teks(7.27, Y1 + 0.1, "$\\mathbf{a}_{\\mathrm{cmd}}$", va="bottom")
garis(ax, [0.0, SJ2], [6.8, 6.8])
panah(ax, (SJ2, 6.8), (SJ2, Y1 + R)); teks(0.32, 6.9, "$\\mathbf{v}_{\\mathrm{ref}}$", va="bottom")
umpan(SJ1, Y1, "$\\hat{\\mathbf{p}}$")
umpan(SJ2, Y1, "$\\hat{\\mathbf{v}}$")

# ── kalang rotasi ───────────────────────────────────────────────────────
Y2 = 2.95
YQ = 4.25
garis(ax, [8.2, 8.2], [ak["y"], YQ])
garis(ax, [8.2, 0.8], [YQ, YQ])
garis(ax, [0.8, 0.8], [YQ, Y2])
panah(ax, (0.8, Y2), (SJ1 - R, Y2))
teks(6.0, YQ + 0.1, "$\\mathbf{q}_{\\mathrm{des}}$", va="bottom")
jumlah(SJ1, Y2)
ps = kotak(ax, 1.75, Y2 - H/2, 1.5, H, "P sikap", **B)
jumlah(SJ2, Y2)
pw = kotak(ax, 4.35, Y2 - H/2, 2.45, H, "PID laju sudut", **B)
mx = kotak(ax, 7.75, Y2 - H/2, 1.6, H, "mixer", **B)
es = kotak(ax, 10.85, Y2 - H/2, 1.0, H, "ESC", **B)
mo = kotak(ax, 12.45, Y2 - H/2, 1.45, H, "4 motor", **B)
panah(ax, (SJ1 + R, Y2), ps["kiri"])
panah(ax, ps["kanan"], (SJ2 - R, Y2))
panah(ax, (SJ2 + R, Y2), pw["kiri"])
panah(ax, pw["kanan"], mx["kiri"]); teks(7.27, Y2 + 0.1, "$\\boldsymbol{\\tau}$", va="bottom")
panah(ax, (9.05, ak["y"]), (9.05, mx["y"] + H)); teks(9.17, YQ, "$T$", ha="left")
panah(ax, mx["kanan"], es["kiri"]); teks(10.3, Y2 + 0.1, "DShot", va="bottom")
panah(ax, es["kanan"], mo["kiri"])
umpan(SJ1, Y2, "$\\hat{\\mathbf{q}}$")
umpan(SJ2, Y2, "$\\hat{\\boldsymbol{\\omega}}$")

# ── estimator ───────────────────────────────────────────────────────────
ek = kotak(ax, 6.0, 0.45, 2.4, 0.85, "EKF3", **B)
panah(ax, (9.5, 1.08), (ek["x"] + ek["w"], 1.08)); teks(8.95, 1.18, "IMU", va="bottom")
panah(ax, (12.6, 0.67), (ek["x"] + ek["w"], 0.67)); teks(11.2, 0.77, "pose kamera", va="bottom")
panah(ax, ek["kiri"], (4.95, ek["cy"]))
teks(4.85, ek["cy"], "$\\hat{\\mathbf{p}},\\ \\hat{\\mathbf{v}},\\ \\hat{\\mathbf{q}},\\ \\hat{\\boldsymbol{\\omega}}$", ha="right")

ax.set_xlim(0, 14); ax.set_ylim(0, TINGGI); ax.axis("off")
simpan(fig, "pengendali")
