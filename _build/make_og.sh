#!/bin/bash
# Пересобирает og-image.png (превью ссылки 1200x630) из шаблона _build/og_image.html.
# Нужен headless-браузер: в этом окружении — сборка Playwright, локально подойдёт
# любой Chrome/Chromium (подставьте свой путь в CHROME).
set -e
CHROME="${CHROME:-/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell}"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
"$CHROME" --disable-gpu --no-sandbox --hide-scrollbars --virtual-time-budget=2000 \
  --window-size=1200,630 --screenshot="$ROOT/og-image.png" "file://$ROOT/_build/og_image.html"
echo "og-image.png пересобран"
