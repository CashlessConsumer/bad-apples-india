# Fabrication Forensics — the Pretext Supply Chain in BAI-2026-010

*Date: 2026-10-29. Case: BAI-2026-010 (TN-CHENNAI-ECONOMIST-KALAIYARASAN-DETENTION-2026-10-28). Companion to OSINT-NOTE.md; this document is the deeper pass requested after the first analysis. Append-only per Constitution Art. II 2.5.*

## 1. The question, restated properly

The first pass opened with "was the account created by the police themselves?" — and answered with public observables. That framing was a trap. Attribution of the account is not publicly answerable: the operator identity lives behind Meta's wall, and the implicated agency controls the only other data source (the complaint file). Asking the attribution question first produces confident-sounding claims from signals that cannot discriminate. The publicly answerable question is the **pretext supply chain**: how did an anonymous slur account become sufficient for a dawn detention of the person in its profile photo — and at which link of the chain could the record have been manufactured? This document models the chain and re-weights every signal from the first pass.

## 2. Stress-testing the first pass's "cuts against fabrication" claims

The first note concluded that three observables "cut against police creation." Deeper pass: **none of them discriminates.** They are demoted here, with reasons.

**Claim 1 — "A three-month organic history cuts against a purpose-built pretext." Demoted.**
Aged accounts are the standard instrument of manufactured pretext, not a counter-signal. A fresh account created the day before the "offense" would be indefensible in any proceeding and obvious to a first-semester forensic examiner. Purchase of aged, seeded accounts is an open commodity market. The account's anatomy — a generic filler bio ("Research analyst | cosmopolitan"), three inert posts, two followers, a stolen high-recognition portrait — fits acquisition-and-repurposing at least as well as organic growth. The only data that settles acquisition is Meta's (creation date, prior ownership, device/session history).

**Claim 2 — "Low-grade abuse is not worth fabricating." Demoted — and partly inverted.**
The legally operative offense in this episode is not "abusive comment about an MLA." It is **impersonation**: the account wears Kalaiyarasan's face, so the identity-misuse victim is Kalaiyarasan himself (cf. IT Act §66C identity theft; BNS §319 cheating by personation). A pretext needs a complainant and a face, not incitement. The corpus delivers both, and the content choice is optimal for framing: abuse aimed at the ruling party's women MLAs simultaneously (a) motivates a complaint from the ruling party's side, and (b) arms public revulsion against whoever wears the face. The abuse is low-grade because low-grade sufficed. It produced exactly the outcome a pretext operation would want — an extraordinary-priority dawn action, a signed disclaimer, and maximum chilling publicity — without ever requiring an arrest that could collapse in court.

**Claim 3 — "The account stayed live; fabricators delete." Demoted to neutral.**
Live-but-inert is consistent with an unbothered troll, with evidence held in an open "inquiry," and with an instrument kept in reserve. A fabricator's calculus is unchanged by the account being findable: it is only useful as a screenshot.

**Claim 4 — "Officers asked the victim for the username — conduct consistent with not controlling the account." Withdrawn.**
Asking is equally what one does to get the detainee to connect himself to the account on the record. Non-discriminating; withdrawn as an argument.

**Net re-weighting:** no public observable currently separates troll from fabrication. The first pass's asymmetry claim was methodologically naive. That is not a moot conclusion — it is the finding, and it constrains every future statement: *unsupported is not disproven.*

## 3. The signals that survive — and one that strengthens

**Mask-identifiability asymmetry (strengthened).** The operator concealed themselves completely — a two-follower lurker with no biographical trace, no cross-platform presence, no engagement history — while wearing the single most identifiable face available to the content's audience: a named, Googleable, televised critic of the government. Consequence asymmetry: face-theft with this face transfers essentially all risk to the victim (complaint, arrest, social ruin) and almost none to the operator. A consequence-avoiding troll picks an untraceable mask; this mask was selected to be found. The innocent reading is transgressive irony (trolls do wear famous faces). The alternative reading is design. Public data cannot separate indifference from intent — but the choice is now on the record as a fabrication-consistent design decision, not waved away.

**Face-centric anatomy (survives).** Everything about the account except the mask is dead weight. An account whose only load-bearing element is a specific person's photograph is functioning as an attribution device: it does not need to be believed, only to be *attributed*.

**The extraction asymmetry (survives).** The state took a signed disclaimer *from* the victim (addressed to the Inspector, T4 Sankar Nagar) and issued no paper *to* him: no acknowledgment, no case number, no Section 35 notice. The only artifact created in the entire episode belongs to the state. Whatever the disclaimer's function — verification, cover, or both — the direction of paper flow is the signature of a process where evidence-fabrication risk lives.

## 4. The chain, link by link — where fabrication hides and what is testable

