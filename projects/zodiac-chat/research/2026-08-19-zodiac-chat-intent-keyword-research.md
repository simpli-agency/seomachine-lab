# zodiac-chat.com — интент, ключи, KD и объёмы (surface/mid-depth research)

**Дата:** 2026-08-19
**Проект:** `zodiac-chat` (`projects/zodiac-chat/`)
**Домен:** zodiac-chat.com
**Рынок по умолчанию:** location_code 2840 (USA), language_code `en`
**Источники данных:** DataForSEO (Labs keyword overview, Google Ads search volume, keyword suggestions, ranked keywords, live SERP), Google Search Console (property `sc-domain:zodiac-chat.com`), прямой запрос к сайту (HTTP)
**GSC:** доступен, данные собраны — см. раздел 3.1

> **Правка от 2026-08-19.** В первой версии отчёта было написано, что GSC недоступен из-за отсутствующего файла сервис-аккаунта. Это неверно: сервис-аккаунт существует, у него `siteFullUser` на property `sc-domain:zodiac-chat.com`, данные выгружены. Разделы 1, 3, 10 и 11 исправлены по факту.

---

## 1. Краткий вывод

**Копать стоит, но не туда, где стоит сайт сейчас.**

Ниша большая и живая: `zodiac signs` — 673 000/мес, `horoscope today` — 368 000, `daily horoscope` — 301 000, `birth chart` — 246 000. Но верхушка этих кластеров занята медиа и старыми контентными доменами с десятками тысяч ранжирующихся страниц, и KD там 60–76.

Реально доступны три вещи:

1. **Compatibility / synastry** — 20–25k объёма на запрос при **KD 18–36**. Это самая недооценённая зона: там сидят калькуляторы, а не медиа.
2. **AI-astrology кластер** (`ai astrology`, `astrology ai`, `astrology chatbot`, `ai horoscope`) — объёмы маленькие (10–1 300), но **KD 0–22**, CPC $2.6–4.9, и это ровно то, чем сайт является. Это не источник трафика, это источник позиционирования и первых сигналов.
3. **Посигнальный лонгтейл дневных гороскопов** — `leo horoscope daily` 90 500 при **KD 10**, `virgo horoscope daily` 74 000 KD 23, `aries horoscope daily` 74 000 KD 20. Шаблонные страницы, идеальный кандидат на programmatic.

**Главный минус:** у сайта сейчас нет контентной поверхности вообще. В US-выдаче zodiac-chat.com ранжируется по **одному** ключу — `zodiac ai` (объём 90, позиция 58, ETV 0.19). Всё остальное — с нуля.

Это подтверждено фактическими данными Google Search Console: за 90 дней **20 кликов и 357 показов** с **одной-единственной страницы** (`https://zodiac-chat.com/`), первый показ — 21.06.2026. То есть сайт в индексе и уже получает поисковый трафик, но footprint микроскопический, и весь он приходится на главную. Детали — раздел 3.1.

**Главная ловушка:** сам термин «zodiac chat» как продуктовый интент не существует. Подробности в разделе 4.

---

## 2. Что сейчас представляет собой сайт

Проверено прямым запросом (HTTP 200, Next.js, SSR-рендер присутствует):

| Параметр | Значение |
|---|---|
| Title | `Free Zodiac & Horoscope AI Chat Generator Tool - Zodiac-Chat.com` |
| Canonical | `https://zodiac-chat.com` |
| Meta description | есть |
| Meta keywords | есть, ~40 фраз (устаревший тег, Google игнорирует) |
| OG / Twitter / itemprop | есть, картинка захостена на внешнем `i.ibb.co` |
| Страницы в навигации | `/` (Generator, Features, Pricing, FAQs — якоря на одной странице), `/pricing`, `/dashboard/signin` |
| Блог / контентный раздел | **нет** |
| `robots.txt` | есть, но только комментарии Cloudflare content-signals — **ни одной директивы `User-agent`/`Disallow`/`Sitemap`** |
| `sitemap.xml` | **404** (также 404: `sitemap_index.xml`, `sitemap-index.xml`) |

Позиционирование по тексту главной: бесплатный AI-генератор гороскопов и зодиакальных ответов, freemium с PRO от $5, «Used by 30,000+ users monthly», основан в EU. Модель — западная тропическая астрология + AI-чат.

**Вывод по структуре:** это одностраничный SaaS-лендинг. Индексируемых точек входа фактически три. Никакого SEO-фундамента нет — и это одновременно проблема и возможность, потому что ничего не нужно переделывать.

---

## 3. Текущая органическая видимость

### 3.1. Фактические данные Google Search Console

Property: **`sc-domain:zodiac-chat.com`**, доступ сервис-аккаунта — `siteFullUser`.

**Форма property важна:** работает только domain-property `sc-domain:zodiac-chat.com`. URL-prefix `https://zodiac-chat.com/` отдаёт **403** — такой property сервис-аккаунту не выдан (и, судя по списку, не заведён). Все скрипты должны обращаться к `sc-domain:`-форме; в `project.json` она уже прописана верно.

#### Итоги по периодам

| Метрика | 90 дней (2026-05-21 — 2026-08-18) | 30 дней (2026-07-20 — 2026-08-18) |
|---|---|---|
| Clicks | **20** | **10** |
| Impressions | **357** | **200** |
| CTR | **5.60%** | **5.00%** |
| Avg position | **14.57** | **15.89** |
| Страниц с показами | **1** | **1** |
| Строк запросов (не анонимизированных) | 16 | 13 |

