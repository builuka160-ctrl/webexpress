#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Вставляет (или обновляет) JSON-LD блок в латышский index.html."""
import io, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import seo

SRC = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'index.html')
html = io.open(SRC, encoding='utf-8').read()
block = seo.block('lv')

pattern = re.compile(re.escape(seo.MARK_START) + r'.*?' + re.escape(seo.MARK_END), re.S)
if pattern.search(html):
    html = pattern.sub(lambda m: block, html, count=1)
    action = 'обновлён'
else:
    html = html.replace('</head>', block + '\n</head>', 1)
    action = 'добавлен'

io.open(SRC, 'w', encoding='utf-8').write(html)
print('JSON-LD ' + action)
