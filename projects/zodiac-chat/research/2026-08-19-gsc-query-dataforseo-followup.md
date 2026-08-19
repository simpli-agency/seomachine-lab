# zodiac-chat.com — GSC-запросы через DataForSEO: что реально ищут пользователи

**Дата:** 2026-08-19
**Проект:** zodiac-chat
**Тип:** surface follow-up к `2026-08-19-zodiac-chat-intent-keyword-research.md`
**Вопрос:** «запросы из GSC видны — что по ним в DataForSEO, что там ищут юзеры, меняет ли это выводы?»

**Источники:** GSC (`2026-08-19-gsc-queries-90d.csv`, `-30d.csv`), DataForSEO Labs `keyword_overview`, Google Ads `search_volume` (US/en, FR/fr, worldwide), DataForSEO SERP `organic/live/advanced` по 7 ключам.
**Сырые данные:** `2026-08-19-gsc-query-dataforseo-data.json`, `2026-08-19-gsc-query-dataforseo-metrics.csv`.

---

## Короткий ответ

Да, картина меняется — но не в объёме, а в **смысле**. Объёмы подтвердили то, что уже было в основном отчёте: спроса нет. Новое даёт разбор SERP: **большая часть видимых показов приходит на запросы, за которыми стоит вообще не тот интент**, а один вывод основного отчёта (про «пустой франкоязычный сегмент») оказался неверным и требует правки.

Три факта, которых в основном отчёте не было:

1. **`astrologie chat` — это не «астрология-чат», это «астрология кота».** По-французски *chat* = кот. Самый «объёмный» запрос выборки (11 показов из 57) — мусор.
2. **`zodiac chat` в US-выдаче Google разбирает как опечатку от `zodiac chart`.** Весь топ — калькуляторы натальных карт. Это объясняет мифические 27 100/мес из Google Ads.
3. **Настоящий продуктовый интент нашёлся, но в других формулировках** — `zodiac ai` (US) и `tchat horoscope` (FR). Оба с живыми продуктовыми SERP и монетизацией.

---

## 1. GSC-запрос → метрики DataForSEO

US = location 2840 / en. FR = 2250 / fr. Labs = DataForSEO Labs (KD, intent), Ads = Google Ads search_volume. `—` означает **null у провайдера** («ниже порога / нет в базе»), а не нулевой спрос.

| GSC-запрос | 90d показы / клики | Поз. | US vol (Labs / Ads) | US KD | US CPC | US intent | FR vol | Worldwide |
|---|---|---|---|---|---|---|---|---|
| astrologie chat | 11 / 0 | 22.91 | — / 480 | — | $6.68 | — | 70 | 4 400 |
| zodiac chat | 9 / 2 | **5.11** | — / **27 100** | — | $0.32 | — | 260 | 49 500 |
| zodiac ai | 7 / 0 | 31.71 | 90 / 90 | **4** | $2.68 | informational | 30 | 480 |
| zodiac com | 7 / 0 | 53.43 | — / 210 | — | $0.56 | — | 30 | 590 |
| ai zodiac | 5 / 0 | 43.80 | 20 / 20 | **4** | — | informational | 10 | 70 |
| zodiac ai generator | 4 / 1 | 26.00 | 10 / 10 | — | $4.60 | informational | 10 | 30 |
| tchat horoscope | 3 / 0 | 37.00 | — / 0 | — | — | — | **70** | 90 |
| my zodiac ai official website | 2 / 0 | 9.50 | — / — | — | — | — | — | — |
| zodiacap7 | 2 / 0 | 11.00 | — / 20 | — | — | — | 10 | 40 |
| fake horoscope maker | 1 / 1 | 7.00 | 10 / 10 | 48 | — | informational | 10 | 20 |
| chat horoscope | 1 / 0 | 51.00 | — / 20 | — | — | — | 40 | 170 |
| horoscope chat | 1 / 0 | 50.00 | 20 / 20 | **94** | — | informational | 40 | 170 |
| zodiac chats | 1 / 0 | 10.00 | 27 100 / 27 100 | 66 | $0.62 | informational | 260 | 49 500 |
| zodiac talk | 1 / 0 | 42.00 | 30 / 30 | 27 | — | informational | 10 | 90 |
| zodiac28 | 1 / 0 | 27.00 | — / 10 | — | — | — | — | 70 |
| zodiask | 1 / 0 | 40.00 | — / 10 | — | — | — | 10 | 1 300 |

**Сумма по US Labs-объёмам всех 16 запросов, кроме кластерного артефакта `zodiac chats`: ~200/мес.** Это весь измеримый спрос за тем, что сайт сегодня показывает Google.

### Нормализованные варианты (проверены, в GSC не появлялись)

