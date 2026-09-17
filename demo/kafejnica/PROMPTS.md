# Промпты ассетов — GRAIN & ROAST — кофейня

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

## `assets/hero-cup.webp`
**Где:** коллаж первого экрана, крупная карточка  
**Размер:** 900×672, 4:3  
**Модель:** `gemini-3.1-flash-image`  
**Aspect ratio в запросе:** `4:3`

```text
Macro product shot of a ceramic cappuccino cup with delicate rosetta latte art on a warm beige linen surface, soft warm side light from the left, creamy oat and caramel palette, shallow depth of field, editorial specialty coffee photography, natural film grain, no text, no logos, no watermarks, no people
```

## `assets/hero-iced.webp`
**Где:** коллаж первого экрана, вертикальная карточка  
**Размер:** 700×933, 3:4  
**Модель:** `gemini-3.1-flash-image`  
**Aspect ratio в запросе:** `3:4`

```text
Tall glass of iced latte with layered milk and espresso and a black paper straw, standing on a warm beige backdrop, soft warm key light with gentle rim light on the glass, condensation droplets, caramel and cream palette, editorial beverage photography, shallow depth of field, no text, no logos, no watermarks, no people
```

## `assets/hero-shelf.webp`
**Где:** коллаж первого экрана, квадрат слева внизу  
**Размер:** 700×700, 1:1  
**Модель:** `gemini-3.1-flash-image`  
**Aspect ratio в запросе:** `1:1`

```text
Interior corner of a small specialty coffee shop: light oak shelf with unbranded kraft coffee bags, ceramic cups and a small plant, warm afternoon light through a window, beige and oat palette, calm minimal scandinavian interior, soft shadows, no text, no logos, no watermarks, no people
```

## `assets/hero-counter.webp`
**Где:** коллаж первого экрана, квадрат по центру  
**Размер:** 700×700, 1:1  
**Модель:** `gemini-3.1-flash-image`  
**Aspect ratio в запросе:** `1:1`

```text
Interior of a small modern coffee bar: light wood counter, matte espresso machine, stack of ceramic cups, dried flowers in a vase, warm side light, beige cream and caramel palette, airy minimal composition, no text, no logos, no watermarks, no people
```

## `assets/menu-espresso.webp`
**Где:** карточка меню «Эспрессо»  
**Размер:** 800×1000, 4:5  
**Модель:** `gemini-3.1-flash-image`  
**Aspect ratio в запросе:** `4:5`

```text
Single espresso shot in a deep burgundy ceramic cup with thick crema on a saucer, warm beige gradient backdrop, dramatic soft side light, rich brown and cream palette, premium editorial coffee photography, shallow depth of field, no text, no logos, no watermarks, no people
```

## `assets/menu-latte.webp`
**Где:** карточка меню «Флэт уайт» + коллаж хиро  
**Размер:** 800×1000, 4:5  
**Модель:** `gemini-3.1-flash-image`  
**Aspect ratio в запросе:** `4:5`

```text
White ceramic cup of flat white with silky tulip latte art seen from a low angle, soft cream backdrop, gentle diffused light, minimal beige palette, editorial coffee photography, shallow depth of field, no text, no logos, no watermarks, no people
```

## `assets/menu-filter.webp`
**Где:** карточка меню «Фильтр V60»  
**Размер:** 800×1000, 4:5  
**Модель:** `gemini-3.1-flash-image`  
**Aspect ratio в запросе:** `4:5`

```text
Pour over filter coffee brewing: glass carafe and ceramic dripper with paper filter, thin stream of hot water, steam visible, warm beige backdrop, warm key light with rim light on the steam, caramel and cream palette, editorial coffee photography, no text, no logos, no watermarks, no people
```

## `assets/pastry.webp`
**Где:** блок «Пекарня»  
**Размер:** 1400×788, 16:9  
**Модель:** `gemini-3.1-flash-image`  
**Aspect ratio в запросе:** `16:9`

```text
Flat lay of freshly baked croissants and cinnamon buns with flaky golden crust on a beige linen cloth and stone tray, scattered crumbs, warm soft side light, cream caramel and oat palette, editorial bakery photography, no text, no logos, no watermarks, no people
```

## `assets/interior-wide.webp`
**Где:** блок «Зал», фон под текстом  
**Размер:** 1600×900, 16:9  
**Модель:** `gemini-3.1-flash-image`  
**Aspect ratio в запросе:** `16:9`

```text
Wide interior of a calm modern cafe: light oak tables, soft beige upholstered bench, large window with sheer curtain, warm afternoon sunlight casting soft shadows on a plaster wall, cream beige and caramel palette, architectural interior photography, empty seats, no text, no logos, no watermarks, no people
```

## `assets/roast-poster.webp`
**Где:** постер скролл-видео (кадр «до»)  
**Размер:** 1200×900, 4:3  
**Модель:** `gemini-3.1-flash-image`  
**Aspect ratio в запросе:** `4:3`

```text
Top down macro flat lay of raw green unroasted coffee beans filling a shallow ceramic bowl on a warm beige linen surface, even soft daylight from the left, pale sage and beige palette, locked frame, editorial macro photography, no text, no logos, no watermarks, no people
```

## `assets/og.jpg`
**Где:** превью в соцсетях  
**Размер:** 1200×630, 16:9  
**Модель:** `gemini-3.1-flash-image`  
**Aspect ratio в запросе:** `16:9`

```text
Minimal editorial still life: ceramic cup of cappuccino, scattered roasted coffee beans and a folded beige linen napkin on a warm cream plaster surface, soft warm side light, large empty space on the left for typography, cream caramel and mocha palette, no text, no logos, no watermarks, no people
```

## `assets/roast-scrub.mp4` (скролл-видео) + `assets/roast-poster.webp`
**Где:** секция «Вторник — день обжарки», прокрутка мотает ролик кадр за кадром  
**Модель:** `veo-3.1-fast-generate-preview`, 16:9, 720p, 6 секунд  
**Опорные кадры:** первый — `reveal-green.png`, последний — `reveal-roasted.png`

```text
Locked camera, static top down shot, single continuous take: raw green coffee beans in the ceramic bowl slowly darken and roast into glossy dark brown beans, slow steady linear progression, soft daylight unchanged, no camera movement, no cuts, no people, no text
```

**Negative prompt:**

```text
camera movement, zoom, pan, cuts, transitions, people, hands, text, logos
```

Ролик обязан проматываться кадр за кадром, поэтому камера неподвижна, склеек нет,
движение равномерное. После генерации:

```bash
ffmpeg -i новый.mp4 -t 6 -an -vf "scale=900:-2" \
  -c:v libx264 -crf 31 -g 1 -keyint_min 1 -sc_threshold 0 \
  -movflags +faststart assets/roast-scrub.mp4
ffmpeg -i assets/roast-scrub.mp4 -frames:v 1 poster.png && magick poster.png -resize 900x -quality 78 assets/roast-poster.webp
```

`-g 1` делает каждый кадр ключевым — без этого перемотка идёт ступеньками.
Держи файл в пределах 1,5 МБ.
