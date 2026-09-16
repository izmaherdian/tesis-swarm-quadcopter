"""Diagram blok arsitektur sistem: aliran data kamera hingga motor."""
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch
from gaya_gambar import simpan, TEBAL, TIPIS, PUTUS, ABU

# Kanvas lega beresolusi proporsional
fig, ax = plt.subplots(figsize=(9.4, 8.2))

def kotak(x, y, w, h, teks, fs=7.8, fc="white", ec="#1e293b", lw=1.0):
    ax.add_patch(Rectangle((x, y), w, h, fc=fc, ec=ec, lw=lw, zorder=3,
                           joinstyle="round"))
    ax.text(x+w/2, y+h/2, teks, ha="center", va="center", fontsize=fs,
            color="#0f172a", zorder=4, linespacing=1.45)
    return dict(x=x, y=y, w=w, h=h, cx=x+w/2, cy=y+h/2,
                atas=(x+w/2, y+h), bawah=(x+w/2, y),
                kiri=(x, y+h/2), kanan=(x+w, y+h/2))

def panah(p1, p2, teks="", fs=7.2, ls="-", dua=False, geser_x=0.0, geser_y=0.0,
          warna="#0f172a", bbox_bg="white", ec_box="#cbd5e1"):
    ax.add_patch(FancyArrowPatch(p1, p2,
                 arrowstyle="<|-|>" if dua else "-|>", mutation_scale=9,
                 lw=0.95, color=warna, linestyle=ls, shrinkA=1, shrinkB=1, zorder=2))
    if teks:
        ax.text((p1[0]+p2[0])/2 + geser_x, (p1[1]+p2[1])/2 + geser_y, teks, fontsize=fs,
                ha="center", va="center", zorder=5, color=warna,
                bbox=dict(fc=bbox_bg, ec=ec_box, lw=0.6, pad=1.5,
                          boxstyle="round,pad=0.25"))

# ─────────────────────────────────────────────────────────────
# 1. ZONA DARAT (GROUND SYSTEM)
# ─────────────────────────────────────────────────────────────
ax.add_patch(Rectangle((0.30, 6.90), 12.80, 3.40, fc="#f8fafc", ec="#94a3b8",
                       lw=1.0, ls=PUTUS, zorder=1))
ax.text(0.55, 10.15, "SISTEM DI DARAT", fontsize=8.2, fontweight="bold",
        color="#475569", va="top")

# Baris 1: Kamera & GCS
k1  = kotak(0.60, 8.85, 3.10, 0.90, "Kamera Atas 1\n4K, HFOV ±109°\n(Pemantau Agen 1--3)")
k2  = kotak(4.00, 8.85, 3.30, 0.90, "Kamera Atas 2\n4K, HFOV ±109°\n(Liputan Tumpang Tindih)")
gcs = kotak(9.80, 8.85, 3.00, 0.90, "Stasiun Kendali Darat\nTelemetri & Komando\n(Protokol MAVLink)")

# Baris 2: Pemroses Citra
viz = kotak(1.60, 7.20, 6.20, 1.05,
            "Stasiun Pemroses Citra (PC Ground)\nDeteksi AprilTag → Estimasi PnP → Pose 3D Kelima Agen")

# Panah Kamera ke Pemroses Citra
panah(k1["bawah"], (viz["cx"]-1.4, viz["atas"][1]))
panah(k2["bawah"], (viz["cx"]+1.4, viz["atas"][1]))

# ─────────────────────────────────────────────────────────────
# 2. ZONA JARINGAN (NETWORK)
# ─────────────────────────────────────────────────────────────
net = kotak(3.60, 5.50, 6.20, 0.80,
            "Jaringan Wi-Fi Lokal — Protokol Soket UDP",
            fs=8.2, fc="#f0f9ff", ec="#0284c7", lw=1.2)

# Panah dari Darat ke Jaringan
panah(viz["bawah"], (net["cx"]-1.2, net["atas"][1]), "Pose Absolut 5 Agen", geser_x=-0.2)
panah(gcs["bawah"], (net["cx"]+2.0, net["atas"][1]), "MAVLink", geser_x=0.0)

# ─────────────────────────────────────────────────────────────
# 3. ZONA WAHANA (ONBOARD QUADCOPTER - IDENTIK PADA 5 AGEN)
# ─────────────────────────────────────────────────────────────
ax.add_patch(Rectangle((0.30, 0.55), 13.00, 4.45, fc="#f8fafc", ec="#94a3b8",
                       lw=1.0, ls=PUTUS, zorder=1))