Половина всех 90-дневных показов пришлась на последние 30 дней — сайт молодой и набирает индексацию, а не затухает. Первый показ в GSC — **2026-06-21**, показы были в 58 днях из 90.

| Месяц | Clicks | Impressions |
|---|---|---|
| 2026-06 (с 21-го) | 3 | 49 |
| 2026-07 | 11 | 190 |
| 2026-08 (по 17-е) | 6 | 118 |

#### Страницы

| URL | Clicks | Impressions | CTR | Avg position |
|---|---|---|---|---|
| `https://zodiac-chat.com/` | 20 | 357 | 5.60% | 14.57 |

**Это вся page-level выгрузка за 90 дней — одна строка.** Ни `/pricing`, ни `/dashboard/signin` показов не собрали. Полностью совпадает с выводом раздела 2: индексируемая поверхность сайта = главная страница. 30-дневный срез идентичен по составу (та же одна страница, 10 кликов / 200 показов).

#### Запросы, 90 дней

| Запрос | Clicks | Impressions | CTR | Position |
|---|---|---|---|---|
| astrologie chat | 0 | 11 | 0% | 22.91 |
| zodiac chat | 2 | 9 | 22.2% | **5.11** |
| zodiac ai | 0 | 7 | 0% | 31.71 |
| zodiac com | 0 | 7 | 0% | 53.43 |
| ai zodiac | 0 | 5 | 0% | 43.80 |
| zodiac ai generator | 1 | 4 | 25.0% | 26.00 |
| tchat horoscope | 0 | 3 | 0% | 37.00 |
| my zodiac ai official website | 0 | 2 | 0% | 9.50 |
| zodiacap7 | 0 | 2 | 0% | 11.00 |
| fake horoscope maker | 1 | 1 | 100% | 7.00 |
| chat horoscope | 0 | 1 | 0% | 51.00 |
| horoscope chat | 0 | 1 | 0% | 50.00 |
| zodiac chats | 0 | 1 | 0% | 10.00 |
| zodiac talk | 0 | 1 | 0% | 42.00 |
| zodiac28 | 0 | 1 | 0% | 27.00 |
| zodiask | 0 | 1 | 0% | 40.00 |

За 30 дней — 13 строк, состав тот же минус `zodiac ai generator`, `my zodiac ai official website`, `chat horoscope`; единственный клик — `fake horoscope maker` (позиция 7).

**Критично для интерпретации:** 16 названных запросов дают всего **57 показов и 4 клика** — это **16% показов и 20% кликов**. Остальные 300 показов и 16 кликов скрыты анонимизацией GSC (запросы, которые Google считает слишком редкими, чтобы показывать). За 30 дней доля названных запросов ещё ниже: 23 показа из 200 (11.5%). Поэтому список выше описывает форму спроса, но **не** является полной картиной трафика.

`query` + `page` выгрузка за 90 дней даёт те же 16 строк — все до единой ведут на `https://zodiac-chat.com/`. Распределения трафика по страницам не существует, потому что страница одна.

#### Распределение по позициям

Считается по строкам запросов, то есть покрывает только те самые 16% показов. Позиция — средняя за период.

| Бакет | 90 дней (строк / показов / кликов) | 30 дней (строк / показов / кликов) |
|---|---|---|
| 1-3 | **0** / 0 / 0 | **0** / 0 / 0 |
| 4-10 | 4 / 13 / 3 | 3 / 5 / 1 |
| 10-30 | 4 / 18 / 1 | 4 / 8 / 0 |
| 30+ | 8 / 26 / 0 | 6 / 10 / 0 |

**Ни одного запроса в топ-3.** Половина строк — за пределами топ-30. Все клики собраны бакетами 4-10 и 10-30, что ожидаемо. Page-level бакет тривиален: единственная страница со средней позицией 14.57 попадает в 10-30.

#### География и устройства (90 дней)

| Страна | Clicks | Impressions | Avg position |
|---|---|---|---|
| USA | 5 | 97 | 16.52 |
| United Kingdom | 0 | 16 | 19.12 |
| Germany | 3 | 15 | 13.80 |
| India | 0 | 15 | 17.40 |
| Philippines | 0 | 15 | 19.73 |
| Spain | 3 | 11 | 18.82 |
| Indonesia | 1 | 9 | 14.78 |
| Italy | 1 | 8 | 7.00 |

Всего показы пришли из **78 стран**. На США — 97 показов (27%), остальное размазано по единицам показов на страну. То есть текущий трафик не сфокусирован на целевом рынке US, а является случайным международным хвостом.

| Устройство | Clicks | Impressions | Avg position |
|---|---|---|---|
| MOBILE | 16 | 192 | **7.64** |
| DESKTOP | 4 | 162 | **22.94** |
| TABLET | 0 | 3 | 6.33 |

Разрыв позиций между мобильной (7.64) и десктопной (22.94) выдачей — трёхкратный, и 80% кликов приходит с мобильных. При таком объёме данных это может быть артефактом малой выборки, но проверить мобильную выдачу отдельно стоит.

#### Что данные GSC говорят по существу

