# Bad Apples India 🍎

A public, searchable, verifiable archive of police misconduct in India. Every entry links to evidence — video, documents, official records.

Inspired by **Aaron Swartz's Bad Apple** project — a suite of law enforcement accountability tools.

## Constitution

Read the full principles: [CONSTITUTION.md](./CONSTITUTION.md) or [constitution.html](./constitution.html)

## Quick Start

### Deploy to Vercel (one click)

[![Deploy to Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/CashlessConsumer/bad-apples-india)

1. Fork this repo on GitHub
2. Import into Vercel — it's a static site, zero config
3. Add incidents via `data/incidents.json`

### Deploy to GitHub Pages

1. Enable GitHub Pages in repo Settings → Pages → deploy from `main` / `root`
2. Site is live at `https://<username>.github.io/bad-apples-india/`

### Run locally

```bash
# Any static file server works
python3 -m http.server 8000
# or
npx serve .
```

## Project Structure

```
bad-apples-india/
├── index.html            # Main archive — searchable, filterable
├── constitution.html     # Constitution & principles
├── CONSTITUTION.md       # Constitution in Markdown
├── README.md             # This file
├── data/
│   └── incidents.json    # Structured incident data
└── scripts/
    └── add-incident.js   # (Optional) CLI to scaffold new entries
```

## Adding an Incident

Edit `data/incidents.json` and add a new entry following the schema:

```json
{
  "id": "DL-ND-2026-002",
  "date": "2026-07-22",
  "location": "New Delhi, Delhi",
  "officers": [
    { "name": "Constable Name", "badge": "DL-#####", "rank": "Constable", "station": "Station Name" }
  ],
  "description": "Factual summary of what happened.",
  "evidence": [
    { "type": "video", "url": "https://x.com/user/status/123", "embed_url": "https://x.com/user/status/123", "description": "Bystander video" }
  ],
  "source": "Journalist / RTI / Citizen report",
  "legal_status": "fir",
  "category": "excessive_force",
  "tags": ["traffic_stop", "caught_on_camera"]
}
```

Supported evidence types: `video`, `doc`, `audio`
Supported legal statuses: `complaint_filed`, `fir`, `charge`, `convicted`, `pending`
Supported categories: `excessive_force`, `illegal_detention`, `fabrication`, `extortion`, `other`

## Principles

1. **Evidence above allegation** — every entry links to verifiable primary evidence
2. **Naming with precision** — individual officers named with badge, station, rank
3. **Non-violence** — documentation, not retribution
4. **Verifiability** — attributable sources through trusted intermediaries
5. **Open data** — machine-readable JSON, MIT/CC0/ODbL licensed
6. **Statutory compliant** — operates within Indian legal framework
7. **Video-first** — embedded evidence is the core format
8. **Permanent record** — no statute of limitations on public memory
9. **Built in public** — community-governed, no single owner

## License

- Constitution: [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/)
- Incident data: [Open Database License (ODbL)](https://opendatacommons.org/licenses/odbl/)
- Code: [MIT](./LICENSE)
