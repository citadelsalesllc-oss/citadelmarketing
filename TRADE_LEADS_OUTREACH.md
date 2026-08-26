# Cold Outreach System — New Trade Business Leads

Written 2026-08-26. Companion to ROADMAP.md section 7, which covers **warm** outreach
(texting people you already know from Consolidated Supply). This doc covers the
opposite problem: reaching **net-new** trade business owners in North Idaho you've
never talked to, with automatic follow-up so nothing falls through the cracks and
"who do I need to personally call" is a filtered view, not a guess.

---

## 1. Tool recommendation

**Start with GMass. Upgrade to Instantly.ai only if you outgrow it.** Skip Apollo.io
for this specific use case, and don't use Mailchimp for this at all — it will get your
account suspended. Details below.

### Why not Mailchimp + Sheets + Zapier as originally scoped

Mailchimp's Acceptable Use Policy requires **express, verifiable opt-in** from every
recipient and explicitly bans sending to purchased/researched lists. Cold outreach —
emailing a plumber who's never heard of you — is exactly what it prohibits. This isn't
a gray area or a rate-limit issue: Mailchimp actively bans accounts for it, which means
you could lose your whole email history and any legitimate opted-in list (like your own
newsletter, later) in the same account termination. Don't build the cold-outreach engine
on top of your future opted-in marketing tool.

The good news: the "cheap, DIY, spreadsheet-driven" instinct behind that idea is right —
you just need a tool built for cold outreach instead of one that forbids it. **GMass**
fills that exact slot: it runs cold sequences from a normal Gmail/Google Workspace
inbox, mail-merges from a Google Sheet (so you keep the spreadsheet-as-source-of-truth
workflow), and is legal to use for cold B2B email under CAN-SPAM (see section 6).

### The comparison

| | **GMass** (recommended start) | **Instantly.ai** (upgrade path) | **Apollo.io** (skip for this) |
|---|---|---|---|
| What it's actually for | Cold email + mail merge, bolted onto your real Gmail inbox | Cold email at volume — dedicated sending, warmup, multiple inboxes | B2B sales database + sequencer, built for teams prospecting SaaS/tech-style companies |
| Cost (solo, 2026 pricing) | ~$21-29/mo (Standard/Premium, annual) | ~$37-47/mo (Growth, annual/monthly) for sending; add a paid lead-database module if you want their contact data | $49-79/user/mo for real sequencing (free tier caps at 2 active sequences) |
| Setup time | Minutes — installs as a Gmail/Chrome extension, uses your existing inbox and reputation | 30-60 min — connect a domain/inbox, run warmup for 1-2 weeks before real sending | 30-60 min, but most of the setup effort goes into a database you won't use (see below) |
| Built-in Day 1/4/10-style follow-ups with auto stop-on-reply | Yes, native — this is one of its core features | Yes, native, more configurable (branching, multiple inboxes) | Yes, but geared toward sales teams working sequences alongside a CRM |
| Where leads come from | You supply the list (see section 2) — no database included | You supply the list, or pay extra for their lead-database add-on | Includes a large B2B contact database — but see caveat below |
| Sending volume ceiling | Bounded by your Gmail account's normal sending limits (~500/day Workspace) — plenty for a solo local pipeline | Built for higher volume across multiple dedicated inboxes/domains | Built for high volume, per-seat |
| Best fit | **You, right now** — a solo agency doing dozens to low hundreds of local trade-business touches | You, later, if you're doing hundreds/week and want to protect your main inbox's sender reputation with a separate warmed domain | A team selling into companies well-represented in a generic B2B database |

**The Apollo caveat that matters most:** Apollo's contact database is built around
companies that show up in normal B2B data sources — mostly tech, SaaS, and larger
firms with a marketing/ops presence online. A residential plumber or a two-truck
excavation outfit in Coeur d'Alene or Post Falls is exactly the kind of business that
database is weak on. You'd be paying $49+/user/month largely for a sequencer you could
get cheaper elsewhere, without the database advantage that's supposed to justify the
price. Skip it unless a future service line (e.g., prospecting GCs/developers on
LinkedIn-adjacent data) specifically calls for it.

**Bottom line:** sign up for GMass, connect it to your Citadel Sales & Marketing Gmail
(or Google Workspace address if you have one), and build your list in a Google Sheet.
If you're regularly sending 300+/week and worried about your main inbox's deliverability
taking a hit, that's the trigger to move to Instantly.ai with a separate sending domain
— not before.

---

## 2. Where the lead list itself comes from

None of these tools hand you a list of North Idaho trade businesses — you still have
to build it, but it's mechanical, not hard:

1. **Google Maps / Search**, by trade + city: "plumber Coeur d'Alene," "HVAC Post
   Falls," "excavation Hayden," etc. Pull business name, phone, website (if any), and
   whatever email you can find on their site or GBP listing.
2. **Idaho Division of Occupational & Professional Licenses** (dopl.idaho.gov) —
   plumbers and electricians are state-licensed in Idaho; the license lookup is public
   and gives you a clean, verifiable list of real, active businesses by trade.
