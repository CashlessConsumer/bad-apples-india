# Bad Apples India — Agent Guidance

## What This Is

A public, searchable, verifiable archive of police misconduct in India, inspired by Aaron Swartz's Bad Apple project. Every entry links to evidence — video, documents, official records — with clearly identified officer names.

## Key URLs

- **GitHub:** https://github.com/CashlessConsumer/bad-apples-india
- **Live site:** https://cashlessconsumer.github.io/bad-apples-india/
- **Constitution:** https://cashlessconsumer.github.io/bad-apples-india/constitution.html

## Architecture

- **Static site** — single HTML SPA (no framework, no build dependency)
- **Data** — JSON files in `data/incidents/` (one file per incident, single JSON object)
- **Build** — `scripts/build.sh` combines + copies to `_site/`
- **Deploy** — GitHub Pages (main branch, /root) or Vercel (zero config)

## How to Add an Incident

1. Create a new JSON file in `data/incidents/<id>.json` following `data/incidents/TEMPLATE.json`
2. Or use: `node scripts/add-incident.js 'Location' 'State' 'District' 'OfficerName' 'BadgeNo' 'Rank' 'Station'`
3. Run `bash scripts/build.sh` to verify
4. Commit and push — GitHub Pages auto-deploys

## Incident Schema

| Field | Required | Description |
|-------|----------|-------------|
| `id` | Yes | Unique ID (e.g., DL-ND-2026-0001) |
| `date` | Yes | ISO 8601 date |
| `location` | Yes | City, district |
| `officers` | Yes | Array: {name, badge, rank, station} |
| `narrative` | Yes | Factual 2-4 sentence description |
| `status` | Yes | Legal status (complaint_filed, fir_registered, etc.) |
| `evidence` | Yes | Object with videos array and other evidence flags |
| `sources` | Yes | Array of {type, url, description} |

## Evidence Tiers

- Tier 1: Court judgment, judicial inquiry
- Tier 2: Verified video (multiple sources), FIR, medical report
- Tier 3: Single-source video, credible news, sworn affidavit
- Tier 4: Unverified (not accepted as sole evidence)

## Status

- [x] Constitution drafted (CONSTITUTION.md + constitution.html)
- [x] GitHub repo created under CashlessConsumer org
- [x] GitHub Pages configured at `cashlessconsumer.github.io/bad-apples-india`
- [x] Data schema + sample incident
- [x] Build script produces `_site/` 
- [x] Runtime feed fetcher (serves `_site/data/feed.json`)
- [x] Vercel config
- [ ] First real incident entry from the momentum-generating tweet
- [ ] Published link shared in reply to the tweet