1. **Блокера «нет доступа к GSC» не существует** — доступ есть, данные есть. Ограничение здесь другое: объём данных настолько мал, что quick-wins в обычном смысле (запросы на позициях 11-20 с сотнями показов) просто не из чего строить. Порог `min_impressions=50` в `research_quick_wins.py` не проходит ни один запрос.
2. **Раздел 4 подтверждён фактами Google, а не только базой DataForSEO.** Все 16 названных запросов — это варианты написания названия сайта и его функции (`zodiac chat`, `zodiac ai`, `zodiac com`, `ai zodiac`, `zodiac talk`, `zodiask`, `zodiacap7`, `my zodiac ai official website`). Ни одного запроса из целевых кластеров: нет ни compatibility, ни synastry, ни birth chart, ни посигнальных гороскопов. По `zodiac chat` сайт стоит на **позиции 5.11 и получает 9 показов за 90 дней** — это и есть прямое измерение того, что спроса за фразой нет: почти топ-5 при трёх показах в месяц.
3. **Два запроса из 16 — французские** (`astrologie chat` — самый «объёмный» запрос выборки, `tchat horoscope`). Плюс `chat horoscope`. При нулевом контенте это чистая случайность выдачи, но она указывает, что франкоязычный сегмент пустой — там сайт цепляется вообще без усилий.
4. **CTR 5.6% при средней позиции 14.57** — аномально высокий для второй страницы выдачи. Объяснение простое: часть показов брендовая/навигационная. Использовать этот CTR как базовую линию для планирования нельзя.
5. **Стартовая точка зафиксирована.** 20 кликов / 357 показов за 90 дней — та база, относительно которой измеряется эффект любых работ из раздела 8.

### 3.2. Оценка по сторонней базе

DataForSEO Labs `ranked_keywords`, US/en:

| Домен | Ранжирующихся ключей (total) | Комментарий |
|---|---|---|
| **zodiac-chat.com** | **1** | `zodiac ai`, vol 90, поз. 58, ETV 0.19 |
| theastro.chat | 122 | AI-чат, тот же тип продукта |
| jyotinow.com | 145 | AI-астролог (ведический) |
| astrogpt.ai | 223 | AI-астролог |
| kundligpt.com | 477 | AI-кундли |
| astroo.ai | 817 | AI-астрология + блог + инструменты |
| asknebula.com | 25 177 | продукт + контент |
| costarastrology.com | 36 299 | Co–Star |
| astrotalk.com | 73 502 | маркетплейс астрологов |
| horoscope.com | 91 599 | медиа |
| zodiacsign.com | 97 863 | контент |
| cafeastrology.com | 98 895 | контент + калькуляторы |
| astro-seek.com | 116 460 | калькуляторы |

Разрыв с AI-конкурентами — 2–3 порядка, но сами AI-конкуренты мелкие: 122–817 ключей. Это догоняемо. Разрыв с контентными доменами (25k–116k ключей) в горизонте surface-проекта не закрывается.

### 3.3. astroo.ai как рабочий шаблон

Единственный AI-астрологический продукт в выборке, который набрал заметный трафик, и сделал он это **инструментами + блогом**, а не лендингом:

| URL | Ключ | Объём | KD | Поз. | ETV |
|---|---|---|---|---|---|
| `/blog/birth-chart-love-compatibility` | birth chart love compatibility | 22 200 | 11 | 12 | 250.9 |
| `/synastry` | birth chart synastry | 18 100 | 13 | 18 | 92.3 |
| `/blog/astrology-relationship-compatibility-guide` | chart astrology compatibility | 22 200 | 30 | 22 | 53.3 |
| `/blog/1-to-12-houses-in-astrology-calculator` | houses horoscope | 22 200 | 27 | 27 | 51.1 |
| `/calendar` | astrology calendar | 5 400 | 29 | 14 | 49.1 |
| `/blog/what-is-my-rising-sign` | what is my rising sign | 18 100 | 16 | 42 | 38.0 |

Обратите внимание: почти весь их трафик — **compatibility и chart-инструменты**, не «AI chat». Это прямое эмпирическое подтверждение вывода из раздела 1.

---

## 4. Ловушка: «zodiac chat» — не продуктовый интент

Это самая важная находка для продуктовых решений.

- `zodiac chat` **отсутствует** в базе DataForSEO Labs (нет ни KD, ни clickstream-объёма).
- Google Ads возвращает для `zodiac chat` **27 100/мес** — но это агрегат по близким вариантам, а не спрос на продукт.
- Что реально стоит за этой фразой, видно по suggestions: `zodiac signs group chat` (10), `zodiac group chat names` (10), `zodiac chat room` / `zodiac chat rooms` (10), `zodiac signs in a group chat` (10), `chat noir zodiac sign` (10), `what is chat noir's zodiac sign`, `zodiac signs group chat wattpad`, `zodiac chat discord`, `chat gpt zodiac`, `zodiac casino live chat`.

То есть: фанфики на Wattpad, названия для групповых чатов, Discord, персонаж Chat Noir (Miraculous) и онлайн-казино Zodiac. Ни одного коммерческого или продуктового запроса.

Также **не найдены в базе**: `zodiac chatbot`, `horoscope chatbot`, `natal chart chat`. `birth chart chat` — 10/мес.

**Подтверждение по GSC (раздел 3.1):** сайт стоит по `zodiac chat` на средней позиции **5.11** и получил за 90 дней **9 показов и 2 клика**. Почти топ-5 — и три показа в месяц. Это независимое от DataForSEO измерение того же факта: за фразой нет спроса.

**Следствие:** доменное имя не даёт keyword-преимущества, и строить SEO вокруг фразы «zodiac chat» бессмысленно. Продуктовый интент живёт в формулировках `ai astrology` / `astrology ai` / `astrology chatbot`.

---

## 5. Кластеры: объёмы и KD

Ниже — данные DataForSEO. `vol (CS)` — clickstream-объём из Labs, `vol (Ads)` — Google Ads. Они расходятся (например, `daily horoscope`: 301 000 против 246 000) — это нормальная разница методик, привожу оба.

### 5.1. Zodiac signs — справочная информация

