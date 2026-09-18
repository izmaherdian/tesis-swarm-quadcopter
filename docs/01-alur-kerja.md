# Alur Kerja Riset

> Diperbarui 2026-09-18. Baca setelah [`00-mulai-di-sini.md`](00-mulai-di-sini.md).

Aturan pokoknya satu, yaitu **keputusan mengikuti data, bukan sebaliknya.** Urutan
kerjanya selalu sama, yakni ukur dan data dulu apa yang ada di lab, cari sumber yang
menerangkannya, baru putuskan, lalu beli dan tulis. Nomor folder `docs/` mengikuti
urutan itu.

---

## 1. Prinsip

1. **Keputusan berdiri di atas data.** Setiap keputusan perancangan (KP) menyebut dari
   mana dasarnya, yaitu data lab, pustaka, lembar data produk, hasil uji, atau keputusan
   penulis. Tidak ada KP tanpa tabel dasar keputusan.
2. **Desain sebelum kode, desain sebelum terbang.** Eksperimen dirancang di atas kertas
   dulu (pertanyaan, hipotesis, variabel, metrik, kriteria keberhasilan).
3. **Konfigurasi adalah sumber kebenaran.** Parameter tidak ditulis langsung di kode.
   Semua masuk `experiments/<id>/config.yaml` dan ikut tersalin ke `results/<id>/`.
4. **Angka mengikat.** Klaim di naskah tanpa angka dari `results/`, dari tabel naskah,
   atau dari sumber yang dicatat di `docs/` adalah cacat, bukan gaya bahasa.
5. **Hasil negatif tetap ditulis.** Bila ERC tidak lebih baik pada kondisi tertentu, itu
   temuan dan masuk Keterbatasan Penelitian.
6. **Beli setelah gerbang lolos.** Komponen untuk lima wahana baru dibeli setelah uji
   terbang tunggal lolos ([KP05](04-keputusan/KP05-baterai-dan-pengadaan.md)).

---

## 2. Rantai bukti

```
        ┌──────────────────────────────┐
        │ 02-lab/  DATA LAPANGAN       │  ukur ruang, inventaris barang,
        │ ruang · barang · harga       │  timbang, survei harga
        └──────────────┬───────────────┘
                       │  apa yang benar-benar ada dan berapa ukurannya
        ┌──────────────┴───────────────┐
        │ 03-pustaka/  SUMBER          │  paper Q1/Q2, lembar data pabrikan,
        │ ilmiah · lembar data         │  dokumentasi resmi, listing penjual
        └──────────────┬───────────────┘
                       │  apa yang sudah diketahui orang lain dan spesifikasi resminya
        ┌──────────────┴───────────────┐
        │ 04-keputusan/  KP01…KP<NN>   │  opsi, keputusan, alasan,
        │ dasar keputusan + alasan     │  syarat peninjauan ulang
        └──────────────┬───────────────┘
            ┌──────────┴──────────┐
            ▼                     ▼
   naskah + pengadaan     05-eksperimen/ → experiments/ → results/
   (Bab III, Bab IV RAB)   hasil uji ────┐
                                         │
        hasil uji yang bertentangan ─────┘ kembali ke KP terkait
        (KP diperbarui, bukan hasilnya yang dihaluskan)
```

### 2.1 Empat jenis dasar

| Dasar | Tempat | Contoh | Yang wajib ditulis |
|---|---|---|---|
| **Data lab** | [`02-lab/`](02-lab/README.md) | plafon 300 cm, koridor 270 cm, 6 rangka, 20 motor | tanggal ukur, cara ukur, galat, atau nomor foto |
| **Pustaka** | [`03-pustaka/`](03-pustaka/README.md) → `tulisan/common/references.bib` | galat pose kamera eksternal < 3 cm (Bultmann dkk. 2023) | kunci bib, kuartil jurnal, angka apa yang dipinjam |
| **Lembar data / listing** | [`03-pustaka/`](03-pustaka/README.md) dan [`02-lab/4-survei-harga.md`](02-lab/4-survei-harga.md) | OG05B10 60 fps, baterai 6S 1050–1300 mAh, harga Rp6.600.000 | tautan resmi atau nomor foto, tanggal baca |
| **Hasil uji** | `results/<id>/` | beban CPU HITL, piksel penanda hasil kalibrasi | ID eksperimen dan folder hasil |

Kalau sebuah pilihan tidak punya satu pun dari empat dasar itu, tulis jelas sebagai
**keputusan penulis** beserta tanggalnya. Jangan disamarkan menjadi seolah-olah terukur.

### 2.2 Urutan mengerjakan satu pertanyaan perancangan

1. **Lihat lab dulu.** Apa yang sudah ada, berapa ukurannya, berapa jumlahnya. Catat di
   berkas `02-lab/` yang sesuai beserta tanggal dan sumbernya (foto, ukur, konfirmasi).
