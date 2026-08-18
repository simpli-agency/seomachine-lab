# SEO Machine Lab

Исследовательский воркспейс для SEO-анализа по множеству независимых проектов. Основной источник данных — DataForSEO, опционально Google Search Console и GA4. Контент здесь не производится: только рисёрч и отчёты.

Форк [SEO Machine](https://github.com/TheCraigHewitt/seo-machine), переработанный под мультипроектный рисёрч.

## Как устроено

Каждый запуск привязан к проекту:

```
projects/
  _general/          # рисёрч вне проектов (цель по умолчанию)
  _example/          # шаблон для нового проекта
  acme/
    project.json     # домен, GSC-property, рынок, конкуренты, ключевики
    context.md       # опциональные заметки по проекту
    research/        # отчёты: YYYY-MM-DD-<тип>.md (коммитятся в git)
```

Креды — общие и лежат вне git (`.env`, `credentials/`). В `project.json` их быть не должно.

## Установка

```bash
pip install -r data_sources/requirements.txt
cp .env.example .env      # заполнить DataForSEO и пути к Google-кредам
python3 test_dataforseo.py --project _general
```

Нужно заполнить в `.env`:

| Переменная | Обязательность | Что это |
|---|---|---|
| `DATAFORSEO_LOGIN` / `DATAFORSEO_PASSWORD` | да | доступ к DataForSEO API |
| `DATAFORSEO_LOCATION_CODE` / `DATAFORSEO_LANGUAGE_CODE` | нет | рынок по умолчанию (2840/`en`), если проект не задал свой |
| `GSC_CREDENTIALS_PATH` | для GSC | JSON сервисного аккаунта с доступом к нужным property |
| `GA4_CREDENTIALS_PATH` / `GA4_PROPERTY_ID` | для GA4 | доступ к GA4 |
| `SEO_PROJECT` | нет | проект по умолчанию, если не передан `--project` |

## Новый проект

Репозиторий поставляется без реальных проектов — только шаблон `_example` и общая папка `_general`. Проект заводится под конкретную задачу, вручную или агентом:

```bash
cp -r projects/_example projects/acme
$EDITOR projects/acme/project.json
```

Минимум для DataForSEO-рисёрча — `domain`, `location_code`, `language_code`, `direct_competitors`. Для GSC-рисёрча дополнительно `gsc_site_url` (URL property ровно как в Search Console) и доступ сервисного аккаунта к этому property.

## Запуск

```bash
python3 research_quick_wins.py --project acme            # позиции 11-20
python3 research_competitor_gaps.py --project acme       # гэпы против конкурентов
python3 research_serp_analysis.py "ключевая фраза" --project acme
python3 research_topic_clusters.py --project acme        # тематические кластеры
python3 research_trending.py --project acme              # растущие запросы
python3 research_performance_matrix.py --project acme    # нужен GSC/GA4
python3 seo_baseline_analysis.py --project acme          # базовый срез
python3 seo_bofu_rankings.py --project acme              # BOFU-позиции
python3 seo_competitor_analysis.py --project acme        # сравнение с конкурентами
```

Без `--project` берётся `$SEO_PROJECT`, затем `_general`.

Слэш-команды Claude Code: `/research`, `/research-serp`, `/research-gaps`, `/research-trending`, `/research-topics`, `/research-performance`, `/research-ai-citations`, `/priorities`, `/performance-review`.

Отчёты пишутся на русском; ключевые слова, метрики и URL остаются в исходном виде.

## Работа на VPS

`.env` и `credentials/` не в git — на сервере они раскладываются отдельно от репозитория. Артефакты рисёрча (`projects/*/research/`) коммитятся, так что результаты синхронизируются между машинами через git.

Docker:

```bash
docker compose build
docker compose run --rm seomachine python3 research_quick_wins.py --project acme
```

## Git

Артефакты рисёрча и новые проекты коммитятся в `main` и пушатся — так результаты синхронизируются между VPS-агентом и остальными машинами. `.env` и `credentials/` в git не попадают.

## Тесты

```bash
python3 -m unittest discover -s tests
```

## Лицензия

MIT — см. [LICENSE](LICENSE).
