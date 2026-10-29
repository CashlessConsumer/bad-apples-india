# OSINT Note — Instagram account @yourvijayamani (impersonation pretext in BAI-2026-010)

**Case:** BAI-2026-010 — TN-CHENNAI-ECONOMIST-KALAIYARASAN-DETENTION-2026-10-28
**Date of probe:** 2026-10-29 (~05:30–06:00 IST)
**Method:** Read-only public-surface inspection (Google index, Instagram unauthenticated page render, archive lookups). No follow, no contact, no interaction with the account. All artifacts hash-listed at the bottom.

## Why this account matters

Per the victim's complaint letter to the DGP dated 28 October 2026 (artifact `dgp-complaint-letter-2026-10-28.jpg`), three plain-clothes men who picked him up at ~5 AM showed him a screenshot of "an abusive comment posted from an Instagram account" whose profile picture was his photograph, with a username he did not recognise — written in the letter as "@youvijayamani". The letter adds: "The culprit appears to have taken my photograph from the website of Harvard University where I was a research affiliate." This note verifies the account's public surface and the photo-source claim.

## Findings

### 1. The account exists, is live, and matches the letter (verified)

| Attribute | Value (as of 2026-10-29) | Verification |
| --- | --- | --- |
| Handle | `@yourvijayamani` (letter's "@youvijayamani" appears to be a one-letter misreading of the police screenshot) | Live page render + Google index |
| Display name | "vijaya manikandan" | Live page render |
| Bio | "Research analyst \| cosmopolitan" | Live page render + Google-indexed profile snippet |
| Followers / following | 2 followers / 35 following (Google's pre-incident index showed 33 following — the account followed ~2 more accounts after the 28 Oct incident, i.e. it remained active) | Live render vs indexed snippet |
| Live status | Live and resolvable at instagram.com/yourvijayamani at probe time | Screenshot `ig-profile-screenshot-2026-10-29.png` |
| Archive state | No Wayback Machine captures; no archive.today capture found before probe time (SPN and archive.today submission attempts on 2026-10-29 failed with 5xx/429; local captures in this folder are the preservation of record) | CDX query + archive.ph lookup |

### 2. Profile picture = his Harvard Mittal Institute portrait (verified by direct comparison)

The profile picture (`ig-profilepic-2026-10-29.jpg`) is the same portrait published on his Lakshmi Mittal and Family South Asia Institute, Harvard University researcher page (`wp-content/uploads/2021/08/Kalai-1200x1505.jpg`, uploaded Aug 2021; page screenshot `harvard-mittal-page-screenshot-2026-10-29.jpg`): same pose, glasses, grey-and-maroon attire, bookstore backdrop. The letter's photo-source claim checks out.

### 3. Content surface: repost memes as posts; abusiveness in comments

Indexed activity attributable to the account:

- **Own post, ~5 Aug 2026** (post id `Dbqpo9KyeDZ`): caption "Elaathaium adipom......." (Tamil: "we'll beat everyone"). Thumbnail `ig-post-meme-oldme-newme-aug2026.webp` — an AI-generated "Old me / New me" Tamil-language personality meme.
- **Grid content** (visible in `ig-profile-screenshot-2026-10-29.png`): a "LEARN WITH LEGEND" video thumbnail, the Aug 2026 meme, a "Story behind 'Escalator'" video thumbnail — repost/aggregator-style content, not original political commentary.
- **Comments on others' posts** (via Google-indexed snippets): "Kanja college" on an Ayudha Pooja reel tagged @mariewilson_tvk (`DejrFEoJFIe`) and "Kanjaavum" on a post captioned "Some people are more than just Ministers…" concerning a minister receiving a 'Best Creator Award' (`DegC23kTseX`) — derogatory Tamil slang, consistent with the "abusive comments" characterisation. These snippet attributions are Tier 4 on their own (search-engine snippets) and are recorded as pattern corroboration only.

**Not independently verified:** the specific abusive comment "against Pallavaram TVK MLA J. Kamatchi" that police showed the victim. That attribution rests on the victim's letter (primary document) and secondhand X accounts. The Kamatchi identification (TVK MLA, Pallavaram AC-30, Chengalpattu district; won May 2026 with 1,33,611 votes) is verified separately.

### 4. The persona "vijaya manikandan" is unverifiable (deliberately so)

"Vijaya/Vijay(a) Manikandan" is a common Tamil personal name; multiple unrelated professionals with that name appear on LinkedIn across Chennai, Chengalpattu, Madurai and Bengaluru. None can be tied to the account from public surface, and we make no attempt to do so. Per Constitution Art. II (no doxxing), the account operator's identity is out of scope until a court or police record identifies it.

### 5. Jurisdiction note (from the letter, unverified)

The men said they were taking him to **T4 Sankar Nagar Police Station, Pammal** — a Tambaram City Police Commissionerate station (Chengalpattu side), while the pickup occurred at his Adyar residence (Greater Chennai Police jurisdiction) and the vehicle used was "a rented car (not a police vehicle)". The detention therefore crossed commissionerate lines on its face; the letter's account is the only source for the station name so far.

## Gaps and watch items

1. Whether police have registered anything against the unknown operator of @yourvijayamani (that would be the actual offence: impersonation under IT Act s.66C/66D, BNS ss.316/319 as applicable) — and why a 5 AM residential pickup was the response to an account with 2 followers.
2. Whether the account is removed or preserved as evidence; if it disappears after this publicity, preservation falls to Instagram's legal-process record.
3. Whether the "Kamatchi comment" screenshot is ever produced in any inquiry.
4. Archive submission to be retried for the live profile (Wayback SPN was returning 523s on 2026-10-29).

## Artifact manifest (this folder)

| File | What it is |
| --- | --- |
| `dgp-complaint-letter-2026-10-28.jpg` | Photograph of the complaint letter to the DGP (as circulated on X by @karur_kaaran). Contains the victim's home address — the address must not be republished; crop/redact before any web embedding. **Kept locally only and git-ignored: not committed to the public repo (Art. II minimization; a journalist's repost carrying it was already deleted for this reason).** |
| `ig-profile-screenshot-2026-10-29.png` | Full profile render at probe time (handle, name, bio, 2/35 counts, grid, profile pic). |
| `ig-profilepic-2026-10-29.jpg` | Profile picture file (150px render served by Instagram CDN). |
| `ig-post-meme-oldme-newme-aug2026.webp` | The account's ~5 Aug 2026 post (AI "Old me / New me" Tamil meme). |
| `ig-post-thumb-yourtears.jpg` / `ig-post-thumb-escalator.jpg` | Grid thumbnails of two other visible posts. |
| `harvard-mittal-page-screenshot-2026-10-29.jpg` | His Harvard Mittal Institute researcher page showing the source portrait. |

*Probe conducted under Constitution Art. II (non-partisan, no doxxing) and Art. III tiering; snippet-level items are Tier 4 and labelled as such above.*
