#!/bin/bash
# crude LCP probe: injects PerformanceObserver, writes result into <title>, reads it from dumped DOM
SRC="$1"; W="${2:-1440}"; H="${3:-900}"
DIR=$(dirname "$SRC"); TMP="$DIR/.lcp.html"
python3 - "$SRC" "$TMP" <<'PY'
import sys
src,dst=sys.argv[1],sys.argv[2]
s=open(src).read()
probe="""<script>
var _lcp=0;new PerformanceObserver(function(l){l.getEntries().forEach(function(e){_lcp=e.startTime})}).observe({type:'largest-contentful-paint',buffered:true});
setTimeout(function(){document.title='LCP='+Math.round(_lcp)+'ms DCL='+Math.round(performance.timing.domContentLoadedEventEnd-performance.timing.navigationStart)},2500);
</script></body>"""
open(dst,'w').write(s.replace('</body>',probe))
PY
timeout 90 google-chrome-stable --headless=new --disable-gpu --no-sandbox --virtual-time-budget=6000 \
  --window-size=$W,$H --dump-dom "file://$TMP" 2>/dev/null | grep -o '<title>[^<]*</title>' | head -1
rm -f "$TMP"