| Ключ | US vol | US KD | US CPC | US intent | FR vol | Worldwide |
|---|---|---|---|---|---|---|
| astrology chat | 480 | 51 | $5.74 | informational | 70 | 4 400 |
| horoscope generator | 390 | 44 | $0.84 | informational | 10 | 9 900 |
| fake horoscope | 90 | **4** | — | informational | 10 | 210 |
| ai astrology chat | 50 | **3** | $3.12 | informational | 10 | **6 600** |
| horoscope maker | 30 | 63 | $0.33 | informational | 10 | 390 |
| astrology chatbot | 20 | **3** | $3.50 | informational | 10 | 140 |
| zodiac sign ai | 20 | **0** | — | informational | 10 | 70 |
| zodiac sign chat | 20 | 22 | $0.02 | informational | 10 | 70 |
| zodiac ai art | 10 | — | — | informational | 0 | 10 |
| ai horoscope generator | 10 | **0** | $2.30 | informational | 0 | 40 |
| zodiac gpt | — / 10 (Ads) | — | — | — | 10 | 20 |
| my zodiac ai | — / 10 (Ads) | — | — | — | 10 | 110 |
| astrologie ia (FR) | — | — | — | — | 20 | 30 |
| astrologue en ligne gratuit (FR) | — | — | — | — | 20 (KD 52) | 30 |
| zodiacs | 246 000 | 47 | $0.42 | informational | 33 100 | 1 000 000 |

**Null у провайдера (нет данных ни в Labs, ни в Ads):** `zodiac chatbot`, `zodiac ai chat`, `ai zodiac chat`, `ai zodiac generator`, `zodiac ai image generator`, `chat with astrology ai`, `talk to zodiac`, `horoscope generator ai`, `chat horoscope gratuit`, `my zodiac ai official website`.

---

## 2. Разбор SERP: что реально ищут пользователи

Здесь и находится содержательная часть ответа. По объёмам всё было ясно; SERP показывает, **какой интент Google приписывает этим фразам**.

### 2.1. `zodiac chat` (US) → выдача про **натальные карты**

Топ-19 органики: `astro.cafeastrology.com`, `astro-charts.com`, `thepattern.com`, `maressabrown.com`, `costarastrology.com`, `astro-seek.com`, `alabe.com`, `chart.spiritdaughter.com`, `astro.com`, `almanac.com`, `astrotheme.com`, `astrologicalassociation.com`, `reddit.com`, `vogue.com`, YouTube. Заголовки: «Free Astrology Birth Chart Report», «Create Your Birth Chart — Free», «NATAL CHART».

Ни одного чата. Google трактует `zodiac chat` как опечатку от **`zodiac chart` / birth chart**. Отсюда и 27 100/мес в Google Ads — это агрегат по `zodiac chart(s)`, а не спрос на продукт. Основной отчёт объяснял этот объём через suggestions (`zodiac signs group chat`, `zodiac chat room`); реальная причина проще и жёстче — опечаточный кластер к `chart`.

`zodiac-chat.com` **отсутствует в топ-19** этой выдачи. Позиция 5.11 из GSC — это по узкой доле показов (буквальный набор фразы плюс, вероятно, мобильная/персонализированная выдача), а не по основному кластеру.

**Практический вывод:** доменное имя не просто не даёт keyword-преимущества — оно попадает в чужой, чисто информационный кластер калькуляторов натальных карт с сильными старыми доменами.

### 2.2. `astrologie chat` (FR) → выдача про **кошек**

Топ-19: `fidanimo.com` («Les signes astrologiques du chat»), `femmeactuelle.fr` («portrait de votre chat selon son signe»), `lemagduchat.ouest-france.fr`, `caats.co`, `homycat.com`, `assurance.carrefour.fr` («Quel est le signe astrologique de votre chat ?»), `unebelleviedechat.com`, `noovomoi.ca`, `amazon.fr`, `assuropoil.fr`, `figo.fr`.

Страховки для животных, зоо-медиа и магазины. По-французски *chat* = кот, и запрос читается как «астрология кота». Это **самый крупный запрос в GSC-выборке** (11 показов, 19% всех видимых) — и он на 100% нерелевантен. Ноль кликов при позиции 22.91 полностью согласуется.

Отдельно: US-объём 480 и CPC $6.68 у `astrologie chat` — тоже артефакт, Google Ads склеил его с `astrology chat` (480 / $5.74). Реальный французский объём — 70/мес.

### 2.3. `tchat horoscope` (FR) → **настоящий продуктовый интент, платный**

