# Daftar yang Perlu Dicari Penulis

> Dibuat 2026-09-17. Hal-hal yang tidak bisa dipastikan dari lingkungan kerja Claude
> (halaman Tokopedia dan SCImago terblokir, atau butuh pengecekan fisik di lab).
> Centang bila sudah, lalu kabari supaya naskah dan anggaran diperbarui.

## A. Harga (Tokopedia)

- [x] **Kamera ELP-U3GS05B10C-IB21** — Rp6.600.000 (Fast Importir), lensa 2,1 mm
  harga sama, **pra-pesan 3 minggu**. Lembar data: `foto/18-datasheet-kamera-elp-og05b10.png`.
  - [ ] Saat kamera pertama tiba (Fase 2): kalibrasi intrinsik + distorsi, lalu
    ukur piksel sisi penanda 12 cm di tengah, di tepi koridor, dan di ujung liputan.
    Menentukan apakah dua kamera cukup (lihat risiko distorsi di BAB III).
- [x] **VL53L1X** — Rp98.500 (CNC Store Bandung).
- [x] **Lakban lantai 3M 764** — Rp55.000 (Dewielectrical). Pilih warna **putih atau
  kuning** karena lantai gelap.
- [x] Kabel USB 3.0 aktif 10 m, dudukan *super clamp*, HC-SR04, akrilik A4, kertas
  stiker vinil, kardus — listing Tokopedia (batas atas) sudah di RAB.
- [x] **Perlengkapan keselamatan:** 1 kacamata pengaman (Rp113.220). Tas baterai tidak perlu
  karena kontainer lab tersedia; jaring pengaman tidak diperlukan.

## B. Harga yang sudah diisi

Sudah diperiksa langsung di halaman Tokopedia (2026-09-17), detail per listing di
[`survei-harga.md`](survei-harga.md). Tersisa satu hal yang perlu kamu putuskan:

- [x] Pemancar RadioMaster Pocket — Rp2.339.000 (batas atas dari 7 listing).
- [x] Penerima EP2 TCXO — Rp337.000 (batas atas dari 5 listing).
- [x] XIAO ESP32-S3 — Rp282.500 (batas atas dari 4 listing).
- [x] *Stack* F405 Mini + BLS 35A **V1** — Rp1.906.700 (batas atas dari 11 listing).
  Angka lama Rp2.244.428 ternyata produk lain (*kit board metal*).
  - [ ] Cek versi ESC pada wahana yang ada (opsional). Perbedaan V1/V2 ada di
    **ESC**-nya (BLS 35A Mini V2), bukan di *flight controller*; halaman resmi
    SpeedyBee untuk *stack* ini kini mencantumkan ESC V2, dan V2 kompatibel
    (20×20, 35A, BLHeli_S). Cara cek: cari tulisan "V2" pada papan ESC (sisi atas
    dan bawah, foto 14 hanya memperlihatkan sisi atas tanpa tanda versi), label
    kotak, atau nota pembelian. Bila ingin anggaran konservatif untuk V2:
    Rp2.151.700–2.646.000 per set.

## C. Inventaris lab (dikerjakan saat di lab)

Isi kolom "Hasil" langsung di sini atau kirim fotonya. Urutan = prioritas.

> **2026-09-17:** inventaris dari penulis sudah dicatat di `spesifikasi-hw.md` dan
> analisis baterai di `analisis-baterai.md`. Propeler = Gemfan D90S dan pengisi daya =
> SkyRC T6X80 (dikonfirmasi). Yang masih terbuka: bobot terbang, firmware FC, dan
> perangkat darat (C3–C4).

### C1. Kelengkapan untuk lima wahana — **menentukan RAB**