| Ключ | vol (CS) | vol (Ads) | KD | CPC |
|---|---|---|---|---|
| zodiac signs | 673 000 | 673 000 | 38 | $0.17 |
| zodiac sign dates | 246 000 | 246 000 | 48 | $0.24 |
| zodiac signs dates | 246 000 | 246 000 | 37 | $0.24 |
| zodiac personality | 18 100 | 18 100 | 41 | $0.85 |
| zodiac signs meaning | 12 100 | 12 100 | 39 | $1.06 |
| zodiac sign traits | 4 400 | 4 400 | 23 | $0.26 |
| zodiac traits | 3 600 | 3 600 | 24 | $1.04 |
| what is my zodiac sign | 14 800 | 14 800 | 58 | $0.51 |
| zodiac sign personality traits | 1 900 | 1 900 | 25 | $1.78 |

Огромный, но чисто информационный кластер с CPC $0.2–1.0 — то есть плохо монетизируемый. Голова (KD 38–58) занята Britannica, Wikipedia, Allure, Almanac, Co-Star, zodiacsign.com. **Хвост (traits, KD 23–25) — заходимо**, но денег там мало.

### 5.2. Compatibility — лучшее соотношение объёма к сложности

| Ключ | vol | KD | CPC |
|---|---|---|---|
| zodiac signs compatibility | 22 200 | 35 | $0.37 |
| birth chart compatibility | 22 200 | **24** | $2.00 |
| natal chart compatibility | 22 200 | **19** | $2.00 |
| zodiac compatibility birth chart | 22 200 | **19** | $2.14 |
| birth chart zodiac compatibility | 22 200 | **23** | $2.14 |
| zodiac sign compatibility | 22 200 | **24** | — |
| zodiac love compatibility | 22 200 | 36 | $1.08 |
| zodiac compatibility | 18 100 | 36 | $1.09 |
| synastry chart | 18 100 | **18** | $2.69 |
| birth chart synastry | 18 100 | **13** | — |
| birth chart love compatibility | 22 200 | **11** | — |
| astrology compatibility | 9 900 | **25** | $1.71 |
| zodiac compatibility chart | 8 100 | 31 | $0.57 |
| horoscope compatibility | 4 400 | **26** | $0.74 |
| zodiac sign compatibility test | 3 600 | 33 | $1.44 |
| synastry calculator | 2 900 | **18** | $2.55 |
| love compatibility zodiac | 1 600 | 33 | $1.08 |

**Это главная находка.** Как только запрос переформулирован через `birth chart` / `natal chart` / `synastry`, объём остаётся тем же (22 200 / 18 100), а KD падает с 35–36 до **11–24**, и CPC при этом вырастает вчетверо ($0.37 → $2.00–2.69), то есть аудитория качественнее.

### 5.3. Daily horoscope — голова закрыта, хвост открыт

| Ключ | vol | KD |
|---|---|---|
| horoscope today | 368 000 | 75 |
| daily horoscope | 301 000 | 71 |
| free daily horoscope | 40 500 | 76 |
| weekly horoscope | 27 100 | **32** |
| monthly horoscope | 12 100 | **27** |
| **leo horoscope daily** | 90 500 | **10** |
| **virgo horoscope daily** | 74 000 | **23** |
| **aries horoscope daily** | 74 000 | **20** |
| **daily horoscope for taurus for today** | 60 500 | **20** |
| cancer zodiac daily horoscope | 90 500 | 32 |

Голова (KD 71–76) — Horoscope.com, USA Today, Washington Post, Elle, Chicago Sun-Times, Astrostyle, Chani. Туда не идём.

А вот посигнальный срез — аномалия: **90 500 при KD 10**. Даже с поправкой на то, что KD у DataForSEO по лонгтейлу шумит, разрыв слишком велик, чтобы его игнорировать. Это 12 шаблонных страниц с ежедневным обновлением — ровно та задача, которую AI-продукт закрывает дешевле, чем редакция.

### 5.4. Charts / calculators

| Ключ | vol | KD |
|---|---|---|
| birth chart | 246 000 | 65 |
| birth chart calculator | 165 000 | 59 |
| natal chart calculator | 165 000 | 59 |
| natal chart | 74 000 (Ads: 90 500) | 60 |
| moon sign calculator | 27 100 (Ads: 33 100) | **29** |
| rising sign calculator | 27 100 | **30** |
| what is my rising sign | 18 100 | **16** |
| free birth chart reading | 1 000 | 66 |
| big three astrology | 1 000 | **4** |

Голова (KD 59–65) — Astro-Seek, Cafe Astrology, Astro.com. Но `moon sign calculator` / `rising sign calculator` при KD 29–30 и 27k объёма — вполне рабочая цель, и это функциональность, которую AI-продукт может отдать нативно.

### 5.5. AI astrology / chat — своя территория, малые объёмы

| Ключ | vol | KD | CPC |
|---|---|---|---|
| astrology ai | 1 300 | **17** | $3.81 |
| ai astrology | 1 000 | **22** | $4.01 |
| ai astrologer | 1 000 | **17** | $4.01 |
| ai powered astrology apps | 880 | **19** | — |
| chatgpt astrology | 880 | **15** | — |
| astrology bot | 1 600 | **5** | — |
| ai fortune teller | 1 000 | **0** | — |
| ai astrology chart | 260 | **19** | $6.53 |
| best ai for astrology | 210 | **0** | $4.47 |
| ai horoscope | 210 | **3** | $2.63 |
| ai astrology app | 170 | **19** | $3.96 |
| ai astrology free chat | 170 | **6** | $3.51 |
| astrology ai chat | 140 | **2** | $4.93 |
| astrology ai chatbot | 140 | **12** | $4.93 |
| ai astrology reading | 110 | **16** | $3.86 |
| ai astrology website free | 110 | **6** | $1.98 |
| ai astrology chat | 50 | **3** | $3.12 |
| best ai astrology app | 30 | n/a | $6.22 |
| astrology chatbot | 20 | **3** | $4.91 |
| horoscope chat | 20 | 94 | — |
| ai horoscope generator | 10 | **0** | — |

