# KP03 — Kamera ELP-U3GS05B10C-IB21 lensa 2,1 mm, dua unit, penanda 12 cm

**Tanggal:** 2026-09-17 · **Diperbarui:** 2026-09-18 · **Status:** diputuskan, pemesanan mengikuti jadwal pengadaan
**Terkait:** [KP01](KP01-lokalisasi-kamera-apriltag.md) · [ruang uji](../02-lab/1-ruang-uji-dan-arena.md) ·
[survei harga](../02-lab/4-survei-harga.md) · proposal Subbab "Penentuan Jumlah Kamera dan Ukuran Penanda"

## Konteks

Kamera atas harus meliput segmen uji 7,20 × 2,70 m dari plafon 300 cm. Bidang penanda berada
pada ketinggian terbang + tinggi wahana 0,08 m + tiang penanda 0,07 m, sehingga jarak kamera
ke penanda hanya **1,55 m** pada ketinggian terbang 1,3 m. Syarat yang dipakai:

- **Rana global.** Rana bergulir memelintir citra penanda saat wahana bergerak.
- **Sisi penanda > 70 piksel.** DeGol dkk. mengukur *recall* deteksi penanda fidusial dan
  mendapati *recall* menurun seiring mengecilnya penanda, sedangkan di atas sekitar 70 piksel
  AprilTag dan pembandingnya sama-sama tinggi (`degolChromaTagColoredMarker2017`, ICCV 2017,
  Gambar 9a). Dipakai sebagai **acuan konservatif**, karena AprilTag sendiri bertahan lebih
  baik pada ukuran kecil dan makalah itu tidak menyebut batas mutlak AprilTag.
- Laju bingkai tinggi pada resolusi penuh.

## Riwayat pilihan

| Tanggal | Pilihan | Nasib |
|---|---|---|
| 2026-09-16 | Kamera USB 4K (IMX415), HFOV ±109°, penanda 10 cm | ditolak, rana bergulir |
| 2026-09-16 | ELP 5 MP *global shutter* "lensa 120°", penanda 12 cm | digantikan; arti "120°" (horizontal atau diagonal) tidak jelas sebelum lembar data ada |
| 2026-09-17 | **ELP-U3GS05B10C-IB21, lensa CS 2,1 mm** | **dipilih** setelah lembar data diterima ([foto 18](../02-lab/foto/18-datasheet-kamera-elp-og05b10.png)) dan penjual mengonfirmasi lensa 2,1 mm |
| 2026-09-18 | penanda 10 cm dan ambang 48 piksel | **ditolak.** Ambang bersumber adalah 70 piksel, dan 10 cm hanya 61 piksel di sumbu optik. Ketinggian terbang dinaikkan 1,2 → 1,3 m agar penanda 12 cm mencapai 73 piksel |

Dari tujuh listing kamera yang dikirim penulis, hanya ELP OG05B10 (Fast Importir) yang
berana global dan 5 MP; sisanya rana bergulir atau resolusi ≤ 1 MP
([survei kamera k1–k7](../02-lab/4-survei-harga.md)).

## Pilihan lensa untuk OG05B10

Dihitung dengan `liputan()` di [`parameter.py`](../../tulisan/gambar/parameter.py) (model
lubang jarum, jarak 1,55 m, larik 5,737 × 4,312 mm, piksel 2,2 µm).

| Lensa | HFOV menurut ELP | Liputan satu kamera | Penanda 12 cm di sumbu | Dua kamera pada segmen 7,20 m |
|---|---|---|---|---|
| **2,1 mm (IB21)** | 150° | **4,23 × 3,18 m** | 73 px | tumpang tindih **1,27 m** |
| 2,5 mm | 142° | 3,56 × 2,67 m | 88 px | **tidak tertutup**, kurang 0,09 m |
| 3,6 mm (ujung lebar lensa bawaan 3,6–10 mm) | 85° | 2,47 × 1,86 m | 127 px | **tidak tertutup**, kurang 2,26 m; melintang juga < 2,70 m |

Hanya lensa 2,1 mm yang menutup segmen 7,20 m dengan dua kamera pada ketinggian terbang
1,3 m, dan penanda 12 cm tetap di atas acuan 70 piksel di sumbu optik.

## Dasar keputusan

