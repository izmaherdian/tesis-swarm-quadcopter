"""Sumber angka tunggal untuk gambar dan tabel perancangan.

Setiap nilai di sini punya sumber: pengukuran lapangan (docs/lab/), keputusan
perancangan (docs/keputusan/), atau MultiAgentConfig.py simulator.
"""
import math

# ── Ruang (docs/lab/analisis-kelayakan.md; ukur lapangan, galat ±5 cm) ──
H_PLAFON   = 3.00      # m
W_KORIDOR  = 2.70      # m, lebar bersih lengan koridor
L_SEGMEN   = 7.20      # m, panjang segmen uji

# ── Wahana (foto 06, 09-11) ────────────────────────────────────────────
W_WAHANA, L_WAHANA, H_WAHANA = 0.25, 0.21, 0.08   # m
D_SALURAN  = 0.105     # m, diameter luar saluran propeler
R_WAHANA   = W_WAHANA / 2
TIANG      = 0.07      # m, tinggi tiang penyangga penanda

# ── Kamera: ELP 5 MP global shutter, lensa 120° (keputusan penulis) ────
NPX_PANJANG, NPX_PENDEK = 2592, 1944
FOV_DERAJAT = 120.0
H_TERBANG   = 1.20     # m
PENANDA     = 0.12     # m, sisi penanda AprilTag
PX_MINIMUM, PX_NYAMAN = 48, 80

# ── Arena (docs/lab/analisis-kelayakan.md bagian 11) ───────────────────
K_SKALA    = 0.90
CELAH      = 0.90      # m
KANAL      = 1.80      # m
KOLOM_W, KOLOM_D = 0.60, 0.79

# ── Simulator (MultiAgentConfig.py @ 0d7ed5a) ──────────────────────────
TOPOLOGI = [(1.0, 0.0), (0.0, -0.5), (0.0, 0.5), (-1.0, 1.0), (-1.0, -1.0)]
ALPHA, R_SIM = 8, 0.2


def liputan(h_terbang=H_TERBANG, tafsiran="horizontal"):
    """Liputan satu kamera pada bidang puncak wahana, sensor 4:3."""
    d = H_PLAFON - (h_terbang + H_WAHANA)
    setengah = math.radians(FOV_DERAJAT) / 2
    if tafsiran == "horizontal":
        th = setengah
        tv = math.atan(math.tan(th) * 3 / 4)
    else:                                   # diagonal 4:3 -> 4:3:5
        th = math.atan(math.tan(setengah) * 4 / 5)
        tv = math.atan(math.tan(setengah) * 3 / 5)
    panjang, lebar = 2 * d * math.tan(th), 2 * d * math.tan(tv)
    mm_px = panjang / NPX_PANJANG * 1000
    return dict(d=d, panjang=panjang, lebar=lebar, mm_px=mm_px,
                px10=100 / mm_px, px12=120 / mm_px,
                tumpang=2 * panjang - L_SEGMEN)


if __name__ == "__main__":
    print(f"Plafon {H_PLAFON} m, terbang {H_TERBANG} m, sensor {NPX_PANJANG}x{NPX_PENDEK}, lensa {FOV_DERAJAT:.0f}°\n")
    for taf in ("horizontal", "diagonal"):
        g = liputan(tafsiran=taf)
        print(f"[{taf:>10}] jarak {g['d']:.2f} m | liputan {g['panjang']:.2f} x {g['lebar']:.2f} m "
              f"| {g['mm_px']:.2f} mm/px | penanda 10 cm {g['px10']:.0f} px, 12 cm {g['px12']:.0f} px "
              f"| tumpang tindih 2 kamera {g['tumpang']:.2f} m | lebar lorong tertutup: {g['lebar'] >= W_KORIDOR}")
    for h in (1.0, 1.2, 1.5):
        a, b = liputan(h, "horizontal"), liputan(h, "diagonal")
        print(f"terbang {h:.1f} m: 12 cm = {a['px12']:.0f} px (horiz) / {b['px12']:.0f} px (diag); "
              f"tumpang tindih {a['tumpang']:.2f} / {b['tumpang']:.2f} m")
