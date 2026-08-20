# Developer tool + hosting: поверхностный keyword research

Дата: 2026-08-20
Проект: `developer-tool-hosting`
Данные: DataForSEO — Labs `keyword_overview` (US/en) + Google Ads `search_volume` (US/en и worldwide) + SERP по 15 запросам
Сырьё: `2026-08-20-keyword-metrics.csv`, `2026-08-20-keyword-data.json`, `2026-08-20-serp-notes.md`
Объём: 129 seed-запросов, 128 вернулись хотя бы одним источником

---

## TL;DR

**Копать стоит, но не там, где ожидалось.**

1. **Смотреть надо worldwide, а не US.** US-объёмы у этих запросов почти все упираются
   в отчётный пол Google Ads (10/мес). Worldwide больше в 5-10 раз:
   `n8n hosting` 390 → 5400, `laravel hosting` 260 → 1900, `nextcloud hosting` 260 → 2900.
   Аудитория разработчиков глобальная; если считать US, вся тема выглядит мёртвой, и это ошибка.

2. **Порог входа реально низкий.** В топ-15 стабильно сидят мелкие домены —
   `xcloud.host`, `elest.io`, `cloudclusters.io`, `webspacekit.com`, `appliku.com`,
   `pella.app`, `getmidnight.com`, `gpu-mart.com`. Это не выдача, занятая гигантами.

3. **Щель конкретная: вендор отвечает «как захостить», а не «у кого».**
   На 13 из 15 проверенных выдач Reddit или форум вендора стоит в топ-3 — Google подставляет
   UGC, потому что нормальной коммерческой страницы нет.

4. **Лучшие ставки — не фреймворки, а self-hosted приложения.**
   `n8n`, `nextcloud`, `ghost`, `ollama`, `prestashop`: объём есть, KD 15-21,
   вендор выдачу не закрыл. У `next.js`/`supabase`/`mongodb` наоборот — вендор владеет запросом.

5. **Отдельный сильный кластер, который в гипотезу не входил: `<provider> alternatives`.**
   `vercel alternatives` ww 3600 KD 0, `netlify alternatives` ww 1600 KD 0,
   `heroku alternatives` ww 1000 KD 3 при CPC $30.72. Дешевле по конкуренции, чем `X hosting`,
   и ближе к деньгам. **Не проверялось по SERP** — это следующий шаг.

6. Пример Кирилла `remix hosting` — ww 20. Как трафик не работает. Как шаблон для
   программатики — да, выдача там пустая.

---

## Top opportunities

Volume — worldwide (Google Ads), в скобках US. KD — DataForSEO Labs, US/en. CPC — worldwide.

| keyword | vol ww (US) | KD | CPC | почему интересно | риск SERP |
|---|---|---|---|---|---|
| n8n hosting | 5400 (390) | 18 | $4.00 | Лучшая выдача из всех проверенных: 4 нишевых хостера + 5 community, вендор всего 1. Рынок автоматизации растёт | Низкий. Hostinger #1, но остальное разобрано мелкими |
| self hosted n8n | 4400 (880) | 18 | $4.93 | Формулировка «self hosted X» даёт больше объёма, чем «X hosting» | Низкий, тот же кластер |
| supabase self hosted | 5400 (480) | 1 | $3.49 | KD 1 при ww 5400. Люди уходят с managed Supabase | Средний: `supabase.com/docs/guides/self-hosting` #1 |
| nextcloud hosting | 2900 (260) | 15 | $3.91 | Гигантов нет вообще: 1 cloud provider на всю выдачу. 6 слотов у community | Низкий |
| ghost hosting | 2400 (1000) | 21 | $4.07 | Подборки — доминирующий тип выдачи (5 из 15). Формат листикла уже выигрывает | Низкий, но конкуренты-аффилиаты активны |
| docker hosting | 3600 (590) | 18 | $9.19 | Высокий CPC + низкий KD | Не проверялся по SERP |
| woocommerce hosting | 2900 (880) | 30 | $16.54 | Самый высокий CPC среди среднего KD | Средний, много денег → активные игроки |
| postgres hosting | 2900 (590) | 28 | $6.28 | Aiven/Instaclustr/Northflank ранжируются → место есть | Средний: DigitalOcean, Heroku, OVH в топе |
| laravel hosting | 1900 (260) | 16 | $2.89 | Классика гипотезы, Cloudways и xcloud.host держатся | Средний: Laravel Cloud #1 + Forge #5, вендор давит |
| magento hosting | 1900 (590) | 31 | $13.53 | Ecommerce-CPC при умеренном KD | Средний |
| prestashop hosting | 1600 (140) | 18 | $10.11 | 4 подборки + 3 нишевых хостера в топ-15, CPC $10 | Низкий |
| joomla hosting | 1600 (390) | 28 | $9.02 | Старый CMS-хвост, дешёвая конкуренция | Не проверялся |
| drupal hosting | 1300 (390) | 17 | $14.08 | CPC $14 при KD 17 | Не проверялся |
| ollama hosting | 880 (110) | 19 | $3.20 | AI/GPU-ниша, растёт. gpu-mart, koyeb, elest.io в топе | Средний: вендор 7 из 15 |
| discord bot hosting | 8100 (1600) | 13 | $2.79 | Самый большой объём с низким KD во всём наборе | Не проверялся. Возможен спам/игровой шум |

