#!/bin/bash
SRC=$(readlink -f "$1"); OUT="$2"; W="${3:-1440}"; H="${4:-1000}"
DIR=$(dirname "$SRC"); TMP="$DIR/.shotlv.html"
python3 - "$SRC" "$TMP" <<'PY'
import sys
src,dst=sys.argv[1],sys.argv[2]
s=open(src).read().replace('loading="lazy"','')
s=s.replace('</head>','<style>.rise,.reveal-item{opacity:1!important;transform:none!important}'
 '.scrub{height:auto!important}.scrub-sticky{position:static!important;min-height:0!important;height:auto!important;padding-block:30px!important}'
 '.scrub-sticky video{display:none}.poster{opacity:1!important}</style></head>')
open(dst,'w').write(s)
PY
REL=$(realpath --relative-to=/home/kali/webexpress-site "$TMP")
timeout 120 google-chrome-stable --headless=new --disable-gpu --no-sandbox --hide-scrollbars \
  --virtual-time-budget=9000 --window-size=$W,$H --screenshot="$OUT" "http://127.0.0.1:8099/$REL?lang=lv" >/dev/null 2>&1
rm -f "$TMP"
