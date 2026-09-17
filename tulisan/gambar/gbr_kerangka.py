"""BAB II: (a) konfigurasi motor + dan X, (b) kerangka acuan NED dan FRD.

Diadaptasi dari Quan dkk. (2020). Arah putar mengikuti gambar sumber:
baling-baling 1 dan 3 berlawanan arah jarum jam, 2 dan 4 searah jarum jam.
Koordinat dalam cm cetak.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch
from gaya import CM, GARIS, TIPIS, FS, FS_KECIL, garis, simpan


def kanvas(w, h):
    fig = plt.figure(figsize=(w * CM, h * CM))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, w); ax.set_ylim(0, h); ax.axis("off")
    return fig, ax


def anak_panah(ax, p1, p2, lw=GARIS, gaya="-", ms=7):
    ax.add_patch(FancyArrowPatch(p1, p2, arrowstyle="-|>", mutation_scale=ms, lw=lw,
                 color="black", linestyle=gaya, shrinkA=0, shrinkB=0, zorder=6))


def putar(ax, c, r, ccw):
    """Busur arah putar di dalam lingkaran baling-baling."""
    a = np.radians(np.linspace(30, 300, 40))
    if not ccw:
        a = a[::-1]
    xs, ys = c[0] + r * np.cos(a), c[1] + r * np.sin(a)
    garis(ax, xs[:-1], ys[:-1], lw=TIPIS, z=5)
    anak_panah(ax, (xs[-3], ys[-3]), (xs[-1], ys[-1]), lw=TIPIS, ms=5)


# ── (a) konfigurasi + dan X ─────────────────────────────────────────────
fig, ax = kanvas(8.0, 4.3)
L, RP = 1.05, 0.46
for c0, sudut, judul in (((2.0, 2.05), 90, "+"), ((6.0, 2.05), 135, "X")):
    cx, cy = c0
    for n in range(4):                       # baling-baling 1..4 searah jarum jam dari depan
        t = np.radians(sudut - 90 * n)
        m = (cx + L * np.cos(t), cy + L * np.sin(t))
        garis(ax, [cx, m[0]], [cy, m[1]], lw=GARIS * 1.3, z=3)
        ax.add_patch(Circle(m, RP, fc="white", ec="black", lw=GARIS, zorder=4))
        ax.add_patch(Circle(m, 0.05, fc="black", ec="none", zorder=6))
        putar(ax, m, 0.26, ccw=(n % 2 == 0))
        tl = t + np.radians(38)
        ax.text(m[0] + (RP + 0.17) * np.cos(tl), m[1] + (RP + 0.17) * np.sin(tl), str(n + 1),
                fontsize=FS_KECIL, ha="center", va="center")
    anak_panah(ax, (cx, cy), (cx, cy + 1.95))
    anak_panah(ax, (cx, cy), (cx + 1.95, cy))
    ax.text(cx + 0.1, cy + 1.95, "$x_B$", fontsize=FS_KECIL, ha="left", va="top")
    ax.text(cx + 1.95, cy - 0.1, "$y_B$", fontsize=FS_KECIL, ha="right", va="top")
    ax.text(cx - 1.85, cy + 1.95, judul, fontsize=FS, ha="left", va="top")
simpan(fig, "konfigurasi-quad")


# ── (b) kerangka NED dan FRD, proyeksi miring ───────────────────────────
fig, ax = kanvas(5.3, 4.3)
K = 0.45                                     # pemendekan sumbu yang menembus bidang gambar


def proyeksi(o, v):
    x, y, z = v
    return (o[0] + y + K * x, o[1] + K * x - z)


N0 = (0.35, 1.6)
for v, s, off in (((1.9, 0, 0), "$x_N$", (0.05, 0.08)), ((0, 1.7, 0), "$y_N$", (0.08, 0.0)),
                  ((0, 0, 1.35), "$z_N$", (0.12, 0.05))):
    p = proyeksi(N0, v)
    anak_panah(ax, N0, p)
    ax.text(p[0] + off[0], p[1] + off[1], s, fontsize=FS_KECIL,
            ha="left", va="center")
ax.text(N0[0] + 0.15, N0[1] - 0.12, "$\\{N\\}$", fontsize=FS_KECIL, ha="left", va="top")

B0 = (3.25, 3.0)
psi = np.radians(25)
Rz = np.array([[np.cos(psi), -np.sin(psi), 0], [np.sin(psi), np.cos(psi), 0], [0, 0, 1]])
a = 0.72
for sx, sy in ((1, 1), (1, -1), (-1, -1), (-1, 1)):
    m = Rz @ np.array([sx * a, sy * a, 0])
    pm = proyeksi(B0, m)
    garis(ax, [B0[0], pm[0]], [B0[1], pm[1]], lw=GARIS * 1.3, z=3)
    t = np.linspace(0, 2 * np.pi, 60)
    ring = [proyeksi(B0, m + 0.3 * np.array([np.cos(u), np.sin(u), 0])) for u in t]
    ax.fill([q[0] for q in ring], [q[1] for q in ring], fc="white", ec="black", lw=TIPIS, zorder=4)
for v, s, off in ((Rz @ [1.35, 0, 0], "$x_B$", (0.06, 0.06)), (Rz @ [0, 1.4, 0], "$y_B$", (0.05, -0.1)),
                  ((0, 0, 1.0), "$z_B$", (0.1, 0.0))):
    p = proyeksi(B0, v)
    anak_panah(ax, B0, p)
    ax.text(p[0] + off[0], p[1] + off[1], s, fontsize=FS_KECIL, ha="left", va="center")
ax.text(B0[0] - 0.35, B0[1] + 0.45, "$\\{B\\}$", fontsize=FS_KECIL, ha="right", va="bottom")
anak_panah(ax, N0, (B0[0] - 0.08, B0[1] - 0.05), lw=TIPIS, gaya=(0, (3, 2)))
ax.text(2.05, 2.2, "$\\mathbf{p}$", fontsize=FS_KECIL, ha="left", va="top")
anak_panah(ax, (5.0, 1.75), (5.0, 0.55))
ax.text(4.9, 1.15, "$g$", fontsize=FS_KECIL, ha="right", va="center")
simpan(fig, "kerangka-ned-frd")
