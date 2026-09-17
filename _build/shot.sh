#!/bin/bash
# shot.sh <index.html> <out.png> <width> <height>  — renders a review copy (animations off, images eager)
set -e
SRC=$(readlink -f "$1"); OUT="$2"; W="${3:-1440}"; H="${4:-4000}"
DIR=$(dirname "$SRC")
TMP="$DIR/.shot.html"
python3 - "$SRC" "$TMP" <<'PY'
import sys
src,dst=sys.argv[1],sys.argv[2]
s=open(src).read().replace('loading="lazy"','')
s=s.replace('</head>','<style>.rise,.reveal-item{opacity:1!important;transform:none!important}'
  '.scrub{height:auto!important}.scrub-sticky{position:static!important;min-height:0!important;height:auto!important;padding-block:30px!important}'
  '.scrub-sticky video{display:none}.poster{opacity:1!important}.hero-stage{height:auto!important}.hero-pin{position:static!important;height:auto!important}'
  '</style></head>')
open(dst,'w').write(s)
PY
timeout 120 google-chrome-stable --headless=new --disable-gpu --no-sandbox --hide-scrollbars \
  --virtual-time-budget=9000 --window-size=$W,$H --screenshot="$OUT" "file://$TMP" >/dev/null 2>&1
rm -f "$TMP"
identify "$OUT"
