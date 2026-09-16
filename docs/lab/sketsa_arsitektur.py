"""Diagram arsitektur sistem menyeluruh (aliran data kamera -> motor).

Menghasilkan tulisan/proposal/figures/arsitektur-sistem.png.
"""
import os
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, FancyArrowPatch

fig, ax = plt.subplots(figsize=(13.5, 9.6))
C = dict(sensor="#2E86AB", darat="#6A4C93", wahana="#EF476F",
         fc="#1B9AAA", aktuator="#F4A261", jaringan="#06938C")

def box(x, y, w, h, teks, warna, fs=9.5, tebal=True, alpha=.16):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.10",
                                fc=warna, ec=warna, lw=2, alpha=alpha, zorder=2))
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.10",
                                fc="none", ec=warna, lw=2, zorder=3))
    ax.text(x+w/2, y+h/2, teks, ha="center", va="center", fontsize=fs,
            fontweight="bold" if tebal else "normal", color="#1a1a1a", zorder=4,
            linespacing=1.45)
    return (x+w/2, y, x+w/2, y+h, x, y+h/2, x+w, y+h/2)

def panah(p1, p2, label="", warna="#444", gaya="-|>", off=0.0, fs=8.2, lw=1.9, ls="-"):
    ax.add_patch(FancyArrowPatch(p1, p2, arrowstyle=gaya, mutation_scale=17,
                                 color=warna, lw=lw, linestyle=ls,
                                 shrinkA=2, shrinkB=2, zorder=5))
    if label:
        ax.text((p1[0]+p2[0])/2 + off, (p1[1]+p2[1])/2, label, fontsize=fs,
                color=warna, ha="center", va="center", fontweight="bold", zorder=6,
                bbox=dict(fc="w", ec="none", alpha=.92, boxstyle="round,pad=0.15"))

# ── Zona darat ──────────────────────────────────────────────────────
ax.add_patch(Rectangle((0.2, 6.55), 11.6, 3.15, fc=C["darat"], alpha=.05,
                       ec=C["darat"], lw=1.4, ls=(0,(6,4)), zorder=1))
ax.text(0.45, 9.48, "DI DARAT", fontsize=10.5, color=C["darat"], fontweight="bold")

k1 = box(1.0, 8.55, 2.5, 0.85, "Kamera atas 1\n4K · HFOV ±109°", C["sensor"], 8.6)
k2 = box(4.0, 8.55, 2.5, 0.85, "Kamera atas 2\n(liputan bertumpang tindih)", C["sensor"], 8.0)
gcs = box(8.6, 8.55, 2.9, 0.85, "Stasiun Kendali Darat\n(telemetri & darurat)", C["darat"], 8.4)
viz = box(1.6, 6.95, 5.3, 1.05,
          "Stasiun Pemroses Citra\ndeteksi AprilTag → PnP → pose 3D lima agen", C["darat"], 9)

panah((k1[0], k1[1]), (viz[0]-1.3, viz[3]))
panah((k2[0], k2[1]), (viz[0]+1.3, viz[3]))

# ── Jaringan ────────────────────────────────────────────────────────
net = box(3.6, 5.35, 4.8, 0.78, "Jaringan Wi-Fi lokal  ·  soket UDP", C["jaringan"], 9.2)
panah((viz[0], viz[1]), (net[0]-0.9, net[3]), "pose absolut", C["jaringan"], off=-0.85)
panah((gcs[0], gcs[1]), (net[0]+1.6, net[3]), "MAVLink", C["darat"], off=0.0)

# ── Zona wahana ─────────────────────────────────────────────────────
ax.add_patch(Rectangle((0.2, 0.35), 11.6, 4.55, fc=C["wahana"], alpha=.05,
                       ec=C["wahana"], lw=1.4, ls=(0,(6,4)), zorder=1))
ax.text(0.45, 4.62, "DI ATAS WAHANA   (identik pada kelima agen)", fontsize=10.5,
        color=C["wahana"], fontweight="bold")

snr = box(0.75, 2.85, 2.5, 0.95, "2× sensor jarak\ndiagonal 45°\n→ estimasi $w_e$", C["sensor"], 8.4)
esp = box(4.05, 2.75, 3.9, 1.15,
          "Companion Computer\nXIAO ESP32-S3\nIAPF + ERC (berbasis kejadian)", C["wahana"], 9)
fcb = box(4.05, 1.25, 3.9, 1.05,
          "Flight Controller — SpeedyBee F405 Mini\nArduPilot racikan · EKF3 + EXTNAV", C["fc"], 8.6)
esc = box(8.75, 1.25, 2.6, 1.05, "ESC 4-in-1\nBLS 35A Mini\n→ 4× motor BLDC", C["aktuator"], 8.6)

panah((net[0], net[1]), (esp[0], esp[3]), "pose absolut\nlima agen", C["jaringan"], off=1.15, fs=7.8)
panah((snr[6], snr[7]), (esp[4], esp[5]), "jarak", C["sensor"], fs=8)
panah((esp[0], esp[1]), (fcb[0], fcb[3]), "UART · MAVLink\nsetpoint posisi", C["wahana"], off=-1.5, fs=7.8)
panah((fcb[6], fcb[7]), (esc[4], esc[5]), "DShot", C["aktuator"], fs=8)
panah((fcb[0]+1.1, fcb[3]), (esp[0]+1.1, esp[1]), "state\nestimasi", C["fc"],
      off=1.35, fs=7.6, lw=1.4, ls=(0,(4,3)))

# siaran antar-wahana
ax.add_patch(FancyArrowPatch((esp[6], esp[5]+0.22), (11.45, esp[5]+0.22),
                             arrowstyle="<|-|>", mutation_scale=15,
                             color=C["jaringan"], lw=1.8, ls=(0,(5,3)), zorder=5))
ax.text(9.75, esp[5]+0.52, "siaran UDP antar-wahana\n(posisi & kecepatan)\nke/dari 4 agen lain",
        fontsize=7.8, color=C["jaringan"], ha="center", va="bottom", fontweight="bold")

ax.text(6.0, 0.55,
        "Pemisahan peran dijaga tegas:  kamera atas = LOKALISASI (di mana saya)  ·  "
        "sensor onboard = PERSEPSI (apa di sekitar saya)",
        ha="center", fontsize=8.8, style="italic", color="#333",
        bbox=dict(fc="#FFF3B0", ec="#D4A017", lw=1.2, boxstyle="round,pad=0.4"))

ax.set_xlim(0, 12); ax.set_ylim(0.1, 9.9); ax.axis("off")
ax.set_title("Arsitektur Sistem Menyeluruh — Aliran Data dari Kamera hingga Motor",
             fontsize=13.5, fontweight="bold", pad=10)
plt.tight_layout()
OUT = "tulisan/proposal/figures/arsitektur-sistem.png"
os.makedirs(os.path.dirname(OUT), exist_ok=True)
plt.savefig(OUT, dpi=135, bbox_inches="tight", facecolor="w")
print("✓", OUT)
