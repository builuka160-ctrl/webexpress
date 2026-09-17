#!/usr/bin/env python3
"""Pulls every translatable string (text nodes + attributes) out of a demo page."""
import re, sys, json
from html.parser import HTMLParser

SKIP = {'script', 'style'}
ATTRS = ('alt', 'placeholder', 'aria-label', 'title')

class Ex(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack, self.items = [], []
    def handle_starttag(self, tag, attrs):
        self.stack.append(tag)
        d = dict(attrs)
        for a in ATTRS:
            if d.get(a) and re.search('[А-Яа-яЁё]', d[a]):
                self.items.append(('attr:' + a, d[a]))
        if tag == 'meta' and d.get('content') and re.search('[А-Яа-яЁё]', d['content']):
            self.items.append(('meta:' + (d.get('name') or d.get('property') or '?'), d['content']))
        if tag in ('img', 'br', 'meta', 'link', 'input', 'hr', 'source', 'path', 'svg', 'circle', 'rect'):
            if self.stack and self.stack[-1] == tag:
                self.stack.pop()
    def handle_endtag(self, tag):
        while self.stack:
            t = self.stack.pop()
            if t == tag:
                break
    def handle_data(self, data):
        if self.stack and self.stack[-1] in SKIP:
            return
        t = data.strip()
        if t and re.search('[А-Яа-яЁё]', t):
            self.items.append(('text', t))

for page in sys.argv[1:]:
    p = Ex(); p.feed(open(page).read())
    seen, out = set(), []
    for kind, val in p.items:
        v = ' '.join(val.split())
        if v in seen:
            continue
        seen.add(v); out.append({'kind': kind, 'ru': v})
    print(page, len(out), 'strings')
    json.dump(out, open(page.replace('/index.html', '/.strings.json'), 'w'),
              ensure_ascii=False, indent=1)
