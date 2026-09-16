# Spesifikasi Perangkat Keras

> Diisi tanggal: `<YYYY-MM-DD>` · Kolom yang belum diketahui tulis `?`.
> Kalau ragu, foto saja label/stiker perangkatnya ke `foto/` — saya bisa baca.

## 1. Kamera atas — **PRIORITAS 2**

| Besaran | Nilai | Kenapa ditanya |
|---|---|---|
| Merek & model | `?` | |
| Sudah ada di lab atau harus dibeli? | `?` | RAB Rp1.500.000 sudah dialokasikan |
| Resolusi maksimum | `?` px | menentukan ukuran tag minimum |
| **FPS pada resolusi penuh** | `?` | proposal mengasumsikan 60 FPS |
| FPS pada resolusi diturunkan | `?` | sering jadi kompromi yang dipakai |
| **Rolling atau global shutter?** | `?` | **paling kritis** — rolling shutter membuat pose melenceng saat wahana bergerak |
| FOV horizontal / panjang fokus | `?`° atau `?` mm | menentukan luas liputan |
| Lensa bisa diganti? | `?` | kalau liputan kurang, ini jalan keluarnya |
| Antarmuka | USB2 / USB3 / CSI / IP | USB2 membatasi FPS pada resolusi tinggi |
| Panjang kabel bawaan | `?` m | |

> Kalau spesifikasi tidak diketahui: **foto stiker/label di badan kamera dan
> lensanya.** Dari situ biasanya bisa ditelusuri.

## 2. PC stasiun darat — **PRIORITAS 2**

Harus sanggup mendeteksi 5 tag pada laju kamera secara *real-time*.

| Besaran | Nilai |
|---|---|
| CPU | `?` |
| RAM | `?` GB |
| GPU (kalau ada) | `?` |
| Sistem operasi | `?` |
| Jumlah port USB3 | `?` |
| Milik lab atau laptop pribadi? | `?` |

## 3. Flight controller — **PRIORITAS 2**

| Besaran | Nilai | Kenapa ditanya |
|---|---|---|
| Model | SpeedyBee F4 Mini (?) | |
| **Firmware terpasang** | Betaflight / INAV / ArduPilot / PX4 / `?` | **kritis** — lihat catatan di bawah |
| Versi firmware | `?` | |
| Target build | `?` | |
| Port UART yang masih bebas | `?` | untuk jalur ke companion computer |
| Punya barometer? | `?` | cadangan sumbu z |

> ⚠️ **Ini penentu besar.** Menyuntikkan posisi eksternal (dari kamera atas)
> ke FC butuh firmware yang mendukungnya: ArduPilot dan PX4 mendukung penuh,
> INAV terbatas, **Betaflight praktis tidak**. Kalau ternyata Betaflight, ada
> dua jalan: ganti firmware, atau pindahkan seluruh kalang posisi ke companion
> computer dan kirim hanya perintah sikap ke FC. Keduanya mengubah rencana
> kerja, jadi lebih cepat diketahui lebih baik.

## 4. Companion computer — **PRIORITAS 2**

| Besaran | Nilai |
|---|---|
| Model board | ESP32-S3 (varian?) |
| RAM / PSRAM | `?` |
| Sudah terpasang di wahana? | `?` |
| Cara flash yang dipakai | Arduino / ESP-IDF / PlatformIO |

## 5. Wahana quadcopter — **PRIORITAS 2**

| Besaran | Nilai |
|---|---|
| **Jumlah unit sudah terakit & bisa terbang** | `?` dari 5 |
| Jumlah unit masih berupa komponen | `?` |
| Rangka | SpeedyBee 35 (?) |
| Diagonal / *wheelbase* | `?` mm |
| **Lebar total termasuk propeler** | `?` mm ← penting untuk margin koridor 1,0 m |
| Ukuran propeler | `?` inci |
| Bobot terbang | `?` g |
| Baterai | `?` S, `?` mAh |
| Perkiraan lama terbang | `?` menit |
| Ada pelindung propeler (*prop guard*)? | `?` |
| Ruang datar di atas bodi untuk tag | `?` × `?` mm |

## 6. Sensor ultrasonik — **PRIORITAS 3**

| Besaran | Nilai |
|---|---|
| Model | HC-SR04 (?) |
| Jumlah tersedia | `?` (RAB merencanakan 10) |
| Sudah terpasang di wahana? | `?` |
| Jangkauan terukur efektif | `?` m |

## 7. Modul UWB — **PRIORITAS 3**

Hanya untuk mencatat status; UWB berstatus opsional (lihat
`docs/keputusan/KP01-lokalisasi-apriltag.md`).

| Besaran | Nilai |
|---|---|
| Sudah punya modul? | ya / tidak |
| Model | DWM1000 / DW3000 / `?` |
| Jumlah unit | `?` |
| Pernah dicoba sebelumnya? | `?` |

## 8. Perangkat lain yang tersedia di lab

Kadang ada aset yang tidak terpikir tapi mengubah rencana — misalnya OptiTrack,
LiDAR, atau kamera lain.

> `<daftar di sini>`
