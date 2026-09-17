# Inventaris Perangkat Keras

> Diperbarui 2026-09-17 (inventaris lengkap dari penulis). Sumber: 18 foto di `foto/`
> dan daftar inventaris yang dicatat penulis di lab. Kolom bertanda **?** belum pasti.

## 1. Wahana dan komponen terbang

### 1a. Per rangka (SpeedyBee Bee35)

| Rangka | Isi | Belum ada |
|---|---|---|
| 1 | FC + ESC, XIAO ESP32-S3, EP2 TCXO, 4 motor, GPS (GOKU GM10?), antena, kabel baterai | propeler |
| 2 | Seperti rangka 1, bentuk rangka sedikit berbeda, **+ sensor MTF-01** | propeler |
| 3 | Seperti rangka 2 | propeler |
| 4 | Seperti rangka 1, **tanpa antena** | propeler, antena |
| 5–6 | Rangka kosong | semua komponen |

### 1b. Rekap jumlah

| Komponen | Spesifikasi | Terpasang | Lepas | Total | Catatan |
|---|---|---:|---:|---:|---|
| Rangka *cinewhoop* SpeedyBee Bee35 | propeler bersaluran, 25 × 21 × 8 cm | 4 | 2 kosong | **6** | |
| *Flight controller* SpeedyBee F405 Mini ("F4 Mini") | STM32F405 (flash 1 MB), ICM-42688P, DSP-310 | 4 | 2 | **6** | satu lepas masih terhubung ESC yang diduga rusak; satu lepas sudah berkabel baterai dan kapasitor |
| ESC SpeedyBee BLS 35A Mini 4-in-1 | BLHeli\_S | 4 | 1 (+?) | **5 (+?)** | yang lepas = **V2, diduga rusak**; apakah FC lepas kedua juga membawa ESC **?** |
| Motor SpeedyBee 2006-1950KV | | 16 | 4 | **20** | cukup untuk 5 wahana |
| Propeler Gemfan **D90S** | 3 bilah, 90 mm, *T-mount* 1,5 mm | 0 | 14 | **14** | 5 wahana butuh 20 |
| Seeed XIAO ESP32-S3 | Wi-Fi 2,4 GHz + BLE | 4 | 1 | **5** | cukup untuk 5 wahana |
| Penerima ExpressLRS EP2 TCXO | 2,4 GHz | 4 | — | **4** | + 1 "ELRS" lepas, jenis **?** |
| Sensor MicoAir MTF-01 v1.1 | aliran optik + ToF 8 m, sudut pancar setengah 3°, UART 115200 100 Hz, 4,5 g ([MicoAir](https://micoair.com/optical_range_sensor_mtf-01/)) | 2 | 1 | **3** | **kandidat ketiga uji banding sensor jarak** (keputusan penulis 2026-09-17) |
| Modul GNSS | GPS pada rangka 1–4; RUSHFPV M10 + HMC5883 | 4 | 2 | **6** | tidak dipakai (dalam ruangan) |
| Antena | dipol tipe-T 2,4 GHz/915 MHz; dipol mini 2,4/5,8 GHz IPEX | — | 1 + 3 | **4** | dipol mini dapat untuk rangka 4 |
| Pelindung dan *holder* kuning | cadangan saluran dan penyangga | — | 2 paket | **2 paket** | |
| Kartu program Turnigy AeroStar | untuk ESC Turnigy AeroStar | — | 2 | **2** | **tidak untuk BLS 35A** (BLHeli\_S dikonfigurasi lewat PC/FC) |

### 1c. Baterai LiPo

Analisis kecocokan: [`analisis-baterai.md`](analisis-baterai.md).

| Baterai | Sel | Kapasitas | C | Jumlah | Cocok untuk Bee35 1950KV |
|---|---|---:|---|---:|---|
| CNHL Pizza Series | **6S** 22,2 V | 1200 mAh | 100C | 2 | ✅ |
| CNHL Speedy Pizza | 4S 14,8 V | 1200 mAh | 100C | 2 | ❌ terbang (hanya uji meja) |
| Gens Ace | 5S 18,5 V | 5000 mAh | 40C | 2 | ❌ |
| Onbo lithium polymer | 4S 14,8 V | 2200 mAh | 50C | 1 | ❌ |
| Onbo Nano Power | 3S 11,1 V | 1500 mAh | 25C | 2 | ❌ |
| LPB Power | 2S/3S | 1500 mAh | 20–25C | 1 | ❌ |

## 2. Perangkat darat

| Komponen | Status | Keterangan |
|---|---|---|
| Pengisi daya baterai LiPo | ✅ 1 | **SkyRC T6X80** *balance charger/discharger* AC/DC, 1–6S, maks. 80 W ([foto 19](foto/19-pengisi-daya-skyrc.png)) |
| Papan pengisian paralel Power Genius 2-in-1 | ✅ 1 | 2–6S, untuk mengisi beberapa baterai bersel sama sekaligus |
| SkyRC multi balance board | ✅ 1 | adaptor *balance* 2–6S |
| Kontainer penyimpanan baterai LiPo | ✅ tersedia | konfirmasi penulis 2026-09-17 |
| Komputer stasiun darat | ✅ laptop penulis | **Lenovo 82FN, AMD Ryzen 5 4500U** (6 inti/6 utas), memori 14 GiB terbaca, **Ubuntu 26.04**, Wi-Fi 6 Intel AX200; **dua pengendali USB 3.1** terpisah (tiap kamera dapat di pengendali sendiri; jumlah port fisik per pengendali **?**). Kemampuan deteksi AprilTag dua kamera 5 MP 60 fps diukur di Fase 2 |
| Router Wi-Fi khusus | ✅ tersedia | model dan pita frekuensi **?** |
| Pencetak tiga dimensi + filamen | ✅ tersedia | untuk dudukan penanda dan sensor |

## 3. Belum tersedia — masuk rencana pengadaan

Fase mengikuti BAB IV proposal. Harga dan sumbernya: [`survei-harga.md`](survei-harga.md).

| Komponen | Kebutuhan | Fase |
|---|---|---|
| **Pemancar ExpressLRS** (RadioMaster Pocket) | Pengambilalihan manual dan penghentian darurat | **Fase 2** — sebelum terbang pertama |
| Kamera ELP-U3GS05B10C-IB21 | Lokalisasi | Fase 2 (unit ke-1), Fase 4 (unit ke-2) |
| Kabel USB 3.0 aktif 10 m + dudukan *super clamp* | Lokalisasi | Fase 2 (1 set), Fase 4 (1 set) |
| Sensor ultrasonik HC-SR04 | Kandidat persepsi rintangan | Fase 2 (2 unit) |
| Sensor jarak laser VL53L1X | Kandidat persepsi rintangan | Fase 2 (2 unit) |
| Sensor jarak terpilih | Lima wahana × 2 dikurangi 2 unit uji banding | Fase 4 (8 unit) |
| Akrilik A4 + kertas stiker vinil | Penanda AprilTag (tiang dicetak 3D) | Fase 2 (1 lembar + 1 pak), Fase 4 (2 lembar) |
| Kacamata pengaman | 1 unit (tas baterai dan jaring tidak perlu — keputusan penulis) | Fase 4 — sebelum uji terbang tunggal |
| ESC SpeedyBee BLS 35A Mini V2 | Wahana kelima (ESC lepas diduga rusak) | Fase 4 (1 unit) |
| XIAO ESP32-S3 | Cadangan (5 sudah tersedia) — keputusan penulis | Fase 4 (1 unit) |
| Propeler Gemfan D90S 3 bilah (isi 4, tipe dikonfirmasi penulis) | 20 untuk 5 wahana − 14 tersedia | Fase 4 (2 paket = 8 buah) |
| Baterai CNHL Pizza 6S 1200 mAh 100C | Total 6 baterai 6S (5 wahana + 1 cadangan) − 2 tersedia | Fase 4 (4 unit) |
| Dus kardus rintangan | Arena | Fase 4 (10 unit) |
| Lakban penanda posisi lantai | Arena | Fase 4 |

Tidak perlu dibeli lagi: motor (20 tersedia), *flight controller* (6 tersedia), penerima
ExpressLRS (5 tersedia; yang lepas berbasis ESP8285).

### 🔴 Catatan keselamatan

**Penerima kendali radio sudah ada (5 unit), pemancarnya belum.** Tanpa
pemancar, satu-satunya jalur penghentian darurat adalah MAVLink melalui Wi-Fi —
dan apabila justru jaringan Wi-Fi yang bermasalah, tidak ada jalan keluar
tersisa. Pemancar karenanya diadakan pada **Fase 2**, dan pengambilalihan manual
diuji sebelum terbang pertama.

## 4. Yang masih perlu didata

1. Spesifikasi komputer stasiun darat (CPU, RAM, port USB3).
2. Model pengisi daya LiPo dan router Wi-Fi.
3. ~~Identitas papan pada foto 13~~ → EP2 TCXO (2026-09-16).
4. Jumlah modul RUSHFPV GNSS. FC/ESC dan XIAO ESP32-S3 untuk sementara dianggap
   3 unit (keputusan penulis 2026-09-17) — pastikan saat inventaris ulang.
5. Ukuran propeler (perkiraan 3,5 inci dari kelas rangka — belum dipastikan).
6. Bobot terbang wahana lengkap dengan baterai.