2. **Cari sumber.** Paper untuk klaim kinerja, lembar data pabrikan untuk spesifikasi,
   dokumentasi resmi untuk perangkat lunak. Rujukan ilmiah masuk `references.bib` dan
   dicatat di `03-pustaka/`.
3. **Baru putuskan.** Buat `04-keputusan/KP<NN>-<topik>.md` berisi konteks, opsi yang
   dipertimbangkan, **tabel dasar keputusan**, keputusan, konsekuensi, dan syarat
   peninjauan ulang.
4. **Baru belanja dan menulis.** Harga masuk survei harga, angka masuk naskah, dan
   naskah menunjuk KP-nya. Pengadaan tetap menunggu gerbang fase.
5. **Uji membuktikan atau membatalkan.** Hasil `results/` yang bertentangan dengan KP
   membuat KP diperbarui beserta tanggal dan alasannya, bukan hasilnya yang diperhalus.

### 2.3 Contoh rantai yang sudah jalan

| Pertanyaan | Data lab | Sumber | Keputusan | Akibat di naskah |
|---|---|---|---|---|
| Berapa kamera dan ukuran penanda? | plafon 300 cm, segmen 7,20 × 2,70 m | lembar data ELP (foto 18), Bultmann dkk. 2023, tiga makalah AprilTag | [KP03](04-keputusan/KP03-kamera-elp-lensa-2mm.md) | subbab liputan kamera, RAB Fase 2 dan Fase 4 |
| Sensor jarak apa? | kolom beton dan dinding plester di arena, 3 MTF-01 tersedia | Borenstein 1988 dan Siegwart 2004 (pantulan spekular), lembar data MicoAir | [KP04](04-keputusan/KP04-sensor-jarak-uji-banding.md) | uji banding Fase 2, pos sensor di RAB |
| Baterai berapa dan berapa banyak? | 10 baterai di lab, hanya 2 yang 6S 1200 mAh | halaman resmi SpeedyBee (6S 1050–1300 mAh untuk 1950KV) | [KP05](04-keputusan/KP05-baterai-dan-pengadaan.md) | pos baterai Fase 4, jadwal pengisian |
| FC bisa terima pose kamera? | 6 papan F405 Mini flash 1 MB | `features.txt` dan dokumentasi ArduPilot | [KP02](04-keputusan/KP02-firmware-fc.md) | subbab firmware, lampiran daftar fitur |

---

## 3. Lima fase pelaksanaan (September 2026 – Mei 2027)

Fase di bawah **sama dengan Bab IV proposal** dan diagram
`tulisan/proposal/figures/metodologi_tesis.pdf`. Kalau salah satunya berubah, ubah juga
yang lain. Bagian 2 menjelaskan dari mana isi tiap fase berasal; bagian ini menjelaskan
kapan dikerjakan dan kapan boleh lanjut.

| Fase | Bulan | Kegiatan inti | Gerbang / keluaran | Pengadaan |
|---|---|---|---|---|
| **1** Studi dan Desain Arsitektur | Sep (studi literatur sampai Mei) | studi literatur; terapkan faktor skala κ di simulator; skema simulator yang meniru arena berskala; desain arsitektur FC + *companion computer* | hasil simulasi arena berskala di `results/` sebagai pembanding Fase 5; versi simulator baru di `src/MultiAgentSim.version` | kamera pertama dipesan (pra-pesan 3 minggu) |
| **2** Implementasi Teknologi | Okt–Des | *firmware* racikan ([KP02](04-keputusan/KP02-firmware-fc.md)); UART MAVLink; UDP lewat Wi-Fi; kalibrasi kamera 1 + AprilTag → PnP → MAVLink → EKF3; uji banding sensor jarak ([KP04](04-keputusan/KP04-sensor-jarak-uji-banding.md)); penanaman ERC + IAPF; pemancar ELRS diikat | rantai lokalisasi berjalan menerus; sensor terpilih | Tabel 4.1 (Rp10.046.227) |
| **3** Pengujian HITL | Des–Jan | algoritma di *companion computer* dengan umpan balik simulasi gerak | **gerbang 1** beban CPU dan latensi dalam batas aman; gagal → kembali ke penanaman logika | — |
| **4** Uji Terbang Eksperimen | Des–Apr | (a) uji terbang tunggal, yaitu EKF, tautan, PID, ERC agen tunggal, deteksi penanda saat bergerak; (b) kamera kedua dan kalibrasi gabungan, formasi V ruang terbuka, lintasan arena celah 90 cm, trafik UDP | **gerbang 2** wahana tunggal stabil dan aman; **gerbang 3** manuver kawanan berhasil dan stabil | Tabel 4.2 (Rp12.593.747), bagian kawanan setelah gerbang 2 |
| **5** Analisis Data dan Pelaporan | Mei | ekstraksi log pose EKF, pemicu ERC, trafik UDP; metrik; banding dengan simulasi arena | naskah tesis dan publikasi | — |