---

## Кластеры

### 1. Best bets — умеренная конкуренция, есть куда встать

Критерий: KD ≤ 35, ww volume ≥ 200, коммерческий intent, выдача не закрыта вендором.

**Self-hosted приложения (ядро ставки):**
`n8n hosting` 5400/KD 18 · `self hosted n8n` 4400/KD 18 · `nextcloud hosting` 2900/KD 15 ·
`ghost hosting` 2400/KD 21 · `ollama hosting` 880/KD 19 · `immich hosting` 320/KD 20 ·
`pocketbase hosting` 210/KD 17 · `strapi hosting` 210/KD 16

Здесь совпало всё: живой спрос, слабая коммерческая выдача, вендор без интереса
продавать хостинг, и уже видимые мелкие конкуренты, которых можно обойти.

**CMS/ecommerce хвост (высокий CPC, старая дешёвая конкуренция):**
`woocommerce hosting` 2900/KD 30/$16.54 · `magento hosting` 1900/KD 31/$13.53 ·
`joomla hosting` 1600/KD 28/$9.02 · `prestashop hosting` 1600/KD 18/$10.11 ·
`drupal hosting` 1300/KD 17/$14.08 · `opencart hosting` 480/KD 39 · `shopware hosting` 390/KD 0/$9.55

Менее «девелоперская» тема, чем просил кейс, но экономика лучше всего остального:
CPC $9-16 против $3-5 у фреймворков.

**Инфраструктура:**
`docker hosting` 3600/KD 18/$9.19 · `postgres hosting` 2900/KD 28 ·
`mysql hosting` 1600/KD 38 · `kubernetes hosting` 720/KD 35/$13.59 ·
`elasticsearch hosting` 260/KD 17/$8.24 · `rabbitmq hosting` 210/KD 26

**Кластер `<provider> alternatives` — отдельная сильная находка:**
`vercel alternatives` 3600/KD 0/$7.84 · `netlify alternatives` 1600/KD 0/$5.04 ·
`heroku alternatives` 1000/KD 3/$30.72 · `railway alternatives` 1000/KD 0/$11.75 ·
`render alternatives` 880/KD 0/$8.96 · `digitalocean alternatives` 720/KD 0/$14.00 ·
`fly.io alternatives` 260/KD 0/$9.23

KD 0-3 при таких объёмах выглядит слишком хорошо — почти наверняка Labs занижает.
Но CPC $8-31 говорит, что деньги там настоящие, а intent («ищу, куда уйти с Vercel»)
для аффилиата ближе к конверсии, чем `X hosting`. Проверить SERP до планирования.

### 2. Высокий объём, но слишком конкурентно первым заходом

