# Alur Kerja Riset — Tesis Swarm Quadcopter

Dokumen ini menjelaskan cara bekerja di repo ini: urutan fase, apa yang dihasilkan
tiap fase, dan alat mana yang dipakai di mana. Tujuannya satu — **setiap angka
yang muncul di naskah tesis bisa ditelusuri balik ke kode dan konfigurasi yang
menghasilkannya.**

---

## 1. Prinsip

1. **Desain sebelum kode.** Eksperimen dirancang di atas kertas dulu (hipotesis,
   variabel, metrik). Kode yang ditulis tanpa desain hampir selalu menghasilkan
   data yang tidak bisa dipakai menjawab apa pun.
2. **Konfigurasi adalah sumber kebenaran.** Parameter tidak boleh ditulis
   langsung di dalam kode. Semua masuk `experiments/<id>/config.yaml`, ikut
   tersalin ke `results/<id>/`. Tanpa ini, hasil tidak bisa direproduksi dan BAB
   Metodologi jadi karangan.
3. **Angka mengikat.** Klaim di naskah tanpa angka pendukung dari `results/`
   adalah cacat, bukan gaya bahasa.
4. **Hasil negatif tetap ditulis.** Kalau ERC ternyata tidak lebih baik pada
   kondisi tertentu, itu temuan — masuk Keterbatasan Penelitian, bukan dibuang.

---

## 2. Peta fase

| # | Fase | Keluaran | Alat |
|---|------|----------|------|
| 0 | Persiapan repo | struktur folder, `CLAUDE.md`, git | sudah selesai |
| 1 | Tinjauan pustaka | BAB II + entri di `references.bib` | `/phd-skills:gaps`, skill `literature-research` |
| 2 | Desain eksperimen | `docs/experiments/<id>.md` | skill `experiment-design` |
| 3 | Implementasi | kode di `src/` | Plan Mode + kerja biasa |
| 4 | Menjalankan | `results/<tanggal>-<nama>/` | `make` / skrip sendiri |
| 5 | Analisis | tabel & gambar untuk BAB IV | agen `experiment-analyzer` |
| 6 | Penulisan | BAB di `tulisan/` | skill `paper-writing`, `latex-setup` |
| 7 | Audit sebelum setor | daftar temuan yang harus diperbaiki | `/phd-skills:xray`, `/factcheck` |
| 8 | Pertahanan | antisipasi pertanyaan penguji | `/phd-skills:fortify`, skill `reviewer-defense` |
| 9 | Penandaan versi | git tag | `git tag -a` |

---

## 3. Rincian tiap fase

### Fase 1 — Tinjauan pustaka

```
/phd-skills:gaps kontrol formasi terdesentralisasi quadcopter di ruang sempit
```

Memetakan apa yang sudah dikerjakan orang lain dan di mana celahnya. Pakai ini
untuk mempertajam BAB II, bukan sekadar menumpuk sitasi. Setiap paper yang masuk
`references.bib` harus jelas perannya: pembanding, landasan metode, atau
penunjuk celah.

**Selesai bila:** posisi penelitianmu terhadap Bui dkk. (ERC) dan Wang dkk. (IAPF)
bisa dinyatakan dalam satu paragraf yang tegas.

### Fase 2 — Desain eksperimen (jangan dilewati)

```
Skill experiment-design
```

Salin `docs/experiments/TEMPLATE-desain-eksperimen.md` jadi
`docs/experiments/E01-<nama>.md`, isi sebelum menyentuh kode. Yang wajib ada:
hipotesis yang bisa salah, variabel bebas & terikat, kondisi pembanding
(*baseline*), metrik, dan kriteria keberhasilan yang ditetapkan **di depan**.

Menetapkan kriteria setelah melihat hasil adalah cara paling umum menipu diri
sendiri dalam riset.

**Selesai bila:** dokumennya cukup rinci sehingga orang lain bisa menjalankan
eksperimennya tanpa bertanya apa pun kepadamu.

### Fase 3 — Implementasi

Masuk **Plan Mode** (Shift+Tab) sebelum perubahan besar. Rencana disetujui dulu,
baru kode ditulis. Rujukan yang mengikat adalah dokumen Fase 2 — kalau
implementasi menyimpang dari desain, yang diperbaiki adalah salah satunya secara
sadar, bukan dibiarkan berbeda diam-diam.

### Fase 4 — Menjalankan eksperimen

Satu run = satu folder:

```
results/2026-10-14-E01-iapf-baseline/
├── config.yaml      salinan persis konfigurasi yang dipakai
├── commit.txt       git rev-parse HEAD saat run
├── metrics.csv      metrik per langkah waktu
├── summary.json     metrik ringkas (RMSE, waktu konvergensi, dst.)
└── catatan.md       apa yang dilihat, apa yang aneh
```

