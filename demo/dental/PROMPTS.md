# Промпты ассетов — ESTETIKA DENTAL — стоматология

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

## `assets/hero-implant.webp`
**Где:** первый экран, фон вырезается в прозрачность  
**Размер:** 560×802, 4:5  
**Модель:** `gemini-3-pro-image`  
**Aspect ratio в запросе:** `4:5`

> Идеально — отдать этот объект на прозрачном фоне (PNG с альфой). Если фон
> ровный пастельно-голубой, я вырежу сам скриптом `_build/cutout.py`.

```text
Hyper realistic 3D product render of a single glossy pearl white ceramic molar tooth crown mounted on a polished chrome titanium dental implant abutment, floating centered, soft pale blue studio gradient background, clean rim light and soft top key light, chrome reflections, ultra clean medical product visualisation, centered composition with space above and below, no text, no logos, no watermarks, no people
```

## `assets/tray.webp`
**Где:** карточка «Лечение и реставрация»  
**Размер:** 800×600, 4:3  
**Модель:** `gemini-3.1-flash-image`  
**Aspect ratio в запросе:** `4:3`

```text
Top down shot of a sterile stainless steel dental tray with neatly arranged dental instruments, mirror, probe and tweezers, on a clean pale blue surface, bright even clinical light with soft shadows, white and cool blue palette, minimal medical still life photography, no text, no logos, no watermarks, no people
```

## `assets/aligner.webp`
**Где:** карточка «Имплантация и протезирование»  
**Размер:** 800×600, 4:3  
**Модель:** `gemini-3.1-flash-image`  
**Aspect ratio в запросе:** `4:3`

```text
Studio macro of a transparent clear orthodontic aligner tray resting on a pale blue acrylic surface, crisp specular highlights on the transparent plastic, soft gradient background, cool blue and white palette, clean medical product photography, no text, no logos, no watermarks, no people
```

## `assets/veneers.webp`
**Где:** блок «Оборудование» — Керамика  
**Размер:** 800×600, 4:3  
**Модель:** `gemini-3.1-flash-image`  
**Aspect ratio в запросе:** `4:3`

```text
Macro studio shot of thin ceramic dental veneers arranged in a row on a matte white surface, translucent porcelain edges catching soft light, pale blue reflections, clean laboratory product photography, cool minimal palette, no text, no logos, no watermarks, no people
```

## `assets/chair.webp`
**Где:** блок «Клиника»  
**Размер:** 1400×788, 16:9  
**Модель:** `gemini-3.1-flash-image`  
**Aspect ratio в запросе:** `16:9`

```text
Wide interior of a modern minimal dental office: light grey dental chair, white cabinets, large window with soft daylight, pale blue and white palette, plants in the corner, calm architectural interior photography, empty room, no text, no logos, no watermarks, no people
```

## `assets/scanner.webp`
**Где:** блок «Оборудование» — 3D-сканер  
**Размер:** 800×600, 4:3  
**Модель:** `gemini-3.1-flash-image`  
**Aspect ratio в запросе:** `4:3`

```text
Close up of a modern intraoral 3D dental scanner handpiece resting in its stand next to a monitor showing an abstract blue 3D jaw scan, clean white clinic desk, cool blue clinical light, minimal medical technology photography, unbranded generic device, no text, no logos, no watermarks, no people
```

## `assets/hygiene.webp`
**Где:** карточка «Гигиена и профилактика»  
**Размер:** 800×600, 4:3  
**Модель:** `gemini-3.1-flash-image`  
**Aspect ratio в запросе:** `4:3`

```text
Macro of a dental hygiene setup on a pale blue surface: ultrasonic scaler tip, polishing paste in a small cup and a sterile mirror, cool clinical light, white and pale blue palette, clean minimal medical still life, no text, no logos, no watermarks, no people
```

## `assets/og.jpg`
**Где:** превью в соцсетях  
**Размер:** 1200×630, 16:9  
**Модель:** `gemini-3.1-flash-image`  
**Aspect ratio в запросе:** `16:9`

```text
Clean 3D render of a glossy white ceramic tooth crown on a polished titanium implant post, placed on the right side of a soft pale blue gradient background, large empty space on the left for typography, soft studio light with chrome reflections, medical product visualisation, no text, no logos, no watermarks, no people
```


---

## Чего пока нет: скролл-видео для стоматологии

На этот ролик не хватило кредитов Gemini — секции на сайте нет. Если сгенеришь,
скажи, и я вставлю такую же секцию, как в кофейне и детейлинге.

**Модель:** `veo-3.1-fast-generate-preview`, 16:9, 720p, 6 секунд  
**Первый кадр:** `hero-implant.png`

```text
Locked camera, static studio shot, single continuous take: the glossy white ceramic tooth crown on its polished titanium implant post slowly rotates clockwise on its own axis at constant speed, pale blue seamless background unchanged, studio lighting unchanged, slow steady linear rotation, no camera movement, no cuts, no people, no text
```

**Negative prompt:**

```text
camera movement, zoom, pan, cuts, transitions, people, hands, text, logos, blood, gums
```