Metrik yang dihitung pada Fase 5 adalah RMSE galat formasi, waktu konvergensi, tingkat
keberhasilan melintasi celah, jarak minimum antaragen, serta beban komputasi dan
*bandwidth*.

Setiap kegiatan yang menghasilkan angka untuk naskah dijalankan sebagai **eksperimen**
menurut bagian 4, termasuk uji banding sensor, kalibrasi kamera, uji HITL, dan setiap
sesi uji terbang.

---

## 4. Alur satu eksperimen

```
docs/05-eksperimen/E<NN>-<nama>.md    ← 1. desain (sebelum kode/terbang)
experiments/E<NN>-<nama>/config.yaml  ← 2. konfigurasi + skrip jalan
results/<tanggal>-E<NN>-<nama>/       ← 3. keluaran, tidak pernah diedit
tulisan/…/main.tex                    ← 4. tabel & gambar dari results/, baru narasi
```

### 4.1 Desain

Salin [`05-eksperimen/TEMPLATE-desain-eksperimen.md`](05-eksperimen/TEMPLATE-desain-eksperimen.md)
jadi `05-eksperimen/E<NN>-<nama>.md`. Wajib ada hipotesis yang bisa salah, variabel,
kondisi pembanding, metrik, dan **kriteria keberhasilan yang ditetapkan di depan**.
Kalau eksperimen ini menguji sebuah KP, sebut KP-nya di bagian perangkat dan keadaan.
Skill yang membantu: `experiment-design`.

**Selesai bila** orang lain bisa menjalankan eksperimennya tanpa bertanya kepadamu.

### 4.2 Implementasi

Perubahan besar masuk **Plan Mode** (Shift+Tab) dulu. Bila implementasi menyimpang dari
desain, salah satunya diperbaiki secara sadar dan dicatat, bukan dibiarkan berbeda.
Perubahan simulator dikerjakan di repo MultiAgentSim, lalu hash barunya dicatat di
`src/MultiAgentSim.version`.

### 4.3 Menjalankan

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

### 4.4 Analisis

Agen `phd-skills:experiment-analyzer` membandingkan antar-run. Perbandingan harus
**setara** (kondisi awal, ruang, baterai, parameter sama), dan selisih pada satu run
bukan bukti, sehingga percobaan diulang.

### 4.5 Menulis dan menutup rantai

Gambar dan tabel dulu dari `results/`, baru narasi. Setelah hasil masuk naskah, periksa
KP yang terkait, yaitu apakah hasilnya menguatkan, mengubah, atau membatalkan keputusan
itu. Bila berubah, perbarui KP dengan tanggal dan alasannya.

```
make gambar        skrip tulisan/gambar/ → figures/ (angka dari parameter.py)
make watch-p       kompilasi ulang otomatis sambil menulis proposal
make check         gagal bila masih ada rujukan/sitasi menggantung
```

Skill terkait: `paper-writing` (struktur, notasi), `latex-setup` (masalah kompilasi).

---

## 5. Siklus satu sesi kerja dengan Claude

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
│     Data lab dan sumber dicatat dulu, baru KP ditulis.    │
└───────────────────────────────────────────────────────────┘
                          ↓
┌─ 4. Ringkasan penutup ────────────────────────────────────┐
│     Apa yang berubah, kenapa, cara verifikasi,            │
│     dan apa yang TIDAK dikerjakan.                        │
└───────────────────────────────────────────────────────────┘
```

Plan Mode dan pertanyaan balik adalah fitur bawaan Claude Code, **tidak ada perintah
`/` untuk keduanya.**

---

## 6. Alat per kebutuhan

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

## 7. Daftar periksa sebelum kirim draf ke pembimbing

- [ ] `make check` lolos, tidak ada `??` atau `[?]` di PDF
- [ ] Setiap angka di naskah punya sumber di `results/`, tabel naskah, atau `docs/`
- [ ] Setiap KP punya tabel dasar keputusan yang masih cocok dengan data lab terbaru
- [ ] Angka di narasi cocok dengan angka di tabel (tabel yang benar)
- [ ] Setiap harga di RAB punya baris di [`02-lab/4-survei-harga.md`](02-lab/4-survei-harga.md)
- [ ] Rumus ERC/IAPF cocok dengan kode simulator versi terkunci
- [ ] Tidak ada titik dua di tengah kalimat atau sebelum persamaan
- [ ] `/phd-skills:factcheck` bersih; `/phd-skills:xray` dijalankan dan temuannya ditindaklanjuti
- [ ] Istilah konsisten (satu konsep = satu istilah)
- [ ] Semua perubahan sudah di-*commit*

---

## 8. Penandaan versi

```bash
git tag -a v0.5-proposal -m "Proposal setelah tinjauan pembimbing"
```

Tag yang sudah ada adalah `v0.1-proposal`, `v0.3-proposal-revisi`, dan `v0.4-proposal`.
Tandai setiap kali bab atau eksperimen selesai divalidasi, supaya angka di naskah selalu
bisa dilacak ke keadaan kode saat itu.