| Data yang dicatat | Cara cek | Kenapa perlu | Hasil |
|---|---|---|---|
| Jumlah *flight controller* F405 Mini, ESC BLS 35A, dan XIAO ESP32-S3, dipisah **terpasang** vs **cadangan** | Hitung per rangka + isi kotak/lemari | RAB menganggap masing-masing 3 unit, sehingga membeli 2 set | |
| **Jumlah motor 2006** yang ada (terpasang + cadangan) | Hitung per rangka | Tercatat 4 rangka sudah bermotor (16 motor). Wahana kelima dari rangka kosong butuh 4 motor lagi, **dan motor belum ada di RAB** | |
| Propeler: **ukuran (inci), pitch, jumlah bilah**, dan jumlah cadangan | Tulisan di bilah propeler, mis. "3.5x2.8x3" | Menentukan gaya dorong, dan apakah perlu beli cadangan untuk 5 wahana | |
| Penerima EP2 TCXO: sudah terpasang di wahana mana saja | Lihat kabel ke FC | RAB membeli 2 unit untuk wahana ke-4 dan ke-5 | |
| Versi ESC (V1/V2) | Tulisan "V2" di papan ESC, kotak, atau nota | Lihat bagian B | |

### C2. Baterai dan daya

| Data yang dicatat | Cara cek | Kenapa perlu | Hasil |
|---|---|---|---|
| Tiap baterai: **jumlah sel (S)**, kapasitas, rating C, jenis konektor (XT30/XT60) | Label baterai | Inventaris baru mencatat kapasitas (4×1200, 2×1500, 1×2200, 2×5000 mAh) tanpa jumlah sel; menentukan waktu terbang, bobot, dan apakah 5 wahana bisa memakai baterai seragam | |
| Pengisi daya: merek/model, jumlah port, arus maksimum | Label pengisi daya | Berapa baterai bisa diisi per sesi uji | |

### C3. Wahana

| Data yang dicatat | Cara cek | Kenapa perlu | Hasil |
|---|---|---|---|
| **Bobot terbang** satu wahana lengkap (baterai, ESP32, penerima, tanpa modul GNSS) | Timbangan dapur | Rasio gaya dorong terhadap bobot dan ruang sisa untuk penanda + sensor | |
| *Firmware* yang sekarang terpasang di FC (Betaflight/INAV/ArduPilot + versi) | Colok USB, buka Betaflight Configurator atau Mission Planner | Titik awal sebelum dipasang *firmware* ArduPilot racikan | |
| Jumlah modul RUSHFPV GNSS 25+ | Hitung | Hanya inventaris (modul dilepas) — prioritas rendah | |

### C4. Perangkat darat

| Data yang dicatat | Cara cek | Kenapa perlu | Hasil |
|---|---|---|---|
| Komputer stasiun darat: **CPU, RAM, sistem operasi** | Linux: `lscpu`, `free -h` · Windows: Task Manager → Performance | Deteksi AprilTag dari dua kamera 5 MP 60 fps berjalan di komputer ini | |
| **Jumlah port USB 3.0** dan apakah berada di pengendali USB berbeda | Linux: `lsusb -t` · Windows: Device Manager; port USB 3.0 biasanya biru/berlogo SS | Tiap kamera USB 3.0 sebaiknya di jalur sendiri agar tidak berebut *bandwidth* | |
| Router Wi-Fi: merek/model, **pita 2,4 GHz** tersedia | Label bawah router | ESP32-S3 hanya bekerja di 2,4 GHz; seluruh komunikasi MAVLink/UDP lewat router ini | |

## D. Ruang uji

- [x] Denah lama tetap dipakai. Pengujian hanya di **bagian lurus** koridor (lebar
  270 cm, panjang 720–960 cm), bukan persimpangan T (konfirmasi penulis 2026-09-17).

## E. Pustaka

Rincian di [`../pustaka/kuartil-jurnal.md`](../pustaka/kuartil-jurnal.md).

- [x] Kuartil dibaca langsung dari widget resmi SCImago (SJR 2025).
  Intelligent Service Robotics = **Q1** (sesuai penulis).
- [x] Dua rujukan Q3 (Abro 2025, Kurochkin 2021) tetap dipakai.
- [x] Argiliana 2025 = tesis S2, entri bib diubah jadi `@mastersthesis`.
- [x] **Perhatian:** J. King Saud Univ. – Engineering Sciences (paper penulis)
  berkuartil terbaik **Q2** pada SJR 2025, bukan Q1.
- [x] Lima rujukan 2018–2020 yang bukan metode fundamental diganti rujukan
  2023–2026 berkuartil Q1 (rincian di kuartil-jurnal.md).
