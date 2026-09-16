"""Gaya bersama seluruh gambar tesis: minimalis, hitam-putih, Times New Roman.

Gambar disimpan sebagai PDF vektor ke tulisan/proposal/figures/, dengan
ukuran figur = ukuran cetak (lebar teks 14 cm) sehingga teks gambar tampil
pada ukuran sebenarnya ketika disisipkan dengan width=\\textwidth.
"""
import glob, os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyArrowPatch, Polygon

# ── Fon: daftarkan eksplisit, gagal keras bila tidak ada ───────────────
for f in glob.glob("/usr/share/fonts/truetype/msttcorefonts/[Tt]imes*.ttf"):
    fm.fontManager.addfont(f)
if not any(f.name == "Times New Roman" for f in fm.fontManager.ttflist):
    raise RuntimeError("Times New Roman tidak ditemukan; gambar tidak dibuat.")

matplotlib.rcParams.update({
    "font.family": "serif",
    "font.serif": ["Times New Roman"],
    "mathtext.fontset": "custom",
    "mathtext.rm": "Times New Roman",
    "mathtext.it": "Times New Roman:italic",
    "mathtext.bf": "Times New Roman:bold",
    "font.size": 9,
    "axes.linewidth": 0.6,
    "lines.linewidth": 0.8,
    "patch.linewidth": 0.8,
    "pdf.fonttype": 42,          # fon TrueType tertanam utuh, teks tetap dapat dipilih
    "savefig.dpi": 300,
})

CM        = 1 / 2.54
LEBAR     = 14.0 * CM           # lebar teks A4: 21 - 4 - 3 cm
SETENGAH  = 6.8 * CM            # satu panel pada baris dua gambar
GARIS     = 0.9
TIPIS     = 0.5
ABU       = "0.55"
ABU_MUDA  = "0.90"
PUTUS     = (0, (4, 2.5))
FS        = 9
FS_KECIL  = 8

ROOT   = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
KELUAR = os.path.join(ROOT, "tulisan", "proposal", "figures")
PRATINJAU = os.environ.get("PRATINJAU")   # folder PNG untuk pemeriksaan visual


def kotak(ax, x, y, w, h, teks="", fs=FS, isi="white", garis=GARIS, gaya="-", z=3, **kw):
    ax.add_patch(Rectangle((x, y), w, h, fc=isi, ec="black", lw=garis, ls=gaya, zorder=z))
    if teks:
        ax.text(x + w / 2, y + h / 2, teks, ha="center", va="center", fontsize=fs,
                zorder=z + 1, linespacing=1.25, **kw)
    return dict(x=x, y=y, w=w, h=h, cx=x + w / 2, cy=y + h / 2,
                atas=(x + w / 2, y + h), bawah=(x + w / 2, y),
                kiri=(x, y + h / 2), kanan=(x + w, y + h / 2))


def panah(ax, p1, p2, teks="", fs=FS_KECIL, dua=False, gaya="-", dx=0.0, dy=0.0,
          ha="center", va="center", lw=GARIS):
    ax.add_patch(FancyArrowPatch(p1, p2, arrowstyle="<|-|>" if dua else "-|>",
                 mutation_scale=7, lw=lw, color="black", linestyle=gaya,
                 shrinkA=0, shrinkB=0, zorder=2))
    if teks:
        ax.text((p1[0] + p2[0]) / 2 + dx, (p1[1] + p2[1]) / 2 + dy, teks, fontsize=fs,
                ha=ha, va=va, zorder=5, bbox=dict(fc="white", ec="none", pad=0.6))


def garis(ax, xs, ys, lw=GARIS, gaya="-", warna="black", z=2):
    ax.plot(xs, ys, color=warna, lw=lw, ls=gaya, zorder=z, solid_capstyle="butt")


def ukur(ax, p1, p2, teks, offset, fs=FS_KECIL, bantu=True, celah=0.0):
    """Garis ukur: garis bantu tegak lurus, anak panah dua arah, teks di tengah."""
    (x1, y1), (x2, y2) = p1, p2
    if abs(y2 - y1) < 1e-9:                         # mendatar
        yd = y1 + offset
        if bantu:
            for x in (x1, x2):
                garis(ax, [x, x], [y1 + (celah if offset > 0 else -celah), yd], lw=TIPIS)
        a, b, rot = (x1, yd), (x2, yd), 0
        tx, ty, va, ha = (x1 + x2) / 2, yd, "bottom", "center"
    else:                                           # tegak
        xd = x1 + offset
        if bantu:
            for y in (y1, y2):
                garis(ax, [x1 + (celah if offset > 0 else -celah), xd], [y, y], lw=TIPIS)
        a, b, rot = (xd, y1), (xd, y2), 90
        tx, ty, va, ha = xd, (y1 + y2) / 2, "bottom", "center"
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle="<|-|>", mutation_scale=6,
                 lw=TIPIS, color="black", shrinkA=0, shrinkB=0, zorder=6))
    ax.text(tx, ty, teks, ha=ha, va=va, rotation=rot, fontsize=fs, zorder=7,
            bbox=dict(fc="white", ec="none", pad=0.8))


def simpan(fig, nama):
    os.makedirs(KELUAR, exist_ok=True)
    pdf = os.path.join(KELUAR, f"{nama}.pdf")
    fig.savefig(pdf, bbox_inches="tight", pad_inches=0.02, facecolor="white")
    if PRATINJAU:
        os.makedirs(PRATINJAU, exist_ok=True)
        fig.savefig(os.path.join(PRATINJAU, f"{nama}.png"), bbox_inches="tight",
                    pad_inches=0.02, facecolor="white", dpi=170)
    plt.close(fig)
    print("  ✓", os.path.relpath(pdf, ROOT))
