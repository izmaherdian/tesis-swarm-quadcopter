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
| **Periode** | Agustus 2026 – April 2027 (9 bulan) |
| **Bahasa tulisan** | Indonesia (istilah asing dalam `\textit{}`) |

## Inti teknis

- **Objek:** 5 agen *quadcopter*, kontrol formasi **terdesentralisasi** (tiap agen
  memutuskan sendiri, tanpa komando pusat).
- **Metode yang dievaluasi:** **ERC** (*Event-Based Reconfiguration Control*) —
  rekonfigurasi formasi hanya terpicu saat parameter persepsi melewati ambang
  batas, dipadu **IAPF** (*Improved Artificial Potential Field*) untuk
  penghindaran rintangan.
- **Pemicu utama:** lebar ruang terestimasi $w_e$ turun di bawah toleransi
  formasi → transisi ke formasi *tailgating* (mengekor).
- **Persepsi rintangan:** 2 sensor ultrasonik per agen, dipasang diagonal
  $\theta = 45^\circ$, mengukur jarak lateral $d_l$ dan $d_r$.
- **Lokalisasi:** kamera atas (*ceiling camera*) 60 FPS + penanda visual
  **AprilTag**, pose 3D lewat *Perspective-n-Point*.
  ⚠️ **Bukan UWB.** Proposal sempat memakai UWB lalu diganti; kalau menemukan
  sisa istilah UWB/*anchor*/*two-way ranging* di naskah, itu sisa migrasi yang
  harus dibersihkan.
- **Estimasi state:** EKF, fusi IMU (laju tinggi, *drift*) + kamera atas
  (absolut, tanpa *drift*).
- **Kontrol tingkat rendah:** PID kaskade (posisi → kecepatan → sikap → laju sikap).
- **Perangkat keras:** rangka SpeedyBee 35, FC SpeedyBee F4 Mini, *companion
  computer* ESP32S3, komunikasi MAVLink di atas UDP.
- **Simulasi:** Python (NumPy/SciPy/SymPy/Matplotlib), dinamika diturunkan dengan
  **metode Kane**. Repo terpisah: <https://github.com/izmaherdian/MultiAgentSim>.
- **Metrik evaluasi:** RMSE galat formasi, waktu konvergensi, tingkat keberhasilan
  melewati lorong, jarak minimum antaragen, beban komputasi & *bandwidth*.

## Peta repo

```
tulisan/proposal/        proposal tesis (main.tex) — SUDAH JADI, 48 halaman
tulisan/laporan-akhir/   kerangka laporan akhir — masih placeholder
tulisan/common/          itb-tesis.sty + references.bib + logo (dipakai bersama)
tulisan/diagrams/        sumber diagram *.drawio
docs/workflow.md         alur kerja riset — baca ini sebelum memulai fase baru
docs/experiments/        satu dokumen desain per eksperimen (dibuat SEBELUM ngoding)
experiments/             konfigurasi tiap eksperimen (config.yaml + skrip jalan)
results/                 keluaran run, satu folder per <tanggal>-<nama>
src/                     kode simulasi (MultiAgentSim, belum di-clone ke sini)
```

## Aturan kerja di repo ini

**LaTeX**
- Wajib **XeLaTeX** (`fontspec` + `unicode-math`). `pdflatex` akan gagal.
- Kompilasi lewat `make proposal` / `make laporan`, bukan perintah manual.
- `make check` harus lolos (0 rujukan menggantung) sebelum draf dikirim ke pembimbing.
- Pengaturan format (font, margin, penomoran) **hanya** di
  `tulisan/common/itb-tesis.sty`. Jangan menaruh `\usepackage` atau `\renewcommand`
  format di `main.tex` masing-masing dokumen.
- Satu bibliografi untuk semua: `tulisan/common/references.bib`.
- Artefak build (`*.aux`, `*.pdf`, dll.) tidak di-commit — sudah di `.gitignore`.

**Klaim dan angka**
- Setiap angka di naskah harus bisa ditelusuri ke `results/<id>/` atau ke tabel
  di naskah itu sendiri. Jangan pernah menulis angka yang tidak punya sumber.
- Kalau angka di narasi dan di tabel berbeda, **tabel yang benar** — perbaiki narasinya.
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
