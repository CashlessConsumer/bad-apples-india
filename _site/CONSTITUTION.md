# The Bad Apples Archive — Constitution

> *Every system of accountability begins with a record. Every record is an act of defiance against impunity.*

## Preamble

We hold these truths to be self-evident: that those who wield the power of the state are accountable to the people; that secrecy enables abuse; that the names and actions of public servants are public records; and that when institutions refuse to hold their own to account, the people must build the archives themselves.

The Bad Apples Archive exists to collect, preserve, and make accessible verified evidence of police misconduct in India. It is inspired by Aaron Swartz's vision of a public database of police accountability records — a system he called Bad Apples. This is that idea, rebooted for India, run by volunteers, answerable to no state or party.

## Article I — Purpose

The Archive has one purpose: **accountability through transparency.**

1.1. We document incidents of police misconduct — excessive force, illegal detention, custodial violence, extortion, sexual assault, falsified evidence, and abuse of power — where the identity of the involved personnel is established.

1.2. We do not prosecute. We do not punish. We *record.* A record that cannot be buried, cannot be denied, and cannot be forgotten.

1.3. The Archive serves the public, the press, human rights organisations, legal aid networks, and the judiciary — anyone who needs the facts to do their work.

## Article II — Principles

The Archive is governed by these principles, in order of precedence:

| \# | Principle | Meaning |
| --- | --- | --- |
| 2.1 | **Verifiability** | Every entry must be based on independently verifiable evidence. Unsubstantiated claims are not admitted. |
| 2.2 | **Non-Violence** | The Archive is an evidence-gathering project, not a call to violence. We do not incite harm, doxxing, or harassment. |
| 2.3 | **Due Respect** | We do not presume guilt. We record that an allegation exists with supporting evidence. Legal outcomes are tracked separately. |
| 2.4 | **Proportion** | We name officers where the public interest in accountability outweighs the individual interest in privacy. Public officials acting in official capacity have diminished privacy claims. |
| 2.5 | **Irreversibility-Preservation** | Entries are never deleted on demand. Corrections and updates are appended, not retroactively removed. Only a clear finding of fabrication by a competent court shall result in redaction, and such redaction shall be noted. |
| 2.6 | **Open Data** | All data and code are public. The Archive belongs to no single person or organisation. Anyone may fork it, host it, or verify it. |

## Article III — Data Standards

3.1. **Minimum Viable Entry.** Each incident record must contain:

- Date and location of the incident
- Name(s) of the officer(s) involved, with rank and station where known
- Factual narrative (who, what, when, where — no editorialising)
- At least one piece of verifiable evidence (video, FIR, RTI response, medical report, judgment, or credible news report with named sources)
- Source attribution

3.2. **Naming Standard.** Officers are identified by full name, badge number (where available), rank, and assigned station at the time of the incident. If only a partial name is available (e.g. "Constable Rajesh, PS Mandir Marg"), that is noted with `[partial]`.

3.3. **Evidence Tiers.**

- **Tier 1:** Court judgment, judicial inquiry report, police own enquiry report finding guilt
- **Tier 2:** FIR (First Information Report), video evidence from multiple independent sources, medical report, RTI-obtained documents
- **Tier 3:** Video from a single source, credible news report with named journalists, sworn affidavit from the victim
- **Tier 4:** Social media posts, secondhand accounts, anonymous tips — *not accepted as sole evidence*

3.4. **Legal Status Tracking.** Every entry tracks the legal status of the case:

- `none` — No known legal action
- `complaint_filed` — Complaint/Zero FIR filed
- `fir_registered` — FIR registered
- `investigation_ongoing` — Under investigation
- `chargesheet_filed` — Chargesheet filed in court
- `trial_ongoing` — Trial in progress
- `convicted` — Officer convicted
- `acquitted` — Officer acquitted
- `departmental_action` — Departmental proceeding, suspension, dismissal
- `closed` — Case closed without action (with details of why)

## Article IV — Safeguards

4.1. **No Anonymous Submissions.** Every submission to the Archive must be traceable to a real person, though the submitter's identity may be kept confidential from the public. The editors must know who submitted what.

4.2. **Correction Mechanism.** Any person, including named officers, may submit evidence challenging an entry. Corrections are appended as a new version with the supporting evidence. Original records are preserved.

4.3. **False Submission Policy.** Knowingly submitting false information is grounds for permanent ban from the Archive. Fabricated entries — evidence of collusion to frame an officer — shall be identified, preserved as a record of the attempt, and the submitter's details turned over to relevant authorities.

4.4. **No Party Alignment.** The Archive does not align with any political party, caste group, religious organisation, or ideological movement. Accountability is non-partisan.

## Article V — Governance

5.1. The Archive is maintained by a rotating editorial collective of no fewer than three and no more than seven members.

5.2. Editorial decisions — acceptance, rejection, or reclassification of entries — are made by majority vote, recorded and published.

5.3. Anyone who has submitted verified entries, contributed code, or participated in evidence review for six months or more is eligible for the collective.

5.4. The Archive has no single leader, no founder veto, no paid positions.

## Article VI — Technology

6.1. The Archive is a **static site** — deployable from a GitHub repository to any static host: GitHub Pages, Vercel, Netlify, or a personal server.

6.2. The data is stored as flat JSON files — no database, no backend, no login system. Every incident file is a single JSON document.

6.3. Video evidence is embedded, not hosted. We embed from existing public platforms (YouTube, X/Twitter, etc.) and link to original sources.

6.4. The codebase is minimalist by design — no framework, no build tooling beyond a shell script for data packing. It should compile in one command and deploy in two.

6.5. CIP (Cryptographic Integrity Proofs): Optional but recommended — each incident JSON shall include a SHA-256 hash of its contents, signed by a submitter's PGP key, to create an immutable audit trail independent of the hosting platform.

## Article VII — Amendment

7.1. This Constitution may be amended by a two-thirds vote of the editorial collective, with proposed amendments published for public comment for no less than 30 days before the vote.

7.2. The Constitution itself shall be hosted alongside the Archive, under the path `/constitution`, and every version shall be preserved.

---

*Version 1.0 — July 24, 2026. Inspired by Aaron Swartz's Bad Apples, built for India.*