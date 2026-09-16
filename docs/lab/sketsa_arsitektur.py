"""Diagram blok arsitektur sistem: aliran data kamera hingga motor."""
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch
from gaya_gambar import simpan, TEBAL, TIPIS, PUTUS, ABU

fig, ax = plt.subplots(figsize=(7.2, 6.4))

def kotak(x, y, w, h, teks, fs=7.9):
    ax.add_patch(Rectangle((x, y), w, h, fc="white", ec="black", lw=1.0, zorder=3))
    ax.text(x+w/2, y+h/2, teks, ha="center", va="center", fontsize=fs,
            zorder=4, linespacing=1.5)
    return dict(x=x, y=y, w=w, h=h, cx=x+w/2, cy=y+h/2,
                atas=(x+w/2, y+h), bawah=(x+w/2, y),
                kiri=(x, y+h/2), kanan=(x+w, y+h/2))

def panah(p1, p2, teks="", fs=7.5, ls="-", dua=False, geser=0.0):
    ax.add_patch(FancyArrowPatch(p1, p2,
                 arrowstyle="<|-|>" if dua else "-|>", mutation_scale=9,
                 lw=0.9, color="black", linestyle=ls, shrinkA=1, shrinkB=1, zorder=2))
    if teks:
        ax.text((p1[0]+p2[0])/2 + geser, (p1[1]+p2[1])/2, teks, fontsize=fs,
                ha="center", va="center", zorder=5,
                bbox=dict(fc="white", ec="none", pad=1.2))

# ── zona darat ──
ax.add_patch(Rectangle((0.15, 6.30), 11.7, 3.45, fc="none", ec=ABU,
                       lw=TIPIS, ls=PUTUS, zorder=1))
ax.text(0.30, 9.48, "di darat", fontsize=8.5, style="italic", color=ABU, va="top")

k1  = kotak(0.85, 8.70, 2.7, 0.80, "kamera atas 1\n4K, HFOV ±109°")
k2  = kotak(3.95, 8.70, 2.7, 0.80, "kamera atas 2\nliputan bertumpang tindih")
gcs = kotak(8.55, 8.70, 3.0, 0.80, "stasiun kendali darat\ntelemetri dan darurat")
viz = kotak(1.45, 7.05, 5.7, 0.95,
            "stasiun pemroses citra\ndeteksi AprilTag → PnP → pose 3D lima agen")
panah(k1["bawah"], (viz["cx"]-1.2, viz["y"]+viz["h"]))
panah(k2["bawah"], (viz["cx"]+1.2, viz["y"]+viz["h"]))

net = kotak(3.55, 5.15, 4.9, 0.75, "jaringan Wi-Fi lokal — soket UDP")
panah(viz["bawah"], (net["cx"]-0.8, net["y"]+net["h"]), "pose absolut", geser=-1.15)
panah(gcs["bawah"], (net["cx"]+1.5, net["y"]+net["h"]), "MAVLink")

# ── zona wahana ──
ax.add_patch(Rectangle((0.15, 0.55), 11.7, 4.05, fc="none", ec=ABU,
                       lw=TIPIS, ls=PUTUS, zorder=1))
ax.text(0.30, 4.45, "di atas wahana — identik pada kelima agen",
        fontsize=8.5, style="italic", color=ABU, va="top")

snr = kotak(0.70, 2.85, 2.5, 0.95, "2× sensor jarak\ndiagonal 45°\nestimasi $w_e$")
esp = kotak(4.00, 2.75, 4.0, 1.10,
            "companion computer\nXIAO ESP32-S3\nIAPF + ERC berbasis kejadian")
fcb = kotak(3.80, 1.35, 4.4, 0.95,
            "flight controller SpeedyBee F405 Mini\nArduPilot racikan (EKF3 + EXTNAV)", fs=7.6)
esc = kotak(8.75, 1.35, 2.9, 0.95, "ESC 4-in-1\n4× motor BLDC")

panah(net["bawah"], esp["atas"], "", )
ax.text(6.18, 4.72, "pose absolut lima agen", fontsize=7.5, ha="left",
        va="center", zorder=5, bbox=dict(fc="white", ec="none", pad=1.2))
panah(snr["kanan"], esp["kiri"], "jarak")
panah((esp["cx"]-0.7, esp["y"]), (esp["cx"]-0.7, fcb["y"]+fcb["h"]),
      "setpoint posisi\nUART · MAVLink", geser=-2.05)
panah((esp["cx"]+0.9, fcb["y"]+fcb["h"]), (esp["cx"]+0.9, esp["y"]),
      "state", ls=(0,(4,2.5)), geser=0.70)
panah(fcb["kanan"], esc["kiri"], "")
ax.text((fcb["x"]+fcb["w"]+esc["x"])/2, fcb["y"]+fcb["h"]+0.14, "DShot",
        fontsize=7.5, ha="center", va="bottom", zorder=5)
ax.add_patch(FancyArrowPatch((esp["x"]+esp["w"], esp["cy"]+0.30), (11.55, esp["cy"]+0.30),
             arrowstyle="<|-|>", mutation_scale=9, lw=0.9, color="black",
             linestyle=(0,(4,2.5)), zorder=2))
ax.text(9.85, esp["cy"]+0.46, "siaran UDP antar-wahana\nposisi dan kecepatan\nke/dari 4 agen lain",
        fontsize=7.5, ha="center", va="bottom", linespacing=1.5)

ax.text(6.0, 0.18, "kamera atas berperan sebagai lokalisasi; sensor pada wahana berperan sebagai persepsi",
        ha="center", va="bottom", fontsize=8, style="italic")

ax.set_xlim(0, 12); ax.set_ylim(0, 9.9); ax.axis("off")
simpan(fig, "arsitektur-sistem")
