# Analisis Kelayakan Lab — Hasil Pembacaan Foto & Denah

> Dibuat 2026-09-16 dari 17 foto + denah tulisan tangan di `foto/`.
> Semua ukuran ruangan bergalat ±5 cm (dinyatakan sendiri pada denah).
>
> **Video `video/00-video-ruangan.mp4` tidak dapat dibaca** — seluruh 1081 frame
> ter-*decode* hitam (`min=0 max=0`); `ffmpeg` tidak terpasang di mesin ini.
> Analisis di bawah **tidak memakai video sama sekali**.

## 1. Ruangan

Koridor-L institusi (area pelatihan CITA ITB), **bukan ruang lab tertutup**.

| Besaran | Nilai |
|---|---|
| Tinggi plafon | **300 cm** |
| Lebar lengan lorong | **270 cm** |
| Panjang lengan | 720 cm (sisi dalam) – 960 cm (sisi luar) |
| Segmen lain | 290, 435, 480, 620 cm |
| Kolom di dalam area | 4 buah, 45–60 cm |
| Status akses | **bisa dipakai eksklusif dengan penjadwalan** |

**Plafon:** gipsum tile di rangka-T gantung. Berisi lampu TL *troffer*, *downlight*
bulat, **AC kaset**, sprinkler, detektor asap. Rangka-T hanya kuat menahan beban
ringan — dudukan kamera harus mencantol ke rel rangka atau ke struktur di atasnya,
tidak bisa disekrup ke tile.

**Cahaya:** campuran TL + *downlight* + **jendela besar** (foto 02, 04). Cahaya
matahari berubah sepanjang hari → *auto-exposure* harus dikunci manual saat
merekam data, kalau tidak deteksi tag ikut berfluktuasi.

**Lantai:** ubin abu gelap berukuran besar, memantul. Kontras bagus untuk tag
putih, tapi pantulan lampu berpotensi menimbulkan deteksi palsu.

**Catatan lain:** ada **kipas industri besar** beroda di koridor (foto 02) —
kalau itu memang rencana sumber gangguan angin, perlu dicatat spesifikasinya
karena proposal menguji ketahanan terhadap hembusan angin.

## 2. Liputan kamera — kendala yang mengikat

Plafon 300 cm, wahana setinggi 8 cm ⇒ jarak kamera–penanda hanya **1,4–1,9 m**.

Karena lebar lorong 270 cm wajib tertutup dan sensor berformat 16:9, **liputan
memanjang terkunci di 4,80 m** (= 2,70 × 16/9) **berapa pun ketinggian terbang.**
Ketinggian hanya menggeser lensa yang dibutuhkan:

| Terbang | Jarak kamera | HFOV dibutuhkan | Liputan |
|---|---|---|---|
| 1,0 m | 1,92 m | 103° | 4,80 × 2,70 m |
| 1,2 m | 1,72 m | **109°** | 4,80 × 2,70 m |
| 1,5 m | 1,42 m | 119° | 4,80 × 2,70 m |

### Rencana 2 kamera (sesuai pilihan: satu lengan penuh)

| Sasaran | Liputan 2 kamera | Tumpang tindih | Penilaian |
|---|---|---|---|
| Lengan **7,20 m** | 9,60 m | **2,40 m** | ✅ lega, aman untuk serah-terima antar kamera |
| Lengan **9,60 m** | 9,60 m | **0 m** | ❌ tanpa tumpang tindih — tidak bisa dikalibrasi jadi satu kerangka |

**Rekomendasi: bidik segmen 7,20 m.** Tumpang tindih 2,40 m cukup untuk
menyatukan kedua kamera ke satu kerangka acuan global dan untuk menangani
perpindahan wahana antar-liputan. Kalau 9,60 m penuh yang diinginkan, butuh
**3 kamera**, bukan 2.

## 3. Ukuran AprilTag

Pada liputan 4,80 m, dengan target 80 piksel per tag (deteksi andal saat bergerak):

| Resolusi | mm/piksel | Tag minimum | Muat di wahana? |
|---|---|---|---|
| 1080p | 2,50 | 20 cm | ❌ menutupi duct |
| 1440p | 1,88 | 15 cm | ❌ menutupi duct |
| **4K** | **1,25** | **10 cm** | ✅ |

Wahananya **cinewhoop ber-*duct*** (SpeedyBee Bee35), 25 × 21 × 8 cm. Seluruh
permukaan atas terisi duct; area datar di tengah hanya beberapa sentimeter dan
masih ditempati **modul GPS** serta strap baterai.

**Kenapa tidak boleh asal menutup duct:** propeler ber-*duct* mengisap udara dari
atas. Pelat tag yang menutup mulut duct akan menggerus daya angkat secara
langsung — bukan masalah kecil pada wahana indoor yang sudah terbatas dayanya.

**Jalan keluar yang disarankan:** kamera 4K + **lepas modul GPS** (tidak dipakai
indoor — foto 17 sudah menandainya sendiri, dan melepasnya juga mengurangi bobot)
⇒ bagian tengah bebas untuk tag ±10 cm. Printer 3D yang ada di lab bisa mencetak
dudukannya.

**Alternatif bila 4K tidak terjangkau:** pakai *tag bundle* — beberapa tag kecil
yang disusun kaku pada titik-titik datar yang tersedia. Gabungan beberapa tag
kecil memberi pose lebih baik daripada satu tag kecil tunggal.

## 4. Spesifikasi belanja kamera

