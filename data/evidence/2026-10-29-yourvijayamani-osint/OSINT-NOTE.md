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

---

## Addendum — same night, deeper pass (2026-10-29 ~06:00 IST): operator attribution, followers/following, profile forensics

**Method unchanged:** read-only public-surface inspection (Google index of Instagram pages, unauthenticated profile render via browser, archive lookups). No interaction with the account. All new claims below are tied to indexed post URLs or live-page captures.

### 1. Comment corpus expanded — 15 indexed instances (updated pattern)

| Post | Owner / context | Comment (Tamil) | Approx. date |
| --- | --- | --- | --- |
| reel/DeYMOLqJjWD | Marie Wilson (TVK MLA, RK Nagar) fan reel | "Tharkuri kathalarzzz" | Oct 17 |
| reel/DeZlOAnJqD5 | Marie Wilson reel (Irfan Chennai video) | "Tharkuri kathalarzzz" | — |
| reel/DeKmXoIzpIm | Marie Wilson reel | "Tharkuri kathalarzzz" | Oct 17 |
| reel/DeUsSZypbFd | Marie Wilson/TVK reel (160 comments) | "Tharkuri kathalarzzz" | "6 days ago" (≈Oct 21–22) |
| reel/Dcby-0aylm6 | Marie Wilson/Irfan reel | "Tharkuri kathalarzzz" | — |
| reel/De4f5Xup2MS | "Idhukku Appuram Yenga RK NAGAR" | "Thevidiyaa payale... Poi kudumbatha paarraaa" | — |
| reel/DX6LSaDzqcq | "Congratulations @actorvijay, Chief Minister" reel | "Dei loosu" | — |
| reel/De4MqIZpz2e | Seeman/NTK-TVK reel | "Poi vijay kunja kadi irfan. Nee athukuthaan laaiku... Un kudumbam" | — |
| reel/De3xhVYD6Cp | TVK-vs-DMK reel (Vettri media, Sept 2) | "Thàrkuri... Nee yaaruku peththa un kulanthaya" | Sept 2 |
| reel/DekS5K3Tbvn | @savukku_shankar_official TVK video | "Kanja tharkuri" | Oct 16; reindexed "4 days ago" |
| reel/DdEu76XPeZi | #vck #tvk throwback reel | "Tvk bra and jatti potu oru video podu bro" | "6 days ago" |
| reel/De0goaWJBTQ | "30000 KODI YENGA @mkstalin #tvk" (anti-Stalin, TVK-side reel) | "Poi Stalin sutha nakku.. [mother-line abuse]" | — (reads anti-DMK) |
| reel/DcJXB-OIPZH | non-polical movers reel | "Innaiku evlo saamaan kadathneenga" | "3 days ago" (≈Oct 24–25) |
| reel/DelcEr2p9XE | RK Nagar sports reel | another commenter addresses "yourvijayamani" by name in banter | — |
| reel/DejrFEoJFIe | Irfan Chennai Ayudha Pooja reel | "Kanja college..." (earlier capture) | — |

**Pattern reading (corrected and sharpened):** the account is an embedded regular in Tamil Nadu political Instagram comment threads, overwhelmingly around the TVK ecosystem (TVK MLAs' fan reels, TVK IT Wing's Irfan Chennai, TVK media pages), spamming copy-paste slur abuse — but with at least one anti-DMK slur on a TVK-side anti-Stalin reel, jokes on non-political reels, and visible banter with other commenters. It is not a coherent single-party operative; it reads as a dedicated slur-troll persona. The specific abusive comment "against Pallavaram TVK MLA J. Kamatchi" that police showed the victim remains unlocated in the public index — that attribution still rests on the victim's letter.

### 2. Corrections to the original note

- Original note said the account "followed ~2 more accounts after the 28 Oct incident". The 33-following figure came from a Google cache whose crawl date is unknown; the 2→35/33→35 delta therefore cannot be pinned to the incident window. What is solid: the account was live, resolving, and showing 2 followers / 35 following on 2026-10-29, with only 3 posts — an actively maintained presence, not an abandoned one.
- The "police station" in the letter is **T4 Sankar Nagar, Pammal — Tambaram City Police Commissionerate**, i.e. a cross-commissionerate detention (pickup in Adyar, Greater Chennai Police area). Already reflected in the incident entry.

