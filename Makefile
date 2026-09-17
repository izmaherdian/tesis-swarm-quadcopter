# Makefile tesis — swarm quadcopter (IAPF + ERC)
#
#   make proposal   → kompilasi tulisan/proposal/main.pdf
#   make laporan    → kompilasi tulisan/laporan-akhir/main.pdf
#   make all        → keduanya
#   make gambar     → hasilkan ulang seluruh gambar dari tulisan/gambar/gbr_*.py
#   make watch-p    → kompilasi ulang otomatis tiap kali proposal disimpan
#   make clean      → buang artefak build, PDF tetap ada
#   make distclean  → buang artefak build beserta PDF-nya
#
# Wajib XeLaTeX: dokumen memakai fontspec + unicode-math (Times New Roman).

LATEXMK := latexmk -xelatex -bibtex -interaction=nonstopmode -halt-on-error

.PHONY: all proposal laporan gambar watch-p watch-l clean distclean check

all: proposal laporan

proposal:
	$(LATEXMK) -cd tulisan/proposal/main.tex

laporan:
	$(LATEXMK) -cd tulisan/laporan-akhir/main.tex

# Gambar dibuat skrip (Times New Roman, PDF vektor ukuran cetak) — jangan
# menyunting PDF di tulisan/proposal/figures/ secara manual.
gambar:
	@cd tulisan/gambar && for f in gbr_*.py; do python3 $$f || exit 1; done

watch-p:
	$(LATEXMK) -pvc -cd tulisan/proposal/main.tex

watch-l:
	$(LATEXMK) -pvc -cd tulisan/laporan-akhir/main.tex

# Gagalkan build kalau masih ada rujukan/sitasi yang tidak terdefinisi.
# Pakai ini sebelum mengirim draf ke pembimbing.
check: proposal
	@n=$$(grep -c 'undefined' tulisan/proposal/main.log || true); \
	if [ "$$n" -ne 0 ]; then \
		echo "GAGAL: $$n rujukan/sitasi tidak terdefinisi"; \
		grep 'Warning.*undefined' tulisan/proposal/main.log | head -20; \
		exit 1; \
	fi; \
	echo "OK: tidak ada rujukan atau sitasi yang menggantung"

clean:
	latexmk -c -cd tulisan/proposal/main.tex
	latexmk -c -cd tulisan/laporan-akhir/main.tex

distclean:
	latexmk -C -cd tulisan/proposal/main.tex
	latexmk -C -cd tulisan/laporan-akhir/main.tex
