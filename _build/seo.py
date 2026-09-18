#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Schema.org разметка и мета-теги для лендинга WebExpress.

Один источник правды для обеих языковых версий: латышской (корень сайта)
и русской (/ru/). Скрипты `apply_seo.py` и `make_ru.py` берут данные отсюда.
"""
import json

SITE = 'https://webexpress.lv'
PHONE = '+37122441603'
TELEGRAM = 'https://t.me/webexpresslv'
INSTAGRAM = 'https://instagram.com/lukaostafijs'
WHATSAPP = 'https://wa.me/37122441603'

MARK_START = '  <!-- SEO:JSONLD-START -->'
MARK_END = '  <!-- SEO:JSONLD-END -->'

# Тарифы: (ключ, цена в евро, срок исполнения в днях)
TIERS = [
    ('start', 250, 'P4D'),
    ('standard', 350, 'P7D'),
    ('pro', 550, 'P14D'),
]

TEXT = {
    'lv': {
        'url': SITE + '/',
        'locale': 'lv_LV',
        'business_name': 'WebExpress — mājas lapu izstrāde',
        'business_desc': (
            'Mājas lapu izstrāde vietējiem uzņēmumiem Latvijā: landing page, '
            'vizītkartes vietne un daudzlapu mājaslapa ar fiksētu cenu. '
            'Demo 48 stundu laikā bez priekšapmaksas.'
        ),
        'page_name': 'Mājas lapas izstrāde Latvijā — pasūti mājaslapu no 250 €',
        'page_desc': (
            'Mājas lapas izstrāde uzņēmumiem Latvijā: demo 48 stundu laikā bez '
            'priekšapmaksas. Pasūti mājaslapu no 250 € ar fiksētu cenu.'
        ),
        'service_type': 'Mājas lapu izstrāde',
        'catalog': 'Mājas lapu izstrādes pakalpojumi',
        'city': 'Rēzekne',
        'region': 'Latgale',
        'country': 'LV',
        'areas': ['Latvija', 'Rēzekne', 'Rīga', 'Daugavpils', 'Latgale'],
        'tiers': {
            'start': ('Sākums — vienas lapas mājaslapa',
                      'Adaptīva vienas lapas mājaslapa (līdz 4 ekrāniem), tieša saite uz '
                      'WhatsApp un Telegram, pamata brendings, 3 dienas labojumiem.'),
            'standard': ('Standarts — mājaslapa ar lokālo SEO',
                         'Pilna landing page (līdz 7 blokiem), brenda sistēma, lokālā SEO '
                         'optimizācija Google, pieteikuma forma uz Telegram vai Google Sheets.'),
            'pro': ('Paplašinātais — divvalodu mājaslapa ar integrācijām',
                    'Scrollytelling un interaktīvie elementi, divas valodas (LV + RU vai EN), '
                    'CRM vai pierakstu kalendāra integrācija, 14 dienas atbalsta.'),
        },
        'hosting': {
            'care': ('Care — hostings mājaslapai',
                     'Serveris, SSL sertifikāts, domēna pieslēgšana, pieejamības monitorings '
                     'un rezerves kopijas.', 5),
            'careplus': ('Care+ — hostings un tehniskais atbalsts',
                         'Viss no Care plus tekstu un bilžu labojumi, jauni bloki pēc '
                         'pieprasījuma un prioritāra atbilde.', 25),
        },
        'faq': [
            ('Vai demo tiešām ir bez maksas?',
             'Jā, bez maksas. Demo paraugu izstrādājam uz sava rēķina. Ja sakāt, ka neder — nekas nav jāmaksā.'),
            ('Ko darīt, ja man nepatiks stils?',
             'Tāpēc otrais solis ir jūsu piemēri. Jūs atsūtat 2–3 lapas, kas patīk, un mēs veidojam maketu tieši tajā stilā.'),
            ('Vai var izmantot manas Instagram bildes?',
             'Jā, mēs atlasām labākās bildes un apstrādājam tās, lai lapa ielādētos zibenīgi.'),
            ('Kā tiek rādīts demo?',
             'Ierakstām HD video ar demonstrāciju vai nosūtām pilna izmēra ekrānuzņēmumus WhatsApp/Telegram.'),
            ('Vai domēns un lapa piederēs man?',
             'Pilnībā. Domēns tiek reģistrēts uz jūsu vārdu, un kodu varat paņemt jebkurā brīdī.'),
            ('Cik maksā mājas lapas izstrāde?',
             'Fiksēta cena no 250 € līdz 550 € atkarībā no tarifa. Precīzu summu nosaucam pirms darba sākuma, '
             'bez slēptām piemaksām. Hostings pēc palaišanas — no 5 € mēnesī.'),
            ('Cik ilgā laikā var pasūtīt mājaslapu?',
             'Demo ir gatavs 48 stundu laikā. Pilna mājaslapa — no 3 līdz 14 dienām atkarībā no tarifa.'),
        ],
    },
    'ru': {
        'url': SITE + '/ru/',
        'locale': 'ru_RU',
        'business_name': 'WebExpress — создание и разработка сайтов',
        'business_desc': (
            'Создание сайтов под ключ для бизнеса в Латвии: лендинг, сайт-визитка '
            'и многостраничный сайт по фиксированной цене. Демо за 48 часов без предоплаты.'
        ),
        'page_name': 'Заказать сайт под ключ — создание сайтов от 250 €',
        'page_desc': (
            'Закажите сайт онлайн: демо за 48 часов без предоплаты. Разработка сайтов '
            'под ключ для бизнеса — лендинг, сайт-визитка, хостинг и поддержка.'
        ),
        'service_type': 'Разработка сайтов под ключ',
        'catalog': 'Услуги по созданию сайтов',
        'city': 'Резекне',
        'region': 'Латгалия',
        'country': 'LV',
        'areas': ['Латвия', 'Резекне', 'Рига', 'Даугавпилс', 'Латгалия'],
        'tiers': {
            'start': ('Старт — одностраничный сайт под ключ',
                      'Адаптивный одностраничный сайт (до 4 экранов), прямая связь в WhatsApp '
                      'и Telegram, базовый брендинг, 3 дня на правки.'),
            'standard': ('Стандарт — сайт с локальным SEO',
                         'Полноценный лендинг (до 7 блоков), фирменный стиль, базовая SEO-оптимизация '
                         'под Google, форма заявок в Telegram или Google Sheets.'),
            'pro': ('Расширенный — двуязычный сайт с интеграциями',
                    'Scrollytelling и интерактивные элементы, две языковые версии (LV + RU или EN), '
                    'интеграция CRM или календаря записи, 14 дней поддержки.'),
        },
        'hosting': {
            'care': ('Care — хостинг сайта',
                     'Сервер, SSL-сертификат, подключение домена, мониторинг доступности '
                     'и резервные копии.', 5),
            'careplus': ('Care+ — хостинг и техническая поддержка',
                         'Всё из Care плюс правки текстов и фотографий, новые блоки по запросу '
                         'и приоритетный ответ.', 25),
        },
        'faq': [
            ('Демо правда бесплатное или в конце всплывет чек?',
             'Правда бесплатное. Демонстрационный макет мы делаем за свой счёт. Если вы скажете, что не подходит — '
             'вы просто закрываете переписку и ничего не платите.'),
            ('Что делать, если мне не понравится стиль?',
             'Второй обязательный шаг работы — ваши референсы. Вы присылаете 2–3 примера, которые нравятся вам, '
             'и мы собираем макет строго в том стиле.'),
            ('Можно использовать мои фотографии из Инстаграма?',
             'Да. Мы берём ваши реальные работы, отбираем их вместе, обрабатываем и сжимаем без потери качества.'),
            ('Как вы показываете демо?',
             'Записываем короткое HD-видео с демонстрацией сайта на телефоне и компьютере либо присылаем '
             'полноразмерные скриншоты в WhatsApp или Telegram.'),
            ('Сайт и домен останутся в моей собственности?',
             'Абсолютно. Домен регистрируется на ваше имя, исходный код и архив сайта вы можете забрать в любой момент.'),
            ('Сколько стоит заказать сайт?',
             'Фиксированная цена от 250 € до 550 € в зависимости от тарифа. Точную сумму называем до начала работы, '
             'без скрытых доплат. Хостинг после запуска — от 5 € в месяц.'),
            ('За сколько дней можно заказать сайт под ключ?',
             'Демо готово за 48 часов. Полный сайт — от 3 до 14 дней в зависимости от тарифа.'),
        ],
    },
}


def _offer(lang, name, desc, price, url, duration=None):
    t = TEXT[lang]
    offer = {
        '@type': 'Offer',
        'name': name,
        'description': desc,
        'price': str(price),
        'priceCurrency': 'EUR',
        'url': url,
        'availability': 'https://schema.org/InStock',
        'itemOffered': {
            '@type': 'Service',
            'name': name,
            'serviceType': t['service_type'],
            'provider': {'@id': SITE + '/#business'},
            'areaServed': t['areas'][0],
        },
    }
    if duration:
        offer['deliveryLeadTime'] = {
            '@type': 'QuantitativeValue',
            'value': int(duration.strip('PD')),
            'unitCode': 'DAY',
        }
    return offer


def graph(lang):
    """Собирает @graph со всей разметкой для одной языковой версии."""
    t = TEXT[lang]
    page = t['url']

    business = {
        '@type': ['ProfessionalService', 'WebDesignBusiness'],
        '@id': SITE + '/#business',
        'name': t['business_name'],
        'alternateName': 'WebExpress',
        'description': t['business_desc'],
        'url': page,
        'image': SITE + '/og-image.png',
        'logo': SITE + '/webexpress-favicon-v2.png',
        'telephone': PHONE,
        'priceRange': '250 € - 550 €',
        'currenciesAccepted': 'EUR',
        'address': {
            '@type': 'PostalAddress',
            'addressLocality': t['city'],
            'addressRegion': t['region'],
            'addressCountry': t['country'],
        },
        'geo': {'@type': 'GeoCoordinates', 'latitude': 56.5100, 'longitude': 27.3300},
        'areaServed': [{'@type': 'Place', 'name': a} for a in t['areas']],
        'knowsLanguage': ['lv', 'ru', 'en'],
        'sameAs': [TELEGRAM, INSTAGRAM],
        'openingHoursSpecification': [{
            '@type': 'OpeningHoursSpecification',
            'dayOfWeek': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'],
            'opens': '09:00',
            'closes': '20:00',
        }],
        'contactPoint': [{
            '@type': 'ContactPoint',
            'contactType': 'sales',
            'telephone': PHONE,
            'url': WHATSAPP,
            'availableLanguage': ['lv', 'ru', 'en'],
        }],
        'makesOffer': [
            _offer(lang, t['tiers'][key][0], t['tiers'][key][1], price, page + '#pricing', dur)
            for key, price, dur in TIERS
        ],
    }

    website = {
        '@type': 'WebSite',
        '@id': SITE + '/#website',
        'url': SITE + '/',
        'name': 'WebExpress',
        'publisher': {'@id': SITE + '/#business'},
        'inLanguage': ['lv', 'ru'],
    }

    webpage = {
        '@type': 'WebPage',
        '@id': page + '#webpage',
        'url': page,
        'name': t['page_name'],
        'description': t['page_desc'],
        'isPartOf': {'@id': SITE + '/#website'},
        'about': {'@id': SITE + '/#business'},
        'inLanguage': lang,
        'primaryImageOfPage': {'@type': 'ImageObject', 'url': SITE + '/og-image.png'},
    }

    catalog_items = [
        _offer(lang, t['tiers'][key][0], t['tiers'][key][1], price, page + '#pricing', dur)
        for key, price, dur in TIERS
    ]
    for key in ('care', 'careplus'):
        name, desc, price = t['hosting'][key]
        item = _offer(lang, name, desc, price, page + '#maintenance')
        item['priceSpecification'] = {
            '@type': 'UnitPriceSpecification',
            'price': str(price),
            'priceCurrency': 'EUR',
            'billingIncrement': 1,
            'unitCode': 'MON',
        }
        catalog_items.append(item)

    service = {
        '@type': 'Service',
        '@id': page + '#service',
        'name': t['service_type'],
        'serviceType': t['service_type'],
        'description': t['business_desc'],
        'provider': {'@id': SITE + '/#business'},
        'areaServed': [{'@type': 'Place', 'name': a} for a in t['areas']],
        'hasOfferCatalog': {
            '@type': 'OfferCatalog',
            'name': t['catalog'],
            'itemListElement': catalog_items,
        },
    }

    faq = {
        '@type': 'FAQPage',
        '@id': page + '#faq',
        'inLanguage': lang,
        'mainEntity': [
            {'@type': 'Question', 'name': q,
             'acceptedAnswer': {'@type': 'Answer', 'text': a}}
            for q, a in t['faq']
        ],
    }

    return {'@context': 'https://schema.org', '@graph': [business, website, webpage, service, faq]}


def block(lang):
    """JSON-LD в виде готового куска HTML с маркерами для пересборки."""
    payload = json.dumps(graph(lang), ensure_ascii=False, indent=2)
    payload = '\n'.join('  ' + line for line in payload.split('\n'))
    return (MARK_START + '\n'
            '  <script type="application/ld+json">\n'
            + payload + '\n'
            '  </script>\n'
            + MARK_END)


if __name__ == '__main__':
    import sys
    print(block(sys.argv[1] if len(sys.argv) > 1 else 'lv'))
