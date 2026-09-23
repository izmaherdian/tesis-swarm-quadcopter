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
  penghindaran rintangan. ⚠️ Medan tolaknya **bentuk klasik**; `behavior_random()`
  ada di kode tetapi **tidak pernah dipanggil**. Yang "improved" adalah paduan
  perilakunya (migrasi, formasi berotasi + skala κ, antitabrakan, mengekor).
  Batas klaim ini ditulis di Bab II dan Bab III (KP07).
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
  USB 3.0 (lembar data: `docs/02-lab/foto/18-…`; keputusan: KP03). Penanda **AprilTag 12 cm** bertiang 7 cm,
  **terbang 1,3 m**, pose lewat PnP di stasiun darat. Bidang penanda 1,55 m dari kamera; model lubang
  jarum: liputan 4,23 × 3,18 m, 1,62 mm/px, 12 cm = 73 px, tumpang tindih 1,27 m, kamera di x = 2,12
  dan 5,08 m (`parameter.py`). **Acuan konservatif deteksi > 70 px** (DeGol dkk. ICCV 2017, Gambar 9a); penanda 10 cm (61 px)
  ditolak karena itu. UWB tidak dipakai karena EKF UWB+inersia hanya 10–20 cm (MILUV, IJRR 2026).
  ⚠️ ELP menyebut HFOV 150° (lubang jarum 107,6°) → distorsi kuat; batas pesimistis
  ekuidistan: 12 cm hanya ±26 px radial di ujung segmen. Diukur saat kalibrasi Fase 2.
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
  ada**), 14 propeler Gemfan D90S (T-mount 1,5 mm), 3 MTF-01, pengisi daya SkyRC T6X80 (80 W). Bobot terbang perkiraan ≈ 520 g (batas bawah dari lembar data, belum ditimbang). Baterai yang sesuai hanya **6S 1200 mAh
  CNHL** (2 unit, beli 4 di Fase 4 → total 6; SpeedyBee menyarankan 6S 1050–1300 mAh untuk 1950KV). Stasiun darat = laptop
  penulis (Ryzen 5 4500U, Ubuntu 26.04). Semua lalu lintas MAVLink/UDP lewat satu router **TP-Link Archer C54** (2,4 GHz 802.11n untuk ESP32-S3). Rincian: `docs/02-lab/2-inventaris.md`,
  `docs/02-lab/3-baterai-dan-bobot.md`; harga: `docs/02-lab/4-survei-harga.md`; aturan pengadaan: KP05.
- **Arena:** koridor 2,70 m, celah 0,90 m (kolom bangunan + dinding 32 dus 60×40×40 cm, dua baris × empat lapis, tinggi 1,60 m), formasi V
  diskalakan 0,9; untuk wahana $R=0{,}125$ m ambang $\alpha R=1{,}0$ m.
- **Metodologi:** 5 fase mengikuti `figures/metodologi_tesis.pdf`. Halaman Metodologi di
  `proposal-tesis.drawio` **dihasilkan skrip** `tulisan/diagrams/buat-metodologi.py` (tata
  letak, ukuran huruf, dan rute garis dihitung di sana), lalu diekspor dengan
  `tulisan/diagrams/ekspor-drawio.sh Metodologi tulisan/proposal/figures/metodologi_tesis.pdf`
  (penampil draw.io di Chrome *headless* → cetak PDF → `pdfcrop`). Ubah isi diagram lewat
  skrip itu, jangan menyunting XML-nya langsung. Fasenya: 1 Studi & Desain, 2 Implementasi,
  3 HITL, 4 Uji Terbang (**tunggal → tiga wahana → lima wahana**, masing-masing bergerbang),
  5 Analisis. Anggaran ada di Fase 2 (satu tabel) dan Fase 4 (**tiga tabel**, yaitu sebelum uji
  terbang tunggal Rp113.220, setelah Gerbang 2 Rp10.242.427 untuk tiga wahana dan arena,
  setelah Gerbang 3 Rp3.001.500 untuk melengkapi lima wahana). Total RAB Rp23.403.374.
- **Simulasi:** Python (NumPy/SciPy/SymPy/Matplotlib), dinamika diturunkan dengan
  **metode Kane**. Repo terpisah: <https://github.com/izmaherdian/MultiAgentSim>.
- **Hipotesa & evaluasi (KP06, 2026-09-22):** klaim lama "hemat *bandwidth* vs komunikasi
  periodik" **dibuang** — simulator terkunci **tidak punya model komunikasi sama sekali** dan
  makalah penulis tidak mengklaimnya. Klaim baru: ERC membawa 5 wahana melintasi celah 0,90 m
  yang lebih sempit dari bentang formasi 2,05 m, formasi pulih setelahnya, tanpa pelanggaran
  jarak aman. Formasi kaku **tidak** diterbangkan menembus celah (tabrakan pasti secara
  geometris); pembanding = simulasi arena berskala Fase 1 + kondisi kontrol formasi V di
  koridor terbuka. 10 lintasan tiap kondisi, dijalankan pada tiga wahana lalu lima wahana.
  Bentang formasi tiga agen 1,15 m (masih > celah 0,90 m), lima agen 2,05 m.
