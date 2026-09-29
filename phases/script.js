/* PHASES — скелет логики. Данные и цены — заглушки, заменить данными Мартина. */

// TODO: 10–20 SKU из ChargeShop. Цены/остатки/страны — от Мартина.
const PRODUCTS = [
  { id: 'easee',   name: 'Easee',            cat: 'station', price: null },
  { id: 'vool',    name: 'Vool',             cat: 'station', price: null },
  { id: 'zaptec',  name: 'Zaptec',           cat: 'station', price: null },
  { id: 'nexblue', name: 'Nexblue',          cat: 'station', price: null },
  { id: 'portable',name: 'Portable Charger', cat: 'station', price: null },
  { id: 'dlm',     name: 'DLM',              cat: 'dlm',     price: null },
  { id: 'holder',  name: 'Держатель кабеля', cat: 'holder',  price: null },
  { id: 'type2',   name: 'Кабель Type 2',    cat: 'cable',   price: null },
];

// TODO: «нулевая смета» от Мартина. Числа ниже — заглушки, НЕ показывать клиентам как реальные.
const PRICING = {
  base:  { easee: 0, vool: 0, zaptec: 0, nexblue: 0, portable: 0 },
  perMeter: 0,
  route: { easy: 0, medium: 0, hard: 0 },
  dlm: 0,
  visit: { ee: 0, lv: 0, lt: 0 },
  configured: false, // true, когда цены заполнены
};

const WHATSAPP = '37127744375'; // TODO: проверить номер
const EMAIL = 'martins@placenphase.lv';

const $ = (sel, root = document) => root.querySelector(sel);
const $$ = (sel, root = document) => [...root.querySelectorAll(sel)];

/* ---------- Каталог ---------- */
function renderCatalog(filter = 'all') {
  const grid = $('#catalog-grid');
  grid.innerHTML = '';
  PRODUCTS.filter(p => filter === 'all' || p.cat === filter).forEach(p => {
    const el = document.createElement('article');
    el.dataset.cat = p.cat;
    el.innerHTML = `
      <h3>${p.name}</h3>
      <p>${p.price == null ? 'Цена по запросу' : p.price + ' €'}</p>
      <a href="#estimate">Запросить</a>`;
    grid.appendChild(el);
  });
}

$$('.filters button').forEach(btn =>
  btn.addEventListener('click', () => renderCatalog(btn.dataset.filter)));

/* ---------- Калькулятор ---------- */
function fillCalcStations() {
  const sel = $('#calc-form [name=station]');
  PRODUCTS.filter(p => p.cat === 'station').forEach(p => {
    sel.add(new Option(p.name, p.id));
  });
}

$('#calc-form').addEventListener('submit', e => {
  e.preventDefault();
  const f = new FormData(e.target);
  const total =
    (PRICING.base[f.get('station')] || 0) +
    PRICING.perMeter * Number(f.get('cable')) +
    (PRICING.route[f.get('route')] || 0) +
    (f.get('dlm') ? PRICING.dlm : 0) +
    (PRICING.visit[f.get('country')] || 0);
  $('#calc-total').textContent = PRICING.configured
    ? `от ${total} €`
    : 'цены пока не заданы (нужна таблица от Мартина)';
  $('#calc-result').hidden = false;
});

/* ---------- Заявка ---------- */
// Скелет: пока нет бэкенда, собираем текст и открываем WhatsApp.
// TODO: заменить на POST на бэкенд/почту (файлы через wa.me не передаются).
$('#lead-form').addEventListener('submit', e => {
  e.preventDefault();
  const f = new FormData(e.target);
  const text = [
    'Заявка на смету (сайт PHASES)',
    `Имя: ${f.get('name')}`,
    `Тел.: ${f.get('phone')}`,
    `Email: ${f.get('email') || '-'}`,
    `Страна: ${f.get('country')}`,
    `Адрес: ${f.get('address') || '-'}`,
    `Клиент: ${f.get('client')}`,
    `Авто: ${f.get('car') || '-'}`,
    `Комментарий: ${f.get('message') || '-'}`,
  ].join('\n');
  $('#lead-status').textContent = 'Открываем WhatsApp… Фото пришлите в чате.';
  window.open(`https://wa.me/${WHATSAPP}?text=${encodeURIComponent(text)}`, '_blank', 'noopener');
});

$('#partner-form').addEventListener('submit', e => {
  e.preventDefault();
  const f = new FormData(e.target);
  const body = `Имя: ${f.get('name')}\nГород: ${f.get('city')}\nТел.: ${f.get('phone')}\nОпыт: ${f.get('experience') || '-'}`;
  location.href = `mailto:${EMAIL}?subject=${encodeURIComponent('Партнёр PHASES')}&body=${encodeURIComponent(body)}`;
});

/* ---------- Языки ---------- */
// TODO: словари RU/EN/LV/LT/ET/PL. Пока переключатель только ставит атрибут lang.
$$('.lang a').forEach(a => a.addEventListener('click', e => {
  e.preventDefault();
  document.documentElement.lang = a.dataset.lang;
}));

renderCatalog();
fillCalcStations();