3. **Local chamber of commerce directories** (Coeur d'Alene, Post Falls, Hayden,
   Rathdrum) — usually a public member list, often with an owner name attached.
4. While you're researching each one, jot **one specific observation** per business
   (no GBP photos, 3 reviews from 2019, no website, listing under the wrong category)
   in your sheet — this is what makes Template D in section 3 work, and it's the single
   biggest thing that makes a cold email read as researched instead of copy-pasted.

Feed this straight into the same Google Sheet that GMass mail-merges from (section 5)
— no separate list-building tool needed at your current volume.

---

## 3. Follow-up email templates

Four templates: three form the Day 1 / Day 4 / Day 10 sequence, and a fourth is a
swap-in Day 1 opener for when you found something specific during research (section 2)
— use it instead of Template A whenever you have a real hook, since specific beats
generic every time.

Merge fields shown as `{{FirstName}}`, `{{BusinessName}}`, `{{Trade}}`, `{{City}}` —
GMass and Instantly both pull these straight from your sheet's column headers.

### Template A — Day 1, initial outreach (general)

> **Subject:** quick question about {{BusinessName}}
>
> Hey {{FirstName}},
>
> I run a small marketing shop here in North Idaho — Citadel Sales & Marketing — and I
> work specifically with trade businesses like {{BusinessName}}, not big national
> franchises.
>
> Most {{Trade}} owners I talk to have the same complaint: leads come in waves —
> slammed one month, dead quiet the next — instead of a steady stream. That's usually
> a Google/reviews problem more than a "not enough marketing" problem, and it's often
> fixable in a few weeks, not a few months.
>
> No pitch in this email — just want to know if that sounds familiar. If it does,
> happy to send over a quick, specific rundown of what I'd fix first for
> {{BusinessName}} — no charge, no obligation.
>
> {{YourFirstName}}
> Citadel Sales & Marketing
> {{Phone}}

### Template B — Day 4, follow-up (pain point: inconsistent leads)

> **Subject:** re: quick question about {{BusinessName}}
>
> Hey {{FirstName}}, following up in case this got buried.
>
> The thing I see most with {{Trade}} businesses around {{City}} isn't a lack of
> demand — it's that the leads that do come in are inconsistent, so it's hard to plan a
> crew or a schedule around them. A little bit of consistent visibility (Google, mostly)
> smooths that out more than people expect.
>
> If the feast-or-famine thing sounds familiar, I'll put together a quick, specific
> look at {{BusinessName}}'s Google presence — takes me 15 minutes, costs you nothing,
> and you can do whatever you want with it, including nothing.
>
> Worth a look?
>
> {{YourFirstName}}
> Citadel Sales & Marketing

### Template C — Day 10, final follow-up (low-pressure breakup)

> **Subject:** last one from me, {{FirstName}}
>
> Hey {{FirstName}}, I'll keep this short — last note from me on this.
>
> Two things I noticed poking around for {{BusinessName}}: the Google listing looks
> like it hasn't been touched in a while, and there aren't many recent reviews showing
> up. Neither one is a big deal on its own, but together they're probably costing you
> a few jobs a month to competitors who just have a fresher-looking listing — not
> better work, just better visibility.
>
> If you ever want a second set of eyes on it, I'm around — just reply to this email.
> Otherwise, no hard feelings, and good luck out there.
>
> {{YourFirstName}}
> Citadel Sales & Marketing

### Template D — Alternate Day 1 opener (when you found something specific)

Use this instead of Template A whenever your research (section 2) turned up a
concrete, real observation — it converts better because it proves you actually looked.