`config.yaml` dan `commit.txt` itu yang membuat hasilmu bisa dipertahankan di
sidang. Tanpa keduanya, kamu tidak bisa membuktikan angka di BAB IV berasal dari
kode yang mana.

### Fase 5 — Analisis

```
Agen phd-skills:experiment-analyzer
```

Membandingkan antar-run dan menyusun ringkasan. Hati-hati pada dua hal:
perbandingan harus **setara** (jumlah langkah, kondisi awal, seed acak sama), dan
selisih kecil pada satu run bukan bukti — ulangi dengan beberapa seed.

### Fase 6 — Penulisan

```
Skill paper-writing     — struktur bab, konsistensi notasi
Skill latex-setup       — masalah kompilasi, paket, gaya sitasi
make watch-p            — kompilasi ulang otomatis sambil menulis
```

Urutan menulis BAB IV yang paling tidak menyakitkan: gambar dan tabel dulu dari
`results/`, baru narasi yang menjelaskannya. Menulis narasi duluan hampir selalu
berakhir dengan kalimat yang harus dibuang karena datanya tidak mendukung.

### Fase 7 — Audit sebelum setor ke pembimbing

```
make check                  — pastikan 0 rujukan/sitasi menggantung
/phd-skills:factcheck       — verifikasi entri BibTeX ke DBLP
/phd-skills:xray            — audit naskah vs kode vs hasil (5 sub-agen paralel)
```

`/xray` memeriksa akurasi numerik, konsistensi istilah, kesesuaian kode dengan
naskah, ketepatan sitasi, dan integritas evaluasi. Jalankan ini sebelum, bukan
sesudah, pembimbing menemukan masalahnya.

### Fase 8 — Persiapan sidang

```
/phd-skills:fortify         — pilih ablasi terkuat, antisipasi pertanyaan
Skill reviewer-defense      — susun jawaban atas titik lemah
```

### Fase 9 — Penandaan versi

```bash
git tag -a v0.2-sim-iapf -m "IAPF tervalidasi pada skenario koridor"
```

Tandai setiap kali sebuah bab atau eksperimen selesai divalidasi, supaya angka di
naskah selalu bisa dilacak ke keadaan kode saat itu.

---

## 4. Siklus per sesi kerja

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
│     Skill fase terkait menyala sesuai kebutuhan.          │
└───────────────────────────────────────────────────────────┘
                          ↓
┌─ 4. Ringkasan penutup ────────────────────────────────────┐
│     Apa yang berubah, kenapa, cara verifikasi,            │
│     dan apa yang TIDAK dikerjakan.                        │
└───────────────────────────────────────────────────────────┘
```

Plan Mode dan pertanyaan-balik adalah fitur bawaan Claude Code — **tidak ada
perintah `/` untuk keduanya.** Plan Mode dinyalakan dengan Shift+Tab (tekan
berulang untuk berputar antar mode); pertanyaan balik muncul sendiri saat ada
keputusan yang mengubah arah pekerjaan.

---

## 5. Skill yang sengaja tidak dipakai

Jujur soal batasnya: sebagian isi `phd-skills` dirancang untuk riset *machine
learning* berskala GPU, bukan simulasi kontrol.

| Skill | Alasan tidak cocok |
|---|---|
| `launch` | Daftar periksa untuk job latihan ML multi-jam (`torchrun`, `deepspeed`, `sbatch`). Simulasi Python-mu selesai dalam hitungan menit. |
| `compare` | Mengandaikan pelacak eksperimen ML: wandb, neptune, tensorboard, mlflow. Kamu memakai CSV. |
| `debug` | Menyelidiki OOM GPU, divergensi *training loss*. Bug-mu ada di dinamika dan penyetelan kontrol. |
| `dataset-curation` | Tentang bias dataset dan sampel berstrata. Tidak ada dataset di penelitian ini. |
| `reproduce` | Untuk mereproduksi paper orang lain dari URL arXiv. Berguna hanya jika kamu perlu mereplikasi Bui dkk. sebagai pembanding. |

Yang benar-benar terpakai: `experiment-design`, `literature-research`,
`paper-writing`, `latex-setup`, `paper-verification`, `reviewer-defense`,
`research-publishing`, dan keempat perintah `/gaps`, `/factcheck`, `/xray`,
`/fortify`.

---

## 6. Daftar periksa sebelum kirim draf ke pembimbing

- [ ] `make check` lolos — tidak ada `??` atau `[?]` di PDF
- [ ] Setiap angka di naskah punya sumber di `results/` atau di tabel naskah
- [ ] Angka di narasi cocok dengan angka di tabel
- [ ] `/phd-skills:factcheck` bersih — tidak ada entri BibTeX salah tahun/venue
- [ ] `/phd-skills:xray` dijalankan, temuannya sudah ditindaklanjuti
- [ ] Istilah konsisten (satu konsep = satu istilah sepanjang naskah)
- [ ] Semua perubahan sudah di-*commit*
