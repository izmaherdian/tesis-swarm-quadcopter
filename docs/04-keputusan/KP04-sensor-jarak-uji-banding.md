# KP04 — Sensor jarak dipilih lewat uji banding HC-SR04, VL53L1X, MTF-01

**Tanggal:** 2026-09-17 · **Status:** diputuskan (metode pemilihan); sensor belum terpilih
**Terkait:** proposal Subbab "Pemilihan Sensor Jarak" · [inventaris](../02-lab/2-inventaris.md) ·
[survei harga](../02-lab/4-survei-harga.md)

## Konteks

Tiap agen membawa **dua sensor jarak** yang dipasang diagonal bersudut β terhadap arah
maju. Dari pembacaan kiri dan kanan, agen mengestimasi lebar ruang $w_e$ yang memicu ERC.
Pada sudut datang 45° terhadap permukaan halus (dinding berplester, kolom beton), sensor
ultrasonik rawan kehilangan gema karena pantulan bersifat spekular. Kardus memantul
secara baur sehingga lebih ramah, tetapi arena memakai kolom beton sebagai satu sisi celah.
Jenis sensor karenanya **tidak ditetapkan di atas kertas**.

## Kandidat

| Sensor | Prinsip | Data yang tercatat | Ketersediaan | Harga (batas atas) |
|---|---|---|---|---|
| HC-SR04 | ultrasonik | — | beli 2 (Fase 2) | Rp26.600 |
| VL53L1X (modul TOF400C) | laser ToF | 4 cm–4 m, resolusi 1 mm, sudut pandang 27°, I²C, 2,6–3,5 V (deskripsi listing) | beli 2 (Fase 2) | Rp98.500 |
| MicoAir MTF-01 v1.1 | aliran optik + ToF | jangkauan 8 m, sudut pancar setengah 3°, UART 115200 100 Hz, 4,5 g ([MicoAir](https://micoair.com/optical_range_sensor_mtf-01/)) | **3 unit tersedia** di lab | Rp1.565.000 |

MTF-01 ditambahkan sebagai kandidat ketiga atas keputusan penulis (2026-09-17) karena
sudah tersedia di lab.

## Dasar keputusan

| Dasar | Sumber | Isi yang dipakai |
|---|---|---|
| Data lab | [ruang uji](../02-lab/1-ruang-uji-dan-arena.md) | sisi celah berupa kolom beton, dinding berplester, dan dus kardus |
| Data lab | [inventaris](../02-lab/2-inventaris.md) | 3 unit MTF-01 sudah tersedia |
| Pustaka | `borensteinObstacleAvoidanceUltrasonic1988`, `siegwartIntroductionAutonomousMobile2004` | pantulan spekular ultrasonik pada permukaan halus bersudut datang miring |
| Pustaka | `pedroSenseAvoidSystem2025` | rancangan sistem *sense and avoid* pada UAV kecil |
| Lembar data | `micoairMTF01`, deskripsi listing VL53L1X | jangkauan, sudut pancar, antarmuka, laju |
| Listing | [survei harga](../02-lab/4-survei-harga.md) | Rp26.600, Rp98.500, Rp1.565.000 |
| Keputusan penulis | 2026-09-17 | MTF-01 masuk sebagai kandidat ketiga karena sudah ada |
| **Belum ada data** | uji banding Fase 2 | keberhasilan baca pada 45°, sebaran galat, laju dua sensor |

## Keputusan

Ketiga kandidat diuji banding pada **Fase 2** dengan kriteria yang ditetapkan **sebelum**
pengujian (sama dengan proposal):

1. tingkat keberhasilan pembacaan pada sudut 45° dan 90° terhadap dinding berplester,
   kolom beton, dan permukaan kardus;
2. sebaran galat pembacaan terhadap jarak acuan;
3. laju pembaruan yang dapat dicapai untuk **dua sensor sekaligus**.

Sensor yang memenuhi kriteria dengan margin terbesar dipakai untuk kelima wahana. Bila
seluruh kandidat gagal pada 45°, sudut pemasangan diperkecil lalu konsekuensinya terhadap
jangkauan deteksi ke depan dievaluasi ulang. Uji banding dirancang sebagai eksperimen di
`05-eksperimen/` sebelum dijalankan.

## Anggaran

| Pos | Fase | Nilai di RAB |
|---|---|---|
| 2 HC-SR04 + 2 VL53L1X untuk uji banding | 2 | Rp53.200 + Rp197.000 |
| 8 sensor terpilih (10 untuk lima wahana − 2 dari uji banding) | 4 | memakai harga VL53L1X, 8 × Rp98.500 = Rp788.000 |
| bila HC-SR04 terpilih | 4 | 8 × Rp26.600 = Rp212.800 |
| bila MTF-01 terpilih | 4 | 3 tersedia, kurang 7; **naskah hanya menulis harga satuan tertinggi Rp1.565.000** (keputusan penulis), tidak masuk subtotal |

## Yang perlu diperhatikan saat uji

- MTF-01 memakai UART. Dua sensor ditambah tautan MAVLink ke FC berarti tiga jalur serial
  pada XIAO ESP32-S3; ketersediaan pin dan UART perangkat kerasnya dicek sebelum uji.
- HC-SR04 bekerja pada 5 V, sedangkan logika ESP32-S3 3,3 V; pin *echo* butuh pembagi
  tegangan atau modul setara.
- Hasil negatif (mis. semua kandidat buruk pada kolom beton) ditulis apa adanya di
  Keterbatasan Penelitian.