| keyword | vol ww (US) | KD | причина |
|---|---|---|---|
| wordpress hosting | 74000 (27100) | 67 | Самая дорогая ниша хостинга в принципе. CPC US $59 |
| managed wordpress hosting | 6600 (3600) | 63 | То же, CPC US $79.88 |
| static site hosting | 2900 (880) | 49 | Netlify/Vercel/Cloudflare владеют категорией |
| api hosting | 2400 (140) | 43 | Размытый интент + KD 43 |
| next.js hosting | 1300 (210) | 27 | KD обманчив: `vercel.com` #2 и `nextjs.org` ×3. Vercel владеет запросом |
| supabase hosting | 1300 (170) | 28 | `supabase.com` 6 слотов из 15, intent navigational. Брать через `supabase self hosted` |
| mongodb hosting | 880 (210) | 27 | `mongodb.com` 7 из 15, Atlas съел категорию |
| gitlab hosting | 720 (140) | 67 | Вендор + KD 67 |
| redis hosting | 590 (140) | 55 | Redis Cloud/Upstash закрыли |
| grafana hosting | 170 (40) | 60 | Grafana Cloud |
| home assistant hosting | 170 (30) | 63 | Nabu Casa владеет |
| kafka hosting | 90 (20) | 57 | Confluent |
| gitea hosting | 70 (20) | 63 | Вендор |

Зафиксировать и вернуться, когда домен наберёт вес. Первым заходом — нет.

### 3. Малый объём, но высокий intent — программатика / BOFU

Хвост под один шаблон. Индивидуально по 10-300 в месяц, суммарно — заметно.
Отдельные CPC сигнализируют о сильном коммерческом намерении вопреки объёму.

| keyword | vol ww | KD | сигнал |
|---|---|---|---|
| immich hosting | 320 | 20 | Растущий self-hosted проект |
| fastapi hosting | 210 | 23 | Выдача из деплой-доков, коммерческого слоя мало |
| pocketbase hosting | 210 | 17 | — |
| strapi hosting | 210 | 16 | Вендор давит, но 8-15 свободны |
| nuxt hosting | 170 | 9 | — |
| clickhouse hosting | 140 | 16 | — |
| mautic hosting | 110 | 0 | — |
| laravel cloud hosting | 110 | n/a | — |
| bun hosting | 110 | n/a | Растущий runtime |
| matomo hosting | 90 | n/a | Analytics, платящая аудитория |
| sentry hosting | 90 | 48 | KD высокий для объёма |
| payload cms hosting | 70 | n/a | CPC $4.40 |
| appwrite hosting | 50 | n/a | **CPC US $24.42** при ww 50 |
| vaultwarden hosting | 50 | n/a | **CPC US $13.10**, платящая аудитория |
| sveltekit hosting | 50 | 0 | **CPC US $26.71** при ww 50 |
| svelte hosting | 50 | 40 | CPC US $25.89 |
| directus hosting | 50 | n/a | — |
| metabase hosting | 50 | n/a | BI, B2B-аудитория |
| medusa / medusajs hosting | 30 / 20 | n/a | Ecommerce-dev |
| typesense hosting | 30 | n/a | — |
| remix hosting | 20 | 5 | Выдача пустая: ни одной коммерческой страницы |
| meilisearch hosting | 10 | n/a | — |

Отдельно — модификатор `free`, открывающий свои слоты:
`free node.js hosting` 1900/KD 4 · `free django hosting` 390/KD 3 ·
`best laravel hosting` 260/KD 15 · `best node.js hosting` 260/KD 6 · `best django hosting` 140/KD 9.
Для аффилиата «free» отлично работает как вход в воронку (free tier → платный апгрейд).

### 4. Avoid / шум / не hosting-intent

- **`vite hosting`** (880/KD 22) — выдача это `vite.dev/guide/static-deploy` и Stack Overflow
  про то, как открыть dev-сервер наружу. Запрос про конфиг, не про покупку.
- **`deploy laravel`** (1300), **`deploy next.js`** (390) — intent informational, выдача туториальная.
  Это MOFU-контент, не лендинг.
- **`python hosting`** (2900), **`react hosting`** (590) — Labs даёт main_intent informational.
  Размытые зонтичные запросы.
