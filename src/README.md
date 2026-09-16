# src/

Kode simulasi. Saat ini dikembangkan di repo terpisah:
<https://github.com/izmaherdian/MultiAgentSim>

Dua pilihan saat kode mulai digarap bersama naskah:

**a. Submodule** — riwayat simulasi tetap terpisah, tapi tesis merekam versi
   persis yang dipakai:
```bash
git submodule add https://github.com/izmaherdian/MultiAgentSim src/MultiAgentSim
```

**b. Satukan** — pindahkan kode ke sini dan kembangkan dalam satu repo. Lebih
   sederhana, dan setiap commit naskah selalu sejalan dengan kodenya.

Pilih (a) kalau simulator akan dipakai di luar tesis ini; (b) kalau tidak.