> **Subject:** noticed something on {{BusinessName}}'s Google listing
>
> Hey {{FirstName}},
>
> Was looking up {{Trade}} businesses around {{City}} and pulled up {{BusinessName}}'s
> Google listing — noticed [specific thing: "it's still listed under the wrong
> category," "there's no photos on it," "last review is from 2021," etc.]. Small fix,
> but it's probably quietly costing you some "near me" search visibility.
>
> I run a small marketing shop here in North Idaho and work specifically with trade
> businesses. Happy to point out exactly what I'd fix, no charge — just reply if you
> want the quick version.
>
> {{YourFirstName}}
> Citadel Sales & Marketing
> {{Phone}}

**Tone notes, so future templates stay consistent:**
- Contractions, short sentences, no "I hope this email finds you well," no corporate
  throat-clearing.
- Every email offers something concrete and free (a look, a rundown) before ever
  asking for money — this segment trusts "show me" over "trust me," same as
  ROADMAP.md section 3.
- Sign with a first name and phone number, not a full corporate signature block — you
  want a reply or a text back, not a click into a form.

---

## 4. The automated sequence (Day 1 → 4 → 10 → auto-stop)

### In GMass

1. Build your master list in one Google Sheet tab: `Email | FirstName | BusinessName |
   Trade | City | Phone` (this doubles as your tracker — see section 5).
2. In Gmail, open the sheet's contacts via GMass's "Google Sheets" data source, or
   paste the recipient list directly into a Gmail compose window with GMass's compose
   sidebar open (GMass reads the sheet columns as merge fields automatically).
3. Draft **Campaign Email 1** using Template A (or D when you have a hook).
4. Use GMass's **Auto Follow-Up** feature to schedule:
   - Follow-up 1 → **Day 4** → Template B
   - Follow-up 2 → **Day 10** → Template C
5. Turn on **"Stop sending follow-ups to people who reply"** — this is a toggle in the
   auto follow-up settings, on by default. That's your auto-remove-on-response: the
   moment someone replies (even "not interested"), GMass pulls them out of the queue.
6. After the Day 10 email sends with still no reply, the sequence simply ends — nobody
   emails them again automatically. That's your "auto-remove after final follow-up"
   behavior; section 5 covers how to reflect that in your tracker.

### In Instantly.ai (if/when you upgrade)

Same shape, more explicit controls:
1. Create a **Campaign**, upload your lead list (CSV export from the same Google
   Sheet).
2. Build a 3-step sequence: Step 1 (Day 0/1) → Template A/D, Step 2 (+3 days, lands
   Day 4) → Template B, Step 3 (+6 days, lands Day 10) → Template C.
3. Under campaign settings, **"Stop sending emails to lead if it replies"** is on by
   default — leave it on.
4. Leads with no reply after Step 3 automatically fall out of the active sequence on
   their own (no step 4 exists) — Instantly marks them "Finished" in the campaign
   dashboard, which is your auto-remove signal.

### Compliance note either way

Every send needs: an honest "From" name, a working reply address (both templates
above satisfy this), and an unsubscribe/opt-out path — GMass and Instantly both
auto-append an unsubscribe link. This is a CAN-SPAM requirement for commercial email,
cold or not; honor an opt-out within 10 business days (both tools do this
automatically once someone unsubscribes).

---

## 5. Tracking responses — who to personally follow up with

Keep one Google Sheet as the single source of truth — the same one that feeds the mail
merge. Add these columns to the list from section 2:

| Column | Purpose |
|---|---|
| `Email`, `FirstName`, `BusinessName`, `Trade`, `City`, `Phone` | Merge fields + your reference |
| `Date Added` | When the lead entered the pipeline |
| `Sequence Status` | `Not Started` / `Day 1 Sent` / `Day 4 Sent` / `Day 10 Sent` / `Finished - No Reply` |
| `Replied?` | `Y` / `N` — this is the column you actually watch |
| `Reply Type` | Quick tag: `Interested`, `Not Now`, `Not Interested`, `Wrong Contact` |
| `Last Contact Date` | Auto or manual — when the last touch happened |
| `Next Action` | e.g., "Call Tuesday," "Send leave-behind," "Archive" |

**Two ways to keep `Replied?` and `Sequence Status` current:**

- **Manual (fine at low volume):** GMass and Instantly both show a per-campaign
  dashboard listing who replied, who's still active, and who finished the sequence.
  Check it 2-3x/week and update the sheet — takes a few minutes at the volumes you're
  running.
- **Semi-automated (worth it once volume grows):** Both tools have a Zapier
  integration with a "New Reply" / "Lead Replied" trigger. Build a Zap: trigger = new
  reply in GMass/Instantly → action = find the matching row in your Sheet (by email)
  and set `Replied? = Y`, `Sequence Status = Replied`, `Last Contact Date = today`.
  This mirrors the Zap pattern already documented in CONTENT_PIPELINE.md section 2, so
  the setup will feel familiar.

**The habit that matters more than the automation:** filter the sheet by `Replied? =
Y` every time you sit down for outreach (Mon/Wed in ROADMAP.md's weekly rhythm) — that
filtered view is your actual to-do list of who to personally call or text next, same as
the warm-contact tracker in ROADMAP.md section 7. Cold sequence gets someone to raise a
hand; you still close it with a real conversation.

---

## 6. Quick-start checklist

1. Sign up for GMass, connect your Citadel Sales & Marketing Gmail/Workspace inbox.
2. Build the lead list (section 2): 15-20 North Idaho trade businesses to start, via
   Google Maps + DOPL license lookup + chamber directories. Note one specific
   observation per business.
3. Set up the tracker sheet (section 5) — this is the same sheet GMass mail-merges
   from.
4. Load Templates A/D, B, and C into a GMass campaign with Day 4 and Day 10
   auto-follow-ups, stop-on-reply on.
5. Send to your first small batch (15-20), watch the campaign dashboard for a week,
   confirm replies are landing in your inbox and stop-on-reply is working as expected.
6. Once trusted, scale up batch size weekly and start the Zapier reply-sync if the
   manual check becomes a chore.
7. Revisit the GMass → Instantly.ai upgrade decision only once you're sending 300+/week
   or want a sending domain separate from your main inbox.
