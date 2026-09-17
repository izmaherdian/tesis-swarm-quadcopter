# Survei Harga Pengadaan

> Diperbarui 2026-09-17. Dipakai oleh tabel anggaran BAB IV proposal (Tabel 4.1
> Fase 2, Tabel 4.2 Fase 4, Tabel 4.3 Rekapitulasi). Total RAB **Rp23.840.874**.
> FC/ESC dan ESP32-S3 dianggap 3 unit tersedia (asumsi penulis).

## Aturan

- **Sumber** hanya dua: RAB awal penulis, atau listing Tokopedia yang tautannya
  dicatat di sini.
- **Harga dibaca dari halaman Tokopedia** yang dibuka lewat Chrome *headless*
  (halaman produk atau halaman hasil pencarian), bukan dari cuplikan mesin pencari.
  Harga kartu pencarian adalah harga tayang saat itu, dapat berubah.
- Bila ada beberapa listing **untuk produk yang sama persis**, dipakai **batas atas**
  (keputusan penulis). Yang dikecualikan dan alasannya ditulis per pos:
  paket berisi barang lain, versi berbeda (mis. V2), produk lain berjudul mirip,
  dan harga yang jelas salah input.
- Pos tanpa harga ditulis *survei* di naskah. Tidak ada angka yang diperkirakan.

## Harga dari RAB awal penulis

Diambil dari tabel RAB proposal sebelum revisi (commit `18a62a8`). Sejak
2026-09-17 **seluruh angka ini sudah diganti** listing Tokopedia di bawah.

| Pos | Harga satuan (Rp) | Status |
|---|---:|---|
| Kabel USB ekstensi 10 m + dudukan langit-langit | 150.000 / set | diganti: kabel USB 3.0 aktif + *super clamp* |
| Sensor ultrasonik HC-SR04 | 20.000 | diganti listing |
| Penanda AprilTag + akrilik | 20.000 / set | diganti: lembar akrilik A4 + kertas stiker vinil |
| Dus kardus rintangan | 30.000 | diganti listing |
| Perlengkapan keselamatan | 500.000 / set | diganti: 1 kacamata pengaman; tas baterai tidak perlu (kontainer lab tersedia); jaring tidak perlu (keputusan penulis) |

Harga kamera Rp1.500.000 pada RAB awal adalah untuk **kamera 60 FPS**, bukan kamera
5 MP *global shutter* yang kini dipilih, sehingga tidak dipakai.

## Harga dari Tokopedia (dibaca 2026-09-17)

### Pemancar RadioMaster Pocket ELRS 2,4 GHz — dipakai **Rp2.339.000**

