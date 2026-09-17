# Survei Harga Pengadaan

> Diperbarui 2026-09-17 (batas atas; FC/ESC dan ESP32-S3 dianggap 3 unit tersedia;
> seluruh pos kini berharga, total RAB Rp22.132.856). Dipakai oleh tabel anggaran BAB IV proposal
> (Tabel 4.1 Fase 2, Tabel 4.2 Fase 4, Tabel 4.3 Rekapitulasi).

## Aturan

- **Sumber** hanya dua: RAB awal penulis, atau listing Tokopedia yang tautannya
  dicatat di sini.
- Bila ada beberapa listing, dipakai **batas atas** (keputusan penulis, 2026-09-17).
- Halaman produk Tokopedia tidak dapat dibuka dari lingkungan kerja Claude
  (*timeout*); angka Tokopedia di bawah berasal dari **cuplikan hasil pencarian**.
  Cuplikan bisa merujuk varian yang berbeda, sehingga harga bertanda ⚠️ perlu
  dicek langsung sebelum dipakai membeli.
- Pos tanpa harga tetap *survei* di naskah. Tidak ada angka yang diperkirakan.

## Harga dari RAB awal penulis

Diambil dari tabel RAB proposal sebelum revisi (commit `18a62a8`).

| Pos | Harga satuan (Rp) |
|---|---:|
| Kabel USB ekstensi 10 m + dudukan langit-langit | 150.000 / set |
| Sensor ultrasonik HC-SR04 | 20.000 |
| Penanda AprilTag + akrilik | 20.000 / set |
| Dus kardus rintangan | 30.000 |
| Perlengkapan keselamatan | 500.000 / set |

Harga kamera Rp1.500.000 pada RAB awal adalah untuk **kamera 60 FPS**, bukan kamera
5 MP *global shutter* yang kini dipilih, sehingga tidak dipakai.

## Harga dari survei Tokopedia (2026-09-16 s.d. 2026-09-17)

