# experiments/

Satu folder per eksperimen, dinamai dengan ID yang sama seperti dokumen
desainnya di `docs/experiments/`.

```
experiments/
└── E01-iapf-baseline/
    ├── config.yaml     seluruh parameter — TIDAK ADA angka ajaib di dalam kode
    └── run.py          skrip yang membaca config.yaml lalu menjalankan simulasi
```

Aturannya satu: `run.py` tidak boleh punya parameter yang tidak berasal dari
`config.yaml`, dan `config.yaml` harus ikut tersalin ke folder hasil. Kalau
dilanggar, hasil di `results/` tidak bisa direproduksi dan BAB Metodologi tidak
punya dasar.