- **`git hosting`** (480/KD 21) — означает «альтернатива GitHub», а не покупку хостинга.
- **`node.js hosting`** (5400/**KD 7**), **`php hosting`** (2900/**KD 2**) — KD явно сломан.
  Это старейшие и самые заезженные категории хостинга; KD 2-7 не бывает. Не доверять,
  проверять SERP отдельно.
- **`llama hosting`**, **`langchain hosting`**, **`sanity hosting`**, **`minio hosting`** —
  navigational/ambiguous, бренд ищут, а не хостинг.
- **Нет данных вообще** (не вернулись ни Labs, ни Ads): `vendure hosting`, `penpot hosting`,
  `uptime kuma hosting`. Спроса нет, из планов убрать.
- **Не возвращены Labs** (но объём в Ads есть — значит запрос живой, просто Labs не крawлил):
  `comfyui hosting` 140, `dify hosting` 20, `langflow hosting` 10, `open webui hosting` 20,
  `budibase hosting` 10, `baserow hosting` 10, `typesense hosting` 30, `minio hosting` 50.

---

## Рекомендация: первые 20 страниц

**Волна 1 — проверить шаблон (6 страниц).** Максимум спроса при минимально занятой выдаче.

1. `n8n hosting` — плюс отдельный блок под `self hosted n8n`
2. `nextcloud hosting`
3. `ghost hosting` — формат подборки, там он уже выигрывает
4. `prestashop hosting`
5. `ollama hosting` — вход в AI/GPU-нишу
6. `docker hosting`

Формат: **не** вендорский «как установить», а именно «у кого хостить» —
сравнение провайдеров, цены, tiers, free tier, «когда self-host дешевле managed».
То, чего не даёт вендор и что сейчас закрывает Reddit.

**Волна 2 — кластер alternatives (4 страницы).** Сначала снять SERP, потом делать.

7. `vercel alternatives`
8. `heroku alternatives` — CPC $30.72
9. `netlify alternatives`
10. `railway alternatives`

**Волна 3 — CMS/ecommerce, лучшая экономика (4 страницы).**

11. `woocommerce hosting`
12. `magento hosting`
13. `drupal hosting`
14. `joomla hosting`

**Волна 4 — программатика по одному шаблону (6 страниц как пилот).**
Каркас: что за инструмент → требования к ресурсам → варианты хостинга →
сравнение провайдеров → цена → deploy-инструкция.

15. `strapi hosting`
16. `pocketbase hosting`
17. `immich hosting`
18. `matomo hosting`
19. `appwrite hosting`
20. `remix hosting` — контрольная точка: если тонкая страница берёт топ-10 на ww 20,
    шаблон можно раскатывать на 40+ инструментов из кластера 3

Если волна 1 не поднимается за ~3 месяца — гипотеза не работает, дальше не идти.

---

## Ограничения данных

1. **KD и intent — только US/en.** Labs `keyword_overview` не даёт worldwide-KD,
   поэтому KD из US сопоставляется с worldwide-объёмом. Для глобального
   девелоперского спроса это приблизительно.
2. **KD местами недостоверен.** `node.js hosting` KD 7, `php hosting` KD 2,
   весь кластер alternatives KD 0-3 — для таких заезженных запросов не бывает.
   Labs считает KD по бэклинк-профилям ранжирующихся страниц; на смешанных выдачах
   с Reddit и доками он занижен. **KD здесь — сигнал, а не решение.** Решение — по SERP.
3. **SERP снят по 15 запросам из 129 и только по US.** Кластер alternatives,
   ecommerce-хвост, `docker hosting` и `discord bot hosting` не проверялись — при том,
   что они попали в рекомендации. Это следующий шаг, до планирования контента.
4. **US-объёмы упираются в пол Google Ads (10/мес)** — 60 из 128 запросов показывают
   ровно 10. Это «ниже порога отчётности», а не реальные 10 запросов.
5. **Labs не покрывает 13 seed-запросов** — при этом Ads по некоторым даёт объём
   (`comfyui hosting` 140, `minio hosting` 50). Отсутствие в Labs ≠ отсутствие спроса.
6. **AI overview на 10 из 15 проверенных выдач** — часть кликов уйдёт в ноль.
   Прогноз трафика по всему кластеру надо дисконтировать.
7. **Сезонность не смотрели.** `monthly_searches` есть в JSON, в анализ не входил.
8. **Не оценивалось**, что партнёрская платформа реально умеет хостить.
   Список выше — спрос, а не набор поддерживаемых технологий.
