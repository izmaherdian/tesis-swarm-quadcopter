"""Perencana tingkat tinggi: perilaku penyusun, pemicu ERC, dan pemilihan mode.

Setia pada MultiAgentERC.py (0d7ed5a) dan Subbab 3.4.3. Koordinat dalam cm cetak.
"""
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from gaya import LEBAR, CM, GARIS, TIPIS, ABU, PUTUS, FS_KECIL, kotak, panah, garis, simpan

TINGGI = 7.95
fig = plt.figure(figsize=(LEBAR - 0.3 * CM, TINGGI * CM))
ax = fig.add_axes([0, 0, 1, 1])
B = dict(fs=FS_KECIL)


def teks(x, y, s, **kw):
    ax.text(x, y, s, **{"fontsize": FS_KECIL, "ha": "center", "va": "center", **kw})


def titik(x, y):
    ax.add_patch(Circle((x, y), 0.05, fc="black", ec="none", zorder=5))


# ── masukan dan bus ─────────────────────────────────────────────────────
BUS = 2.65
garis(ax, [BUS, BUS], [1.1, 7.6], lw=1.6)
for y, s in ((6.9, "keadaan diri\ndan tetangga"), (4.65, "tujuan dan\ntopologi"), (2.4, "rintangan")):
    k = kotak(ax, 0.0, y - 0.4, 2.05, 0.8, s, **B)
    panah(ax, k["kanan"], (BUS, y))

# ── pemicu berbasis kejadian ────────────────────────────────────────────
YT = 7.6
garis(ax, [3.0, 9.05, 9.05, 3.0, 3.0], [7.0, 7.0, 8.45, 8.45, 7.0], lw=TIPIS, gaya=PUTUS, warna=ABU)
teks(3.1, 8.35, "pemicu berbasis kejadian", ha="left", va="top", style="italic", color="0.35")
we = kotak(ax, 3.3, YT - 0.35, 2.6, 0.7, "estimasi lebar $w_e$", **B)
sw = kotak(ax, 6.6, YT - 0.35, 2.2, 0.7, "pensaklaran", **B)
panah(ax, (BUS, YT), we["kiri"])
panah(ax, we["kanan"], sw["kiri"])

# ── perilaku penyusun ───────────────────────────────────────────────────
W = 2.6
baris = {
    "form": (6.0, "formasi $\\mathbf{v}_i^{\\mathrm{form}}$"),
    "tail": (5.1, "mengekor $\\mathbf{v}_i^{\\mathrm{tail}}$ ke $l_i$"),
    "mig":  (4.2, "migrasi $\\mathbf{v}_i^{\\mathrm{mig}}$"),
    "obs":  (3.3, "rintangan $\\mathbf{v}_i^{\\mathrm{obs}}$"),
    "col":  (2.2, "tabrakan $\\mathbf{v}_i^{\\mathrm{col}}$"),
    "to":   (1.1, "lepas landas $\\mathbf{v}_i^{\\mathrm{to}}$"),
}
k = {}
for n, (y, s) in baris.items():
    k[n] = kotak(ax, 3.3, y - 0.3, W, 0.6, s, **B)
    panah(ax, (BUS, y), k[n]["kiri"])

# κ ke formasi, σ ke pemilih
garis(ax, [6.85, 6.85], [sw["y"], 6.72]); garis(ax, [6.85, 5.4], [6.72, 6.72])
panah(ax, (5.4, 6.72), (5.4, k["form"]["y"] + 0.6)); teks(6.1, 6.8, "$\\kappa$", va="bottom")
sel = kotak(ax, 6.6, 4.8, 1.0, 1.5, "", **B)
teks(sel["cx"], sel["cy"], "$\\sigma_i$", fontsize=FS_KECIL + 1)
teks(sel["x"] + 0.08, 6.0, "1", ha="left", fontsize=FS_KECIL - 1)
teks(sel["x"] + 0.08, 5.1, "0", ha="left", fontsize=FS_KECIL - 1)
panah(ax, (7.35, sw["y"]), (7.35, sel["y"] + sel["h"])); teks(7.47, 6.65, "$\\sigma_i$", ha="left")
panah(ax, k["form"]["kanan"], (sel["x"], 6.0))
panah(ax, k["tail"]["kanan"], (sel["x"], 5.1))
# ── penjumlahan mode misi ───────────────────────────────────────────────
sm = kotak(ax, 8.6, 1.95, 0.55, 4.05, "$\\Sigma$", fs=FS_KECIL + 2)
panah(ax, sel["kanan"], (sm["x"], sel["cy"]))
for n in ("mig", "obs", "col"):
    panah(ax, k[n]["kanan"], (sm["x"], baris[n][0]))
# penjumlahan mode lepas landas
XS = 7.1
titik(XS, baris["col"][0])
ax.add_patch(Circle((XS, 1.1), 0.2, fc="white", ec="black", lw=GARIS, zorder=4))
teks(XS, 1.1, "$\\Sigma$", fontsize=FS_KECIL, zorder=6)
panah(ax, (XS, baris["col"][0]), (XS, 1.3))
panah(ax, k["to"]["kanan"], (XS - 0.2, 1.1))

# ── pemilih mode dan integrator ─────────────────────────────────────────
md = kotak(ax, 9.8, 0.75, 1.3, 3.5, "mode", **B)
garis(ax, [sm["x"] + sm["w"], 9.45], [sm["cy"], sm["cy"]]); garis(ax, [9.45, 9.45], [sm["cy"], 3.6])
panah(ax, (9.45, 3.6), (md["x"], 3.6)); teks(9.9, 3.6, "misi", ha="left", fontsize=FS_KECIL - 1)
panah(ax, (XS + 0.2, 1.1), (md["x"], 1.1)); teks(9.9, 1.4, "lepas\nlandas", ha="left", fontsize=FS_KECIL - 1, linespacing=1.0)
panah(ax, (md["cx"], 5.0), (md["x"] + md["h"] * 0 + md["w"] / 2, md["y"] + md["h"]))
teks(md["cx"], 5.08, "$|z_i - z_{\\mathrm{target}}| \\leq 0{,}1$ m, $\\forall i$", va="bottom")
it = kotak(ax, 11.75, 2.1, 0.7, 0.8, "$\\int$", fs=FS_KECIL + 2)
panah(ax, (md["x"] + md["w"], it["cy"]), it["kiri"]); teks(11.43, it["cy"] + 0.1, "$\\mathbf{v}_i$", va="bottom")
panah(ax, it["kanan"], (13.95, it["cy"])); teks(13.2, it["cy"] + 0.1, "$\\mathbf{p}_{\\mathrm{ref}}$", va="bottom")

ax.set_xlim(0, 14); ax.set_ylim(0.65, 0.65 + TINGGI); ax.axis("off")
simpan(fig, "perencana")
