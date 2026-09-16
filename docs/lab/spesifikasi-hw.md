# Inventaris Perangkat Keras

> Diperbarui 2026-09-16. Sumber: 17 foto di `foto/` (dibaca langsung) dan
> konfirmasi lisan dari peneliti. Kolom bertanda **?** belum terdata.

## 1. Wahana dan komponen terbang

| Komponen | Spesifikasi | Jumlah | Sumber |
|---|---|---|---|
| Rangka *cinewhoop* SpeedyBee Bee35 | Propeler bersaluran, $25 \times 21 \times 8$ cm | **6** — 2 siap terbang, 2 terpasang sebagian, 2 rangka kosong | foto 07, 08 |
| Motor BLDC | **2006 – 1950 KV** | 4 per wahana terpasang | foto 15 |
| ESC | SpeedyBee **BLS 35A Mini** 4-in-1, BLHeli\_S | 4 | konfirmasi peneliti |
| *Flight controller* | SpeedyBee **F405 Mini** — STM32F405 (flash 1 MB), IMU ICM-42688P, barometer DSP-310 | 4 | foto 14 + dok. ArduPilot |
| *Companion computer* | Seeed Studio **XIAO ESP32-S3** — Wi-Fi 2,4 GHz + BLE, USB-C | 1 (**?** apakah ada lagi) | foto 16 |
| Modul navigasi | **RUSHFPV GNSS 25+** — mesin u-Blox M10 (GPS/GLONASS/BDS/Galileo), kompas **HMC5883**, 115200 baud, masukan 5 V, antena tipe T | **?** | foto 12 |
| Dudukan modul navigasi | Cetakan 3D, terpasang di tengah-depan bodi | terpasang | foto 17 |
| Baterai LiPo | $4 \times 1200$ mAh · $2 \times 1500$ mAh · $1 \times 2200$ mAh · $2 \times 5000$ mAh | **9** | foto 07, 08 |
| Propeler cadangan | Tiga bilah | beberapa | foto 07, 08 |
| Saluran (*duct*) cadangan | Cincin kuning | beberapa | foto 07, 08 |
| Kartu program ESC | Turnigy AeroStar | 1 | foto 07, 08 |

### ⚠️ Komponen belum teridentifikasi

Foto 13 memperlihatkan papan mungil berbungkus *heatshrink* bening, dipasang di
atas busa peredam, dengan **empat kabel** (merah, hitam, kuning, hijau). Peneliti
menamainya "IMU", namun *flight controller* sudah memuat IMU ICM-42688P sehingga
identitas papan ini belum pasti. Tulisan yang terbaca pada papannya:
**`1281 2343 45909`** — pola tersebut lebih menyerupai kode lot atau tanggal
produksi daripada nomor komponen, sehingga belum cukup untuk identifikasi.
Resolusi foto (720 × 1280) tidak memadai untuk dibaca ulang.

**Cara memastikan:** foto lebih dekat pada papannya, atau telusuri keempat kabel
ke pena mana pada *flight controller* (UART menandakan penerima atau modul
serial; I\textsuperscript{2}C menandakan sensor).

## 2. Perangkat darat

| Komponen | Status | Keterangan |
|---|---|---|
| Pengisi daya baterai LiPo | ✅ tersedia | model **?** |
| Komputer stasiun darat | ✅ tersedia | CPU, RAM, jumlah port USB3 **?** — menentukan apakah deteksi penanda dua kamera 4K dapat berjalan seketika |
| Router Wi-Fi khusus | ✅ tersedia | model dan pita frekuensi **?** |
| Pencetak tiga dimensi + filamen | ✅ tersedia | untuk dudukan penanda dan sensor |

## 3. Belum tersedia — masuk rencana pengadaan

| Komponen | Kebutuhan | Tahap RAB |
|---|---|---|
| **Kendali radio (pemancar + penerima)** | Pengambilalihan manual dan penghentian darurat | **Tahap 1 — keselamatan** |
| Kamera atas 4K + lensa sudut lebar | Lokalisasi | Tahap 1 (unit ke-1), Tahap 2 (unit ke-2) |
| Sensor ultrasonik HC-SR04 | Kandidat A persepsi rintangan | Tahap 1 (2 unit), Tahap 2 (sisanya) |
| Sensor jarak laser VL53L1X | Kandidat B persepsi rintangan | Tahap 1 (2 unit) |
| Penanda AprilTag + akrilik + tiang | Lokalisasi | Tahap 1 (1 set), Tahap 2 (4 set) |
| Dus kardus rintangan | Arena | Tahap 3 |
| Perlengkapan keselamatan | Tas tahan api, jaring, kacamata | Tahap 3 |

### 🔴 Catatan keselamatan

**Tautan kendali radio belum tersedia.** Tanpa itu, satu-satunya jalur
penghentian darurat adalah MAVLink melalui Wi-Fi — dan apabila justru jaringan
Wi-Fi yang bermasalah, tidak ada jalan keluar tersisa. Untuk uji terbang lima
wahana di koridor yang juga dipakai orang lain, ini risiko yang tidak dapat
diterima. Pengadaannya dinaikkan ke Tahap 1 dan prosedur keselamatan pada naskah
harus menyebutkan mekanisme pengambilalihan manual secara eksplisit.

## 4. Yang masih perlu didata

1. Spesifikasi komputer stasiun darat (CPU, RAM, port USB3).
2. Model pengisi daya LiPo dan router Wi-Fi.
3. Identitas papan pada foto 13.
4. Jumlah unit XIAO ESP32-S3 dan modul RUSHFPV GNSS.
5. Ukuran propeler (perkiraan 3,5 inci dari kelas rangka — belum dipastikan).
6. Bobot terbang wahana lengkap dengan baterai.
