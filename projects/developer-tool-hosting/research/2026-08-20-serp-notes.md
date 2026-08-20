# SERP-заметки: developer tool + hosting

Дата: 2026-08-20
Источник: DataForSEO SERP (Google organic, location_code 2840 / en, top-20, разобрано top-15)
Сырьё: `2026-08-20-keyword-data.json` → ключ `serp`

Классификация доменов (ручная, по спискам в разборе):

- **official/vendor** — сайт и документация самого инструмента (`strapi.io`, `nextjs.org`, `docs.n8n.io`)
- **cloud provider** — крупные платформы (Vercel, Netlify, Render, DigitalOcean, AWS, GCP, Heroku, Railway, Koyeb, OVH, Cloudflare, Hostinger)
- **managed/niche host** — мелкие специализированные хостеры (`xcloud.host`, `elest.io`, `cloudclusters.io`, `webspacekit.com`, `massivegrid.com`, `librecloud.host`, `appliku.com`, `stormkit.io`, `pella.app`, `getmidnight.com`, `tiiny.host`, `gpu-mart.com`, `aiven.io`, `instaclustr.com`, `scalegrid.io`, `cloudways.com`)
- **directory/listicle** — обзоры и подборки (`hostadvice.com`, `techradar.com`, `cybernews.com`, `hostingadvice.com`, `makerkit.dev`, `back4app.com`, `medium.com`, `dev.to`, тематические блоги)
- **community** — Reddit, Stack Overflow, GitHub, форумы вендора (`community.n8n.io`, `help.nextcloud.com`, `forum.djangoproject.com`)
- **video** — YouTube

## Сводная таблица

| keyword | official | cloud | managed/niche | directory | community | video | SERP features |
|---|---|---|---|---|---|---|---|
| n8n hosting | 1 | 2 | **4** | 1 | 5 | 2 | PAA, AI overview |
| nextcloud hosting | 5 | 1 | 3 | 0 | **6** | 0 | PAA |
| ghost hosting | 3 | 2 | 2 | **5** | 1 | 2 | discussions, PAA |
| prestashop hosting | 5 | 2 | 3 | **4** | 1 | 0 | discussions, AI overview |
| postgres hosting | 5 | 4 | 3 | 2 | 1 | 0 | discussions, PAA, AI overview |
| laravel hosting | 5 | 4 | 2 | 1 | 2 | 1 | PAA, AI overview |
| django hosting | 2 | **6** | 1 | 1 | 3 | 2 | discussions, PAA, AI overview |
| ollama hosting | **7** | 2 | 3 | 1 | 1 | 1 | PAA, AI overview |
| fastapi hosting | 4 | **5** | 1 | 3 | 1 | 1 | PAA |
| strapi hosting | **7** | 2 | 3 | 1 | 1 | 1 | discussions, AI overview |
| remix hosting | 5 | 5 | 0 | 1 | 3 | 1 | video, AI overview |
| next.js hosting | **6** | 4 | 0 | 3 | 1 | 1 | PAA, AI overview |
| supabase hosting | **6** | 1 | 1 | 3 | 2 | 2 | discussions, PAA |
| mongodb hosting | **7** | 3 | 1 | 2 | 2 | 0 | PAA, AI overview |
| vite hosting | **6** | 2 | 1 | 2 | 3 | 1 | AI overview |

## Что видно из выдач

### 1. Вендор занимает верх почти везде, но не отвечает на вопрос

На 13 из 15 запросов сайт/доки инструмента стоят в топ-3. Это потолок: слот
`strapi.io/hosting` по запросу `strapi hosting` не отбить.

Но вендорская страница отвечает на «как захостить», а не на «у кого хостить».
Поэтому на **13 из 15** запросов Reddit или форум вендора стоит в топ-3
(`n8n hosting` #3 и #6, `nextcloud hosting` #2, `postgres hosting` #2,
`laravel hosting` #2, `django hosting` #2, `remix hosting` #1). Google подставляет
UGC, потому что коммерческой страницы нужного качества нет. Это и есть щель.

### 2. Мелкие хостеры реально ранжируются

Не только гиганты. В топ-15 стабильно сидят маленькие домены:

- `xcloud.host` — #5 на `n8n hosting`, #11 на `laravel hosting`
- `elest.io` — #13 на `n8n hosting`, #11 на `supabase hosting`, #11 на `ollama hosting`
- `cloudclusters.io` — #6 `ollama`, #9 `strapi`, #9 `prestashop`, #14 `ghost`, #16 `postgres`
- `webspacekit.com` #8 `n8n`, `librecloud.host` #4 `nextcloud`, `massivegrid.com` #6 `nextcloud`
- `appliku.com` #10 `django`, `pella.app` #11 `fastapi`, `stormkit.io` #14 `strapi`
- `getmidnight.com` #4 `ghost`, `gpu-mart.com` #10 `ollama`, `tiiny.host` #7 `vite`

Порог входа низкий. Это главный аргумент за гипотезу.

### 3. Формат подборки работает как аффилиатный формат

`hostadvice.com` ранжируется листиклами с датой в тайтле:
«10 Best n8n Hosting Providers: (Aug 2026)» #11, «10 Best Strapi Hosting Providers (Aug 2026)» #12,
«7 Best Free Laravel Hosting Services (Aug 2026)» #14, «6 Best Free PrestaShop Hosting (Aug 2026)» #8.

На `ghost hosting` подборки — вообще доминирующий тип (5 из 15).
Модификатор `free` открывает отдельные слоты: `free django hosting` (ww 390, KD 3),
`free node.js hosting` (ww 1900, KD 4).

### 4. Где вендор закрыл выдачу — заходить не надо

- `next.js hosting` — `vercel.com` #2 + `nextjs.org` ×3. Vercel владеет запросом, KD 27 обманчив.
- `supabase hosting` — `supabase.com` 6 из 15, intent navigational (ищут сам Supabase).
- `mongodb hosting` — `mongodb.com` 7 из 15, Atlas съел категорию.
- `strapi hosting`, `ollama hosting` — вендор 7 из 15, но остаток разобран мелкими хостерами,
  так что позиции 8-15 доступны.

### 5. Часть запросов — не про покупку хостинга

- `vite hosting` — выдача это `vite.dev/guide/static-deploy` и Stack Overflow про dev-server `host`.
  Смешанный интент, включая «как открыть Vite наружу». Не BOFU.
- `django hosting`, `fastapi hosting` — выдача из деплой-доков облаков
  (`render.com/docs/deploy-django`, `railway.com/deploy/fastapi`). Ближе к туториалу,
  чем к выбору хостера, хотя коммерческий слой есть.
- `remix hosting` — 5 официальных + 5 облаков, при этом ни одной специализированной
  коммерческой страницы. Пусто, но и спроса почти нет (ww 20).

### 6. AI overview

AI overview присутствует на 10 из 15 запросов. Часть кликов уйдёт в ноль —
это надо закладывать в прогноз трафика по всему кластеру.

## Ограничение

SERP снимался только по US (location_code 2840). Основной объём у этих запросов —
worldwide, и состав выдачи в EU/IN может отличаться (в `nextcloud hosting` уже
всплыл `ionos.co.uk`). Поле `search_volume` в SERP-ответе пришло пустым для всех
15 запросов — объёмы брать из `2026-08-20-keyword-metrics.csv`, не отсюда.
