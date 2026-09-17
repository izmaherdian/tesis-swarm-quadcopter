# Inventaris Perangkat Keras

> Diperbarui 2026-09-17. Sumber: 17 foto di `foto/` (dibaca langsung) dan
> konfirmasi lisan dari peneliti. Kolom bertanda **?** belum terdata.

## 1. Wahana dan komponen terbang

| Komponen | Spesifikasi | Jumlah | Sumber |
|---|---|---|---|
| Rangka *cinewhoop* SpeedyBee Bee35 | Propeler bersaluran, $25 \times 21 \times 8$ cm | **6** — 2 siap terbang, 2 terpasang sebagian, 2 rangka kosong | foto 07, 08 |
| Motor BLDC | **2006 – 1950 KV** | 4 per wahana terpasang | foto 15 |
| ESC | SpeedyBee **BLS 35A Mini** 4-in-1, BLHeli\_S | **3** (asumsi penulis 2026-09-17) | konfirmasi peneliti |
| *Flight controller* | SpeedyBee **F405 Mini** — STM32F405 (flash 1 MB), IMU ICM-42688P, barometer DSP-310 | **3** (asumsi penulis 2026-09-17) | foto 14 + dok. ArduPilot |
| Penerima kendali radio | **ExpressLRS EP2 TCXO** 2,4 GHz | **3** | foto 13 + konfirmasi peneliti |
| *Companion computer* | Seeed Studio **XIAO ESP32-S3** — Wi-Fi 2,4 GHz + BLE, USB-C | **3** (asumsi penulis 2026-09-17) | foto 16 |
| Modul navigasi | **RUSHFPV GNSS 25+** — mesin u-Blox M10 (GPS/GLONASS/BDS/Galileo), kompas **HMC5883**, 115200 baud, masukan 5 V, antena tipe T | **?** | foto 12 |
| Dudukan modul navigasi | Cetakan 3D, terpasang di tengah-depan bodi | terpasang | foto 17 |
| Baterai LiPo | $4 \times 1200$ mAh · $2 \times 1500$ mAh · $1 \times 2200$ mAh · $2 \times 5000$ mAh | **9** | foto 07, 08 |
| Propeler cadangan | Tiga bilah | beberapa | foto 07, 08 |
| Saluran (*duct*) cadangan | Cincin kuning | beberapa | foto 07, 08 |
| Kartu program ESC | Turnigy AeroStar | 1 | foto 07, 08 |

### Foto 13 — teridentifikasi

Papan berbungkus *heatshrink* dengan empat kabel pada foto 13 adalah **penerima
ExpressLRS EP2 TCXO** (konfirmasi peneliti, 2026-09-16). Tersedia **3 unit**;
**pemancarnya belum ada**.

## 2. Perangkat darat

| Komponen | Status | Keterangan |
|---|---|---|
| Pengisi daya baterai LiPo | ✅ tersedia | model **?** |
| Kontainer penyimpanan baterai LiPo | ✅ tersedia | konfirmasi penulis 2026-09-17 |
| Komputer stasiun darat | ✅ tersedia | CPU, RAM, jumlah port USB3 **?** — menentukan apakah deteksi penanda dua kamera 4K dapat berjalan seketika |
| Router Wi-Fi khusus | ✅ tersedia | model dan pita frekuensi **?** |
| Pencetak tiga dimensi + filamen | ✅ tersedia | untuk dudukan penanda dan sensor |

## 3. Belum tersedia — masuk rencana pengadaan

Fase mengikuti BAB IV proposal. Harga dan sumbernya: [`survei-harga.md`](survei-harga.md).

| Komponen | Kebutuhan | Fase |
|---|---|---|
| **Pemancar ExpressLRS** (RadioMaster Pocket) | Pengambilalihan manual dan penghentian darurat | **Fase 2** — sebelum terbang pertama |
| Kamera USB 5 MP *global shutter*, lensa 120° | Lokalisasi | Fase 2 (unit ke-1), Fase 4 (unit ke-2) |
| Kabel USB ekstensi 10 m + dudukan langit-langit | Lokalisasi | Fase 2 (1 set), Fase 4 (1 set) |
| Sensor ultrasonik HC-SR04 | Kandidat A persepsi rintangan | Fase 2 (2 unit) |
| Sensor jarak laser VL53L1X | Kandidat B persepsi rintangan | Fase 2 (2 unit) |
| Sensor jarak terpilih | Lima wahana × 2 dikurangi 2 unit uji banding | Fase 4 (8 unit) |
| Penanda AprilTag + akrilik + tiang | Lokalisasi | Fase 2 (1 set), Fase 4 (4 set) |
| Kacamata pengaman | 1 unit (tas baterai tidak perlu, jaring tidak perlu — keputusan penulis) | Fase 4 — sebelum uji terbang tunggal |
| Penerima ExpressLRS EP2 TCXO | 5 wahana − 3 tersedia | Fase 4 (2 unit) |
| *Stack* SpeedyBee F405 Mini + ESC BLS 35A | 5 wahana − 3 tersedia | Fase 4 (2 set) |
| XIAO ESP32-S3 | 5 wahana − 3 tersedia | Fase 4 (2 unit) |
| Dus kardus rintangan | Arena | Fase 4 (10 unit) |
| Lakban penanda posisi lantai | Arena | Fase 4 |

### 🔴 Catatan keselamatan

**Penerima kendali radio sudah ada (3 × EP2 TCXO), pemancarnya belum.** Tanpa
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
