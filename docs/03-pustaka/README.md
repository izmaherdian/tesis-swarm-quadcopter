# 03-pustaka — Sumber yang Menopang Keputusan dan Naskah

> Diperbarui 2026-09-18. Folder ini adalah **rak sumber**. Data lapangan ada di
> [`02-lab/`](../02-lab/README.md), keputusannya di [`04-keputusan/`](../04-keputusan/).
> Rantai lengkapnya di [`01-alur-kerja.md`](../01-alur-kerja.md) bagian 2.

| Berkas | Isinya |
|---|---|
| berkas ini | indeks sumber per topik, yaitu rujukan mana menopang keputusan dan subbab mana |
| [`kuartil-jurnal.md`](kuartil-jurnal.md) | kuartil SCImago (SJR 2025) seluruh entri Daftar Pustaka, termasuk rujukan lama dan penggantinya |
| [`landasan-lokalisasi.md`](landasan-lokalisasi.md) | catatan riset 2026-09-16 tentang lokalisasi dalam ruangan (status verifikasi saat itu) |
| [`sjr-widget/`](sjr-widget/) | salinan widget resmi SCImago, nama berkas = *source id* |

Entri pustaka yang sebenarnya hidup di **`tulisan/common/references.bib`** (gaya
`IEEEtranN`). Berkas di folder ini hanya mencatat perannya, bukan menggandakan entrinya.

## Dua jenis sumber

| Jenis | Dipakai untuk | Aturan |
|---|---|---|
| **Rujukan ilmiah** (jurnal, prosiding, buku, tesis) | klaim metode dan angka kinerja | 2021–2026 dan Q1/Q2 untuk klaim angka; rujukan lama hanya untuk metode fundamental, kuartilnya dicatat di `kuartil-jurnal.md` |
| **Lembar data, dokumentasi resmi, listing** | spesifikasi barang dan harga | tautan resmi atau nomor foto di `02-lab/foto/`, beserta tanggal baca; harga masuk `02-lab/4-survei-harga.md` |

## Indeks sumber per topik

Kolom "Menopang" menunjuk keputusan (KP) dan subbab proposal yang bersandar pada sumber itu.

### Metode formasi dan ERC

| Kunci bib | Isi yang dipinjam | Menopang |
|---|---|---|
| `buiEventbasedReconfigurationControl2025` | konsep ERC untuk formasi kawanan di ruang sempit (simulasi dan SIL, belum uji fisik) | Bab I–II, perencana tingkat tinggi |
| `herdianDecentralizedFormationControl2026` | hasil simulasi penulis, 5 agen, geometri yang diskalakan ke arena | perencana tingkat tinggi, rancangan arena |
| `wangUAVFormationObstacle2021` | IAPF + konsensus untuk penghindaran rintangan | Bab I latar belakang, Bab II, formulasi IAPF |
| `ohSurveyMultiagentFormation2015` | taksonomi metode kontrol formasi | Bab II studi terkait dan klasifikasi |
| `linLeaderFollowerUAV2026`, `caoComputationalIntelligenceAlgorithms2024` | koordinasi dan jaringan kawanan UAV | Bab II, protokol komunikasi |

### Lokalisasi dalam ruangan dan penanda visual

| Kunci bib | Isi yang dipinjam | Menopang |
|---|---|---|
| `bultmannExternalCameraBased2023` | galat pose sistem kamera eksternal < 3 cm dan < 1° tanpa *drift* | [KP01](../04-keputusan/KP01-lokalisasi-kamera-apriltag.md), subbab lokalisasi |
| `olsonAprilTagRobustFlexible2011`, `wangAprilTag2Efficient2016`, `krogiusFlexibleLayoutsFiducial2019` | keluarga penanda AprilTag dan pendeteksinya | KP01, KP03, subbab lokalisasi |
| `garridojuradoAutomaticGenerationDetection2014` | ArUco sebagai pembanding penanda fidusial | subbab lokalisasi |
| `zhangIntegratedFrameworkEnhancing2026` | ketelitian pose AprilTag kecil pada jarak jauh | subbab lokalisasi, risiko distorsi [KP03](../04-keputusan/KP03-kamera-elp-lensa-2mm.md) |
| `hoDesignIndoorPositioning2023` | lokalisasi dalam ruangan berbasis UWB (jalur yang tidak dipilih) | KP01 |
| `georgiadisReviewLocalizationSensing2025` | tinjauan metode lokalisasi dan penginderaan | Bab I latar belakang |

