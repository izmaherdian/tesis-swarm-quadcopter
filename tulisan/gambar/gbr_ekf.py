"""Diagram blok fusi sensor EKF."""
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from gaya import LEBAR, CM, GARIS, TIPIS, ABU, PUTUS, FS, FS_KECIL, kotak, panah, garis, simpan

fig, ax = plt.subplots(figsize=(LEBAR, 6.4 * CM))
B = dict(fs=FS_KECIL)

imu = kotak(ax, 0.2, 3.775, 2.9, 1.1, "IMU\n$\\mathbf{a}_B,\\ \\boldsymbol{\\omega}_B$", **B)
cam = kotak(ax, 0.2, 0.975, 2.9, 1.1, "kamera atas\n$x,\\ y,\\ z,\\ \\psi$", **B)

ax.add_patch(Rectangle((4.0, 0.35), 5.3, 5.3, fc="none", ec="black", lw=TIPIS, ls=PUTUS))
ax.text(4.15, 5.52, "EKF", fontsize=FS, va="top", style="italic")
pre = kotak(ax, 4.6, 3.55, 4.1, 1.55, "prediksi\n$\\hat{\\mathbf{x}}_{k|k-1},\\ \\mathbf{P}_{k|k-1}$", **B)
upd = kotak(ax, 4.6, 0.75, 4.1, 1.55, "pembaruan\n$\\mathbf{K}_k,\\ \\hat{\\mathbf{x}}_{k|k},\\ \\mathbf{P}_{k|k}$", **B)
tunda = kotak(ax, 8.72, 2.62, 0.62, 0.52, "$z^{-1}$", **B)

panah(ax, imu["kanan"], pre["kiri"], "$\\mathbf{u}_{k-1}$", dy=0.25)
panah(ax, cam["kanan"], upd["kiri"], "$\\mathbf{z}_k$", dy=0.25)
panah(ax, pre["bawah"], upd["atas"])
garis(ax, [upd["x"] + upd["w"], tunda["cx"]], [upd["cy"], upd["cy"]])
panah(ax, (tunda["cx"], upd["cy"]), (tunda["cx"], tunda["y"]))
garis(ax, [tunda["cx"], tunda["cx"]], [tunda["y"] + tunda["h"], pre["cy"]])
panah(ax, (tunda["cx"], pre["cy"]), (pre["x"] + pre["w"], pre["cy"]))

llc = kotak(ax, 10.9, 3.775, 2.9, 1.1, "pengendali\ntingkat rendah", **B)
hlp = kotak(ax, 10.9, 0.975, 2.9, 1.1, "perencana\ntingkat tinggi", **B)
garis(ax, [9.03, 10.2], [2.1, 2.1])
garis(ax, [10.2, 10.2], [hlp["cy"], llc["cy"]])
panah(ax, (10.2, llc["cy"]), llc["kiri"])
panah(ax, (10.2, hlp["cy"]), hlp["kiri"])
ax.text(9.62, 2.2, "$\\hat{\\mathbf{x}}_{k|k}$", fontsize=FS_KECIL, ha="center", va="bottom")

ax.set_xlim(0, 14); ax.set_ylim(0.2, 5.8); ax.axis("off")
simpan(fig, "ekf")
