# Konteks Riset — Tesis Magister

Berkas ini dibaca otomatis oleh Claude Code di awal setiap sesi. Isinya fakta
tentang penelitian ini dan aturan kerja yang berlaku. Perbarui kalau ada yang
berubah — jangan biarkan usang, karena sesi berikutnya akan mempercayainya.

## Identitas penelitian

| | |
|---|---|
| **Judul** | Implementasi Fisik dan Evaluasi *Event-Based Reconfiguration Control* pada Sistem Formasi Adaptif Terdesentralisasi Kawanan *Quadcopter* di Ruang Sempit |
| **Penulis** | Izma Alhazmi Herdian (23825301) |
| **Program** | Magister Instrumentasi dan Kontrol, FTI, Institut Teknologi Bandung |
| **Laboratorium** | PTIO ITB |
| **Periode** | September 2026 – Mei 2027 (9 bulan) |
| **Bahasa tulisan** | Indonesia (istilah asing dalam `\textit{}`) |

## Inti teknis

- **Objek:** 5 agen *quadcopter*, kontrol formasi **terdesentralisasi** (tiap agen
  memutuskan sendiri, tanpa komando pusat).
- **Metode yang dievaluasi:** **ERC** (*Event-Based Reconfiguration Control*) —
  rekonfigurasi formasi hanya terpicu saat parameter persepsi melewati ambang
  batas, dipadu **IAPF** (*Improved Artificial Potential Field*) untuk
  penghindaran rintangan.
- **Pemicu utama:** lebar ruang terestimasi $w_e$. Sesuai kode simulator
  (`MultiAgentERC.py`, versi `0d7ed5a`): $w_e \le \alpha R$ → mode mengekor
  ($\sigma_i=0$); selain itu formasi ($\sigma_i=1$) dengan faktor skala
  $\kappa=\min\{1,(w_e-2R)/w_f\}$. **Tanpa histeresis.** ⚠️ $\kappa$ dihitung tetapi
  **belum diterapkan** di `behavior_formation()` — penerapannya dijadwalkan Fase 1.
  Parameter sim: $R=0{,}2$, $\alpha=8$, $R_a=3R$, $w_f=2{,}0$, $V_{ref}=0{,}5$,
  $d_{ref}=1{,}0$, $W_{form}=1{,}0$, $W_{tail}=1{,}2$, $W_{obs}=W_{col}=8{,}0$.
- **Persepsi rintangan:** 2 sensor jarak per agen, dipasang diagonal bersudut
  $\beta$ terhadap arah maju ($\theta$ dipakai untuk *pitch*). Jenisnya **belum
  ditetapkan**: HC-SR04 vs VL53L1X vs MicoAir MTF-01 (3 unit tersedia) diuji banding pada Fase 2.
- **Lokalisasi:** 2 kamera atas **ELP-U3GS05B10C-IB21**: OG05B10 *global shutter*
  2592×1944, piksel 2,2 µm, larik 5,737 × 4,312 mm, **lensa CS 2,1 mm**, 60 fps MJPEG
  USB 3.0 (lembar data: `docs/lab/foto/18-…`). Penanda **AprilTag 12 cm** bertiang 7 cm,
  terbang 1,2 m, pose lewat PnP di stasiun darat. Model lubang jarum: liputan
  4,70 × 3,53 m, 1,80 mm/px, 12 cm = 66 px, tumpang tindih 2,20 m (`parameter.py`).
  ⚠️ ELP menyebut HFOV 150° (lubang jarum 107,6°) → distorsi kuat; batas pesimistis
  ekuidistan: 12 cm hanya ±23 px radial di ujung segmen. Diukur saat kalibrasi Fase 2.
  Pra-pesan 3 minggu. **Bukan UWB, bukan 4K, bukan "120°"** (keputusan lama).
- **Estimasi state:** EKF3 bawaan ArduPilot, fusi IMU + pose kamera (ExtNav).
- **Firmware FC:** SpeedyBee F405 Mini (flash 1 MB) — build stabil ArduPilot
  menonaktifkan ExtNav, jadi dipakai **firmware racikan** (Custom Firmware Builder).
  Cadangan: kalang posisi/kecepatan pindah ke *companion computer*.
- **Kontrol tingkat rendah:** kaskade ArduPilot (P posisi → PID kecepatan → P sikap
  → PID laju sudut → mixer → DShot).
- **Perangkat keras (inventaris 2026-09-17):** 6 rangka Bee35 (4 terakit tanpa propeler,
  2 kosong), 6 FC F405 Mini, 5 ESC BLS 35A (1 V2 lepas diduga rusak), 20 motor
  2006-1950KV (poros 1,5 mm), 5 XIAO ESP32-S3, 5 penerima ExpressLRS (**pemancar belum
  ada**), 14 propeler Gemfan D90S (T-mount 1,5 mm), 3 MTF-01, pengisi daya SkyRC T6X80 (80 W). Baterai yang sesuai hanya **6S 1200 mAh
  CNHL** (2 unit; SpeedyBee menyarankan 6S 1050–1300 mAh untuk 1950KV). Stasiun darat = laptop
  penulis (Ryzen 5 4500U, Ubuntu 26.04). Semua lalu lintas MAVLink/UDP lewat satu router Wi-Fi. Rincian: `docs/lab/spesifikasi-hw.md`,
  `docs/lab/analisis-baterai.md`; harga: `docs/lab/survei-harga.md`.