Топ-12: `horoscope.fr`, `jimini.fr` («consultation en ligne par tchat et par téléphone»), Google Play «Astro Chat», `esmeralda.chat` («Voyance par tchat : 5 messages gratuits à l'inscription»), `tarotap.com` («Chat Voyance IA 24/7»), `voyance.fr`, `astrowi.com`, `astrologie.fr`, `astrocenter.fr`.

Вот где во французском живёт то, что делает zodiac-chat.com. Причём с готовой моделью монетизации: freemium-чат с лимитом бесплатных сообщений (`esmeralda.chat`) и AI-чат voyance 24/7 (`tarotap.com`). Объём FR — 70/мес, мало, но интент чистый и коммерческий.

### 2.4. `horoscope chat` (US) → продуктовый SERP, занятый индийским рынком

Топ-12: `kundligpt.com`, `kundlichat.in`, `astrotalk.com`, Google Play «Astro Chat: Astrology Talk», `astrosage.com`, `jyotinow.com`, `charts.sasstrology.com`, `costarastrology.com`, `ganeshaspeaks.com`, `hiastro.in`.

Интент правильный — «поговорить с астрологом/ИИ». Но US-выдача по нему занята индийскими астро-платформами (три из них — `kundligpt.com`, `jyotinow.com`, `astrotalk.com` — уже записаны в `project.json` как конкуренты). US KD = **94** при объёме 20/мес: худшее сочетание из возможных. Заодно это объясняет географию GSC (Индия, Филиппины в топе стран по показам).

### 2.5. `zodiac ai` (US) → **тот самый продуктовый кластер**

Топ-19: `my-zodiac-ai.com` (#1, «Free AI Astrology & Natal Chart»), `jenova.ai` («AI Zodiac Reading»), `deepai.org`, `zodiac.faetalize.dev`, Google Play «Zodiac AI Finder», `gen.ai`, `astrosage.com`, `github.com`, `aizodiac.com`, `bestofai.com` (каталог, карточка «Zodiac Chat AI»), `aistro.io`, `kundligpt.com`, `astrovoice.ai`, `destinyaiastrology.com`.

Это единственная из проверенных выдач, где стоят прямые аналоги продукта. US 90/мес, **KD 4**, CPC $2.68, worldwide 480. Плюс `ai astrology chat` (50 US, KD 3, worldwide **6 600**) и `astrology chatbot` (20 US, KD 3) — та же формулировка, KD околонулевой.

Отсюда же объясняется GSC-запрос `my zodiac ai official website` (2 показа, позиция 9.5): это навигационный запрос **к конкуренту** `my-zodiac-ai.com`, который стоит #1 по `zodiac ai`. Сайт ловит чужой бренд-трафик из-за похожего имени — это не спрос.

### 2.6. `zodiac ai generator` (US) → **генерация картинок, не чат**

Топ-17: `deepai.org` («Zodiac Design Generator»), `seeles.ai` («Zodiac Sign Illustrations AI Image Generator»), `gen.ai` («Astrology Photo Styles»), `lumenor.ai`, `elevenlabs.io` («AI Zodiac Card Generator | Create Astrology Art»), `magicshot.ai` («Zodiac AI Art»), `videnly.com` («Zodiac AI Video Generator»), `ailogogenerator.net`, `logoai.ai`, `deepdreamgenerator.com`, `promeai.pro`, Instagram, Facebook.

Интент — **AI-арт по знакам зодиака**, не астрологическая консультация. `zodiac-chat.com` стоит здесь на **позиции 20** — единственная из проверенных выдач, где домен вообще присутствует, и попал он туда в чужой интент. Клик, полученный по этому запросу в GSC, почти наверняка отскок.

### 2.7. `fake horoscope maker` (US) → шуточные генераторы

Топ-19: `randomstupidshit.com` (#1, «Fake Horoscope Generator - As Accurate as the Real Ones»), `interacty.me`, `draftwithai.com`, `thenextweb.com` («Here's your stupid horoscope made by smart AI»), Reddit («where can I make a fake natal chart?»), `nichesss.com`, `astro-seek.com` («Random Astrology Chart Generator»), `perchance.org` («Random Zodiac Sign Generator»), `canva.com`.

Развлекательный / пародийный интент: сделать шуточный гороскоп, разыграть друга, сгенерировать случайную карту. Не астрология. При этом это **единственный запрос выборки со 100% CTR** (1 показ / 1 клик, позиция 7) и единственный клик за 30 дней. Родственный `fake horoscope` — 90/мес US при **KD 4**.

---

## 3. Меняет ли это выводы

### Что подтвердилось

- **Спроса за фразой «zodiac chat» нет** (раздел 4 основного отчёта). Подтверждено ещё жёстче: не просто «объём — агрегат», а вся выдача — про натальные карты, и домена в ней нет.
- **Целевые кластеры не работают.** Ни один GSC-запрос не относится к compatibility / synastry / birth chart / посигнальным гороскопам.
- **Продуктовый интент живёт в `ai astrology` / `astrology chatbot`** — SERP по `zodiac ai` это прямо показывает.
- **Объёмы микроскопические.** Весь измеримый US-спрос по видимым запросам ≈ 200/мес.

### Что изменилось

**Вывод основного отчёта о французском сегменте неверен.** Раздел 3.1, пункт 3 говорит: два французских запроса указывают, что «франкоязычный сегмент пустой — там сайт цепляется вообще без усилий». На деле:

- `astrologie chat` — это «астрология кота», выдача из зоо-медиа и страховок. Сегмент не пустой, он **чужой**. Ноль кликов при 11 показах — не «зацепился без усилий», а показы по нерелевантному запросу.
- Реальный французский интент — `tchat horoscope` (70/мес FR), и там выдача уже занята зрелыми voyance-платформами с платной моделью.

**Структура видимых показов оказалась хуже, чем выглядела.** Из 57 видимых показов за 90 дней:

| Тип интента | Запросы | Показы | Доля |
|---|---|---|---|
| Нерелевантный (кошки, натальные карты как опечатка, AI-арт, чужой бренд) | astrologie chat, zodiac chat, zodiac ai generator, my zodiac ai official website | 26 | **46%** |
| Брендовый / шумовой (варианты имени домена) | zodiac com, zodiacap7, zodiac28, zodiask, zodiac talk, zodiac chats | 13 | 23% |
| Целевой продуктовый | zodiac ai, ai zodiac, horoscope chat, chat horoscope, tchat horoscope | 17 | 30% |
| Развлекательный | fake horoscope maker | 1 | 2% |

То есть даже те 16% показов, которые GSC показывает поимённо, наполовину состоят из промахов по интенту. Остальные 84% показов (300 из 357) анонимизированы — состав неизвестен, и экстраполировать на них эту структуру нельзя.

**Появилась дешёвая точка входа, которой не было в отчёте.** Кластер с околонулевым KD и правильным интентом: `ai astrology chat` (50, KD 3, worldwide 6 600), `zodiac ai` (90, KD 4), `astrology chatbot` (20, KD 3), `zodiac sign ai` (20, KD 0), `ai horoscope generator` (10, KD 0), `fake horoscope` (90, KD 4). Суммарно US ~280/мес. Это не бизнес — но это ровно то, что продукт делает, и это берётся одной страницей.

### Что вывод не меняет

Общая оценка ниши остаётся прежней: **объёмы не оправдывают инвестиции в SEO как основной канал**. Follow-up добавляет не оптимизма, а точности — теперь понятно, что текущие показы в основном мимо, и что единственный доступный кластер измеряется сотнями запросов в месяц, а не тысячами.

---

## 4. Что из этого делать (surface-уровень, без разработки стратегии)

1. **Перестать считать `zodiac chat` целевым ключом** и не оптимизировать под него title/H1 — фраза уводит в кластер `zodiac chart`.
2. **Переписать главную под `ai astrology chat` / `zodiac ai` / `astrology chatbot`** — KD 0-4, интент совпадает с продуктом, конкуренты в выдаче слабые (`my-zodiac-ai.com`, `aizodiac.com`, `jenova.ai`).
3. **Французское направление — только `tchat horoscope` / `astrologie ia`**, и трезво: объёмы 20-70/мес, выдача занята платными voyance-сервисами. `astrologie chat` игнорировать.
4. **`fake horoscope` (90/мес, KD 4) — отдельная лёгкая точка.** Развлекательный интент, единственный запрос выборки с реальным CTR.
5. **Добавить в `project.json` конкурентов, найденных в SERP:** `my-zodiac-ai.com`, `aizodiac.com`, `jenova.ai`, `aistro.io`, `astrovoice.ai`, `destinyaiastrology.com`, `kundlichat.in`, `hiastro.in`, `sasstrology.com` (US); `esmeralda.chat`, `tarotap.com`, `jimini.fr`, `horoscope.fr`, `astrocenter.fr` (FR).

---

## Ограничения

- Объёмы Google Ads по близким вариантам склеиваются (`zodiac chat` ↔ `zodiac chart(s)`, `astrologie chat` ↔ `astrology chat`) — брать их за чистую монету нельзя, что этот отчёт и демонстрирует.
- `—` в таблицах = **null у DataForSEO**, то есть «ниже порога провайдера / нет в базе», а не подтверждённый нулевой спрос.
- SERP снят один раз, desktop, 2026-08-19. Данные GSC показывают трёхкратный разрыв позиций между mobile (7.64) и desktop (22.94) — мобильная выдача по этим ключам не проверялась.
- 84% показов за 90 дней анонимизированы GSC; распределение интентов из раздела 3 описывает только видимую часть.
- Проверено 7 SERP из 44 ключей. Остальные оценены только по метрикам.