Суммарно кластер даёт порядка 8–10k показов/мес — мало. Но KD 0–22 и CPC $3–6.5 означают: занять его можно быстро и дёшево, а аудитория там — целевая и платёжеспособная. Это база для бренд-позиционирования, а не трафиковый драйвер.

### 5.6. «Astrology chat» / «ask astrologer» — интент чужой

| Ключ | vol | KD | CPC |
|---|---|---|---|
| astrology chat | 480 | 51 | $6.68 |
| free astrology chat | 480 | 41 | $3.60 |
| free astrology chat online | 170 | **24** | $4.35 |
| online astrologer free chat | 170 | 24 | $4.35 |
| ask an astrologer | 1 300 | 45 | $6.13 |
| talk to an astrologer | 70 | 69 | **$26.14** |
| ask astrologer online | 10 | n/a | — |
| **vedic astrology chat** | **33 100** | n/a | $1.81 |

Ключевое: `vedic astrology chat` — 33 100, то есть в 69 раз больше, чем `astrology chat`. Что именно за этим стоит — в разделе 6.

### 5.7. Tarot — данных нет

`ai tarot reading` и `tarot chat` — объём **null** (ниже порога провайдера, что не равно нулевому спросу), KD 11 и 45 соответственно. Для решения о расширении в таро этих данных недостаточно; нужен отдельный прогон с taro-специфичными сидами.

### 5.8. Бренды-конкуренты

| Ключ | vol | KD |
|---|---|---|
| astro seek | 201 000 | 11 |
| cafe astrology | 110 000 | 10 |
| co star astrology | 14 800 (Ads: 18 100) | 45 |
| astrotalk | 8 100 | 27 |
| co-star app | 2 900 | 37 |
| the pattern app | 1 600 | 14 |
| chani app | 1 300 | 26 |
| nebula horoscope | 880 | 26 |
| sanctuary astrology | 210 | 27 |
| astrology.com | 22 200 (Ads) | n/a |

Брендовый спрос сконцентрирован у Astro-Seek и Cafe Astrology — это подтверждает, что пользователи ищут **инструменты**, а не чат.

---

## 6. SERP: кто реально стоит в выдаче

Живой SERP-скан, 12 запросов, топ-20, US/en. Домены ниже — фактические из выдачи.

**AI Overview присутствует в 9 из 12 проверенных SERP** (нет только у `zodiac compatibility`, `daily horoscope`, `birth chart compatibility`). Это значит: часть информационного трафика будет съедена, и ставку логичнее делать на интерактив (калькуляторы, чат), который AI Overview не заменяет.

### `astrology chat`, `free astrology chat`, `ask astrologer online` — индийский ведический сегмент

Топ US-выдачи: `kundligpt.com`, `jyotinow.com`, `kundlichat.in`, `ganeshaspeaks.com`, `astrosage.com`, `astroyogi.com`, `astrotalk.com`, `talkndheal.com`, `chat.prashnakundli.com`, `product.mypandit.com`, `astromanch.com`, `hiastro.in`, `satyarishi.ai`, `play.google.com`.

Заголовки говорят сами за себя: «Free AI Kundli Reading & Astrology Chat», «Free AI Astrology Chat with Guruji, Your AI Jyotishi», «Talkndheal: India's Best Astrologers», «First Free Chat With Astrologer Online 24x7».

**Это ведическая астрология (кундли, джйотиш) и маркетплейсы живых астрологов, ориентированные на индийскую аудиторию** — даже в выдаче по США. Согласуется с `vedic astrology chat` = 33 100 против `astrology chat` = 480.

zodiac-chat.com — западная тропическая астрология с AI. **Интент не совпадает.** Ранжироваться по `astrology chat` в US означает конкурировать за пользователя, которому нужна кундли и живой пандит. Кластер надо снять с приоритетов, несмотря на привлекательный CPC.

### `ai astrology`, `ai horoscope`, `astrology chatbot` — своя лига

Топ: `astrogpt.ai`, `theastro.chat`, `kundligpt.com`, `astroo.ai`, `trustastrology.ai`, `destinyaiastrology.com`, `hiastro.in`, `vedicq.com`, `astrologerbotai.com`, `charts.sasstrology.com`, `easemate.ai`, `character.ai`, плюс `reddit.com`, `quora.com`, `youtube.com`, `play.google.com`, `github.com`, `microsoft.com`, `chani.com`.

Это выдача из мелких AI-продуктов (122–817 ключей) и UGC. Нет ни одного тяжёлого домена. **Сюда zodiac-chat.com может зайти реалистично** — и присутствие Reddit/Quora/YouTube означает, что часть работы вообще не SEO, а посев.

### `zodiac compatibility`, `zodiac signs compatibility`

Топ: `zodiacsign.com`, `horoscopes.astro-seek.com`, `astro.cafeastrology.com`, `horoscope.com`, `astroved.com`, `asknebula.com`, `dailyom.com`, `elle.com`, `today.com`, `match.com`, `wikihow.com`, `youtube.com`, а также ювелирные магазины с контент-блогами (`brilliantearth.com`, `bluenile.com`) и `loveatfirstsign.co.uk`.