- **Arena:** koridor 2,70 m, celah 0,90 m (kolom bangunan + dus), formasi V
  diskalakan 0,9; untuk wahana $R=0{,}125$ m ambang $\alpha R=1{,}0$ m.
- **Metodologi:** 5 fase mengikuti `figures/metodologi_tesis.pdf` (diagram draw.io
  penulis, isinya sudah diselaraskan; ekspor ulang lewat penampil draw.io di Chrome
  *headless* → cetak PDF → `pdfcrop`): 1 Studi & Desain, 2 Implementasi,
  3 HITL, 4 Uji Terbang (tunggal → kawanan), 5 Analisis. Anggaran ada di Fase 2
  dan Fase 4; pembelian untuk lima wahana menunggu uji terbang tunggal lolos.
- **Simulasi:** Python (NumPy/SciPy/SymPy/Matplotlib), dinamika diturunkan dengan
  **metode Kane**. Repo terpisah: <https://github.com/izmaherdian/MultiAgentSim>.
- **Metrik evaluasi:** RMSE galat formasi, waktu konvergensi, tingkat keberhasilan
  melewati lorong, jarak minimum antaragen, beban komputasi & *bandwidth*.

## Peta repo

```
tulisan/proposal/        proposal tesis (main.tex), 5 bab, ±56 halaman
tulisan/laporan-akhir/   kerangka laporan akhir — masih placeholder
tulisan/common/          itb-tesis.sty + references.bib + logo (dipakai bersama)
tulisan/gambar/          skrip gambar (gaya.py, parameter.py, gbr_*.py) → `make gambar`
tulisan/diagrams/        sumber *.drawio; halaman Metodologi → figures/metodologi_tesis.pdf
docs/workflow.md         alur kerja riset — baca ini sebelum memulai fase baru
docs/lab/                inventaris, survei harga, analisis ruang, foto & video lab
docs/experiments/        satu dokumen desain per eksperimen (dibuat SEBELUM ngoding)
experiments/             konfigurasi tiap eksperimen (config.yaml + skrip jalan)
results/                 keluaran run, satu folder per <tanggal>-<nama>
src/MultiAgentSim/       clone simulator (gitignored); versi dikunci di src/MultiAgentSim.version
```

## Aturan kerja di repo ini

**LaTeX**
- Wajib **XeLaTeX** (`fontspec` + `unicode-math`). `pdflatex` akan gagal.
- Kompilasi lewat `make proposal` / `make laporan`, bukan perintah manual.
- `make check` harus lolos (0 rujukan menggantung) sebelum draf dikirim ke pembimbing.
- Pengaturan format (font, margin, penomoran) **hanya** di
  `tulisan/common/itb-tesis.sty`. Jangan menaruh `\usepackage` atau `\renewcommand`
  format di `main.tex` masing-masing dokumen.
- Satu bibliografi untuk semua: `tulisan/common/references.bib`, gaya `IEEEtranN`.
  Entri ber-DOI wajib punya `url = {https://doi.org/...}` agar dapat diklik.
- Gambar diagram dibuat skrip di `tulisan/gambar/` (hitam-putih, Times New Roman,
  tanpa judul, ukuran cetak 14 cm, disisipkan 1:1). Gambar yang isinya berkaitan
  disusun satu baris dengan `\subcaptionbox`. Angka geometri diambil dari
  `parameter.py`, bukan diketik ulang.
- Artefak build (`*.aux`, `*.pdf`, dll.) tidak di-commit — sudah di `.gitignore`.

**Klaim dan angka**
- Setiap angka di naskah harus bisa ditelusuri ke `results/<id>/` atau ke tabel
  di naskah itu sendiri. Jangan pernah menulis angka yang tidak punya sumber.
- Harga di RAB hanya dari RAB awal penulis atau listing yang dicatat di
  `docs/lab/survei-harga.md`. Tanpa sumber → tulis *survei*, jangan diperkirakan.
- Setiap rumus perencana (ERC/IAPF) harus cocok dengan kode simulator versi terkunci.
- Kalau angka di narasi dan di tabel berbeda, **tabel yang benar** — perbaiki narasinya.
- Gaya kalimat: mengalir, tanpa titik dua di tengah kalimat atau sebelum persamaan
  (pakai yaitu/karena/sehingga/melalui). Titik dua hanya di judul dan label tabel.
- Jangan menghaluskan hasil yang jelek. Hasil negatif ditulis apa adanya di
  bagian Keterbatasan Penelitian.

**Alur kerja dengan Claude**
- Perubahan yang menyentuh banyak berkas atau mengubah metode: masuk **Plan Mode**
  dulu (Shift+Tab), susun rencana, tunggu persetujuan, baru kerjakan.
- Di titik keputusan yang mengubah arah pekerjaan, tanyakan balik dengan opsi
  dan rekomendasi — jangan menebak sendiri.
- Tutup setiap tugas dengan ringkasan: apa yang berubah, kenapa, bagaimana
  memverifikasinya. Sebutkan juga apa yang **tidak** dikerjakan.
- Sebelum menghapus berkas apa pun: pastikan sudah ter-*commit* lebih dulu.

**Git**
- Pesan commit bahasa Indonesia, awalan: `proposal:`, `laporan:`, `sim:`,
  `eksperimen:`, `docs:`, `chore:`.
- Tandai milestone dengan tag: `v0.1-proposal`, `v0.2-sim-iapf`, `v0.3-erc`, dst.
