# results/

Satu folder per run, **tidak pernah diedit setelah dibuat**. Kalau perlu
mengulang, buat folder baru — jangan menimpa.

```
results/
└── 2026-10-14-E01-iapf-baseline/
    ├── config.yaml     salinan persis konfigurasi yang dipakai
    ├── commit.txt      keluaran `git rev-parse HEAD` saat run
    ├── metrics.csv     metrik per langkah waktu
    ├── summary.json    metrik ringkas
    ├── figures/        gambar yang masuk ke naskah
    └── catatan.md      pengamatan, kejanggalan, dugaan
```

`config.yaml` + `commit.txt` adalah dua berkas yang membuat angka di BAB IV bisa
dipertanggungjawabkan di sidang. Data mentah berukuran besar (`*.npz`, `*.mp4`,
`raw/`) diabaikan git — yang di-commit hanya ringkasan dan metrik.
