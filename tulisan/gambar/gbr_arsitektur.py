"""Diagram blok arsitektur sistem menyeluruh."""
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from gaya import LEBAR, CM, GARIS, TIPIS, ABU, PUTUS, FS_KECIL, kotak, panah, garis, simpan

fig, ax = plt.subplots(figsize=(LEBAR, 10.2 * CM))
B = dict(fs=FS_KECIL)

# ── stasiun darat ──
ax.add_patch(Rectangle((0.1, 5.6), 13.8, 4.4, fc="none", ec=ABU, lw=TIPIS, ls=PUTUS))
ax.text(0.25, 9.88, "stasiun darat", fontsize=FS_KECIL, style="italic", va="top", color="0.35")
k1  = kotak(ax, 0.5, 8.55, 2.7, 0.85, "kamera K1", **B)
k2  = kotak(ax, 3.6, 8.55, 2.7, 0.85, "kamera K2", **B)
gcs = kotak(ax, 7.0, 8.55, 3.0, 0.85, "stasiun\nkontrol darat", **B)
tx  = kotak(ax, 10.6, 8.55, 3.0, 0.85, "pemancar ELRS", **B)
viz = kotak(ax, 1.05, 7.05, 4.7, 0.95, "pemroses citra\ndeteksi AprilTag, PnP", **B)
net = kotak(ax, 3.7, 5.9, 4.6, 0.7, "jaringan Wi-Fi lokal (UDP)", **B)
panah(ax, k1["bawah"], (viz["cx"] - 1.1, viz["y"] + viz["h"]))
panah(ax, k2["bawah"], (viz["cx"] + 1.1, viz["y"] + viz["h"]))
panah(ax, viz["bawah"], (net["cx"] - 1.2, net["y"] + net["h"]))
panah(ax, gcs["bawah"], (net["cx"] + 1.4, net["y"] + net["h"]), "MAVLink", dx=0.62, ha="left")

# ── setiap wahana ──
ax.add_patch(Rectangle((0.1, 0.1), 13.8, 5.2, fc="none", ec=ABU, lw=TIPIS, ls=PUTUS))
ax.text(0.25, 5.18, "setiap wahana", fontsize=FS_KECIL, style="italic", va="top", color="0.35")
snr = kotak(ax, 0.4, 3.3, 2.6, 1.0, "sensor jarak\n(2 unit)", **B)
esp = kotak(ax, 3.9, 3.2, 4.4, 1.2, "companion computer\nXIAO ESP32-S3\nIAPF + ERC", **B)
rx  = kotak(ax, 10.6, 3.3, 3.0, 1.0, "penerima ELRS\nEP2 TCXO", **B)
fc  = kotak(ax, 3.9, 0.5, 4.4, 1.3, "flight controller\nSpeedyBee F405 Mini\nArduPilot, EKF3", **B)
esc = kotak(ax, 9.2, 0.7, 2.1, 0.9, "ESC 4-in-1", **B)
mot = kotak(ax, 11.8, 0.7, 1.8, 0.9, "4 motor", **B)

panah(ax, net["bawah"], esp["atas"], "pose kelima agen", dx=0.18, ha="left")
panah(ax, snr["kanan"], esp["kiri"], "$d_l, d_r$", dy=0.28)
panah(ax, (esp["cx"] - 1.0, esp["y"]), (esp["cx"] - 1.0, fc["y"] + fc["h"]), "setpoint", dx=-0.15, ha="right")
panah(ax, (esp["cx"] + 1.0, fc["y"] + fc["h"]), (esp["cx"] + 1.0, esp["y"]), "state", dx=0.15, ha="left", gaya=PUTUS)
panah(ax, fc["kanan"], esc["kiri"])
panah(ax, esc["kanan"], mot["kiri"])
panah(ax, tx["bawah"], rx["atas"], "2,4 GHz", dx=0.15, ha="left", gaya=PUTUS)
garis(ax, [rx["cx"], rx["cx"]], [rx["y"], 2.55])
garis(ax, [rx["cx"], 8.95], [2.55, 2.55])
panah(ax, (8.95, 2.55), (fc["x"] + fc["w"], 1.55))
ax.text(10.55, 2.62, "ambil alih manual", fontsize=FS_KECIL, ha="center", va="bottom")
panah(ax, (esp["x"] + esp["w"], esp["y"] + esp["h"] - 0.25), (9.2, 4.75), dua=True, gaya=PUTUS)
ax.text(9.3, 4.75, "agen lain (UDP)", fontsize=FS_KECIL, ha="left", va="center")

ax.set_xlim(0, 14); ax.set_ylim(0, 10.1); ax.axis("off")
simpan(fig, "arsitektur-sistem")
