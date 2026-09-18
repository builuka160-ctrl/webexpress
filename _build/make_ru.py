#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Генерирует /ru/index.html — русскую версию лендинга со статическим текстом.

Зачем отдельная страница, а не переключатель на лету: поисковые роботы
индексируют то, что пришло в HTML. Пока русский текст подставлялся скриптом
поверх латышского на том же URL, запросы вроде «заказать сайт» не имели
ни одной страницы-ответа. Теперь у каждого языка свой адрес, свой title,
свой canonical и своя микроразметка.

Запуск:  python3 _build/make_ru.py
Источник правды — index.html: правим его, потом пересобираем эту страницу.
"""
import io, os, re, sys, html as html_mod

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import seo

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'index.html')
OUT_DIR = os.path.join(ROOT, 'ru')
OUT = os.path.join(OUT_DIR, 'index.html')


def read_dictionary(src):
    """Достаёт русский словарь из inline-скрипта лендинга.

    Ключи там простые идентификаторы, значения — строки в двойных кавычках
    с экранированием, как в JS. Разбираем построчно, без исполнения кода.
    """
    start = src.index('      ru: {')
    end = src.index('\n      },', start)
    body = src[start:end]
    pairs = re.findall(r'^\s{8}([A-Za-z0-9_]+):\s*"(.*)",?\s*$', body, re.M)
    if not pairs:
        sys.exit('русский словарь не разобран')
    out = {}
    for key, raw in pairs:
        out[key] = raw.replace('\\"', '"').replace('\\\\', '\\')
    return out


def apply_dictionary(src, ru):
    """Подставляет русский текст в узлы с data-i18n прямо в разметке."""
    counters = {'text': 0, 'placeholder': 0, 'aria': 0, 'wa': 0}

    def text_sub(m):
        head, key, tail = m.group(1), m.group(2), m.group(3)
        if key not in ru:
            return m.group(0)
        counters['text'] += 1
        return head + key + tail + ru[key] + '</'

    # <tag ... data-i18n="key" ...>СОДЕРЖИМОЕ</
    pattern = re.compile(r'(<[a-zA-Z0-9]+[^>]*?data-i18n=")([A-Za-z0-9_]+)("[^>]*>)(?:(?!</).)*?</', re.S)
    src = pattern.sub(text_sub, src)

    def attr_sub(attr, target, counter):
        def repl(m):
            key = m.group('key')
            if key not in ru:
                return m.group(0)
            counters[counter] += 1
            tag = m.group(0)
            value = html_mod.escape(ru[key], quote=True)
            new_attr = target + '="' + value + '"'
            if re.search(r'\b' + re.escape(target) + r'="[^"]*"', tag):
                return re.sub(r'\b' + re.escape(target) + r'="[^"]*"', lambda _: new_attr, tag, count=1)
            return tag[:-1] + ' ' + new_attr + '>'
        return re.compile(r'<[a-zA-Z0-9]+[^>]*?data-i18n-' + attr + r'="(?P<key>[A-Za-z0-9_]+)"[^>]*>').sub(repl, src)

    src = attr_sub('placeholder', 'placeholder', 'placeholder')
    src = attr_sub('aria-label', 'aria-label', 'aria')

    # Ссылки WhatsApp: текст заготовленного сообщения тоже на русском.
    def wa_sub(m):
        key = m.group('key')
        if key not in ru:
            return m.group(0)
        counters['wa'] += 1
        from urllib.parse import quote
        href = 'https://wa.me/37122441603?text=' + quote(ru[key], safe='')
        return re.sub(r'href="[^"]*"', lambda _: 'href="' + href + '"', m.group(0), count=1)

    src = re.compile(r'<a[^>]*?data-i18n-wa="(?P<key>[A-Za-z0-9_]+)"[^>]*>').sub(wa_sub, src)
    return src, counters


def localize_head(src, ru):
    """Меняет язык, мета-теги, canonical и микроразметку на русские."""
    t = seo.TEXT['ru']
    src = src.replace('<html lang="lv">', '<html lang="ru">', 1)

    replacements = [
        ('<title>Mājas lapas izstrāde Latvijā — pasūti mājaslapu no 250 € | WebExpress</title>',
         '<title>Заказать сайт под ключ — создание сайтов от 250 € | WebExpress</title>'),
        ('content="Mājas lapas izstrāde uzņēmumiem Latvijā: demo 48 stundu laikā bez priekšapmaksas. '
         'Pasūti mājaslapu no 250 € ar fiksētu cenu. Rēzekne, Rīga."',
         'content="Закажите сайт онлайн: демо за 48 часов без предоплаты. Создание и разработка сайтов '
         'под ключ для бизнеса — лендинг, сайт-визитка, хостинг и поддержка. Латвия."'),
        ('<link rel="canonical" href="https://webexpress.lv/">',
         '<link rel="canonical" href="https://webexpress.lv/ru/">'),
        ('<meta property="og:locale" content="lv_LV">',
         '<meta property="og:locale" content="ru_RU">'),
        ('<meta property="og:locale:alternate" content="ru_RU">',
         '<meta property="og:locale:alternate" content="lv_LV">'),
        ('<meta property="og:title" content="Mājas lapas izstrāde Latvijā — pasūti mājaslapu no 250 €">',
         '<meta property="og:title" content="Заказать сайт под ключ — создание сайтов от 250 €">'),
        ('<meta property="og:description" content="Demo vietne 48 stundu laikā bez priekšapmaksas. '
         'Maksā tikai tad, kad redzi rezultātu. Rēzekne / Rīga.">',
         '<meta property="og:description" content="Демо-сайт за 48 часов без предоплаты. '
         'Платите только тогда, когда видите результат. Резекне / Рига.">'),
        ('<meta property="og:url" content="https://webexpress.lv/">',
         '<meta property="og:url" content="https://webexpress.lv/ru/">'),
        ('<meta property="og:image:alt" content="WebExpress — mājas lapas izstrāde Latvijā">',
         '<meta property="og:image:alt" content="WebExpress — создание сайтов под ключ в Латвии">'),
        ('<meta name="twitter:title" content="Mājas lapas izstrāde Latvijā — pasūti mājaslapu no 250 €">',
         '<meta name="twitter:title" content="Заказать сайт под ключ — создание сайтов от 250 €">'),
        ('<meta name="twitter:description" content="Demo 48 stundu laikā bez priekšapmaksas. '
         'Maksā tikai par rezultātu.">',
         '<meta name="twitter:description" content="Демо за 48 часов без предоплаты. '
         'Платите только за результат.">'),
        ('<meta name="geo.placename" content="Rēzekne">',
         '<meta name="geo.placename" content="Резекне">'),
        ('<!-- Valodu versijas: latviešu sakne, krievu /ru/ -->',
         '<!-- Языковые версии: латышская в корне, русская в /ru/ -->'),
    ]
    for old, new in replacements:
        if old not in src:
            sys.exit('не найден фрагмент head: ' + old[:70])
        src = src.replace(old, new, 1)

    # Микроразметка — русская.
    pattern = re.compile(re.escape(seo.MARK_START) + r'.*?' + re.escape(seo.MARK_END), re.S)
    if not pattern.search(src):
        sys.exit('блок JSON-LD не найден')
    src = pattern.sub(lambda m: seo.block('ru'), src, count=1)
    return src


def rebase_assets(src):
    """Страница лежит на уровень глубже — относительные пути получают ../."""
    prefixes = ('favicon.ico', 'webexpress-favicon-v2.png', 'webexpress-apple-touch-icon.png',
                'demo/', 'assets/', 'kalkulators.html')
    def repl(m):
        attr, value = m.group(1), m.group(2)
        if value.startswith(prefixes):
            return attr + '="../' + value + '"'
        return m.group(0)
    return re.sub(r'\b(href|src)="([^"]+)"', repl, src)


def localize_static_strings(src):
    """Текст без data-i18n: стартовые подписи 3D-разбора и подвал.

    Скролл-движок дальше сам переписывает подписи по currentLang, но в HTML
    они должны прийти уже на русском — робот и пользователь без JS видят
    именно исходную разметку.
    """
    pairs = [
        ('<span id="active-layer-indicator">Salikts • Monolīta mājaslapa</span>',
         '<span id="active-layer-indicator">Собрано • Монолитный лендинг</span>'),
        ('Saliktā veidā visi trīs slāņi strādā kā viens ļoti ātrs mehānisms.',
         'В собранном виде все три слоя работают как единый сверхбыстрый механизм.'),
        ('WebExpress • Rēzekne', 'WebExpress • Резекне'),
        ('data-i18n="contacts_location_label">Локация:</span> Rēzekne, Latvija',
         'data-i18n="contacts_location_label">Локация:</span> Резекне, Латвия'),
        # Alt-тексты у картинок тоже должны быть на языке страницы.
        ('alt="Zobārstniecības demo mājaslapa Estetika Dental: pirmais ekrāns"',
         'alt="Демо-сайт стоматологии Estetika Dental: первый экран"'),
        ('alt="Detailinga centra demo mājaslapa Nordic Detailing: pirmais ekrāns"',
         'alt="Демо-сайт детейлинг-центра Nordic Detailing: первый экран"'),
        ('alt="Kafejnīcas demo mājaslapa Grain &amp; Roast: pirmais ekrāns"',
         'alt="Демо-сайт кофейни Grain &amp; Roast: первый экран"'),
        ('alt="Maksims A. — WebExpress mārketinga speciālists"',
         'alt="Максим А. — маркетолог WebExpress"'),
        ('alt="Luka O. — WebExpress IT speciālists"',
         'alt="Лука О. — IT-специалист WebExpress"'),
    ]
    for old_s, new_s in pairs:
        if old_s not in src:
            sys.exit('статичный текст: не найден фрагмент ' + old_s[:60])
        src = src.replace(old_s, new_s, 1)
    return src


def fix_switcher(src):
    """RU-версия активна, ссылка LV ведёт на корень сайта."""
    pairs = [
        ('<div id="languageSwitcher" class="language-switcher" data-lang="lv">',
         '<div id="languageSwitcher" class="language-switcher" data-lang="ru">'),
        ('<a id="lang-ru" href="ru/" hreflang="ru" lang="ru" class="language-button" '
         'aria-label="Переключить на русскую версию сайта">RU</a>',
         '<a id="lang-ru" href="./" hreflang="ru" lang="ru" class="language-button" '
         'aria-current="page" aria-label="Русская версия сайта">RU</a>'),
        ('<a id="lang-lv" href="./" hreflang="lv" lang="lv" class="language-button" '
         'aria-current="page" aria-label="Pārslēgt uz latviešu valodu">LV</a>',
         '<a id="lang-lv" href="../" hreflang="lv" lang="lv" class="language-button" '
         'aria-label="Pārslēgt uz latviešu valodu">LV</a>'),
        # Стартовый язык рантайма, если словарь всё же понадобится.
        ("let currentLang = 'lv';", "let currentLang = 'ru';"),
    ]
    for old, new in pairs:
        if old not in src:
            sys.exit('переключатель языка: не найден фрагмент ' + old[:60])
        src = src.replace(old, new, 1)
    return src


def main():
    src = io.open(SRC, encoding='utf-8').read()
    ru = read_dictionary(src)
    src, counters = apply_dictionary(src, ru)
    src = localize_head(src, ru)
    src = rebase_assets(src)
    src = localize_static_strings(src)
    src = fix_switcher(src)

    if not os.path.isdir(OUT_DIR):
        os.makedirs(OUT_DIR)
    io.open(OUT, 'w', encoding='utf-8').write(src)
    print('ru/index.html собран: %d текстовых узлов, %d placeholder, %d aria-label, %d WhatsApp-ссылок'
          % (counters['text'], counters['placeholder'], counters['aria'], counters['wa']))


if __name__ == '__main__':
    main()
