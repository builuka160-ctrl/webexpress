#!/usr/bin/env python3
"""Builds demo/<site>/PROMPTS.md out of the generation manifests."""
import json, os, collections

B = '/home/kali/webexpress-site/_build'
SITE = '/home/kali/webexpress-site/demo'

# raw stem -> (final asset, размер, где стоит)
MAP = {
 'kafejnica': {
  'hero-cup':      ('hero-cup.webp',      '900×672, 4:3',  'коллаж первого экрана, крупная карточка'),
  'hero-iced':     ('hero-iced.webp',     '700×933, 3:4',  'коллаж первого экрана, вертикальная карточка'),
  'hero-shelf':    ('hero-shelf.webp',    '700×700, 1:1',  'коллаж первого экрана, квадрат слева внизу'),
  'hero-counter':  ('hero-counter.webp',  '700×700, 1:1',  'коллаж первого экрана, квадрат по центру'),
  'menu-espresso': ('menu-espresso.webp', '800×1000, 4:5', 'карточка меню «Эспрессо»'),
  'menu-latte':    ('menu-latte.webp',    '800×1000, 4:5', 'карточка меню «Флэт уайт» + коллаж хиро'),
  'menu-filter':   ('menu-filter.webp',   '800×1000, 4:5', 'карточка меню «Фильтр V60»'),
  'pastry':        ('pastry.webp',        '1400×788, 16:9','блок «Пекарня»'),
  'interior-wide': ('interior-wide.webp', '1600×900, 16:9','блок «Зал», фон под текстом'),
  'reveal-green':  ('roast-poster.webp',  '1200×900, 4:3', 'постер скролл-видео (кадр «до»)'),
  'og':            ('og.jpg',             '1200×630, 16:9','превью в соцсетях'),
 },
 'detailing': {
  'hero-car':       ('hero-car.webp',     '1500×837, 16:9','первый экран, фон вычищается до белого'),
  'hero-car-clean': ('hero-car.webp',     '1500×837, 16:9','первый экран (правка кадра выше)'),
  'hero-car-dark':  ('car-rear.webp',     '1100×614, 16:9','конец прайса, справа внизу'),
  'polish':         ('polish.webp',       '800×600, 4:3',  'сетка «Что входит в работу» — Полировка'),
  'beading':        ('beading.webp',      '800×600, 4:3',  'сетка — Керамика'),
  'wheel':          ('wheel.webp',        '800×600, 4:3',  'сетка — Диски'),
  'interior':       ('interior.webp',     '800×600, 4:3',  'сетка — Салон'),
  'engine':         ('engine.webp',       '800×600, 4:3',  'сетка — Моторный отсек'),
  'tools':          ('tools.webp',        '1400×788, 16:9','сетка — Чем работаем'),
  'reveal-dirty':   ('reveal-dirty.webp', '1200×675, 16:9','ползунок «до/после», левая половина'),
  'reveal-clean':   ('reveal-clean.webp', '1200×675, 16:9','ползунок «до/после», правая половина'),
  'og':             ('og.jpg',            '1200×630, 16:9','превью в соцсетях'),
 },
 'dental': {
  'hero-implant': ('hero-implant.webp','560×802, 4:5','первый экран, фон вырезается в прозрачность'),
  'tray':         ('tray.webp',        '800×600, 4:3','карточка «Лечение и реставрация»'),
  'aligner':      ('aligner.webp',     '800×600, 4:3','карточка «Имплантация и протезирование»'),
  'hygiene':      ('hygiene.webp',     '800×600, 4:3','карточка «Гигиена и профилактика»'),
  'veneers':      ('veneers.webp',     '800×600, 4:3','блок «Оборудование» — Керамика'),
  'scanner':      ('scanner.webp',     '800×600, 4:3','блок «Оборудование» — 3D-сканер'),
  'chair':        ('chair.webp',       '1400×788, 16:9','блок «Клиника»'),
  'og':           ('og.jpg',           '1200×630, 16:9','превью в соцсетях'),
 },
}
SITE_OF = {'coffee':'kafejnica','coffee2':'kafejnica','detailing':'detailing',
           'detailing2':'detailing','dental':'dental'}
TITLE = {'kafejnica':'GRAIN & ROAST — кофейня','detailing':'NORDIC DETAILING — детейлинг',
         'dental':'ESTETIKA DENTAL — стоматология'}

jobs = collections.defaultdict(list)
for man, site in SITE_OF.items():
    path = os.path.join(B, man + '.json')
    if not os.path.exists(path):
        continue
    for j in json.load(open(path)):
        stem = os.path.splitext(os.path.basename(j['out']))[0]
        jobs[site].append((stem, j))

