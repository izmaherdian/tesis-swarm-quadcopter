"""Sumber angka tunggal untuk gambar dan tabel perancangan.

Setiap nilai di sini punya sumber: pengukuran lapangan (docs/03-lab/), keputusan
perancangan (docs/02-keputusan/), atau MultiAgentConfig.py simulator.
"""
import math

# ── Ruang (docs/03-lab/1-ruang-uji-dan-arena.md; ukur lapangan, ±5 cm) ─
H_PLAFON   = 3.00      # m
W_KORIDOR  = 2.70      # m, lebar bersih lengan koridor
L_SEGMEN   = 7.20      # m, panjang segmen uji

# ── Wahana (foto 06, 09-11) ────────────────────────────────────────────
W_WAHANA, L_WAHANA, H_WAHANA = 0.25, 0.21, 0.08   # m
D_SALURAN  = 0.105     # m, diameter luar saluran propeler
R_WAHANA   = W_WAHANA / 2
TIANG      = 0.07      # m, tinggi tiang penyangga penanda

# ── Kamera: ELP-U3GS05B10C-IB21 (docs/03-lab/foto/18, KP03) ─────────
NPX_PANJANG, NPX_PENDEK = 2592, 1944
PIKSEL      = 2.2e-6   # m, ukuran piksel
SENSOR_W, SENSOR_H = 5.737e-3, 4.312e-3   # m, larik aktif OG05B10
F_LENSA     = 2.1e-3   # m, lensa CS 2,1 mm
HFOV_ELP    = 150.0    # derajat, dicantumkan ELP untuk lensa IB21
FPS         = 60       # MJPEG 2592x1944 pada USB 3.0
H_TERBANG   = 1.20     # m
PENANDA     = 0.12     # m, sisi penanda AprilTag
PX_MINIMUM, PX_NYAMAN = 48, 80

# ── Arena (docs/03-lab/1-ruang-uji-dan-arena.md bagian 2) ──────────────
K_SKALA    = 0.90
CELAH      = 0.90      # m
KANAL      = 1.80      # m
KOLOM_W, KOLOM_D = 0.60, 0.79

# ── Simulator (MultiAgentConfig.py @ 0d7ed5a) ──────────────────────────
TOPOLOGI = [(1.0, 0.0), (0.0, -0.5), (0.0, 0.5), (-1.0, 1.0), (-1.0, -1.0)]
ALPHA, R_SIM = 8, 0.2


def liputan(h_terbang=H_TERBANG):
    """Liputan dan resolusi satu kamera pada bidang puncak wahana, model lubang jarum."""
    d = H_PLAFON - (h_terbang + H_WAHANA)
    panjang, lebar = d * SENSOR_W / F_LENSA, d * SENSOR_H / F_LENSA
    mm_px = d * PIKSEL / F_LENSA * 1000
    return dict(d=d, panjang=panjang, lebar=lebar, mm_px=mm_px,
                px10=100 / mm_px, px12=120 / mm_px,
                tumpang=2 * panjang - L_SEGMEN,
                hfov=2 * math.degrees(math.atan(SENSOR_W / 2 / F_LENSA)))


def px_ekuidistan(x, y, sisi=PENANDA, h_terbang=H_TERBANG):
    """Piksel sisi penanda di (x, y) dari sumbu optik bila lensa berproyeksi ekuidistan.

    Batas pesimistis untuk lensa sudut lebar terdistorsi: arah radial menyusut cos^2(theta),
    arah tangensial theta/tan(theta).
    """
    d = H_PLAFON - (h_terbang + H_WAHANA)
    th = math.atan(math.hypot(x, y) / d)
    pusat = sisi / (d * PIKSEL / F_LENSA)
    if th == 0:
        return pusat, pusat
    return pusat * math.cos(th) ** 2, pusat * th / math.tan(th)


if __name__ == "__main__":
    g = liputan()
    print(f"Plafon {H_PLAFON} m, terbang {H_TERBANG} m, jarak {g['d']:.2f} m, lensa {F_LENSA*1e3:.1f} mm")
    print(f"lubang jarum: HFOV {g['hfov']:.1f} deg (ELP: {HFOV_ELP:.0f}) | liputan {g['panjang']:.2f} x {g['lebar']:.2f} m "
          f"| {g['mm_px']:.2f} mm/px | penanda 10 cm {g['px10']:.1f} px, 12 cm {g['px12']:.1f} px "
          f"| tumpang tindih 2 kamera {g['tumpang']:.2f} m")
    for x, y in ((0, 0), (0, W_KORIDOR / 2), (g['panjang'] / 2, 0), (g['panjang'] / 2, W_KORIDOR / 2)):
        r, t = px_ekuidistan(x, y)
        print(f"ekuidistan di ({x:.2f}, {y:.2f}) m: radial {r:.0f} px, tangensial {t:.0f} px")