Смешанная выдача: калькуляторы + редакционные гайды + SEO-блоги e-commerce. Присутствие Brilliant Earth и Blue Nile — сигнал, что барьер не запредельный: если ювелирный магазин ранжируется гайдом, профильный астрологический продукт тем более может.

### `birth chart compatibility` — самый доступный SERP из проверенных

Топ: `horoscopes.astro-seek.com`, `astro.cafeastrology.com`, `astrolibrary.org`, `astrolis.com`, `astro.com`, `astrotheme.com`, `micheleknight.com`, `gotohoroscope.com`, `farfaraway.co`, `reddit.com`, `youtube.com`, `play.google.com`.

**Ни одного медиа-домена, нет AI Overview, KD 24.** Все первые позиции — калькуляторы совместимости. Это ровно та функция, которую AI-чат отдаёт лучше статического калькулятора (можно объяснить результат, а не показать процент). Лучшая точка входа.

### `zodiac signs`, `zodiac sign dates`

Топ: `zodiacsign.com`, `britannica.com`, `en.wikipedia.org`, `costarastrology.com`, `allure.com`, `almanac.com`, `astrostyle.com`, плюс e-commerce блоги (`sininlinen.com`, `tenthousandvillages.com`, `wonderbly.com`, `eartha.life`, `emma.ca`, `somethingsilver.com`) и `physics.weber.edu`.

Энциклопедический интент. Обходить Britannica и Wikipedia — не наша задача.

### `daily horoscope`

Топ: `horoscope.com`, `dailyhoroscope.com`, `play.usatoday.com`, `elle.com`, `yourtango.com`, `astrostyle.com`, `washingtonpost.com`, `chani.com`, `chicago.suntimes.com`, `californiapsychics.com`, `karmaandluck.com`.

Чистое медиа + established-бренды. Голова закрыта наглухо, работаем только с посигнальным хвостом.

---

## 7. Гео: US — не обязательно лучший рынок

Прогон 6 зондирующих ключей по 5 англоязычным странам:

| Страна | ai astrology | daily horoscope | zodiac compatibility | astrology chat |
|---|---|---|---|---|
| **India (2356)** | **135 000, KD 12** | 60 500, KD 80 | 1 600, KD 27 | 2 900, KD 75 |
| Canada (2124) | 480, KD **3** | 90 500, KD 52 | 1 600, KD 31 | 110, KD 40 |
| UK (2826) | 260, KD **13** | 49 500, KD 54 | 1 600, KD 20 | — |
| Australia (2036) | 210, KD **5** | 22 200, KD 58 | 720, KD 24 | 70, KD 4 |
| Philippines (2608) | — | 4 400, KD 78 | 1 300, KD 34 | — |
| USA (2840) | 1 000, KD 22 | 301 000, KD 71 | 18 100, KD 36 | 480, KD 51 |

**Индия — аномалия: `ai astrology` 135 000 при KD 12.** Это в 135 раз больше американского объёма при вдвое меньшей сложности. Но там же `astrology chat` KD 75 и `daily horoscope` KD 80 — рынок насыщен локальными игроками (AstroSage, Astrotalk, GaneshaSpeaks), и интент ведический, а не тропический.

Честная оценка: индийский объём **не берётся текущим продуктом** без ведического модуля (кундли, дашá, накшатры). Это стратегический вопрос к продукту, а не SEO-задача. Но если такой модуль появится — там на порядок больше спроса, чем во всём западном сегменте.

Канада, UK и Австралия по `daily horoscope` дают 22k–90k при KD 52–58 — заметно мягче американских 71. Если делать посигнальные страницы, эти рынки логично захватить тем же шаблоном.

---

## 8. Стоит ли копать: приоритеты

Отправная точка по GSC — **20 кликов и 357 показов за 90 дней с одной страницы** (раздел 3.1). Ни один из перечисленных ниже кластеров сейчас не даёт сайту ни одного показа: в GSC нет ни одного запроса про compatibility, synastry, birth chart или посигнальные гороскопы. Приоритеты ниже — это не оптимизация существующего трафика, а создание его с нуля. Соответственно и мерить эффект нужно абсолютным приростом кликов относительно базы 20/90 дней, а не процентами.

### Копать (высокий приоритет)

**1. Compatibility / synastry как продуктовая фича + посадочные страницы.**
Объём 18 000–22 200 на запрос, **KD 11–26**, CPC $2.0–2.7. SERP из калькуляторов, без медиа, без AI Overview. astroo.ai уже доказал, что это работает (`/synastry`, `/blog/birth-chart-love-compatibility` — их два главных источника трафика). Целевые формулировки — через `birth chart` / `natal chart` / `synastry`, а не через `zodiac`: тот же объём, вдвое-втрое ниже KD.

**2. Посигнальный лонгтейл дневных гороскопов, programmatic.**
`leo horoscope daily` 90 500 KD 10, `aries` 74 000 KD 20, `virgo` 74 000 KD 23, `taurus` 60 500 KD 20. 12 шаблонных страниц + ежедневное обновление. AI-генерация здесь — не костыль, а честное конкурентное преимущество по себестоимости. Обязательно проверить KD выборочно перед запуском (см. раздел 10).

**3. AI-astrology кластер — как позиционирование.**
`astrology ai` (1 300, KD 17), `ai astrologer` (1 000, KD 17), `astrology bot` (1 600, KD 5), `ai fortune teller` (1 000, KD 0), `chatgpt astrology` (880, KD 15), `astrology ai chat` (140, KD 2), `astrology chatbot` (20, KD 3). Трафика мало, но занимается быстро, CPC $3–6.5, и это единственный кластер, где продукт — буквально ответ на запрос. Плюс присутствие Reddit/Quora/YouTube в выдаче: часть результата достигается посевом, а не ссылками.