videos = {}
for man in ['video.json', 'video2.json']:
    for j in json.load(open(os.path.join(B, man))):
        videos[os.path.splitext(os.path.basename(j['out']))[0]] = j

VID = {
 'kafejnica': ('roast-scrub.mp4', 'roast-poster.webp', 'kafejnica',
   'секция «Вторник — день обжарки», прокрутка мотает ролик кадр за кадром'),
 'detailing': ('wash-scrub.mp4', 'wash-poster.webp', 'detailing',
   'секция «Результат», прокрутка мотает ролик кадр за кадром'),
}

HEAD = """# Промпты ассетов — {title}

Всё, что здесь перечислено, сгенерировано в Gemini. Если генеришь лучше — клади
файл с **тем же именем и теми же пропорциями** в `assets/`, вёрстка подхватит
без правок. Исходники и скрипты генерации — в `_build/`.

Формат: прогоняй промпт как есть (английский), потом ужимай под размер:

```bash
magick новый.png -resize 800x -strip -quality 80 assets/имя.webp
```

Общие правила по всем кадрам: без текста, логотипов и водяных знаков, без людей
и лиц, свет задан явно, пропорции — под контейнер, а не квадрат по умолчанию.

---

"""

for site, items in jobs.items():
    seen = set(); out = [HEAD.format(title=TITLE[site])]
    for stem, j in items:
        info = MAP[site].get(stem)
        if not info:
            continue
        asset, size, where = info
        if (asset, stem) in seen:
            continue
        seen.add((asset, stem))
        out.append('## `assets/%s`\n' % asset)
        out.append('**Где:** %s  \n**Размер:** %s  \n**Модель:** `%s`  \n**Aspect ratio в запросе:** `%s`\n'
                   % (where, size, j.get('model', 'gemini-3.1-flash-image'), j.get('ratio', '16:9')))
        if j.get('ref'):
            out.append('\n> Кадр-правка: сначала генерится `%s`, потом он же отдаётся моделью как\n'
                       '> референс вместе с этим промптом — так совпадают ракурс, фон и свет.\n'
                       % os.path.basename(j['ref']))
        out.append('\n```text\n%s\n```\n\n' % j['prompt'].strip())
    if site in VID:
        mp4, poster, key, where = VID[site]
        v = videos[key]
        out.append('## `assets/%s` (скролл-видео) + `assets/%s`\n' % (mp4, poster))
        out.append('**Где:** %s  \n**Модель:** `%s`, 16:9, 720p, 6 секунд  \n'
                   '**Опорные кадры:** первый — `%s`, последний — `%s`\n'
                   % (where, v.get('model', 'veo-3.1-fast-generate-preview'),
                      os.path.basename(v['image']), os.path.basename(v.get('lastFrame', '—'))))
        out.append('\n```text\n%s\n```\n' % v['prompt'].strip())
        out.append('\n**Negative prompt:**\n\n```text\n%s\n```\n' % v.get('negativePrompt', ''))
        out.append("""
Ролик обязан проматываться кадр за кадром, поэтому камера неподвижна, склеек нет,
движение равномерное. После генерации:

```bash
ffmpeg -i новый.mp4 -t 6 -an -vf "scale=900:-2" \\
  -c:v libx264 -crf 31 -g 1 -keyint_min 1 -sc_threshold 0 \\
  -movflags +faststart assets/%s
ffmpeg -i assets/%s -frames:v 1 poster.png && magick poster.png -resize 900x -quality 78 assets/%s
```

`-g 1` делает каждый кадр ключевым — без этого перемотка идёт ступеньками.
Держи файл в пределах 1,5 МБ.
""" % (mp4, mp4, poster))
    open(os.path.join(SITE, site, 'PROMPTS.md'), 'w').write(''.join(out))
    print('written', site, len(seen), 'images')

# отдельный файл: чего не хватает
v = videos['dental']
open(os.path.join(SITE, 'dental', 'PROMPTS.md'), 'a').write("""
---

## Чего пока нет: скролл-видео для стоматологии

На этот ролик не хватило кредитов Gemini — секции на сайте нет. Если сгенеришь,
скажи, и я вставлю такую же секцию, как в кофейне и детейлинге.

**Модель:** `%s`, 16:9, 720p, 6 секунд  \n**Первый кадр:** `hero-implant.png`

```text
%s
```

**Negative prompt:**

```text
%s
```
""" % (v.get('model', 'veo-3.1-fast-generate-preview'), v['prompt'].strip(), v.get('negativePrompt', '')))
print('dental video note appended')
