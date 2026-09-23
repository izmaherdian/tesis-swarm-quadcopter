#!/usr/bin/env bash
# Ekspor satu halaman proposal-tesis.drawio menjadi PDF terpangkas.
#
#   ./ekspor-drawio.sh Metodologi ../proposal/figures/metodologi_tesis.pdf
#
# Caranya memuat halaman lewat penampil resmi draw.io di Chrome headless, mencetaknya
# ke PDF, lalu memangkas marginnya dengan pdfcrop. Butuh google-chrome, pdfcrop, dan
# sekali unduhan viewer-static.min.js yang disimpan di cache.
set -euo pipefail

HALAMAN="${1:?nama halaman drawio, misalnya Metodologi}"
KELUARAN="${2:?berkas PDF tujuan}"
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SUMBER="$DIR/proposal-tesis.drawio"
CACHE="${XDG_CACHE_HOME:-$HOME/.cache}/drawio-viewer"
KERJA="$(mktemp -d)"
trap 'rm -rf "$KERJA"' EXIT

mkdir -p "$CACHE"
if [ ! -s "$CACHE/viewer-static.min.js" ]; then
    echo "Mengunduh penampil draw.io sekali saja ke $CACHE"
    curl -sfL -o "$CACHE/viewer-static.min.js" https://viewer.diagrams.net/js/viewer-static.min.js
fi
cp "$CACHE/viewer-static.min.js" "$KERJA/viewer.js"

python3 - "$SUMBER" "$HALAMAN" "$KERJA/diagram.html" <<'PY'
import html, json, sys, xml.etree.ElementTree as ET

sumber, halaman, tujuan = sys.argv[1], sys.argv[2], sys.argv[3]
akar = ET.parse(sumber).getroot()
cocok = [d for d in akar.findall("diagram") if d.get("name") == halaman]
if not cocok:
    raise SystemExit(f"halaman '{halaman}' tidak ada di {sumber}")
model = cocok[0].find("mxGraphModel")
xml_halaman = ET.tostring(model, encoding="unicode")

konfigurasi = {"xml": xml_halaman, "highlight": "#ffffff", "nav": False,
               "resize": True, "toolbar": None, "zoom": 1}
atribut = html.escape(json.dumps(konfigurasi), quote=True)
open(tujuan, "w").write(f"""<!doctype html>
<html><head><meta charset="utf-8">
<style>@page {{ size: 320mm 420mm; margin: 0 }}
 html, body {{ margin: 0; padding: 12px; background: #fff }}</style>
</head><body>
<div class="mxgraph" data-mxgraph="{atribut}"></div>
<script src="viewer.js"></script>
</body></html>""")
PY

google-chrome --headless=new --disable-gpu --no-sandbox --no-pdf-header-footer \
    --virtual-time-budget=20000 --print-to-pdf="$KERJA/mentah.pdf" \
    "file://$KERJA/diagram.html" 2>/dev/null

pdfcrop --margins 4 "$KERJA/mentah.pdf" "$KERJA/terpangkas.pdf" >/dev/null
mkdir -p "$(dirname "$KELUARAN")"
cp "$KERJA/terpangkas.pdf" "$KELUARAN"
echo "✓ $KELUARAN"
