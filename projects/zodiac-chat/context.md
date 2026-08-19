# Zodiac Chat AI — context

## Product

zodiac-chat.com — freemium AI astrology / horoscope chat generator. Western
tropical astrology, not Vedic. Free generator + PRO plan from $5. Claims 30,000+
monthly users, founded in the EU.

Next.js, server-rendered. Indexable surface as of 2026-08-19: `/`, `/pricing`,
`/dashboard/signin`. No blog, no `sitemap.xml` (404), `robots.txt` contains only
Cloudflare content-signal comments and no `Sitemap:` directive.

## Market note

The `astrology chat` / `ask astrologer online` SERP in the US is held by Indian
Vedic (kundli/jyotish) platforms and live-astrologer marketplaces, so that
intent does not match this product. The reachable intent lives in
`ai astrology` / `astrology ai` / `astrology chatbot` and in compatibility and
chart-calculator queries phrased through `birth chart` / `natal chart` /
`synastry`.

## Credentials

GSC is not connected. `GSC_CREDENTIALS_PATH` in `.env` points at a service
account JSON that is not present on this machine, so every GSC-dependent script
fails before touching the API. Unblocking needs both the JSON file provisioned
and that service account granted access to the zodiac-chat.com property.

`gsc_site_url` is set to `sc-domain:zodiac-chat.com` on the assumption of a
domain property; if the property turns out to be URL-prefix, switch it to
`https://zodiac-chat.com/`.
