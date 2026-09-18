#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Собирает sitemap.xml со всеми страницами и языковыми альтернативами."""
import io, os, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = 'https://webexpress.lv'

# (путь, приоритет, частота, альтернативы hreflang)
LANG_PAIR = [('lv', SITE + '/'), ('ru', SITE + '/ru/'), ('x-default', SITE + '/')]

# Демо-концепты сознательно закрыты от индексации (noindex в их <head>):
# это вымышленные заведения с вымышленными адресами, в поиске им не место.
# Поэтому в карте сайта их нет — иначе Search Console справедливо ругается.
PAGES = [
    ('/',                 '1.0', 'weekly',  LANG_PAIR),
    ('/ru/',              '1.0', 'weekly',  LANG_PAIR),
    ('/kalkulators.html', '0.6', 'monthly', []),
]


def build(lastmod=None):
    lastmod = lastmod or datetime.date.today().isoformat()
    out = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
           '        xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for path, priority, freq, alts in PAGES:
        out.append('  <url>')
        out.append('    <loc>%s%s</loc>' % (SITE, path))
        out.append('    <lastmod>%s</lastmod>' % lastmod)
        out.append('    <changefreq>%s</changefreq>' % freq)
        out.append('    <priority>%s</priority>' % priority)
        for lang, href in alts:
            out.append('    <xhtml:link rel="alternate" hreflang="%s" href="%s"/>' % (lang, href))
        out.append('  </url>')
    out.append('</urlset>')
    return '\n'.join(out) + '\n'


if __name__ == '__main__':
    target = os.path.join(ROOT, 'sitemap.xml')
    io.open(target, 'w', encoding='utf-8').write(build())
    print('sitemap.xml: %d адресов' % len(PAGES))
