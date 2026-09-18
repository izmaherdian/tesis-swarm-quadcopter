# Tesis — Kontrol Formasi Adaptif Kawanan Quadcopter di Ruang Sempit

Implementasi fisik dan evaluasi *Event-Based Reconfiguration Control* (ERC) pada
sistem formasi terdesentralisasi 5 agen *quadcopter*.

**Izma Alhazmi Herdian** (23825301) · Magister Instrumentasi dan Kontrol, FTI ITB
· September 2026 – Mei 2027

---

## Mulai dari mana

**Baca [`docs/00-mulai-di-sini.md`](docs/00-mulai-di-sini.md) lebih dulu.** Berkas itu
berisi urutan baca seluruh dokumentasi dan status proyek terkini.

| Kalau kamu mau… | Buka |
|---|---|
| Tahu urutan baca dan status proyek | [`docs/00-mulai-di-sini.md`](docs/00-mulai-di-sini.md) |
| Tahu fase penelitian dan alur kerja | [`docs/01-alur-kerja.md`](docs/01-alur-kerja.md) |
| Data ruang uji, inventaris, harga | [`docs/02-lab/`](docs/02-lab/README.md) |
| Sumber dan rujukan tiap pilihan | [`docs/03-pustaka/`](docs/03-pustaka/README.md) |
| Tahu kenapa sesuatu dirancang begitu | [`docs/04-keputusan/`](docs/04-keputusan/README.md) |
| Menulis proposal | [`tulisan/proposal/main.tex`](tulisan/proposal/main.tex) |
| Merancang eksperimen baru | [`docs/05-eksperimen/TEMPLATE-desain-eksperimen.md`](docs/05-eksperimen/TEMPLATE-desain-eksperimen.md) |
| Tahu konteks & aturan repo | [`CLAUDE.md`](CLAUDE.md) |

## Kompilasi naskah

Butuh **XeLaTeX** (dokumen memakai `fontspec` + Times New Roman) beserta
`latexmk` dan `bibtex`. Skrip gambar butuh Python 3 + Matplotlib.

```bash
make gambar        # skrip tulisan/gambar/ → tulisan/proposal/figures/
make proposal      # → tulisan/proposal/main.pdf        (58 halaman)
make laporan       # → tulisan/laporan-akhir/main.pdf   (kerangka)
make watch-p       # kompilasi ulang otomatis sambil menulis proposal
make check         # gagal kalau masih ada rujukan/sitasi menggantung
make clean         # buang artefak build
```

## Struktur

```
tulisan/
├── proposal/          proposal tesis (Bab I–V)
├── laporan-akhir/     kerangka laporan akhir
├── common/            itb-tesis.sty · references.bib · logo (dipakai bersama)
├── gambar/            skrip gambar; parameter.py = sumber angka geometri
└── diagrams/          sumber diagram *.drawio (metodologi)
docs/
├── 00-mulai-di-sini.md    urutan baca + status proyek
├── 01-alur-kerja.md       rantai bukti, lima fase, alur eksperimen, siklus sesi
├── 02-lab/                ruang uji, inventaris, baterai, harga, tugas penulis, foto, video
├── 03-pustaka/            indeks sumber per topik, kuartil jurnal, landasan lokalisasi
├── 04-keputusan/          KP01–KP05, tiap KP bertabel dasar keputusan
├── 05-eksperimen/         templat + dokumen desain per eksperimen
└── arsip/                 dokumen lama, bukan acuan
experiments/           konfigurasi tiap eksperimen
results/               keluaran run, satu folder per <tanggal>-<id>
src/                   simulator MultiAgentSim (clone sebagian, versi terkunci)
```

Format dokumen (font, margin, penomoran) terpusat di
`tulisan/common/itb-tesis.sty`, dipakai proposal maupun laporan akhir supaya
keduanya tidak pernah menyimpang satu sama lain. Bibliografinya juga satu:
`tulisan/common/references.bib`.

## Penandaan versi

Tiap bab atau eksperimen yang selesai divalidasi ditandai, misalnya:

```bash
git tag -a v0.5-proposal -m "Proposal setelah tinjauan pembimbing"
```

supaya setiap angka di naskah bisa dilacak ke keadaan kode saat itu.
