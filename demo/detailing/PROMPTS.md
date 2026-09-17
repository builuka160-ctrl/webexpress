# Промпты ассетов — NORDIC DETAILING — детейлинг

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

## `assets/hero-car.webp`
**Где:** первый экран, фон вычищается до белого  
**Размер:** 1500×837, 16:9  
**Модель:** `gemini-3-pro-image`  
**Aspect ratio в запросе:** `16:9`

```text
Studio photograph of a pristine white modern sports sedan, three quarter front view from the left, isolated on a pure white seamless background with a soft contact shadow under the wheels, crisp specular highlights along the body line, cool white studio light with subtle rim light, extremely clean automotive catalogue photography, unbranded generic car design, no badges, no license plate, no text, no logos, no watermarks, no people
```

## `assets/car-rear.webp`
**Где:** конец прайса, справа внизу  
**Размер:** 1100×614, 16:9  
**Модель:** `gemini-3.1-flash-image`  
**Aspect ratio в запросе:** `16:9`

```text
Studio photograph of a silver grey modern coupe, three quarter rear view from the right, isolated on a pure white seamless background with a soft contact shadow, cool studio light, polished paint with mirror reflections, unbranded generic car design, no badges, no license plate, no text, no logos, no watermarks, no people
```

## `assets/polish.webp`
**Где:** сетка «Что входит в работу» — Полировка  
**Размер:** 800×600, 4:3  
**Модель:** `gemini-3.1-flash-image`  
**Aspect ratio в запросе:** `4:3`

```text
Extreme macro of a dual action polisher foam pad working on deep black car paint, fine polishing compound spread on the surface, sharp reflection of a studio softbox in the paint, cool blue white rim light against a dark background, industrial automotive detailing photography, no hands, no text, no logos, no watermarks, no people
```

## `assets/beading.webp`
**Где:** сетка — Керамика  
**Размер:** 800×600, 4:3  
**Модель:** `gemini-3.1-flash-image`  
**Aspect ratio в запросе:** `4:3`

```text
Extreme macro of perfect round water beads on a hydrophobic ceramic coated deep black car hood, each droplet catching cold specular highlights, dark moody background, cool cyan white light, high contrast automotive detailing photography, no text, no logos, no watermarks, no people
```

## `assets/wheel.webp`
**Где:** сетка — Диски  
**Размер:** 800×600, 4:3  
**Модель:** `gemini-3.1-flash-image`  
**Aspect ratio в запросе:** `4:3`

```text
Macro close up of a clean multi spoke dark grey alloy wheel with a fresh dressed black tyre, wet asphalt floor, dark garage background, cold directional light with strong rim light on the spokes, automotive detailing photography, unbranded wheel design, no text, no logos, no watermarks, no people
```

## `assets/interior.webp`
**Где:** сетка — Салон  
**Размер:** 800×600, 4:3  
**Модель:** `gemini-3.1-flash-image`  
**Aspect ratio в запросе:** `4:3`

```text
Close up of an immaculately cleaned dark car interior: black leather seat stitching, dashboard and steering wheel edge, vacuum clean carpet, cold daylight through the window, dark moody automotive interior photography, unbranded generic design, no text, no logos, no watermarks, no people
```

## `assets/engine.webp`
**Где:** сетка — Моторный отсек  
**Размер:** 800×600, 4:3  
**Модель:** `gemini-3.1-flash-image`  
**Aspect ratio в запросе:** `4:3`

```text
Close up of a spotless engine bay of a modern car, clean plastic covers and hoses, cold hard light from above, dark background, technical automotive photography, unbranded generic parts, no text, no logos, no watermarks, no people
```

## `assets/reveal-dirty.webp`
**Где:** ползунок «до/после», левая половина  
**Размер:** 1200×675, 16:9  
**Модель:** `gemini-3.1-flash-image`  
**Aspect ratio в запросе:** `16:9`

```text
Locked frame macro photograph of a car hood corner covered in dried road dust, dirt film and water spots, dull matte looking dark grey paint, flat overcast light, dark garage background, documentary automotive photography, no text, no logos, no watermarks, no people
```

## `assets/tools.webp`
**Где:** сетка — Чем работаем  
**Размер:** 1400×788, 16:9  
**Модель:** `gemini-3.1-flash-image`  
**Aspect ratio в запросе:** `16:9`

```text
Top down flat lay of professional car detailing tools arranged on a dark grey concrete surface: microfibre towels, unbranded spray bottles, polishing pads, soft detailing brushes, cold side light with deep shadows, monochrome dark palette with a single red object, industrial editorial photography, no text, no logos, no watermarks, no people
```

## `assets/og.jpg`
**Где:** превью в соцсетях  
**Размер:** 1200×630, 16:9  
**Модель:** `gemini-3.1-flash-image`  
**Aspect ratio в запросе:** `16:9`

```text
Dark cinematic studio shot of the front corner of a glossy black car with a strong red light streak reflecting along the body line, deep black background with large empty space on the left for typography, cold specular highlights, premium automotive advertising photography, unbranded generic car, no text, no logos, no watermarks, no people
```

## `assets/hero-car.webp`
**Где:** первый экран (правка кадра выше)  
**Размер:** 1500×837, 16:9  
**Модель:** `gemini-3.1-flash-image`  
**Aspect ratio в запросе:** `16:9`

> Кадр-правка: сначала генерится `hero-car.png`, потом он же отдаётся модели как
> референс вместе с этим промптом — так совпадают ракурс, фон и свет.

```text
Using the attached studio photo: keep the exact same white car, same three quarter front angle, same pure white seamless background, same lighting and shadow. Remove every manufacturer emblem and badge from the grille, hood and body so the car is completely unbranded, leaving a smooth clean grille surface. Keep the photograph otherwise identical and photorealistic. No text, no logos, no watermarks, no people.
```

## `assets/reveal-clean.webp`
**Где:** ползунок «до/после», правая половина  
**Размер:** 1200×675, 16:9  
**Модель:** `gemini-3.1-flash-image`  
**Aspect ratio в запросе:** `16:9`

> Кадр-правка: сначала генерится `reveal-dirty.png`, потом он же отдаётся модели как
> референс вместе с этим промптом — так совпадают ракурс, фон и свет.

```text
Using the attached photo as the exact reference for camera angle, framing, car body shape, background and lighting: keep the identical locked frame, but show the same car panel after professional detailing - deep glossy mirror finish dark paint, no dust, no dirt film, no water spots, crisp reflections of the garage lights on the surface. Same composition, same perspective, same background. Photorealistic automotive photography. No text, no logos, no watermarks, no people.
```

## `assets/wash-scrub.mp4` (скролл-видео) + `assets/wash-poster.webp`
**Где:** секция «Результат», прокрутка мотает ролик кадр за кадром  
**Модель:** `veo-3.1-fast-generate-preview`, 16:9, 720p, 6 секунд  
**Опорные кадры:** первый — `reveal-dirty.png`, последний — `reveal-clean.png`

```text
Locked camera, static shot, single continuous take: the dusty dull car panel gradually becomes a deep glossy mirror finish as dirt dissolves away, slow steady linear progression from dirty to perfectly polished, no camera movement, no cuts, no people, no text
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
  -movflags +faststart assets/wash-scrub.mp4
ffmpeg -i assets/wash-scrub.mp4 -frames:v 1 poster.png && magick poster.png -resize 900x -quality 78 assets/wash-poster.webp
```

`-g 1` делает каждый кадр ключевым — без этого перемотка идёт ступеньками.
Держи файл в пределах 1,5 МБ.