### 3. Profile forensics

- **Numeric user ID: 35523406537** (verified — appears as the profile's own `props.id` in the page payload, `profilePage_35523406537`). Stable identifier; quote it in any preservation/disclosure request.
- Cross-check: `@irfanchennai_official` — the TVK IT Wing coordinator whose posts the account abuses (self-described "TVK IT Wing", 65K followers) — carries ID **60538449837**. Instagram user IDs trend upward with allocation time; on that heuristic, `yourvijayamani` was allocated **before** Irfan's TVK-era account (TVK founded Feb 2024). Combined with the first known post on 5 Aug 2026 and only 3 posts total, the profile fits an **aged account repurposed** as the troll persona — a standard sockpuppet practice that defeats "brand-new account" filters. The ID-ordering is a heuristic, not a documented guarantee; no creation date is asserted.
- Bio "Research analyst | cosmopolitan"; display name "vijaya manikandan". The persona's identity remains unverifiable (common name; no doxxing — Art. II).

### 4. Followers / following

Both lists are behind Instagram's login wall; third-party mirrors and the `web_profile_info` API returned login/challenge walls on 2026-10-29. Observable: 2 followers / 35 following. **Follower and following identities are not publicly retrievable and must come from Meta via the channels below.** No public-surface signal ties either follower to any police or party entity, and none is asserted.

### 5. Operator attribution — was the account created by the police?

**Current public evidence: no.** Recorded as unsupported, with the reasoning the Archive will stand behind:

**Against the police-creation hypothesis (observables):**
1. The account predates the incident by at least three months (own post 5 Aug 2026; indexed comment 2 Sept 2026). A purpose-built pretext account would be created near the complaint.
2. The indexed abuse is low-grade copy-paste slur spam across a dozen unrelated reels — including jokes on non-political content and banter where other users know the handle. Nothing in the corpus rises to a threat or incitement that would justify a 5 AM detention. If the police authored the account as pretext, they authored it badly.
3. The account was still live and active after the incident. Fabricators delete or seize their instrument.
4. The police conduct described in the letter — treating the photo-owner as the suspect, producing no FIR or complaint copy, detaining in a rented car, standing down mid-route on "orders" — indicates they did **not** know who operated the account and acted on a complaint that pointed at the victim's photograph. Agencies do not investigate their own false-flag accounts by arresting strangers at dawn and releasing them when asked.

**What keeps the question open (not evidence for, but why it cannot be closed):**
- The one element pointing beyond a random troll is the choice of face: a Harvard portrait of a known economist who had just criticised the government's price record on television. An operator wanting a "clean, credible mask" or to target the photo's owner would pick exactly this. Public data cannot distinguish irony from intent.
- Police-run sockpuppet operations are a known phenomenon in Indian policing, and — structurally — the only parties who can resolve operator identity are Meta (via legal process) and the investigating agency itself. The agency that would verify the account's origin is the one the allegation implicates. That conflict of interest is itself an accountability fact, and the reason the record here says "unsupported", not "disproven".

### 6. Actions this analysis makes urgent

1. **Meta impersonation report by the victim** (or counsel) against `@yourvijayamani` — creates an independent, timestamped record with Meta, outside police control, and triggers Meta's own impersonation review.
2. **Preservation request to Meta** (creation date, signup email/phone, linked accounts, login IPs/devices, follower and following lists) — the account is live; deletion would erase the only first-party evidence. Cite user ID 35523406537.
3. **The police route existed and was not used:** under BNSS §94, the investigating agency could have summoned Meta's records in hours. Detaining the photo's subject instead of tracing the account's operator — then releasing without process — is the misconduct this entry records.
4. Watch: whether the account goes dark after this note's publication; whether any inquiry produces the Kamatchi screenshot.