| Harga (Rp) | Listing | Catatan |
|---:|---|---|
| **2.339.000** | [Dunia Fantasiku, Jakarta Pusat](https://www.tokopedia.com/dfantasiku/radiomaster-pocket-elrs-2-4ghz-radio-controller-tx-charcoal-gratis-ongkir-1730797488802858854) | batas atas |
| 2.035.000 | [Buaya Aerotech, Sleman](https://www.tokopedia.com/buayaaerotech/radiomaster-pocket-hall-gimbals-elrs-transmitter-remote-control-1731231873418430268) | |
| 1.739.000 | [xexxyy, Bekasi](https://www.tokopedia.com/xexxyy/radiomaster-pocket-elrs-2-4ghz-radio-controller-tx-charcoal-1731135157738112412) | |
| 1.699.000 | [FPV addiction, Jakarta Selatan](https://www.tokopedia.com/fpvaddiction/radiomaster-pocket-hall-sensor-gimbals-radio-transmitter-charcoal-transparan-elrs-charcoal-elrs-8da45) | |
| 1.639.000 | [exhobbyfpv, Tangerang](https://www.tokopedia.com/exhobby/radiomaster-pocket-crush-2-4ghz-elrs-hall-gimbal-transmitter-portable-lightweight-foldable-antenna-1736740678019941704-1736740670765761864) | varian *Pocket Crush* |
| 1.329.000 | [Indah Jaya Store 21, Jakarta Timur](https://www.tokopedia.com/indahjayastore21/radiomaster-pocket-elrs-2-4ghz-radio-controller-tx-charcoal-1731530938771933113) | |
| 1.249.000 | [Dandaanan, Tangerang](https://www.tokopedia.com/dandaanan/dand-radiomaster-pocket-elrs-2-4ghz-radio-controller-tx-charcoal) | |
| 985.000 | [RC Hobby Aero, Depok](https://www.tokopedia.com/rchobbyaero/radiomaster-pocket-radio-controller-m2-elrs-2-4ghz-charcoal-f438b) | stok habis |

Dikecualikan: versi M2 ELRS+CC2500 berpaket penerima RP1 (Rp2.389.000–2.880.000),
paket *ready-to-fly* BetaFPV Air65 (Rp10,5–14,7 juta), dan listing Rp7.007.000 serta
Rp29.551.000 yang jelas tidak wajar.

### Penerima ExpressLRS EP2 TCXO — dipakai **Rp337.000**

| Harga (Rp) | Listing | Catatan |
|---:|---|---|
| **337.000** | [Abadi store07, Tangerang](https://www.tokopedia.com/sabinar/terbaru-happymodel-2-4g-expresslrs-elrs-ep2-tcxo-long-range-rc-receiver-terlaris-1731126126732018778) | batas atas |
| 322.000 | [cv gamasentosa, Jakarta Selatan](https://www.tokopedia.com/cgamasentosa/happymodel-2-4g-expresslrs-elrs-ep2-tcxo-long-range-rc-receiver-murah-1730775054842955535) | |
| 310.000 | [Mahatma Tech, Malang](https://www.tokopedia.com/mahatma-tech/happymodel-2-4g-expresslrs-elrs-ep2-tcxo-long-range-rc-receiver) | |
| 295.000 | [ILMIYAID, Jakarta Selatan](https://www.tokopedia.com/ilmiyaid/happymodel-2-4g-expresslrs-elrs-ep2-tcxo-long-range-rc-receiver-1730995429586666948) | |
| 246.000 | [justShopIt, Bandung](https://www.tokopedia.com/justshopit/happymodel-2-4g-expresslrs-elrs-ep2-tcxo-long-range-rc-receiver) | |

Dikecualikan: listing gabungan EP1/EP2/EP1 Dual (Rp500.000–690.000, harga kartu
bisa untuk varian EP1 Dual) dan paket 1/2/3 buah (Rp2.235.150).

### *Stack* SpeedyBee F405 Mini + ESC BLS 35A (V1) — dipakai **Rp1.906.700**

| Harga (Rp) | Listing | Catatan |
|---:|---|---|
| **1.906.700** | [Lapak Fian Prasetyo, Jakarta Barat](https://www.tokopedia.com/lapakfianprasetyo/speedybee-f405-mini-bls-35a-20x20-stack-f405-flight-controller-35) | batas atas, *pre-order* |
| 1.785.400 | [sentry store12, Jakarta Timur](https://www.tokopedia.com/sentrystore/speedybee-f405-mini-bls-35a-20x20mm-stack-flytower-3-6s-lipo-1733837314357560619) | |
| 1.785.400 | [Teacengerdec, Jakarta Timur](https://www.tokopedia.com/teacengerdec/speedybee-f405-mini-bls-35a-20x20mm-stack-flytower-3-6s-lipo-1733836257530382289) | |
| 1.644.000 | [the anaristr](https://www.tokopedia.com/the-anaristr/speedybee-f405-mini-bls-35a-3-6s-20x20mm-stack-flight-controller-fc-esc-for-fpv-drones-dji-vista-link-air-unit-o3-1731303669302985998) | |
| 1.443.000 | [Nusantara Maju1](https://www.tokopedia.com/nusantaramaju1/speedybee-f405-mini-bls-35a-3-6s-20x20mm-stack-flight-controller-fc-esc-for-fpv-drones-dji-vista-link-air-unit-o3-1730860097454638933) | |
| 1.420.000 | [axisacell, Jakarta Barat](https://www.tokopedia.com/sinarmart-jkt/speedybee-f405-mini-bls-35a-20x20-stack-drone-1731009143216505923) | |
| 1.343.000 | [ILMIYAID](https://www.tokopedia.com/ilmiyaid/speedybee-f405-mini-bls-35a-3-6s-20x20mm-stack-flight-controller-fc-esc-for-fpv-drones-dji-vista-link-air-unit-o3-1730995949501318596) | |
| 1.275.000 | [Powerloops, Jakarta Utara](https://www.tokopedia.com/powerloops/speedybee-f405-mini-35a-4in1-bluetooth-fc-esc-flight-controller-stack) | stok habis |
| 1.250.000 | [e-Hely, Jakarta Selatan](https://www.tokopedia.com/e-hely/speedybee-f405-mini-bls-35a-20x20-stack-drone) | stok habis |
| 991.000 | [SEPRAI](https://www.tokopedia.com/grosirsepraii/speedybee-f405-mini-bls-35a-3-6s-20x20mm-stack-flight-controller-fc-esc-for-fpv-drones-dji-vista-link-air-unit-o3-1732251103977047806) | |
| 940.000 | [justShopIt, Bandung](https://www.tokopedia.com/justshopit/speedybee-f405-mini-bls-35a-3-6s-20x20mm-stack-flight-controller-fc-esc-for-fpv-drones-dji-vista-link-air-unit-o3-esc-6a84a), varian *FC ESC Stack* | stok habis |

Dikecualikan: "Drone Stack Kit 4-In-1 ESC Board Metal" (Riannaomi, Rp2.244.428,
*pre-order*) — **ini angka yang sebelumnya dipakai dan ternyata produk lain**; serta
versi **V2** (Rp2.151.700–2.646.000). Beberapa listing V1 berasal dari judul yang
sama dengan pilihan varian ESC/FC/*stack*; harga kartu mungkin bukan harga varian
*stack*. Bila V1 sudah sulit didapat, anggaran V2 perlu dihitung ulang.

### Seeed XIAO ESP32-S3 (tanpa kamera) — dipakai **Rp282.500**

| Harga (Rp) | Listing | Catatan |
|---:|---|---|
| **282.500** | [CNC Store Bandung](https://www.tokopedia.com/cncstorebandung/xiao-esp32s3-original-board-iot-development-kit-dual-core-wifi-bluetooth-5-0-ble-microcontroller-1732253317634623038) | batas atas |
| 279.000 | [GRES STUDIO, Jakarta Barat](https://www.tokopedia.com/gresstudio/seeed-studio-xiao-esp32s3-2-4g-wifi-ble-mesh-5-0-8mb-1730810225826301815) | |
| 245.500 | [warehouseelectronic](https://www.tokopedia.com/warehouseelectronic/seeeduino-xiao-esp32-s3-mini-development-board-original-seeed-studio-esp32s3-2-4ghz-wifi-ble-5-0-dual-core-battery-charge-power-efficiency-8mb-psram-8mb-flash-esp32-s3-xiao) | |
| 198.000 | [Mikatronics, Makassar](https://www.tokopedia.com/mikatronics/seeed-studio-xiao-esp32s3-2-4ghz-wifi-ble-5-0-8mb-psram-8mb-flash) | stok habis |

Dikecualikan: varian *Sense* (berkamera), *Plus*, dan kit LoRa/Meshtastic/ReSpeaker.

### Kabel ekstensi USB 3.0 aktif 10 m — dipakai **Rp674.000**

Hanya listing yang khusus 10 m; listing multi-panjang (5/10/15/20/30 m) dikecualikan
karena harga kartu adalah varian termurah. Catatan: lembar data kamera menyebut
MJPEG 2592×1944 60 fps juga didukung USB 2.0, sehingga kabel aktif USB 2.0 yang lebih
murah dapat menjadi alternatif.

| Harga (Rp) | Listing |
|---:|---|
| **674.000** | [Vention CBMBL 10 m, pampamolshop](https://www.tokopedia.com/pampamolshop/vention-cbmbl-kabel-active-extension-usb-a-3-0-male-to-usb-a-female-1gbps-10-meter-10m-with-type-c-power-supply-2a-tipe-c-cable-aktif-1732878617013290940) — batas atas, diverifikasi |
| 600.000 | [Netline 10 m, Gadget Crown](https://www.tokopedia.com/gadgetcrown/netline-usb-3-0-active-extension-cable-10-meter-kabel-extender-aktif) |
| 510.000 | [Bafo BF-3032 10 m, Edgecom](https://www.tokopedia.com/edgecom8888/bafo-kabel-usb-3-0-extension-aktif-active-male-to-female-with-power-external-10-meter-bf-3032-bf-3032) |
| 345.000 | [Netline 10 m, OBREN SHOP](https://www.tokopedia.com/obrenshop/netline-usb-3-0-active-extension-cable-10-meter-kabel-extender-aktif) |

### Dudukan kamera *super clamp* + *ball head* 1/4" — dipakai **Rp105.027**

Dijepitkan ke rel rangka-T langit-langit; kamera diarahkan tegak lurus ke bawah.
Kit *magic arm* besar (K&F Concept, Ulanzi Rp265.000–449.000) dan penjepit tanpa
*ball head* dikecualikan.

| Harga (Rp) | Listing |
|---:|---|
| **105.027** | [AsteranID](https://www.tokopedia.com/asteranid/super-clamp-magic-arm-ball-head-mount-1-4-3-8-inch-camera-kamera-1732253921075430889) — batas atas, diverifikasi |
| 55.000 | [Focus Technology](https://www.tokopedia.com/focus-technology/super-clamp-articulated-magic-arm-mini-ball-head-with-1-4-20-thread-hole-kit-ball-head-3944e) |
| 44.028 | [MiAcc (Andoer)](https://www.tokopedia.com/idmiacc/andoer-super-clamp-magic-arm-ball-head-mount-1-4-3-8-inch-gopro-insta360-dslr-1420-jt10002-black-1733145386138240537) |

### Sensor ultrasonik HC-SR04 — dipakai **Rp26.600**

| Harga (Rp) | Listing |
|---:|---|
| **26.600** | [sakurashop29.ID](https://www.tokopedia.com/sakurashop29id/sensor-jarak-range-finder-ultrasonic-ultrasonik-hc-sr04-arduino) — batas atas, diverifikasi |
| 25.900 | [semutin](https://www.tokopedia.com/semutin-official/sensor-ultrasonik-hc-sr04-mengukur-jarak-range-finder) |
| 19.990 | [Pi Toserba](https://www.tokopedia.com/pitoserba/sensor-ultrasonic-hc-sr04-ultrasonik-module-sr-04-modul-pengukur-jarak) |
| 19.900 | [Mechatron](https://www.tokopedia.com/mechatron/sensor-jarak-range-finder-ultrasonic-ultrasonik-hc-sr04-arduino) |
| 17.000 | [EasyWare Electronics](https://www.tokopedia.com/easyware-id/hc-sr04-ultrasonic-sensor) |
| 15.000 | [Rajawali3D](https://www.tokopedia.com/rajawali3d/sensor-ultrasonic-module-modul-sensor-ultrasonik-5v-4pin-hc-sr04), [Arduinoku Robotic](https://www.tokopedia.com/arduinoku-robotic/hc-sr04-sensor-ultrasonic-range-module-hcsr04-ultrasonik) |
| 14.400 | [Mirorim](https://www.tokopedia.com/mirorim/hc-sr04-modul-sensor-jarak-ultrasonik-ultrasonic-wave-ping-for-arduino) |
| 13.000 | [Starlectric](https://www.tokopedia.com/starlectric/hc-sr04-sensor-ultrasonik-ultrasonic-ping) |
| 12.500 | [Kyware](https://www.tokopedia.com/kyware/hc-sr04-ultrasonik-pengukur-jarak-hc-sr04-distance-ultrasonic-sensor) |

Dikecualikan: HY-SRF05, kit DIY, *bracket*, dan *casing*.

### Penanda AprilTag

Satu lembar akrilik A4 (21 × 30 cm) menghasilkan dua pelat 12 × 12 cm, sehingga lima
wahana butuh tiga lembar (1 di Fase 2, 2 di Fase 4). Satu pak stiker cukup untuk
seluruh penanda. Tiang dicetak dengan pencetak 3D lab.

| Pos | Harga (Rp) | Listing |
|---|---:|---|
| Akrilik bening 2 mm A4 | **30.000** | [blessing acrylic](https://www.tokopedia.com/jualacrylic/acrylic-akrilik-lembaran-potongan-2mm-clear-bening-ukuran-a4-30-x-21cm) — batas atas listing A4 tunggal, diverifikasi |
| | 27.500 | [solusilight (Marga Cipta)](https://www.tokopedia.com/solusilight/akrilik-lembaran-2mm-a4-akrilik-ukuran-21-x-30cm-2-mm-bening-1-lembar-marga-cipta-acrylic-sheet-clear-1729545140961577474) |
| | 25.000 | [rifad jaya mandiri](https://www.tokopedia.com/rifadjayamandiri/akrilik-potongan-ukuran-a4-bening-tebal-2mm) |
| | 22.000 | [King Acrylic](https://www.tokopedia.com/king-acrylic---raja-akrilik/acrylic-akrilik-bening-lembar-media-lukis-qr-ukuran-a4-21-x-30-cm-tebal-2mm-lembaran-1729670399538923275) |
| | 17.000–20.500 | beberapa listing lain |
| Kertas stiker vinil A4 isi 20, varian *matte* | **48.000** | [QUAFF Official](https://www.tokopedia.com/quaff-offical-store/quaff-stiker-inkjet-vinyl-a4-transparan-glossy-matte-20-lembar-kertas-stiker-glossy-printer-stiker-quaff-ukuran-a4-mengkilap-matte-transparan-kompatibel-dengan-tinta-pewarna-1733700494513112197) — diverifikasi, varian glossy/matte/transparan sama harga |

Dikecualikan: listing akrilik dengan pilihan ukuran A4/A3 atau A5/A4 (harga kartu
ambigu), stiker transparan/bening (penanda perlu dasar putih), dan pak 500 lembar.

### Kacamata pengaman berlensa bening — dipakai **Rp113.220** (1 unit)

Hanya kacamata model biasa berlensa bening; *goggles*, pelindung karet, dan lensa
gelap/cermin dikecualikan.

| Harga (Rp) | Listing |
|---:|---|
| **113.220** | [Safety Jogger Tsavo, Safety Jogger Official](https://www.tokopedia.com/safetyjogger/safety-jogger-works-tsavo-kacamata-safety-dengan-lensa-bening-polikarbonat-anti-gores-anti-kabut-perlindungan-uv-lengkap-ringan-nyaman-1731302808503747796) — batas atas, diverifikasi |
| 55.300 | [Nankai Trial, Nankai Tools](https://www.tokopedia.com/nankaitools/kacamata-safety-trial-bening-nankai) |
| 39.800 | [Allefix bertali](https://www.tokopedia.com/allefixshop/allefix-kacamata-safety-multifungsi-dengan-tali-elastis-adjustable-lensa-bening-perlindungan-mata-dari-pecahan-dan-debu-1735325783902225634-1735326019177252066) |
| 25.200 | [Nankai Sporty](https://www.tokopedia.com/nankaitools/kacamata-safety-sepeda-sporty-bening-nankai) |
| 25.000 | [Juragan Wearfacts](https://www.tokopedia.com/juragan-wearpack/kacamata-safety-merk-juragan-wearfacts-warna-bening-frame-bening) |
| 16.800 | [Allefix APD](https://www.tokopedia.com/allefixshop/allefix-kacamata-safety-apd-dengan-lensa-bening-tahan-benturan-dan-pelindung-samping-untuk-keselamatan-kerja-k3-6917-1735327984383263970-1735328220062975202) |

### Kardus polos 60 × 40 × 40 cm — dipakai **Rp34.700**

| Harga (Rp) | Listing |
|---:|---|
| **34.700** | [berlian90](https://www.tokopedia.com/berlian90/dus-packing-polos-jumbo-60x40x40-cm-kardus-besar-kardus-packing-polos-box-jumbo-kondisi-baru-1730914591889655635) — batas atas, diverifikasi; juga [kotakkemasanbandung](https://www.tokopedia.com/kemasanberlian/kardus-besar-60x40x40-dus-packing-box-polos) |
| 31.000 | [JoyyStoree (tebal 4 mm)](https://www.tokopedia.com/joyystore-1/kardus-besar-jumbo-uk-60x40x40-tebal-4mm-polos-dan-baru) |
| 19.950 | [Markas Packing](https://www.tokopedia.com/markaspacking/kardus-packing-jumbo-60x40x40-karton-kotak-box-polos-c-f) |
| 18.000 | [Kardus Djakarta](https://www.tokopedia.com/kardusdjakarta/kardus-karton-box-packing-polos-besar-60x40x40-cm-1731634500315809138), [RumahPackaging](https://www.tokopedia.com/rumahpackaging/kardus-karton-box-packing-polos-besar-60x40x40-cm-1729819448748115162) |
| 17.500 | [GudangKardus](https://www.tokopedia.com/gudangkardus-954/kardus-karton-box-besar-60x40x40-cm-dus-packing-packaging-pindahan-jumbo-polos-1729774589828958153) |
| 14.500 | [KardusHolic](https://www.tokopedia.com/k-holic/kardus-besar-polos-karton-box-uk-60x40x40-cm) |

Dikecualikan: listing dengan pilihan 1-ply/2-ply atau berbagai ukuran (harga kartu ambigu).

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

**Catatan lensa k1 (diperbarui 2026-09-17).** Lembar data dari penjual
([foto 18](foto/18-datasheet-kamera-elp-og05b10.png)) dan
[halaman resmi ELP](https://www.elpcctv.com/elp-5mp-60fps-global-shutter-usb30-camera-og05b10-sensor-with-cs-3610mm-lens-3x-optical-zoom-p-731.html):
sensor OG05B10 1/2,5", larik aktif 5,737 × 4,312 mm, piksel 2,2 µm, MJPEG
2592×1944 60 fps pada USB 3.0. Pilihan lensa CS dengan HFOV menurut ELP: 2,1 mm
(IB21) 150°, 2,5 mm 142°, 4 mm 90°, 6 mm 59°, 8 mm 46°, varifokal 3,6–10 mm 85–37°.
Model lubang jarum untuk 2,1 mm memberi HFOV 107,6° (diagonal 119,3°), sedangkan
proyeksi ekuidistan memberi 156,5° — dekat dengan angka ELP, jadi lensa kemungkinan
berdistorsi tong kuat. Hitungan di `tulisan/gambar/parameter.py`.

## Kamera, sensor laser, dan lakban (dari tautan penulis, 2026-09-17)

| Pos | Listing | Harga (Rp) | Dipakai (Rp) |
|---|---|---:|---:|
| Kamera ELP-U3GS05B10C-**IB21** (OG05B10, lensa CS 2,1 mm), USB 3.0 | [Fast Importir, Jakarta Selatan](https://www.tokopedia.com/inithriftshop/elp-5mp-global-shutter-color-usb3-0-camera-og05b10-60fps-2592x1944-high-speed-camera-with-3-6-10mm-manual-vafifocus-cs-lens-1736975155939870122) | 6.600.000 | **6.600.000** — penjual mengonfirmasi lensa 2,1 mm **harga sama**, sistem **pra-pesan 3 minggu** |
| Sensor laser VL53L1X (modul TOF400C), varian VL53L1X | [CNC Store Bandung](https://www.tokopedia.com/cncstorebandung/modul-sensor-jarak-tof200c-vl53l0x-tof400c-vl53l1x-tof050c-vl6180x-modules-distance-sersor-vl53l1x-92c0f) | 98.500 | **98.500** |
| Lakban lantai vinil 3M 764, 2" × 33 m | [Dewielectrical, Kota Tangerang](https://www.tokopedia.com/dewielectrical/3m-lakban-lantai-3m-764-vinyl-floor-marking-tape-2-x33-m-hitam) | 55.000 | **55.000** ⚠️ harga terbaca untuk varian hitam |

Deskripsi listing VL53L1X menyebut jangkauan 4 cm–4 m, resolusi 1 mm, sudut
pandang 27°, antarmuka I²C, tegangan 2,6–3,5 V. Lantai ruang uji berwarna gelap,
jadi **pilih lakban putih atau kuning**, bukan hitam; listing yang sama menyediakan
varian warna tersebut, tetapi harganya belum diperiksa per varian.

Sensor jarak terpilih (8 unit, Fase 4) memakai harga VL53L1X sebagai batas atas
(8 × Rp98.500 = Rp788.000); bila HC-SR04 terpilih, nilainya 8 × Rp20.000 = Rp160.000.
