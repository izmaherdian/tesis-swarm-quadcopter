# Tugas Penulis — Yang Hanya Bisa Dicek Sendiri

> Dibuat 2026-09-17, diperbarui 2026-09-22. Hal-hal yang tidak bisa dipastikan dari lingkungan kerja Claude
> (halaman Tokopedia dan SCImago terblokir, atau butuh pengecekan fisik di lab).
> Centang bila sudah, lalu kabari supaya naskah dan anggaran diperbarui.

## A. Harga (Tokopedia)

- [x] **Kamera ELP-U3GS05B10C-IB21** — Rp6.600.000 (Fast Importir), lensa 2,1 mm
  harga sama, **pra-pesan 3 minggu**. Lembar data: `foto/18-datasheet-kamera-elp-og05b10.png`.
  - [ ] Saat kamera pertama tiba (Fase 2): kalibrasi intrinsik + distorsi, lalu
    ukur piksel sisi penanda 12 cm di tengah, di tepi koridor, dan di ujung liputan.
    Menentukan apakah dua kamera cukup (lihat risiko distorsi di BAB III).
- [x] **VL53L1X** — Rp98.500 (CNC Store Bandung).
- [x] **Lakban lantai 3M 764** — Rp55.000 (Dewielectrical), **harga sama untuk semua varian
  warna** (konfirmasi penulis 2026-09-22). Warna **putih** karena lantai gelap.
- [x] Kabel USB 3.0 aktif 10 m, dudukan *super clamp*, HC-SR04, akrilik A4, kertas
  stiker vinil, kardus — listing Tokopedia (batas atas) sudah di RAB.
- [x] **Perlengkapan keselamatan:** 1 kacamata pengaman (Rp113.220). Tas baterai tidak perlu
  karena kontainer lab tersedia; jaring pengaman tidak diperlukan.

## B. Harga yang sudah diisi

Sudah diperiksa langsung di halaman Tokopedia (2026-09-17), detail per listing di
[`4-survei-harga.md`](4-survei-harga.md). Tersisa satu hal yang perlu kamu putuskan:

- [x] Pemancar RadioMaster Pocket — Rp2.339.000 (batas atas dari 7 listing).
- [x] Penerima EP2 TCXO — Rp337.000 (batas atas dari 5 listing). Tidak lagi masuk RAB (5 tersedia).
- [x] XIAO ESP32-S3 — Rp282.500 (batas atas dari 4 listing).
- [x] *Stack* F405 Mini + BLS 35A **V1** — Rp1.906.700 (batas atas dari 11 listing).
  Angka lama Rp2.244.428 ternyata produk lain (*kit board metal*). Tidak lagi masuk RAB
  (6 FC tersedia); yang dibeli hanya 1 ESC V2 Rp941.000.
  - [x] Versi ESC pada wahana yang ada adalah **V2** (konfirmasi penulis 2026-09-22),
    sama dengan unit yang dianggarkan, sehingga tidak ada risiko ketidakcocokan.

## C. Inventaris lab (dikerjakan saat di lab)

Isi kolom "Hasil" langsung di sini atau kirim fotonya. Urutan = prioritas.

> **2026-09-22:** inventaris dan versi ESC sudah tuntas. Yang masih terbuka tinggal **bobot
> terbang terukur**, ***firmware*** **FC yang sekarang terpasang**, serta perangkat darat
> (pemetaan port USB dan merek router).

### C1. Kelengkapan untuk lima wahana

| Data yang dicatat | Hasil |
|---|---|
| Jumlah FC, ESC, XIAO ESP32-S3 (terpasang vs lepas) | ✅ FC 6, ESC 5 (semua V2; 1 lepas diduga rusak), ESP32-S3 5 |
| Jumlah motor 2006 | ✅ 20 (16 terpasang + 4 cadangan) |
| Propeler | ✅ Gemfan D90S, 14 buah |
| Penerima EP2 TCXO | ✅ 4 terpasang di rangka 1–4, + 1 penerima lepas berbasis ESP8285 |
| Versi ESC (V1/V2) pada wahana terakit | ✅ **V2** (konfirmasi penulis 2026-09-22) |
| Apakah FC lepas kedua membawa ESC | ✅ tidak; ESC total tetap 5 unit (4 terpasang + 1 lepas diduga rusak) |

### C2. Baterai dan daya

