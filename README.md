# Tesis — Kontrol Formasi Adaptif Kawanan Quadcopter di Ruang Sempit

Implementasi fisik dan evaluasi *Event-Based Reconfiguration Control* (ERC) pada
sistem formasi terdesentralisasi 5 agen *quadcopter*.

**Izma Alhazmi Herdian** (23825301) · Magister Instrumentasi dan Kontrol, FTI ITB
· Agustus 2026 – April 2027

---

## Mulai dari mana

| Kalau kamu mau… | Buka |
|---|---|
| Tahu alur kerja risetnya | [`docs/workflow.md`](docs/workflow.md) |
| Menulis proposal | [`tulisan/proposal/main.tex`](tulisan/proposal/main.tex) |
| Menulis laporan akhir | [`tulisan/laporan-akhir/main.tex`](tulisan/laporan-akhir/main.tex) |
| Merancang eksperimen baru | [`docs/experiments/TEMPLATE-desain-eksperimen.md`](docs/experiments/TEMPLATE-desain-eksperimen.md) |
| Tahu konteks & aturan repo | [`CLAUDE.md`](CLAUDE.md) |

## Kompilasi naskah

Butuh **XeLaTeX** (dokumen memakai `fontspec` + Times New Roman) beserta
`latexmk` dan `bibtex`.

```bash
make proposal      # → tulisan/proposal/main.pdf        (48 halaman)
make laporan       # → tulisan/laporan-akhir/main.pdf   (kerangka)
make watch-p       # kompilasi ulang otomatis sambil menulis proposal
make check         # gagal kalau masih ada rujukan/sitasi menggantung
make clean         # buang artefak build
```

## Struktur

```
tulisan/
├── proposal/          proposal tesis — selesai
├── laporan-akhir/     kerangka laporan akhir
├── common/            itb-tesis.sty · references.bib · logo (dipakai bersama)
└── diagrams/          sumber diagram *.drawio
docs/
├── workflow.md        alur kerja riset dari pustaka sampai sidang
└── experiments/       dokumen desain, satu per eksperimen
experiments/           konfigurasi tiap eksperimen
results/               keluaran run, satu folder per <tanggal>-<id>
src/                   kode simulasi (MultiAgentSim)
```

Format dokumen (font, margin, penomoran) terpusat di
`tulisan/common/itb-tesis.sty`, dipakai proposal maupun laporan akhir supaya
keduanya tidak pernah menyimpang satu sama lain. Bibliografinya juga satu:
`tulisan/common/references.bib`.

## Penandaan versi

Tiap bab atau eksperimen yang selesai divalidasi ditandai:

```bash
git tag -a v0.2-sim-iapf -m "IAPF tervalidasi pada skenario koridor"
```

supaya setiap angka di naskah bisa dilacak ke keadaan kode saat itu.
