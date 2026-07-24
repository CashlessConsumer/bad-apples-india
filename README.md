# Bad Apples India 🍎

A public, searchable, verifiable archive of police misconduct in India. Every entry links to evidence — video, documents, official records — with clearly identified officer names.

Inspired by **Aaron Swartz's Bad Apple** project — a suite of law enforcement accountability tools.

**Live archive:** https://cashlessconsumer.github.io/bad-apples-india/
**Constitution:** https://cashlessconsumer.github.io/bad-apples-india/constitution.html

## Project Structure

```
bad-apples-india/
├── index.html              # Main archive SPA — searchable, filterable
├── constitution.html       # Constitution & principles
├── CONSTITUTION.md         # Constitution in Markdown
├── README.md
├── data/
│   └── incidents/          # One JSON file per incident
│       ├── TEMPLATE.json           # Schema reference
│       ├── FOUNDING-2026-07-24.json  # Project origin document
│       └── sample-incident.json
├── scripts/
│   ├── add-incident.js     # CLI to scaffold new entries
│   └── build.sh            # Combines incidents -> _site/data/feed.json
├── _site/                  # Built output (gitignored)
├── .github/workflows/      # GitHub Actions auto-deploy
├── vercel.json             # Vercel config (zero-config)
└── LICENSE
```

## Adding an Incident

Create a new file in `data/incidents/<id>.json` following `data/incidents/TEMPLATE.json`, then:

```bash
bash scripts/build.sh    # verify it works
git add data/incidents/<id>.json && git commit -m "add incident: <id>" && git push
```

GitHub Actions auto-deploys.

Or use the CLI:
```bash
node scripts/add-incident.js 'Location' 'State' 'District' 'OfficerName' 'BadgeNo' 'Rank' 'Station'
```

### Evidence Schema (excerpt)

Each incident includes:
- **Officers**: name, badge, rank, station (with `identified_by` flags)
- **Evidence**: videos (with `embed_url` supporting X/Twitter, YouTube), medical reports, FIR copies
- **Evidence Tier**: 1 (court judgment) → 4 (unverified — not accepted alone)
- **Status tracking**: complaint_filed → fir_registered → convicted/acquitted/closed

Full schema at `data/incidents/TEMPLATE.json`.

## Deploy

### GitHub Pages (currently used)

The repo auto-deploys via GitHub Actions on every push to `main`.

### Vercel (one click)

[![Deploy to Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/CashlessConsumer/bad-apples-india)

### Any static host

```bash
bash scripts/build.sh
# deploy _site/ to any static host
```

## Principles

1. **Evidence above allegation** — every entry links to verifiable primary evidence
2. **Naming with precision** — individual officers named with badge, station, rank
3. **Non-violence** — documentation, not retribution
4. **Verifiability** — attributable sources through trusted intermediaries
5. **Open data** — machine-readable JSON, ODbL licensed
6. **Video-first** — embedded evidence is the core format
7. **Permanent record** — entries are never deleted; corrections are appended
8. **Built in public** — community-governed, no single owner

## License

- Constitution: [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/)
- Incident data: [Open Database License (ODbL)](https://opendatacommons.org/licenses/odbl/)
- Code: [MIT](./LICENSE)