| Data yang dicatat | Hasil |
|---|---|
| Tiap baterai (sel, kapasitas, C) | ✅ tercatat; hanya 2 × CNHL 6S 1200 mAh yang cocok ([KP05](../04-keputusan/KP05-baterai-dan-pengadaan.md)) |
| Pengisi daya | ✅ SkyRC T6X80, 80 W ([foto 19](foto/19-pengisi-daya-skyrc.png)) |

### C3. Wahana

| Data yang dicatat | Cara cek | Kenapa perlu | Hasil |
|---|---|---|---|
| **Bobot terbang** satu wahana lengkap | Memakai **perkiraan ≈ 520 g** dari lembar data (keputusan penulis 2026-09-22, tidak ditimbang) | Rasio gaya dorong terhadap bobot dan taksiran waktu terbang | ✅ perkiraan lembar data dipakai |
| *Firmware* yang sekarang terpasang di FC (Betaflight/INAV/ArduPilot + versi) | Colok USB, buka Betaflight Configurator atau Mission Planner, lihat nama dan versi *firmware* | Menentukan apakah papan sudah memakai *bootloader* ArduPilot. Bila masih Betaflight atau INAV, pemasangan ArduPilot racikan butuh langkah DFU untuk memasang *bootloader* lebih dulu, dan urutan nomor motor berbeda sehingga harus dipetakan ulang. Dicek saat mau *flash* di Fase 2, tidak menghambat proposal | ☐ (Fase 2) |
| Jumlah modul RUSHFPV GNSS 25+ | Hitung | Hanya inventaris (modul dilepas) — prioritas rendah | ✅ 2 RUSHFPV M10 lepas + 4 GPS di rangka 1–4 |

### C4. Perangkat darat

| Data yang dicatat | Cara cek | Kenapa perlu | Hasil |
|---|---|---|---|
| ~~Komputer stasiun darat~~ | ✅ laptop penulis (Ryzen 5 4500U, 14 GiB, Ubuntu 26.04) | dicatat 2026-09-17 | ✅ |
| Port USB fisik laptop: mana yang terhubung ke pengendali USB 3.1 pertama dan kedua | Colok flashdisk USB 3 bergantian di tiap port, jalankan `lsusb -t` (lihat Bus 002 vs Bus 004) | Dua kamera sebaiknya di pengendali berbeda | |
| Router Wi-Fi: merek/model, **pita 2,4 GHz** tersedia | — | ESP32-S3 hanya bekerja di 2,4 GHz; seluruh komunikasi MAVLink/UDP lewat router ini | ✅ **TP-Link Archer C54**, AC1200 dwipita, 2,4 GHz tersedia (2026-09-22) |

## D. Ruang uji

- [x] Denah lama tetap dipakai. Pengujian hanya di **bagian lurus** koridor (lebar
  270 cm, panjang 720–960 cm), bukan persimpangan T (konfirmasi penulis 2026-09-17).
  Ringkasan ruang dan arena: [`1-ruang-uji-dan-arena.md`](1-ruang-uji-dan-arena.md).
- [x] Sofa dan banner **aman dipindah** setiap sesi uji (konfirmasi penulis 2026-09-22),
  sehingga lebar bersih penuh 270 cm tersedia dan syarat pemicu ERC terpenuhi.
- [ ] Saat memasang kamera: titik cantol rel plafon dekat 2,12 m dan 5,08 m yang bebas AC
  kaset, lampu, dan *sprinkler*.

## E. Pustaka

Rincian di [`../03-pustaka/kuartil-jurnal.md`](../03-pustaka/kuartil-jurnal.md).

- [x] Kuartil dibaca langsung dari widget resmi SCImago (SJR 2025).
  Intelligent Service Robotics = **Q1** (sesuai penulis).
- [x] Dua rujukan Q3 (Abro 2025, Kurochkin 2021) tetap dipakai.
- [x] Argiliana 2025 = tesis S2, entri bib diubah jadi `@mastersthesis`.
- [x] **Perhatian:** J. King Saud Univ. – Engineering Sciences (paper penulis)
  berkuartil terbaik **Q2** pada SJR 2025, bukan Q1.
- [x] Lima rujukan 2018–2020 yang bukan metode fundamental diganti rujukan
  2023–2026 berkuartil Q1 (rincian di kuartil-jurnal.md).
