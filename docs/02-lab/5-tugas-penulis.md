# Tugas Penulis — Yang Hanya Bisa Dicek Sendiri

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
[`4-survei-harga.md`](4-survei-harga.md). Tersisa satu hal yang perlu kamu putuskan:

- [x] Pemancar RadioMaster Pocket — Rp2.339.000 (batas atas dari 7 listing).
- [x] Penerima EP2 TCXO — Rp337.000 (batas atas dari 5 listing). Tidak lagi masuk RAB (5 tersedia).
- [x] XIAO ESP32-S3 — Rp282.500 (batas atas dari 4 listing).
- [x] *Stack* F405 Mini + BLS 35A **V1** — Rp1.906.700 (batas atas dari 11 listing).
  Angka lama Rp2.244.428 ternyata produk lain (*kit board metal*). Tidak lagi masuk RAB
  (6 FC tersedia); yang dibeli hanya 1 ESC V2 Rp941.000.
  - [ ] Cek versi ESC pada wahana yang ada (opsional). Perbedaan V1/V2 ada di
    **ESC**-nya (BLS 35A Mini V2), bukan di *flight controller*; halaman resmi
    SpeedyBee untuk *stack* ini kini mencantumkan ESC V2, dan V2 kompatibel
    (20×20, 35A, BLHeli_S). Cara cek: cari tulisan "V2" pada papan ESC (sisi atas
    dan bawah, foto 14 hanya memperlihatkan sisi atas tanpa tanda versi), label
    kotak, atau nota pembelian. Bila ingin anggaran konservatif untuk V2:
    Rp2.151.700–2.646.000 per set.

## C. Inventaris lab (dikerjakan saat di lab)

Isi kolom "Hasil" langsung di sini atau kirim fotonya. Urutan = prioritas.

> **2026-09-17:** inventaris dari penulis sudah dicatat di [`2-inventaris.md`](2-inventaris.md)
> dan analisis baterai di [`3-baterai-dan-bobot.md`](3-baterai-dan-bobot.md). Yang masih
> terbuka tinggal versi ESC, bobot terbang, *firmware* FC, dan perangkat darat (C1, C3, C4).

### C1. Kelengkapan untuk lima wahana

| Data yang dicatat | Hasil |
|---|---|
| Jumlah FC, ESC, XIAO ESP32-S3 (terpasang vs lepas) | ✅ FC 6, ESC 5 (+?; 1 V2 lepas diduga rusak), ESP32-S3 5 |
| Jumlah motor 2006 | ✅ 20 (16 terpasang + 4 cadangan) |
| Propeler | ✅ Gemfan D90S, 14 buah |
| Penerima EP2 TCXO | ✅ 4 terpasang di rangka 1–4, + 1 penerima lepas berbasis ESP8285 |
| Versi ESC (V1/V2) pada wahana terakit | ☐ opsional; cari tulisan "V2" di **sisi bawah** papan ESC, label kotak, atau nota (lihat bagian B) |
| Apakah FC lepas kedua membawa ESC | ☐ |

### C2. Baterai dan daya

| Data yang dicatat | Hasil |
|---|---|
| Tiap baterai (sel, kapasitas, C) | ✅ tercatat; hanya 2 × CNHL 6S 1200 mAh yang cocok ([KP05](../04-keputusan/KP05-baterai-dan-pengadaan.md)) |
| Pengisi daya | ✅ SkyRC T6X80, 80 W ([foto 19](foto/19-pengisi-daya-skyrc.png)) |

### C3. Wahana

| Data yang dicatat | Cara cek | Kenapa perlu | Hasil |
|---|---|---|---|
| **Bobot terbang** satu wahana lengkap | Sementara memakai **perkiraan ≈ 520 g** dari lembar data (batas bawah, rincian di [`3-baterai-dan-bobot.md`](3-baterai-dan-bobot.md#bobot-terbang-satu-wahana)); timbang ulang dengan timbangan dapur digital bila ada | Rasio gaya dorong terhadap bobot dan ruang sisa untuk penanda + sensor | perkiraan ✅, timbang ulang ☐ |
| *Firmware* yang sekarang terpasang di FC (Betaflight/INAV/ArduPilot + versi) | Colok USB, buka Betaflight Configurator atau Mission Planner | Titik awal sebelum dipasang *firmware* ArduPilot racikan | |
| Jumlah modul RUSHFPV GNSS 25+ | Hitung | Hanya inventaris (modul dilepas) — prioritas rendah | ✅ 2 RUSHFPV M10 lepas + 4 GPS di rangka 1–4 |

### C4. Perangkat darat

| Data yang dicatat | Cara cek | Kenapa perlu | Hasil |
|---|---|---|---|
| ~~Komputer stasiun darat~~ | ✅ laptop penulis (Ryzen 5 4500U, 14 GiB, Ubuntu 26.04) | dicatat 2026-09-17 | ✅ |
| Port USB fisik laptop: mana yang terhubung ke pengendali USB 3.1 pertama dan kedua | Colok flashdisk USB 3 bergantian di tiap port, jalankan `lsusb -t` (lihat Bus 002 vs Bus 004) | Dua kamera sebaiknya di pengendali berbeda | |
| Router Wi-Fi: merek/model, **pita 2,4 GHz** tersedia | Label bawah router — router **sudah ada** (konfirmasi penulis 2026-09-17), merek dicek nanti | ESP32-S3 hanya bekerja di 2,4 GHz; seluruh komunikasi MAVLink/UDP lewat router ini | ada ✅, merek ☐ |

## D. Ruang uji

- [x] Denah lama tetap dipakai. Pengujian hanya di **bagian lurus** koridor (lebar
  270 cm, panjang 720–960 cm), bukan persimpangan T (konfirmasi penulis 2026-09-17).
  Ringkasan ruang dan arena: [`1-ruang-uji-dan-arena.md`](1-ruang-uji-dan-arena.md).
- [ ] Pastikan ke pengelola bahwa sofa dan banner boleh dipindah setiap sesi uji.
- [ ] Saat memasang kamera: titik cantol rel plafon dekat 2,35 m dan 4,85 m yang bebas AC
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
