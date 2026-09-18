# KP03 — Kamera ELP-U3GS05B10C-IB21 lensa 2,1 mm, dua unit, penanda 12 cm

**Tanggal:** 2026-09-17 · **Status:** diputuskan, pemesanan mengikuti jadwal pengadaan
**Terkait:** [KP01](KP01-lokalisasi-kamera-apriltag.md) · [ruang uji](../02-lab/1-ruang-uji-dan-arena.md) ·
[survei harga](../02-lab/4-survei-harga.md) · proposal Subbab "Penentuan Jumlah Kamera dan Ukuran Penanda"

## Konteks

Kamera atas harus meliput segmen uji 7,20 × 2,70 m dari plafon 300 cm. Dengan ketinggian
terbang 1,2 m dan tinggi wahana 0,08 m, jarak kamera ke penanda hanya **1,72 m**. Syarat
yang dipakai:

- **Rana global.** Rana bergulir memelintir citra penanda saat wahana bergerak.
- **Sisi penanda ≥ 48 piksel** agar terdeteksi andal (80 piksel nyaman untuk wahana bergerak).
- Laju bingkai tinggi pada resolusi penuh.

## Riwayat pilihan

| Tanggal | Pilihan | Nasib |
|---|---|---|
| 2026-09-16 | Kamera USB 4K (IMX415), HFOV ±109°, penanda 10 cm | ditolak, rana bergulir |
| 2026-09-16 | ELP 5 MP *global shutter* "lensa 120°", penanda 12 cm | digantikan; arti "120°" (horizontal atau diagonal) tidak jelas sebelum lembar data ada |
| 2026-09-17 | **ELP-U3GS05B10C-IB21, lensa CS 2,1 mm** | **dipilih** setelah lembar data diterima ([foto 18](../02-lab/foto/18-datasheet-kamera-elp-og05b10.png)) dan penjual mengonfirmasi lensa 2,1 mm |

Dari tujuh listing kamera yang dikirim penulis, hanya ELP OG05B10 (Fast Importir) yang
berana global dan 5 MP; sisanya rana bergulir atau resolusi ≤ 1 MP
([survei kamera k1–k7](../02-lab/4-survei-harga.md)).

## Pilihan lensa untuk OG05B10

Dihitung dengan `liputan()` di [`parameter.py`](../../tulisan/gambar/parameter.py) (model
lubang jarum, jarak 1,72 m, larik 5,737 × 4,312 mm, piksel 2,2 µm).

| Lensa | HFOV menurut ELP | Liputan satu kamera | Penanda 12 cm di sumbu | Dua kamera pada segmen 7,20 m |
|---|---|---|---|---|
| **2,1 mm (IB21)** | 150° | **4,70 × 3,53 m** | 66 px | tumpang tindih **2,20 m** |
| 2,5 mm | 142° | 3,95 × 2,97 m | 79 px | tumpang tindih 0,69 m |
| 3,6 mm (ujung lebar lensa bawaan 3,6–10 mm) | 85° | 2,74 × 2,06 m | 114 px | **tidak tertutup** (celah 1,72 m); melintang juga < 2,70 m |

Lensa 2,1 mm memberi tumpang tindih terlebar untuk menyatukan dua kamera ke satu kerangka
acuan, dengan penanda 12 cm masih di atas 48 px di sumbu optik.

## Dasar keputusan

| Dasar | Sumber | Isi yang dipakai |
|---|---|---|
| Data lab | [ruang uji](../02-lab/1-ruang-uji-dan-arena.md) | plafon 300 cm, segmen 7,20 × 2,70 m, terbang 1,2 m, tinggi wahana 0,08 m |
| Lembar data | `elpGlobalShutterOG05B10`, [foto 18](../02-lab/foto/18-datasheet-kamera-elp-og05b10.png) | OG05B10 *global shutter*, larik 5,737 × 4,312 mm, piksel 2,2 µm, 60 fps USB 3.0, pilihan lensa CS dan HFOV |
| Hitungan | `liputan()` di [`parameter.py`](../../tulisan/gambar/parameter.py) | liputan 4,70 × 3,53 m, 1,80 mm/piksel, penanda 12 cm = 66 px, tumpang tindih 2,20 m |
| Pustaka | `zhangIntegratedFrameworkEnhancing2026`, tiga makalah AprilTag | ketelitian pose penanda kecil dan syarat deteksi |
| Listing | [survei harga](../02-lab/4-survei-harga.md) k1–k7 | Rp6.600.000, satu-satunya kandidat *global shutter* 5 MP |
| Keputusan penulis | 2026-09-17 | dua unit, lensa 2,1 mm, pra-pesan 3 minggu |
| **Asumsi perancangan** | — | ambang deteksi **48 piksel** (dan 80 piksel "nyaman") belum punya rujukan; dikonfirmasi lewat kalibrasi Fase 2 |

## Keputusan

- **Kamera:** ELP-U3GS05B10C-IB21, sensor OmniVision OG05B10 *global shutter* 2592 × 1944,
  MJPEG 60 fps lewat USB 3.0, lensa CS 2,1 mm.
- **Harga:** Rp6.600.000 per unit (Fast Importir, Jakarta Selatan); lensa 2,1 mm harga sama,
  **pra-pesan 3 minggu** (konfirmasi penjual lewat penulis, 2026-09-17).
- **Jumlah:** **dua unit** (keputusan penulis). Unit pertama masuk anggaran Fase 2 tetapi dipesan
  pada Fase 1 karena pra-pesan; unit kedua dipesan setelah uji terbang tunggal lolos (Fase 4).
- **Pemasangan:** posisi 2,35 m dan 4,85 m dari awal segmen, *super clamp* pada rel rangka-T,
  kabel USB 3.0 aktif 10 m ke laptop stasiun darat; kedua kamera sebaiknya di pengendali
  USB 3.1 yang berbeda (pemetaan port belum dicek, [tugas penulis C4](../02-lab/5-tugas-penulis.md)).
- **Penanda:** AprilTag 12 cm pada pelat akrilik yang dinaikkan tiang cetak 3D setinggi
  7 cm, karena jalur datar di bodi hanya 4 cm dan saluran propeler tidak boleh tertutup.
- **Pose:** PnP di laptop stasiun darat, dikirim lewat MAVLink ke EKF3 (ExtNav, [KP02](KP02-firmware-fc.md)).

## Risiko yang diketahui

- **Distorsi tong kuat.** ELP menyebut HFOV 150°, sedangkan lubang jarum hanya 107,6°. Bila
  lensa diasumsikan ekuidistan (batas pesimistis), penanda 12 cm tinggal **±41 px radial di
  tepi koridor** sejajar kamera dan **±23 px di ujung segmen**, di bawah syarat 48 px.
  Angka lubang jarum di atas hanya berlaku dekat sumbu optik.
- **Beban laptop.** Deteksi AprilTag dua aliran 5 MP 60 fps pada Ryzen 5 4500U belum
  diukur; diukur di Fase 2.

## Syarat peninjauan ulang

Saat kamera pertama tiba (Fase 2), kalibrasi intrinsik + distorsi, lalu ukur piksel sisi
penanda di tengah, di tepi koridor, dan di ujung liputan
([tugas penulis A](../02-lab/5-tugas-penulis.md)). Bila penanda di tepi liputan tidak
terdeteksi andal, pilihan yang tercantum di proposal adalah:

1. memperbesar penanda,
2. menaikkan ketinggian terbang agar jarak kamera ke penanda berkurang,
3. menambah kamera ketiga.

Pilihan dibuat setelah data kalibrasi ada dan dicatat sebagai pembaruan keputusan ini.
