# Survei Harga Pengadaan

> Diperbarui 2026-09-17 (batas atas; FC/ESC dan ESP32-S3 dianggap 3 unit tersedia). Dipakai oleh tabel anggaran BAB IV proposal
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

## Menunggu harga dari penulis

| Pos | Jumlah | Fase |
|---|---|---|
| Kamera USB 5 MP *global shutter* 2592×1944, lensa 120° (ELP) — **sertakan spesifikasi FOV: horizontal atau diagonal** | 2 | Fase 2, Fase 4 |
| Sensor jarak laser VL53L1X, varian satuan | 2 | Fase 2 |
| Lakban lantai 48 mm | 1 set | Fase 4 |

Sensor jarak terpilih (8 unit, Fase 4) mengikuti hasil uji banding: bila HC-SR04
terpilih, nilainya 8 × Rp20.000 = Rp160.000; bila VL53L1X, menunggu harga di atas.