### Persepsi rintangan

| Kunci bib | Isi yang dipinjam | Menopang |
|---|---|---|
| `borensteinObstacleAvoidanceUltrasonic1988`, `siegwartIntroductionAutonomousMobile2004` | pantulan spekular ultrasonik pada permukaan halus bersudut datang miring | [KP04](../04-keputusan/KP04-sensor-jarak-uji-banding.md), subbab persepsi rintangan |
| `pedroSenseAvoidSystem2025` | sistem *sense and avoid* pada UAV kecil | KP04, subbab pemilihan sensor |
| `micoairMTF01` (lembar data) | MTF-01 jangkauan 8 m, sudut pancar setengah 3°, UART 100 Hz, 4,5 g | KP04, tabel komponen |

### Estimasi state dan firmware

| Kunci bib | Isi yang dipinjam | Menopang |
|---|---|---|
| `ardupilotFeaturesSpeedyBeeF405Mini` | daftar fitur build stabil, ExtNav dan beacon dimatikan | [KP02](../04-keputusan/KP02-firmware-fc.md) |
| `ardupilotNonGPSPositionEstimation` | navigasi non-GPS butuh flash > 1 MB dan hanya EKF3 | KP02 |
| `ardupilotCustomFirmwareBuilder` | cara membangun firmware dengan fitur terpilih | KP02 |
| `welchIntroductionKalmanFilter2006`, `gelbAppliedOptimalEstimation1974`, `KalmanFilterGeneralizations2006` | dasar filter Kalman | subbab EKF |
| `kabiriGraphBasedErrorState2024` | fusi data inersia dan sinyal eksternal untuk pose MAV dalam ruangan | subbab EKF |

### Perangkat keras dan wahana

| Sumber | Isi yang dipinjam | Menopang |
|---|---|---|
| `elpGlobalShutterOG05B10` (lembar data) | OG05B10 *global shutter*, 2592×1944 60 fps USB 3.0, pilihan lensa CS dan HFOV | [KP03](../04-keputusan/KP03-kamera-elp-lensa-2mm.md), subbab liputan kamera |
| `speedybeeBee35`, `SpeedyBeeBee3535a` (halaman resmi) | motor 2006-1950KV untuk 6S, baterai 1050–1300 mAh, bobot rangka | [KP05](../04-keputusan/KP05-baterai-dan-pengadaan.md), inventaris, perkiraan bobot |
| `argilianaPengembanganSistemKontrol2025` (tesis S2 ITB) | wahana dan perangkat penelitian sebelumnya di lab yang sama | subbab kondisi awal dan komponen yang tersedia |
| Listing Tokopedia | harga tiap pos RAB | [`02-lab/4-survei-harga.md`](../02-lab/4-survei-harga.md), Tabel anggaran |

## Menambah rujukan baru

1. Pastikan metadatanya dibaca dari halaman resmi penerbit, bukan cuplikan mesin pencari,
   lalu jalankan `/phd-skills:factcheck`.
2. Masukkan entri ke `tulisan/common/references.bib`; entri ber-DOI wajib punya
   `url = {https://doi.org/...}`.
3. Catat kuartilnya di [`kuartil-jurnal.md`](kuartil-jurnal.md) dari widget SCImago.
4. Tambahkan barisnya di indeks atas, sebutkan angka atau metode apa yang dipinjam dan
   keputusan atau subbab mana yang memakainya.
5. Bila rujukan itu mengubah sebuah keputusan, perbarui KP-nya beserta tanggal.