ax.text(0.55, 4.82, "SUBSISTEM ONBOARD WAHANA\n(Identik pada tiap agen)",
        fontsize=7.8, fontweight="bold", color="#475569", va="top", linespacing=1.2)

# Lapisan Atas Wahana: Sensor Jarak & Companion Computer
snr = kotak(0.55, 3.15, 3.20, 1.20,
            "2× Sensor Jarak Lateral\nDiagonal 45° (Kiri & Kanan)\nEstimasi Lebar Lorong ($w_e$)")

esp = kotak(4.30, 3.15, 5.20, 1.20,
            "Companion Computer (XIAO ESP32-S3)\nPerencana Gerak IAPF Terdesentralisasi\n+ Logika Rekonfigurasi Formasi ERC",
            fs=7.8, fc="#fffbeb", ec="#d97706", lw=1.1)

# Lapisan Bawah Wahana: Flight Controller & Aktuator
fcb = kotak(4.30, 1.05, 5.20, 1.25,
            "Flight Controller SpeedyBee F405 Mini\nFirmware ArduPilot Copter\n(Kalang Kaskade PID + EKF3 Onboard EXTNAV)",
            fs=7.8, fc="#eff6ff", ec="#2563eb", lw=1.1)

esc = kotak(10.70, 1.05, 2.40, 1.25,
            "ESC 4-in-1\nSpeedyBee BLS 35A\n+ 4× Motor BLDC 2006",
            fs=7.6, fc="#f0fdf4", ec="#16a34a", lw=1.1)

# ─────────────────────────────────────────────────────────────
# KONEKSI & ALIRAN DATA PADA WAHANA
# ─────────────────────────────────────────────────────────────
# Jaringan -> ESP32-S3 (panah vertikal bersih di x=6.80)
panah(net["bawah"], esp["atas"], "Pose Absolut 5 Agen (60 Hz)", geser_x=1.65)

# Sensor Jarak -> ESP32-S3
panah(snr["kanan"], esp["kiri"], "Jarak Lateral\n$d_l, d_r$", geser_y=0.0)

# ESP32-S3 <-> FC SpeedyBee (Jarak vertikal 0.85 lega!)
# Panah turun: Setpoint dari ESP32 ke FC
panah((esp["cx"]-1.3, esp["bawah"][1]), (fcb["cx"]-1.3, fcb["atas"][1]),
      "Setpoint Posisi & Yaw\n(UART MAVLink)", geser_x=-1.35)

# Panah naik: Telemetri dari FC ke ESP32
panah((fcb["cx"]+1.3, fcb["atas"][1]), (esp["cx"]+1.3, esp["bawah"][1]),
      "Telemetri State\nAktual", ls=(0,(4,2.5)), geser_x=1.15)

# FC -> ESC / Motor (Jarak antar kotak 1.20, DShot muat sempurna!)
panah(fcb["kanan"], esc["kiri"], "DShot300\n(Digital DMA)", geser_y=0.22)

# Siaran UDP Antar-Wahana (ke kanan dari ESP32)
ax.add_patch(FancyArrowPatch((esp["kanan"][0], esp["cy"]), (13.15, esp["cy"]),
             arrowstyle="<|-|>", mutation_scale=9, lw=1.0, color="#d97706",
             linestyle=(0,(4,2.5)), zorder=2))
ax.text(11.35, esp["cy"]+0.18,
        "Siaran UDP Antar-Wahana\nPose & Kecepatan Komutatif\n(ke/dari 4 agen lain)",
        fontsize=7.3, ha="center", va="bottom", linespacing=1.35, color="#b45309",
        bbox=dict(fc="#fffbeb", ec="#fcd34d", lw=0.6, pad=1.5, boxstyle="round,pad=0.2"))

# Catatan kaki filosofis arsitektur
ax.text(6.70, 0.18,
        "* Kamera atas berperan sebagai sistem lokalisasi absolut; sensor pada wahana berperan sebagai sistem persepsi lokal.",
        ha="center", va="bottom", fontsize=8.0, style="italic", color="#334155")

ax.set_xlim(0, 13.4); ax.set_ylim(0, 10.5); ax.axis("off")
simpan(fig, "arsitektur-sistem")