### Копать осторожно (средний приоритет)

**4. Chart-калькуляторы среднего эшелона.** `moon sign calculator` 27 100 KD 29, `rising sign calculator` 27 100 KD 30, `what is my rising sign` 18 100 KD 16, `big three astrology` 1 000 KD 4. Требует реальной эфемеридной функциональности, не текста.

**5. Traits-хвост.** `zodiac sign traits` 4 400 KD 23, `zodiac traits` 3 600 KD 24, `zodiac sign personality traits` 1 900 KD 25. Дёшево заходится, но CPC $0.26–1.78 — монетизация слабая. Годится как топикальная обвязка вокруг основных кластеров.

**6. Weekly / monthly horoscope.** 27 100 KD 32 и 12 100 KD 27 — заметно мягче дневных. Тот же шаблонный подход.

### Не копать

**7. `astrology chat` / `ask astrologer online` / `free astrology chat`.** Несмотря на CPC до $26.14 — интент ведический и маркетплейсный, выдача занята индийскими платформами живых астрологов. Продукт этому интенту не соответствует.

**8. Голова дневных гороскопов** (`daily horoscope` 301 000 KD 71, `horoscope today` 368 000 KD 75). Washington Post, USA Today, Elle. Не наша весовая категория.

**9. `zodiac signs` / `zodiac sign dates`** (673 000 KD 38 / 246 000 KD 48). Формально KD терпимый, но выдача — Britannica, Wikipedia, Almanac, Allure, плюс AI Overview. Энциклопедический интент, CPC $0.17–0.24. Даже успех здесь принесёт трафик, который не конвертируется.

**10. Всё вокруг фразы «zodiac chat».** См. раздел 4 — интента не существует.

---

## 9. Где сайт может отличиться именно как chat/AI-продукт

1. **Объяснение вместо процента.** Все конкуренты по compatibility (Astro-Seek, Cafe Astrology, Astrolis, Astrotheme) выдают статический отчёт. Чат может отвечать на «а почему у нас так с Луной в Скорпионе» — это удержание и глубина сессии, которых у калькуляторов нет.
2. **Интерактив против AI Overview.** AI Overview найден в 9 из 12 SERP и будет отъедать информационные клики. Страницы-инструменты (совместимость, rising sign, синастрия) он не заменяет — трафик туда устойчивее.
3. **Западная тропическая ниша не занята AI-продуктами.** Ведический AI-сегмент переполнен (kundligpt, jyotinow, hiastro, satyarishi, vedicq, astrologerbotai). Западный — это фактически astrogpt.ai (223 ключа), theastro.chat (122) и astroo.ai (817). Свободно.
4. **Себестоимость посигнального контента.** 12 знаков × daily/weekly/monthly × 4 рынка — это объём, который редакция не потянет, а генератор потянет.
5. **EU-происхождение и приватность** (заявлено на главной) — дифференциатор против индийских маркетплейсов, где нужна регистрация и оплата за минуты консультации.

---

## 10. Что проверять следующим шагом

**Технический минимум (блокирует всё остальное):**
1. Создать `sitemap.xml` (сейчас 404, перепроверено 2026-08-19) и добавить директиву `Sitemap:` в `robots.txt` (сейчас там только комментарии Cloudflare). Пока страница одна, ценность карты близка к нулю — но она понадобится в тот момент, когда появится первый пакет контента, и делается за час.
2. Решить, где живёт контент: `/blog/` или корневые лендинги. astroo.ai использует и то, и другое (`/synastry` + `/blog/...`). GSC подтверждает, что сейчас индексируемая поверхность = одна главная страница.
3. Настроить регулярный съём GSC (доступ есть, см. 3.1) — сейчас база 20 кликов / 357 показов за 90 дней зафиксирована, дальше нужен трекинг дельты, а не разовый срез.

**Данные, которых не хватает:**
4. **Перепроверить KD посигнальных гороскопов** (`leo horoscope daily` KD 10 при 90 500) отдельным SERP-прогоном — цифра слишком хороша, нужен живой SERP по 3–4 знакам, прежде чем строить на ней план.
5. **Прогнать SERP по compatibility-формулировкам через birth chart / synastry** (`natal chart compatibility` KD 19, `zodiac compatibility birth chart` KD 19) — подтвердить, что выдача такая же «калькуляторная», как у `birth chart compatibility`.
6. **Отдельный прогон по tarot** — сейчас объёмы null, решение о расширении принимать не на чем.
7. **Гео-решение по Индии:** нужен ли ведический модуль. `ai astrology` 135 000 при KD 12 — самая большая цифра во всём исследовании, но продукт под неё не заточен.
8. **Проверить локализацию** под UK/CA/AU: `daily horoscope` там KD 52–58 против 71 в US при 22k–90k объёма.
9. **Backlink-профиль** astroo.ai и theastro.chat — понять, сколько ссылок реально нужно для входа в AI-кластер (в текущем surface-прогоне не делалось).
10. **Уточнить product-angle:** `ai powered astrology apps` (880, KD 19), `best ai for astrology` (210, KD 0), `best ai astrology app` (30, CPC $6.22) — листинговые/сравнительные запросы, которые закрываются не блогом, а присутствием в чужих подборках и в Play Store (`play.google.com` встречается в 7 из 12 SERP).

---

## 11. Блокеры и ограничения данных