| Pos | Listing | Harga (Rp) | Dipakai (Rp) |
|---|---|---:|---:|
| Penerima ExpressLRS EP2 TCXO | [justShopIt, Bandung](https://www.tokopedia.com/justshopit/happymodel-2-4g-expresslrs-elrs-ep2-tcxo-long-range-rc-receiver) | 203.000 | **309.000** (batas atas) |
| | Arema Toys, Malang | 215.000 | |
| | happy pediainc, Jakarta Pusat | 309.000 | |
| Pemancar RadioMaster Pocket ELRS 2,4 GHz | [pencarian "radiomaster pocket elrs"](https://www.tokopedia.com/find/radiomaster-pocket-elrs) — varian *Pocket Crush* | 1.150.000 | **1.150.000** ⚠️ satu listing |
| *Stack* SpeedyBee F405 Mini + ESC BLS 35A | [justShopIt, Bandung](https://www.tokopedia.com/justshopit/speedybee-f405-mini-bls-35a-3-6s-20x20mm-stack-flight-controller-fc-esc-for-fpv-drones-dji-vista-link-air-unit-o3-esc-6a84a) | 1.275.000 | **2.244.428** (batas atas) ⚠️ |
| | listing "…Stack F405 Flight Controller 35" — judul sama dipakai [Lapak Fian Prasetyo](https://www.tokopedia.com/lapakfianprasetyo/speedybee-f405-mini-bls-35a-20x20-stack-f405-flight-controller-35) dan [Fanny Ardhiyansyah](https://www.tokopedia.com/fannyardhiyansyah/speedybee-f405-mini-bls-35a-20x20-stack-f405-flight-controller-35); cuplikan tidak menyebut penjualnya | 1.906.700 | |
| | [e-Hely, Jakarta Selatan](https://www.tokopedia.com/e-hely/speedybee-f405-mini-bls-35a-20x20-stack-drone) | 2.244.428 | |
| Seeed XIAO ESP32-S3 (tanpa kamera) | [Mikatronics](https://www.tokopedia.com/mikatronics/seeed-studio-xiao-esp32s3-2-4ghz-wifi-ble-5-0-8mb-psram-8mb-flash) | 198.000 | **198.000** ⚠️ satu listing |

⚠️ *Stack*: selisih antarlisting besar (Rp1,28–2,24 juta), dan listing e-Hely berjudul "Drone Stack Kit … Board Metal" mungkin bukan produk yang persis sama. Cuplikan justShopIt yang
sama juga memuat angka Rp515.000 untuk listing berakhiran "ESC", yang kemungkinan
varian ESC saja, sehingga tidak dimasukkan.

## Survei kamera dari tautan penulis (dibaca 2026-09-17)

Halaman dibuka lewat Chrome *headless* (WebFetch *timeout*). Kolom "Cocok" menilai
terhadap syarat naskah: 5 MP, *global shutter*, 2592×1944, ≥ 50 fps.

| # | Listing | Toko | Harga (Rp) | Sensor dan spesifikasi dari deskripsi | Cocok |
|---|---|---|---:|---|---|
| k1 | [ELP 5MP Global Shutter USB3.0 OG05B10, lensa 3.6–10 mm](https://www.tokopedia.com/inithriftshop/elp-5mp-global-shutter-color-usb3-0-camera-og05b10-60fps-2592x1944-high-speed-camera-with-3-6-10mm-manual-vafifocus-cs-lens-1736975155939870122) | Fast Importir, Jakarta Selatan | 6.600.000 | *Global shutter* OmniVision (judul OG05B10, deskripsi OX05B1S), 2592×1944 60 fps, USB 3.0; lensa bawaan varifokal CS 3,6–10 mm, pilihan 2,1/2,5/4/6/8 mm | ✅ satu-satunya yang cocok, **tetapi lensa bawaan terlalu sempit** |
| k2 | [ELP USB 5MP varifokal 2.8-12/5-50 mm](https://www.tokopedia.com/citraplora/usb-webcam-5megapixel-2592x1944-with-2-8-12mm-5-50mm-varifocal-lens-industrial-web-camera-for-windows-linux-mac-and-android-1733054592994018467) | citra plora, Jakarta Barat | 3.507.200 | OV5640 (rana bergulir), USB 2.0, *pre-order* 15–20 hari | ❌ bukan *global shutter* |
| k3 | [ELP Fisheye 5MP IMX335 30fps](https://www.tokopedia.com/inithriftshop/elp-fisheye-autofocus-5mp-usb-camera-module-mjpeg-30fps-2592x1944-industrial-embedded-mini-38-38mm-webcam-camera-board-1732440405881750954) | Fast Importir | 1.600.000 | IMX335 (rana bergulir), 30 fps, lensa *fisheye* 180° 1,56 mm, USB 2.0 | ❌ |
| k4 | [ELP 120/210fps Global Shutter 1MP](https://www.tokopedia.com/inithriftshop/elp-120fps-210fps-global-shutter-usb-camera-800p-720p-1mp-1731776613987157418) | Fast Importir | 2.100.000 | OV9281 *global shutter* monokrom 1280×800 120 fps, USB 2.0 | ❌ resolusi 1 MP |
| k5 | [ELP 1080P OV2710](https://www.tokopedia.com/inithriftshop/elp-1080p-camera-module-2-0megapixel-1920-1080-cmos-ov2710-mjpeg-30fps-60fps-120fps-mini-usb-endoscope-mini-usb-camera-module-kamera-1732158503105562026) | Fast Importir | 1.300.000 | OV2710 (rana bergulir) 1920×1080 30 fps | ❌ |
| k6 | [120FPS Global Shutter Color OV9782](https://www.tokopedia.com/cahayaprocure/120fps-global-shutter-color-usb-camera-module-uvc-plug-play-webcam-for-android-linux-windows-mac-1734519382647539006) | CahayaProcure | 1.384.000 | OV9782 *global shutter*, 640×480 120 fps, USB 2.0, kirim 15–20 hari | ❌ resolusi rendah |
| k7 | [ELP 5MP IMX335 Fisheye BL170](https://www.tokopedia.com/herubaguy/elp-5mp-30fps-2592-1944-fisheye-webcam-machine-vision-imx335-usb-camera-with-mini-black-box-case) | herubaguy, Jakarta Timur | 2.599.000 | IMX335 (rana bergulir), 30 fps, *fisheye* 170° | ❌ |

**Catatan lensa k1.** Sensor OG05B berformat optik 1/2,53 inci
([OmniVision](https://www.ovt.com/products/og05b/)). Untuk kamera ELP dengan sensor
yang sama, lensa "100°" dinyatakan ELP setara HFOV ±84° dan VFOV ±68°
([Amazon, ELP OG05B10 100°](https://us.amazon.com/Global-Shutter-USB3-0-Camera-Module/dp/B0H3QM4FQY)),
artinya angka sudut lensa ELP adalah **diagonal**. ELP juga menjual varian lensa
**120°** untuk sensor ini
([Amazon, ELP OG05B10 120°](https://us.amazon.com/Global-Shutter-USB3-0-Camera-Module/dp/B0H3QBBL8H)).
Lensa varifokal 3,6–10 mm pada listing k1 jauh lebih sempit dari 120°, sehingga
perlu ditanyakan ke penjual apakah tersedia lensa 2,1 mm atau modul 120° dan
berapa harganya.

## Kamera, sensor laser, dan lakban (dari tautan penulis, 2026-09-17)

| Pos | Listing | Harga (Rp) | Dipakai (Rp) |
|---|---|---:|---:|
| Kamera ELP 5 MP *global shutter* OG05B10, USB 3.0 | [Fast Importir, Jakarta Selatan](https://www.tokopedia.com/inithriftshop/elp-5mp-global-shutter-color-usb3-0-camera-og05b10-60fps-2592x1944-high-speed-camera-with-3-6-10mm-manual-vafifocus-cs-lens-1736975155939870122) | 6.600.000 | **6.600.000** ⚠️ harga untuk lensa bawaan 3,6–10 mm; harga lensa 2,1 mm/120° ditanyakan ke penjual |
| Sensor laser VL53L1X (modul TOF400C), varian VL53L1X | [CNC Store Bandung](https://www.tokopedia.com/cncstorebandung/modul-sensor-jarak-tof200c-vl53l0x-tof400c-vl53l1x-tof050c-vl6180x-modules-distance-sersor-vl53l1x-92c0f) | 98.500 | **98.500** |
| Lakban lantai vinil 3M 764, 2" × 33 m | [Dewielectrical, Kota Tangerang](https://www.tokopedia.com/dewielectrical/3m-lakban-lantai-3m-764-vinyl-floor-marking-tape-2-x33-m-hitam) | 55.000 | **55.000** ⚠️ harga terbaca untuk varian hitam |

Deskripsi listing VL53L1X menyebut jangkauan 4 cm–4 m, resolusi 1 mm, sudut
pandang 27°, antarmuka I²C, tegangan 2,6–3,5 V. Lantai ruang uji berwarna gelap,
jadi **pilih lakban putih atau kuning**, bukan hitam; listing yang sama menyediakan
varian warna tersebut, tetapi harganya belum diperiksa per varian.

Sensor jarak terpilih (8 unit, Fase 4) memakai harga VL53L1X sebagai batas atas
(8 × Rp98.500 = Rp788.000); bila HC-SR04 terpilih, nilainya 8 × Rp20.000 = Rp160.000.