- **Metrik evaluasi (definisi = kode simulator, Subbab "Metrik Evaluasi dan Kriteria
  Kelayakan"):** RMSE formasi antarpasangan, RMSE mengekor terhadap $d_{ref}$, RMSE operasional
  (berpindah mengikuti mode), $\Phi$ = norma rata-rata vektor satuan kecepatan, waktu tempuh,
  waktu pemulihan formasi, keberhasilan melintas, jarak minimum antaragen, beban CPU, trafik UDP.
  ⚠️ Angka ambang **empat gerbang** (1 HITL: CPU ≤ 70%, latensi ≤ 50 ms · 2 tunggal: hover RMS
  ≤ 0,10 m, deteksi ≥ 95% bingkai · 3 tiga wahana dan 4 lima wahana: ≥ 8/10 lintasan, jarak
  ≥ 0,30 m, pulih ≤ 10 s) adalah **asumsi rancangan**, ditinjau setelah simulasi arena Fase 1.

## Peta repo

```
tulisan/proposal/        proposal tesis (main.tex), 5 bab, 60 halaman
tulisan/laporan-akhir/   kerangka laporan akhir — masih placeholder
tulisan/common/          itb-tesis.sty + references.bib + logo (dipakai bersama)
tulisan/gambar/          skrip gambar (gaya.py, parameter.py, gbr_*.py) → `make gambar`
tulisan/diagrams/        sumber *.drawio; halaman Metodologi → figures/metodologi_tesis.pdf
docs/00-mulai-di-sini.md urutan baca dokumentasi + status proyek — mulai dari sini
docs/01-alur-kerja.md    rantai bukti (lab→pustaka→keputusan), 5 fase (= Bab IV), alur eksperimen
docs/02-lab/             1 ruang uji & arena · 2 inventaris · 3 baterai & bobot · 4 survei harga · 5 tugas penulis · foto/ · video/
docs/03-pustaka/         indeks sumber per topik, kuartil jurnal (SCImago), landasan lokalisasi
docs/04-keputusan/       KP01 lokalisasi · KP02 firmware · KP03 kamera · KP04 sensor · KP05 baterai & pengadaan · KP06 hipotesa & evaluasi
docs/05-eksperimen/      templat + satu dokumen desain per eksperimen (dibuat SEBELUM ngoding/terbang)
docs/arsip/              dokumen lama yang sudah digantikan — bukan acuan
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
  `docs/02-lab/4-survei-harga.md`. Tanpa sumber → tulis *survei*, jangan diperkirakan.
- Setiap rumus perencana (ERC/IAPF) harus cocok dengan kode simulator versi terkunci.
- Kalau angka di narasi dan di tabel berbeda, **tabel yang benar** — perbaiki narasinya.
- Gaya kalimat: mengalir, tanpa titik dua di tengah kalimat atau sebelum persamaan
  (pakai yaitu/karena/sehingga/melalui). Titik dua hanya di judul dan label tabel.
- Istilah **kontrol**, bukan *kendali*, termasuk turunannya (pengontrol, dikontrol).
  Kecualinya istilah perangkat keras **pengendali USB** (*USB host controller*), yang tidak
  ada kaitannya dengan teori kontrol. Nama berkas lama seperti `figures/pengendali.pdf`
  dibiarkan.
- Jangan menulis kode commit, nomor versi kode, atau istilah repositori di dalam naskah.
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
- **Urutannya lab → pustaka → keputusan.** Data lab baru masuk berkas bernomor di
  `docs/02-lab/` beserta tanggal dan sumbernya; sumber ilmiah/lembar data dicatat di
  `docs/03-pustaka/README.md` dan `references.bib`; keputusan baru ditulis sebagai
  `docs/04-keputusan/KP<NN>-<topik>.md` dan **wajib punya tabel dasar keputusan** (data
  lab / pustaka / lembar data / hasil uji / keputusan penulis). Pilihan tanpa dasar
  ditulis jujur sebagai asumsi. Bila struktur `docs/` berubah, perbarui
  `docs/00-mulai-di-sini.md` dan peta repo di atas.

**Git**
- Pesan commit bahasa Indonesia, awalan: `proposal:`, `laporan:`, `sim:`,
  `eksperimen:`, `docs:`, `chore:`.
- Tandai milestone dengan tag `v<besar>.<kecil>-<tahap>`, dan **nama tahap seragam dalam
  satu tahap penelitian**. Tahap proposal memakai akhiran `-proposal` (`v0.1-proposal`
  sampai `v0.6-proposal`). Tahap berikutnya memakai akhiran sendiri, misalnya `-sim`,
  `-hitl`, `-terbang`, `-laporan`. Isi milestone dijelaskan di pesan anotasi tag, bukan
  di namanya.
