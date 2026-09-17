# Alur Kerja Riset

> Diperbarui 2026-09-17. Baca setelah [`00-mulai-di-sini.md`](00-mulai-di-sini.md).
> Fase di sini **sama dengan Bab IV proposal** dan diagram
> `tulisan/proposal/figures/metodologi_tesis.pdf`. Kalau salah satunya berubah,
> ubah juga yang lain.

Tujuannya satu, yaitu **setiap angka di naskah tesis dapat ditelusuri balik ke
konfigurasi, kode, dan log yang menghasilkannya.**

---

## 1. Prinsip

1. **Desain sebelum kode, desain sebelum terbang.** Eksperimen dirancang di atas kertas
   dulu (pertanyaan, hipotesis, variabel, metrik, kriteria keberhasilan). Kode atau
   penerbangan tanpa desain hampir selalu menghasilkan data yang tidak menjawab apa pun.
2. **Konfigurasi adalah sumber kebenaran.** Parameter tidak ditulis langsung di kode.
   Semua masuk `experiments/<id>/config.yaml` dan ikut tersalin ke `results/<id>/`.
3. **Angka mengikat.** Klaim di naskah tanpa angka dari `results/`, dari tabel naskah,
   atau dari sumber yang dicatat di `docs/` adalah cacat, bukan gaya bahasa.
4. **Hasil negatif tetap ditulis.** Bila ERC tidak lebih baik pada kondisi tertentu,
   itu temuan dan masuk Keterbatasan Penelitian.
5. **Beli setelah gerbang lolos.** Komponen untuk lima wahana baru dibeli setelah uji
   terbang tunggal lolos ([KP05](02-keputusan/KP05-baterai-dan-pengadaan.md)).

---

## 2. Lima fase penelitian (September 2026 – Mei 2027)

| Fase | Bulan | Kegiatan inti | Gerbang / keluaran | Pengadaan |
|---|---|---|---|---|
| **1** Studi dan Desain Arsitektur | Sep (studi literatur sampai Mei) | studi literatur; terapkan faktor skala κ di simulator; skema simulator yang meniru arena berskala; desain arsitektur FC + *companion computer* | hasil simulasi arena berskala di `results/` sebagai pembanding Fase 5; versi simulator baru di `src/MultiAgentSim.version` | kamera pertama dipesan (pra-pesan 3 minggu) |
| **2** Implementasi Teknologi | Okt–Des | *firmware* racikan ([KP02](02-keputusan/KP02-firmware-fc.md)); UART MAVLink; UDP lewat Wi-Fi; kalibrasi kamera 1 + AprilTag → PnP → MAVLink → EKF3; uji banding sensor jarak ([KP04](02-keputusan/KP04-sensor-jarak-uji-banding.md)); penanaman ERC + IAPF; pemancar ELRS diikat | rantai lokalisasi berjalan menerus; sensor terpilih | Tabel 4.1 (Rp10.046.227) |
| **3** Pengujian HITL | Des–Jan | algoritma di *companion computer* dengan umpan balik simulasi gerak | **gerbang 1:** beban CPU dan latensi dalam batas aman; gagal → kembali ke penanaman logika | — |
| **4** Uji Terbang Eksperimen | Des–Apr | (a) uji terbang tunggal: EKF, tautan, PID, ERC agen tunggal, deteksi penanda saat bergerak; (b) kamera kedua + kalibrasi gabungan; formasi V ruang terbuka; lintasan arena celah 90 cm; trafik UDP | **gerbang 2:** wahana tunggal stabil dan aman; **gerbang 3:** manuver kawanan berhasil dan stabil | Tabel 4.2 (Rp12.593.747), bagian kawanan setelah gerbang 2 |
| **5** Analisis Data dan Pelaporan | Mei | ekstraksi log pose EKF, pemicu ERC, trafik UDP; metrik; banding dengan simulasi arena | naskah tesis dan publikasi | — |

Metrik yang dihitung pada Fase 5 adalah RMSE galat formasi, waktu konvergensi, tingkat
keberhasilan melintasi celah, jarak minimum antaragen, serta beban komputasi dan
*bandwidth*.

Setiap kegiatan yang menghasilkan angka untuk naskah dijalankan sebagai **eksperimen**
menurut bagian 3, termasuk uji banding sensor, kalibrasi kamera, uji HITL, dan setiap
sesi uji terbang.

---

## 3. Alur satu eksperimen

```
docs/05-eksperimen/E<NN>-<nama>.md    ← 1. desain (sebelum kode/terbang)
experiments/E<NN>-<nama>/config.yaml  ← 2. konfigurasi + skrip jalan
results/<tanggal>-E<NN>-<nama>/       ← 3. keluaran, tidak pernah diedit
tulisan/…/main.tex                    ← 4. tabel & gambar dari results/, baru narasi
```

### 3.1 Desain

Salin [`05-eksperimen/TEMPLATE-desain-eksperimen.md`](05-eksperimen/TEMPLATE-desain-eksperimen.md)
jadi `05-eksperimen/E<NN>-<nama>.md`. Wajib ada hipotesis yang bisa salah, variabel,
kondisi pembanding, metrik, dan **kriteria keberhasilan yang ditetapkan di depan**.
Skill yang membantu: `experiment-design`.

**Selesai bila** orang lain bisa menjalankan eksperimennya tanpa bertanya kepadamu.

### 3.2 Implementasi