1. **Acquisition.** Aged account; Instagram user ID 35523406537. Cross-reference: @irfanchennai_official (TVK IT Wing, active since at least April 2026) carries ID 60538449837 — a higher ID on a TVK-era account is consistent with (heuristic only; ID monotonicity unverified) this account predating TVK's rise, i.e. a repurposed account. Testable only via Meta records.
2. **Seeding.** Meme reposts by 5 Aug 2026 ("Elaathaium adipom......."); anti-TVK abuse corpus from 2 Sept 2026, concentrated on the ruling party's ecosystem (RK Nagar and Pallavaram MLAs' reels, a CM-victory reel, a TVK IT Wing member). The concentration builds the complaint pathway; the face makes the complaint's natural target. Documented; see OSINT-NOTE.md §Comment corpus.
3. **The complaint.** Origin, date, and sections unknown; never produced to the victim. **The hinge of the case.** A genuine complaint makes the state lazy; an engineered complaint makes it a witting or unwitting instrument. Testable: complaint copy, general diary extract of 28 Oct 2026, cyber cell register entry. RTI draft in §8.
4. **The verification skip.** No Meta legal request preceded the dawn action (as far as any record shows). A genuine impersonation inquiry's first move is platform data → operator identity. Skipping it while detaining the *impersonated victim* is either gross incompetence or pretext-use; both are accountability facts. The phone taken from the victim could have been checked for the account's credentials in seconds; nothing indicates that happened.
5. **The extraction.** The signed disclaimer. See §3.
6. **The abort.** Forty-five minutes parked in Pallavaram, several calls, then "orders received" to drop the victim home. Whose calls? The call detail of 05:00–07:45 on 28 Oct 2026 — the officers' phones and whoever commanded them — is the single most probative record the state holds. If those numbers lead to the complainant's side, the fabrication channel is mapped; if they lead only up the police chain, the chain itself is accountable for the priority.
7. **The aftermath.** No FIR known; no inquiry announced; no acknowledgment issued; account live; corpus intact; the victim's DGP letter unanswered as of 29 Oct 2026.

## 5. Hypotheses, re-weighted, with falsifiable predictions

- **H1 — Independent troll (baseline; remains most parsimonious).** Predictions: continued low-grade spam; no escalation; no FIR against the victim unless the complainant side pushes; account proceeds as before.
- **H2 — Complaint-side weaponization (fabrication at the complaint stage, not the account stage).** An existing troll account is curated into a complaint targeting the face. Predictions: the complaint file resists disclosure; the "inquiry" never touches Meta; pressure flows from the Pallavaram side; the extraordinary priority (dawn, cross-commissionerate, rented car) is explained by complainant-side influence.
- **H3 — State-adjacent creation (least supported publicly; structurally unverifiable from outside).** Predictions: the account's material enters an official record (FIR/charge-sheet) despite its provenance problems; sustained resistance to producing the complaint; Meta data never sought.
- **H4 — Escalation watch (applies across H1–H3).** The account's future behavior is the running experiment. If it now posts materially more serious content — content that would justify an arrest — that supports instrument-use. If it spams on as before, H1 gains. The account is therefore under deterministic watch (watch.py; alerts on liveness/count/content changes).

## 6. Precedent — why "unproven" must never be written as "untrue"

**Bhima Koregaon / Arsenal Consulting (2021).** A US digital forensics firm, on court-filed expert examination, found that an attacker had planted over thirty incriminating letters on activist Rona Wilson's laptop — delivered by malware 22 months before his arrest — and similar findings for co-accused Shoma Sen. The prosecution's core evidence would have been invisible as fabrication but for independent forensics the state did not control; the NIA's response was to dispute the firm's locus. Sources: India Development Review; Medianama (second Arsenal report, Apr 2021); Scroll.in; SabrangIndia. Methodological lesson for this archive: **fabricated digital evidence in Indian criminal process is documented, sophisticated, and typically provable only years later, through experts, at material cost.** An archive that writes "no public evidence of fabrication" as if it meant "no fabrication" would be making the same inferential error the NIA relies on. We record the chain, weight the signals, and leave attribution open — with the records demanded (§8) that would settle it.

## 7. The protocol this case adds to the Archive (generalizable)

Wherever a pretext artifact (account, post, screenshot) sits at the head of state action:
1. **Artifact capture** — hash, mirror, archive within hours (done: sha256 ledger in OSINT-NOTE.md).
2. **Anatomy analysis** — what is load-bearing in the artifact? (Here: the face.) Dead weight vs instrument.
3. **Beneficiary analysis** — whose complaint pathway does the content arm? Target constituency of the abuse content, mapped against who benefits from action against the face.
4. **Chain forensics** — complaint → verification skip → extraction → abort; demand each record; treat every skipped investigative step as a finding, not a gap.
5. **Longitudinal watch** — falsifiable predictions attached to the artifact's future behavior; deterministic monitoring (watch.py) rather than episodic OSINT.
6. **Language discipline** — "unsupported," never "disproven." The state's failure to identify the operator is itself a recorded fact.

## 8. Records to demand (ready-to-file)

**RTI application — Public Information Officer, Tambaram City Police (Commissioner of Police, Tambaram City), Chennai:**

> 1. Certified copy of the complaint/information dated on or before 28-10-2026 received by T4 Sankar Nagar Police Station concerning Instagram account "yourvijayamani" / "youvijayamani", including the complainant's name and the sections invoked. [If third-party personal info is claimed, provide the complaint's date, receiving officer, and sections redacting only personal identifiers.]
> 2. General Diary extracts of T4 Sankar Nagar Police Station for 28-10-2026, 04:30–10:00.
> 3. Action-taken report on the impersonation complaint concerning the said account: whether any request was made to Meta Platforms for account-owner data under BNSS §94 / IT Act §91; if yes, copy; if no, why not.
> 4. Whether any FIR has been registered concerning the said account; if yes, copy of the FIR.
> 5. Copy of any written statement/letter collected from Dr. A. Kalaiyarasan on 28-10-2026, and the acknowledgment issued to him.

**Meta preservation request (via counsel):** preservation and disclosure of account 35523406537 — registration data, prior ownership, device and session history, IP logs from 1 Aug 2026.

**CDR question for any future inquiry:** the 05:00–07:45 window of 28-10-2026 — whose phones called whose.

---
*Probe conducted under Constitution Art. II (non-partisan, no doxxing) and Art. III tiering. Snippet-level items remain Tier 4 and are labelled in OSINT-NOTE.md. This document makes no attribution claim; it models what is testable and records what the state has declined to test.*
