"""Gaya gambar teknik bersama untuk seluruh sketsa proposal.

Mengikuti konvensi gambar teknik: garis tipis seragam, tanpa warna jenuh,
tanpa judul di dalam gambar (judul menjadi caption LaTeX), arsiran untuk
benda padat, dan garis ukur dengan garis bantu serta anak panah.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

matplotlib.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 8.5,
    "axes.linewidth": 0.6,
    "lines.linewidth": 0.8,
    "patch.linewidth": 0.8,
    "text.color": "black",
})

TEBAL   = 1.5    # garis benda utama
TIPIS   = 0.6    # garis bantu dan garis ukur
PUTUS   = (0, (5, 3))
ABU     = "0.45"
ABU_MUDA= "0.85"


def ukur(ax, p1, p2, teks, *, offset=0.0, sisi="luar", pad=0.10,
         fs=8.5, warna="black", bantu=None):
    """Garis ukur bergaya teknik: anak panah dua arah, teks di tengah.

    p1, p2  titik ujung ukuran (pada benda)
    offset  pergeseran tegak lurus tempat garis ukur digambar
    bantu   panjang garis bantu dari benda ke garis ukur (None = otomatis)
    """
    (x1, y1), (x2, y2) = p1, p2
    mendatar = abs(y2 - y1) < 1e-9
    if mendatar:
        yd = y1 + offset
        if bantu is not False:
            for x in (x1, x2):
                ax.plot([x, x], [y1, yd + (pad if offset > 0 else -pad)],
                        color=warna, lw=TIPIS, zorder=6)
        a, b = (x1, yd), (x2, yd)
        tx, ty, rot, va, ha = (x1 + x2) / 2, yd, 0, "bottom", "center"
        ty += pad * 0.35
    else:
        xd = x1 + offset
        if bantu is not False:
            for y in (y1, y2):
                ax.plot([x1, xd + (pad if offset > 0 else -pad)], [y, y],
                        color=warna, lw=TIPIS, zorder=6)
        a, b = (xd, y1), (xd, y2)
        tx, ty, rot, va, ha = xd, (y1 + y2) / 2, 90, "bottom", "center"
        tx += pad * 0.35
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle="<|-|>", mutation_scale=8,
                                 color=warna, lw=TIPIS, shrinkA=0, shrinkB=0,
                                 zorder=6))
    ax.text(tx, ty, teks, ha=ha, va=va, rotation=rot, fontsize=fs,
            color=warna, zorder=7,
            bbox=dict(fc="white", ec="none", pad=1.0))


def penunjuk(ax, titik, teks, dxy, *, fs=8.5, ha="left", va="center"):
    """Garis penunjuk (leader) dengan teks di ujungnya."""
    ax.annotate(teks, titik, (titik[0] + dxy[0], titik[1] + dxy[1]),
                fontsize=fs, ha=ha, va=va, zorder=8,
                arrowprops=dict(arrowstyle="-", color="black", lw=TIPIS,
                                shrinkA=0, shrinkB=2))


def simpan(fig, nama):
    """Simpan tanpa judul, latar putih, dipangkas rapat."""
    import os
    out = f"tulisan/proposal/figures/{nama}.png"
    os.makedirs(os.path.dirname(out), exist_ok=True)
    fig.savefig(out, dpi=200, bbox_inches="tight", facecolor="white",
                edgecolor="none", pad_inches=0.04)
    print("tersimpan:", out)