| Syarat | Nilai | Alasan |
|---|---|---|
| Resolusi | 3840 × 2160 (4K) | agar tag 10 cm cukup piksel |
| FPS | ≥ 30 pada 4K (60 lebih baik) | wahana bergerak |
| HFOV | ±109° | menutup lebar lorong 270 cm |
| Rana | **global shutter** diutamakan | *rolling shutter* memelintir pose saat wahana bergerak |
| Antarmuka | USB3 | 4K@30+ tidak muat di USB2 |
| Jumlah | **2 unit** | satu lengan 7,2 m |

⚠️ **RAB perlu direvisi.** Anggaran sekarang Rp1.500.000 untuk **satu** kamera.
Rencana ini butuh **dua**, dan 4K global shutter kemungkinan besar di atas
Rp1,5 juta per unit. Angka barunya harus dipastikan dari harga pasar sebelum
Tabel RAB dan subbab Biaya diperbarui — **jangan menebak angka.**

## 5. Inventaris perangkat keras

| Barang | Temuan |
|---|---|
| Airframe | **6 unit**: 2 siap terbang, 2 setengah jadi (duct terpasang, propeler belum), 2 rangka kosong — cukup untuk 5 agen |
| Wahana | SpeedyBee Bee35 cinewhoop, 25 × 21 cm, tinggi 8 cm dengan baterai |
| Flight controller | **SpeedyBee F405 Mini** (STM32F405, ICM-42688P, barometer DSP-310) |
| ESC | SpeedyBee **BLS 35A Mini** 4-in-1 (BLHeli_S) |
| Companion computer | **Seeed Studio XIAO ESP32-S3** — sangat mungil, GPIO terbatas |
| Baterai | Campur: 4× 1200 mAh, 2× 1500, 1× 2200, 2× Gens Ace 5000 |
| Lain-lain | Propeler cadangan, duct cadangan, kartu program Turnigy, **printer 3D + filament** |
| GPS | Modul terpasang di atas wahana — **tidak dipakai indoor, sebaiknya dilepas** |

## 6. 🔴 Penghalang arsitektur: FC tidak bisa menerima posisi eksternal

**Ini temuan paling penting dari sesi ini.**

ArduPilot memang resmi mendukung papan ini (target `SpeedyBeeF405Mini`, hanya
Copter yang dibuild). **Tetapi** STM32F405 hanya punya 1 MB flash, dan ArduPilot
membuang fitur agar muat. Dari daftar fitur resmi build stabilnya
(`firmware.ardupilot.org/Copter/stable/SpeedyBeeF405Mini/features.txt`):

```
!EK3_FEATURE_EXTERNAL_NAV     DISABLED   ← navigasi eksternal EKF3
!HAL_VISUALODOM_ENABLED       DISABLED   ← odometri visual
!AP_BEACON_ENABLED            DISABLED   ← masukan beacon (jalur UWB)
!HAL_NAVEKF2_AVAILABLE        DISABLED
!AP_OPTICALFLOW_ENABLED       DISABLED
```

Dokumentasi ArduPilot juga menyatakan navigasi non-GPS "requires a board with
more than 1MB of flash" dan "only supported by EKF3 (not EKF2)".

**Artinya:** ArduPilot bawaan pada papan ini **tidak bisa menerima**
`VISION_POSITION_ESTIMATE` dari kamera atas. Perhatikan `AP_BEACON_ENABLED` juga
mati — jadi **jalur UWB pun ikut tertutup** pada papan ini. Ini bukan soal
kamera-lawan-UWB, melainkan keterbatasan flash papannya.

### Tiga jalan keluar

| Jalan | Isi pekerjaan | Risiko | Biaya |
|---|---|---|---|
| **A. Build ArduPilot sendiri** | Aktifkan `EK3_FEATURE_EXTERNAL_NAV` lewat `--extra-hwdef`, matikan fitur lain agar muat 1 MB | Firmware racikan sendiri, kurang teruji; perlu menyiapkan lingkungan build waf + toolchain ARM | Rp0 |
| **B. Ganti FC ke F7/H7 (≥2 MB)** | Pakai papan yang fiturnya lengkap, mis. kelas H743 | Paling kecil risikonya, jalur paling standar untuk riset indoor non-GPS | 5 × papan baru |
| **C. Kalang posisi di companion computer** | FC tetap Betaflight/INAV sebagai penstabil sikap; ESP32-S3 menjalankan kalang posisi & kecepatan, mengirim perintah sikap lewat MSP/CRSF | Paling dekat dengan arsitektur yang sudah digambarkan proposal, tapi EKF & kalang posisi harus ditulis sendiri di ESP32-S3 | Rp0 |

**Catatan untuk jalan C:** proposal sudah menggambarkan pembagian tugas
*companion computer* = perencana tingkat tinggi, FC = penstabil tingkat rendah.
Jalan C hanya menggeser batas itu satu lapis ke bawah. Tetapi XIAO ESP32-S3
sangat terbatas GPIO-nya, dan harus menanggung sekaligus: Wi-Fi/UDP, EKF, kalang
posisi-kecepatan, 2 sensor ultrasonik, dan logika ERC. Beban ini perlu diukur,
bukan diasumsikan.

## 7. Yang masih harus dipastikan

1. **Firmware apa yang terpasang sekarang** di FC (Betaflight bawaan pabrik?) —
   belum terjawab; yang disebut baru nama papannya.
2. Pilihan jalan keluar A / B / C di atas.
3. Spesifikasi **kipas industri** di koridor, bila itu sumber gangguan angin.
4. Harga pasar kamera 4K untuk merevisi RAB.
5. Lebar celah rintangan yang akan dibangun dari dus — perlu diselaraskan dengan
   rasio lebar-celah terhadap lebar-wahana yang dipakai di simulator.