Perubahan besar masuk **Plan Mode** (Shift+Tab) dulu. Bila implementasi menyimpang dari
desain, salah satunya diperbaiki secara sadar dan dicatat, bukan dibiarkan berbeda.
Perubahan simulator dikerjakan di repo MultiAgentSim, lalu hash barunya dicatat di
`src/MultiAgentSim.version`.

### 3.3 Menjalankan

Satu run atau satu sesi terbang = satu folder:

```
results/2026-12-14-E03-uji-terbang-tunggal/
├── config.yaml      salinan persis konfigurasi yang dipakai
├── commit.txt       hash repo tesis + hash simulator (dan berkas .apj firmware untuk uji fisik)
├── metrics.csv      metrik per langkah waktu
├── summary.json     metrik ringkas (RMSE, waktu konvergensi, dst.)
└── catatan.md       apa yang dilihat, apa yang aneh, kondisi ruang dan baterai
```

Untuk uji fisik, log mentah (log FC `.bin`, pose kamera, rekaman video) disimpan di
`raw/` dan tidak di-*commit*; yang di-*commit* hanya ringkasan dan metrik.

### 3.4 Analisis

Agen `phd-skills:experiment-analyzer` membandingkan antar-run. Perbandingan harus
**setara** (kondisi awal, ruang, baterai, parameter sama), dan selisih pada satu run
bukan bukti, sehingga percobaan diulang.

### 3.5 Menulis

Gambar dan tabel dulu dari `results/`, baru narasi. Menulis narasi duluan hampir selalu
berakhir dengan kalimat yang harus dibuang karena datanya tidak mendukung.

```
make gambar        skrip tulisan/gambar/ → figures/ (angka dari parameter.py)
make watch-p       kompilasi ulang otomatis sambil menulis proposal
make check         gagal bila masih ada rujukan/sitasi menggantung
```

Skill terkait: `paper-writing` (struktur, notasi), `latex-setup` (masalah kompilasi).

---

## 4. Siklus satu sesi kerja dengan Claude

```
┌─ 1. Plan Mode (Shift+Tab) ────────────────────────────────┐
│     Claude menyusun rencana. Belum ada berkas berubah.    │
│     Kamu setujui, tolak, atau minta ubah.                 │
└───────────────────────────────────────────────────────────┘
                          ↓
┌─ 2. Pertanyaan balik di titik keputusan ──────────────────┐
│     Muncul sebagai pilihan berisi opsi + rekomendasi,     │
│     bukan tebakan diam-diam.                              │
└───────────────────────────────────────────────────────────┘
                          ↓
┌─ 3. Eksekusi ─────────────────────────────────────────────┐
│     Skill terkait menyala sesuai kebutuhan.               │
└───────────────────────────────────────────────────────────┘
                          ↓
┌─ 4. Ringkasan penutup ────────────────────────────────────┐
│     Apa yang berubah, kenapa, cara verifikasi,            │
│     dan apa yang TIDAK dikerjakan.                        │
└───────────────────────────────────────────────────────────┘
```

Plan Mode dan pertanyaan balik adalah fitur bawaan Claude Code, **tidak ada perintah
`/` untuk keduanya.** Keputusan penting dari sesi dicatat sebagai KP baru di
`02-keputusan/`, data lab baru di `03-lab/`.

---

## 5. Alat per kebutuhan

| Kebutuhan | Alat |
|---|---|
| Memetakan celah pustaka | `/phd-skills:gaps`, skill `literature-research` |
| Merancang eksperimen | skill `experiment-design` |
| Membandingkan run | agen `phd-skills:experiment-analyzer` |
| Menulis dan kompilasi | skill `paper-writing`, `latex-setup`, `make` |
| Memeriksa entri BibTeX | `/phd-skills:factcheck` |
| Audit naskah vs kode vs hasil | `/phd-skills:xray` |
| Persiapan sidang | `/phd-skills:fortify`, skill `reviewer-defense` |

Sengaja tidak dipakai karena dirancang untuk riset *machine learning* berskala GPU:
`launch`, `compare` (mengandaikan wandb/mlflow), `debug` (OOM GPU), `dataset-curation`,
dan `reproduce` (kecuali perlu mereplikasi Bui dkk.).

---

## 6. Daftar periksa sebelum kirim draf ke pembimbing

- [ ] `make check` lolos, tidak ada `??` atau `[?]` di PDF
- [ ] Setiap angka di naskah punya sumber di `results/`, tabel naskah, atau `docs/`
- [ ] Angka di narasi cocok dengan angka di tabel (tabel yang benar)
- [ ] Setiap harga di RAB punya baris di [`03-lab/4-survei-harga.md`](03-lab/4-survei-harga.md)
- [ ] Rumus ERC/IAPF cocok dengan kode simulator versi terkunci
- [ ] Tidak ada titik dua di tengah kalimat atau sebelum persamaan
- [ ] `/phd-skills:factcheck` bersih; `/phd-skills:xray` dijalankan dan temuannya ditindaklanjuti
- [ ] Istilah konsisten (satu konsep = satu istilah)
- [ ] Semua perubahan sudah di-*commit*

---

## 7. Penandaan versi

```bash
git tag -a v0.5-proposal -m "Proposal setelah tinjauan pembimbing"
```

Tag yang sudah ada adalah `v0.1-proposal`, `v0.3-proposal-revisi`, dan `v0.4-proposal`.
Tandai setiap kali bab atau eksperimen selesai divalidasi, supaya angka di naskah selalu
bisa dilacak ke keadaan kode saat itu.
