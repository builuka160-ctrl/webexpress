#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Пересобирает webexpress-latest.zip — то, что кладётся в web-root.

Внутрь попадает всё, кроме служебных каталогов сборки и самих архивов.
"""
import io, os, zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TARGET = os.path.join(ROOT, 'webexpress-latest.zip')

SKIP_DIRS = {'.git', '_build', 'node_modules'}
SKIP_FILES = {'webexpress-latest.zip', 'webexpress-site-29mb.zip',
              'README.md', 'DEMO-NOTES.md', 'SEO.md'}


def collect():
    for base, dirs, files in os.walk(ROOT):
        dirs[:] = sorted(d for d in dirs if d not in SKIP_DIRS and not d.startswith('.'))
        for name in sorted(files):
            if name in SKIP_FILES or name.startswith('.'):
                continue
            full = os.path.join(base, name)
            yield full, os.path.relpath(full, ROOT)


def main():
    files = list(collect())
    with zipfile.ZipFile(TARGET, 'w', zipfile.ZIP_DEFLATED) as z:
        for full, rel in files:
            z.write(full, rel)
    size = os.path.getsize(TARGET) / (1024.0 * 1024.0)
    print('webexpress-latest.zip: %d файлов, %.1f МБ' % (len(files), size))


if __name__ == '__main__':
    main()
