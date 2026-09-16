# src/

Kode simulasi. Dikembangkan di repo terpisah:
<https://github.com/izmaherdian/MultiAgentSim>

## Kenapa bukan submodule

Rencana awal memakai `git submodule`, tapi dibatalkan setelah diukur: **repo
MultiAgentSim berukuran 481 MB**, hampir seluruhnya dari `Documentation/`
(satu PPTX 80,5 MB, PDF presentasi 11 MB, PDF laporan 6 MB) ditambah riwayat
berkas biner tersebut. Sebagai submodule, setiap orang yang meng-clone repo
tesis ini dengan `--recurse-submodules` ikut menarik 481 MB — termasuk kamu
sendiri saat pindah mesin. Percobaan clone penuh di jaringan lab juga gagal
(`fetch-pack: unexpected disconnect`).

Gantinya: simulator di-clone **sebagian** ke `src/MultiAgentSim/` (diabaikan
git), dan versinya dikunci lewat `src/MultiAgentSim.version` yang ikut
di-commit. Ketertelusuran tetap terjaga — tiap `results/<run>/commit.txt`
mencatat hash repo tesis dan hash simulator.

## Menyiapkan simulator

```bash
git clone --depth 1 --filter=blob:none --sparse \
    https://github.com/izmaherdian/MultiAgentSim src/MultiAgentSim
cd src/MultiAgentSim
git sparse-checkout set Agent Environment Visualization
git checkout $(cut -d' ' -f1 ../MultiAgentSim.version)   # kunci ke versi tercatat
```

`--filter=blob:none --sparse` membuat hanya kode yang diunduh; `Documentation/`
dilewati. Kalau suatu saat isi `Documentation/` dibutuhkan:

```bash
git sparse-checkout add Documentation
```

## Kalau nanti ingin disatukan

Bila `Documentation/` dibersihkan dari riwayat MultiAgentSim (`git filter-repo`),
ukurannya akan turun drastis dan submodule kembali masuk akal. Itu menulis ulang
riwayat repo tersebut, jadi keputusan terpisah — bukan bagian pekerjaan ini.