**GSC — доступ есть (исправление первой версии отчёта).**
В первой версии здесь стоял блокер «доступа к GSC нет». Он был ошибочным: сервис-аккаунт существует и заведён вне этого репозитория, у него `siteFullUser` на property `sc-domain:zodiac-chat.com`. Все пункты, помеченные ранее как «не сделано» — traffic footprint, 90d и 30d page-level строки, query+page строки, распределение позиций — **выгружены и приведены в разделе 3.1**.

Что при этом остаётся ограничением уже по существу данных, а не доступа:

- **Форма property.** Работает только `sc-domain:zodiac-chat.com`. URL-prefix `https://zodiac-chat.com/` возвращает **403** — такой property сервис-аккаунту не выдан. Скрипты обязаны использовать `sc-domain:`-форму.
- **Анонимизация запросов.** Названные запросы покрывают лишь **16% показов и 20% кликов** за 90 дней (57 из 357 и 4 из 20); за 30 дней — 11.5% показов. Остальное Google скрывает как редкие запросы. Поэтому распределение по позициям и список запросов характеризуют только видимую часть, а суммарные цифры (20/357) — полные.
- **Объём данных ниже рабочих порогов.** 16 строк запросов за 90 дней означают, что стандартные quick-wins (позиции 11-20, ≥50 показов) не находятся вообще — `research_quick_wins.py` вернёт пустой результат. Это не сбой скрипта, а свойство сайта на текущей стадии.
- **Малая выборка.** Разрыв мобильных и десктопных позиций (7.64 против 22.94) и CTR 5.6% на средней позиции 14.57 при 357 показах статистически ненадёжны — трактовать как гипотезы, не как факты.
- **Сверка sitemap ↔ GSC не сделана**, потому что sitemap отсутствует (см. ниже), а не потому, что нет данных GSC.
- GA4 по проекту не подключён (`ga4_property_id` пуст), поэтому поведенческих данных за кликом нет.

**Прочие ограничения:**
- `sitemap.xml` отдаёт **404** (перепроверено 2026-08-19; `sitemap_index.xml` — тоже 404, `robots.txt` — 200, но без директивы `Sitemap:`). Это остаётся техническим блокером: сверять GSC не с чем, пока карту не создадут.
- Эндпоинт DataForSEO Labs `domain_metrics` возвращает 404 на текущем тарифе — organic keywords count / ETV / domain rank по доменам недоступны. Данные раздела 3.2 получены через `ranked_keywords` (поле `total_count`).
- `keyword_ideas` возвращает пустой ответ для `zodiac chat` — обойдено через `keyword_suggestions`.
- Объёмы clickstream (Labs) и Google Ads расходятся; в отчёте приведены оба, расхождения помечены.
- `ai tarot reading`, `tarot chat`, `zodiac chatbot`, `horoscope chatbot`, `natal chart chat`, `astrology chat with astrologer free` — объём **null** или отсутствуют в базе. Null у DataForSEO означает «ниже порога провайдера», а не «нулевой спрос».
- Backlink-экспорты не делались (surface-глубина по условиям задачи).
- KD у лонгтейла (особенно посигнальных гороскопов) шумит — см. пункт 4 раздела 10.

---

## 12. Артефакты

| Файл | Содержимое |
|---|---|
| `2026-08-19-keyword-surface-data.json` | полный сырой ответ: overview, Google Ads volume, suggestions, geo scan, 12 SERP |
| `2026-08-19-domain-visibility-data.json` | ranked_keywords и метрики по 13 доменам |
| `2026-08-19-keyword-metrics.csv` | 276 ключей: объёмы (CS и Ads), KD, CPC, competition, intent |
| `2026-08-19-geo-scan.csv` | 21 строка: 6 ключей × 5 стран |
| `2026-08-19-surface-scan.log` | консольный вывод surface-скана — **не в git** (`*.log` в `.gitignore`), содержимое полностью дублируется JSON-дампом |
| `2026-08-19-domain-visibility.log` | консольный вывод скана видимости — **не в git**, то же самое |

Google Search Console (добавлено 2026-08-19, property `sc-domain:zodiac-chat.com`):

| Файл | Содержимое |
|---|---|
| `2026-08-19-gsc-summary.json` | итоги по обоим окнам: totals, бакеты позиций, top queries/pages, query+page, разбивка по датам, странам и устройствам, результат проверки доступа к property |
| `2026-08-19-gsc-queries-90d.csv` | 16 строк запросов за 2026-05-21 — 2026-08-18 |
| `2026-08-19-gsc-queries-30d.csv` | 13 строк запросов за 2026-07-20 — 2026-08-18 |
| `2026-08-19-gsc-pages-90d.csv` | page-level, 90 дней (1 строка) |
| `2026-08-19-gsc-pages-30d.csv` | page-level, 30 дней (1 строка) |
| `2026-08-19-gsc-query-page-90d.csv` | query × page, 90 дней (16 строк) |

**Команды:**

```bash
python3 research_keyword_surface.py --project zodiac-chat --geo-scan --suggestions 40 --serp-depth 20
python3 research_domain_visibility.py --project zodiac-chat --ranked-limit 50
python3 research_gsc_footprint.py --project zodiac-chat --long-window 90 --short-window 30
```

`research_gsc_footprint.py` читает путь к сервис-аккаунту из `GSC_CREDENTIALS_PATH` и property — из `project.json` (`gsc_site_url`). Сам файл сервис-аккаунта в репозиторий не попадает (`credentials/` в `.gitignore`), и в артефактах не сохраняется ничего, кроме e-mail сервис-аккаунта и уровня доступа.