| Dasar | Sumber | Isi yang dipakai |
|---|---|---|
| Data lab | [ruang uji](../02-lab/1-ruang-uji-dan-arena.md) | plafon 300 cm, segmen 7,20 × 2,70 m, terbang 1,3 m, tinggi wahana 0,08 m, tiang penanda 0,07 m |
| Lembar data | `elpGlobalShutterOG05B10`, [foto 18](../02-lab/foto/18-datasheet-kamera-elp-og05b10.png) | OG05B10 *global shutter*, larik 5,737 × 4,312 mm, piksel 2,2 µm, 60 fps USB 3.0, pilihan lensa CS dan HFOV |
| Hitungan | `liputan()` di [`parameter.py`](../../tulisan/gambar/parameter.py) | liputan 4,23 × 3,18 m, 1,62 mm/piksel, penanda 12 cm = 73 px, tumpang tindih 1,27 m |
| Pustaka | `degolChromaTagColoredMarker2017` | *recall* deteksi tinggi selama sisi penanda > 70 piksel |
| Pustaka | `zhangIntegratedFrameworkEnhancing2026`, tiga makalah AprilTag | ketelitian pose penanda kecil dan syarat deteksi |
| Listing | [survei harga](../02-lab/4-survei-harga.md) k1–k7 | Rp6.600.000, satu-satunya kandidat *global shutter* 5 MP |
| Keputusan penulis | 2026-09-17 | dua unit, lensa 2,1 mm, pra-pesan 3 minggu |
| ~~Asumsi perancangan~~ | — | ambang lama 48 piksel tanpa rujukan **sudah diganti** acuan 70 piksel di baris pustaka |

## Keputusan

- **Kamera:** ELP-U3GS05B10C-IB21, sensor OmniVision OG05B10 *global shutter* 2592 × 1944,
  MJPEG 60 fps lewat USB 3.0, lensa CS 2,1 mm.
- **Harga:** Rp6.600.000 per unit (Fast Importir, Jakarta Selatan); lensa 2,1 mm harga sama,
  **pra-pesan 3 minggu** (konfirmasi penjual lewat penulis, 2026-09-17).
- **Jumlah:** **dua unit** (keputusan penulis). Unit pertama masuk anggaran Fase 2 tetapi dipesan
  menjelang akhir Fase 1 karena pra-pesan tiga minggu, supaya tiba saat kalibrasi Fase 2
  dimulai; unit kedua dipesan setelah uji terbang tunggal lolos (Fase 4).
- **Pemasangan:** posisi 2,12 m dan 5,08 m dari awal segmen, *super clamp* pada rel rangka-T,
  kabel USB 3.0 aktif 10 m ke laptop stasiun darat; kedua kamera sebaiknya di pengontrol
  USB 3.1 yang berbeda (pemetaan port belum dicek, [tugas penulis C4](../02-lab/5-tugas-penulis.md)).
- **Penanda:** AprilTag **12 cm** (bukan 10 cm) pada pelat akrilik yang dinaikkan tiang cetak
  3D setinggi 7 cm, karena jalur datar di bodi hanya 4 cm dan saluran propeler tidak boleh
  tertutup.
- **Ketinggian terbang 1,3 m**, bukan 1,2 m, karena menaikkan wahana memperpendek jarak ke
  kamera sehingga kepadatan piksel bertambah tanpa menambah biaya.
- **Pose:** PnP di laptop stasiun darat, dikirim lewat MAVLink ke EKF3 (ExtNav, [KP02](KP02-firmware-fc.md)).

## Risiko yang diketahui

- **Distorsi tong kuat.** ELP menyebut HFOV 150°, sedangkan lubang jarum hanya 107,6°. Bila
  lensa diasumsikan ekuidistan (batas pesimistis), penanda 12 cm tinggal **±42 px radial di
  tepi koridor** sejajar kamera dan **±26 px di ujung segmen**, jauh di bawah acuan 70 px.
  Angka lubang jarum di atas hanya berlaku dekat sumbu optik, dan margin terhadap acuan
  memang tipis. Inilah risiko terbesar keputusan ini.
- **Beban laptop.** Deteksi AprilTag dua aliran 5 MP 60 fps pada Ryzen 5 4500U belum
  diukur; diukur di Fase 2.

## Syarat peninjauan ulang

Saat kamera pertama tiba (Fase 2), kalibrasi intrinsik + distorsi, lalu ukur piksel sisi
penanda di tengah, di tepi koridor, dan di ujung liputan
([tugas penulis A](../02-lab/5-tugas-penulis.md)). Bila penanda di tepi liputan tidak
terdeteksi andal, pilihan yang tercantum di proposal adalah:

1. memperbesar penanda (14 cm memberi 86 piksel di sumbu optik),
2. menaikkan ketinggian terbang lagi, dengan konsekuensi liputan menyusut dan tumpang
   tindih dua kamera makin tipis (pada 1,3 m sudah tinggal 1,27 m),
3. menambah kamera ketiga.

Pilihan dibuat setelah data kalibrasi ada dan dicatat sebagai pembaruan keputusan ini.
