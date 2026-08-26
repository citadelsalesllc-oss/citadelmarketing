# Content Pipeline — CapCut to Instagram/Facebook, Automated

Written 2026-08-26. Answers: which scheduler to run multiple client accounts through,
and how to go from "finished video sitting in CapCut" to "queued on Instagram and
Facebook" without manually uploading to each platform every time.

---

## 1. Recommendation: Metricool

For a solo operator managing your own accounts plus multiple client accounts, **use
Metricool**, not Buffer or Later. The deciding factor isn't feature depth — all three
schedule to Instagram and Facebook fine — it's how each one **prices and structures
multi-client access**, which is the part that actually breaks at your stage.

### The comparison that matters: cost as you add client #2, #3, #4...

| | **Metricool** | **Buffer** | **Later** |
|---|---|---|---|
| How it charges | Per **brand** (a brand = one client's full set of connected accounts) | Per **channel** (each individual IG/FB/etc. connection) | Per **Social Set** (bundle of one of each platform, sold in fixed tiers) |
| Entry paid plan | Starter: ~$22/mo (~$18/mo billed annually) for up to **5 brands** | Essentials: $6/channel/mo | Starter: ~$18.75/mo (billed annually), **1** Social Set |
| Adding a client | Free until you exceed your brand cap, then jump tiers | +$6-12/mo **per channel** (2 platforms per client = +$12-24/mo per client) | +~$11.25/mo per additional Social Set, plus +$3.75/mo if you need another seat |
| Client management features | Client roles/permissions, approval workflows, shareable client dashboards, white-label option on the top tier | Basic collaboration, no real client-facing dashboard on lower tiers | Client collaboration exists but scoped by Social Set, not by "client" as a concept |
| API / automation access | Full API + native Zapier integration on **Advanced** (~$54-67/mo, up to 15 brands) | API available, but automation-friendly tiers get expensive fast per-channel | Limited automation surface; not built around API-first workflows |

**Why Metricool wins for you specifically:** you're not paying per social account, you're
paying per *client* (a "brand" bundles all of that client's platforms together). Buffer's
per-channel pricing means every client costs you 2x their platform count in add-on fees,
which compounds badly once you're past 3-4 clients. Later's Social Set model is
functionally similar to Metricool's brand model, but at a given price point it gives you
fewer brands/sets than Metricool's equivalent tier, and its automation/API story is
weaker — which matters directly for requirement #3 below (semi-automating the upload).

**Bottom line at your stage:** start on Metricool's **Starter plan** (~5 brands covers
you + 4 clients) for about $18-22/mo. When you need the Zapier/API automation piece,
or cross 5 clients, move to **Advanced** (~$54-67/mo depending on brand count) — that
plan is also where client roles, approval workflows, and shareable client dashboards
live, which you'll want anyway once you're managing other people's accounts and need to
show them what's queued before it posts.

*(Pricing on all three of these changes often — confirm current numbers on each site
before you commit; treat the figures above as directional, not a quote.)*

---

## 2. The pipeline: CapCut export → drop folder → auto-queued in Metricool

Two ways to build this. **Start with Option A.** It's no-code, takes under an hour to
set up, and covers the actual requirement (drop a video + caption, have it queue up).
Move to Option B only if you outgrow Zapier's limits or want tighter control (e.g., a
real intake form instead of a spreadsheet).

### Option A — Folder + spreadsheet, wired with Zapier (recommended to start)

This uses a Zapier integration that already exists for this exact use case: **"Create
Metricool posts from new Google Drive files in a folder."**

**Setup:**

1. **Folder structure in Google Drive** (or Dropbox, then let Zapier move files into
   Drive first): one subfolder per client, e.g. `/Content Queue/ClientName/`. Export
   directly from CapCut into the matching client's subfolder when a video is done.
2. **Caption source**: a Google Sheet, one tab per client (or one sheet, with a
   `client` column), columns: `filename | caption | platforms | post_date | status`.
   Write the caption for a video in the row matching its filename before or right
   after you export from CapCut.
3. **Zap #1 — file drop → draft post**: Trigger = "New File in Folder" (per client
   folder). Action = "Create Post in Metricool" (Advanced plan, since this needs API
   access), pulling caption text from the matching spreadsheet row via a lookup step
   (Zapier's "Formatter" or a Google Sheets "Lookup Row" action keyed on filename),
   set to the correct Metricool **brand**, and targeting Instagram + Facebook.
4. **Zap #2 — status writeback (optional but worth it)**: Action = update the sheet's
   `status` column to "Queued" once the Metricool post is created, so you have a
   single place to see what's been picked up vs. what's still sitting unprocessed.
5. **Scheduling logic**: either let Metricool auto-schedule into your best-times slots
   for that brand, or set `post_date` in the sheet and pass it through as the
   scheduled time in the Zap.

This gets you: drop file + write caption → post appears queued in Metricool within
a few minutes → you do a final visual check in Metricool's calendar → it posts itself
at the scheduled time.

### Option B — Direct API script (once you outgrow Zapier)

If Zapier's task limits or per-step pricing start to bite, or you want a real form
instead of editing a spreadsheet, replace the Zap with a small script:

1. **Trigger**: a folder-watcher script (Python `watchdog` library, or even a
   scheduled task that diffs folder contents every few minutes) watching your local
   or synced Drive folder for new video files.
2. **Caption input**: read the matching row from a CSV/Sheet (Google Sheets API) or,
   cleaner, a tiny local web form (a single HTML page + a lightweight backend) where
   you pick the client, paste the caption, and hit submit — this replaces "write it
   in a spreadsheet" with something more mistake-proof.
3. **Upload + schedule**: call Metricool's API — `POST` the media to get a `mediaId`,
   then `POST` a scheduled post referencing that `mediaId`, the target brand ID, and
   the caption, authenticated with your API token in the `X-Mc-Auth` header.
4. Requires the **Advanced** plan (API access isn't on Starter).

Only build Option B if Option A is genuinely limiting you — for a solo operator with
a handful of clients, Option A is almost certainly enough for a long time.

---

## 3. What's automatic vs. what you still do manually

Be clear-eyed about this — "automated" here means "semi-automated." Here's the honest
split:

**Becomes automatic:**
- Uploading the video to the platform and publishing at the scheduled time (standard
  IG feed posts, Reels using Metricool's audio library, and all Facebook posts —
  Facebook's API has no manual-publish restriction).
- Pulling the caption in from your sheet/form instead of retyping it per platform.
- Cross-posting the same asset to both Instagram and Facebook from one entry point.
- Basic scheduling logic (best-time slots, or a date you set once).

**Stays manual (Metricool/Instagram platform limits, not a workflow gap):**
- Editing and exporting the final video in CapCut — nothing schedules that for you.
- Writing the caption, hashtags, and any client-specific approval sign-off.
- **A few Instagram post types still require manual publish**: Reels using audio not
  in Metricool's library, and Stories with interactive stickers (polls, links,
  mentions). For these, Metricool sends a push notification at post time that
  downloads the media and copies the caption to your clipboard so you finish the post
  natively in the Instagram app — quick, but not hands-off.
- **Connecting each new client's accounts.** Every client's Instagram (must be a
  Business or Creator account) and Facebook Page has to be linked to Metricool once,
  by whoever has admin access — usually you, logged in as the client, or the client
  granting you Business Manager access. This is a one-time setup per client, not a
  per-post step, but it's not something automation removes — it's an account-linking
  step only a human with the right login can do.
- A final glance at the Metricool calendar before things go live, especially early on
  — worth keeping as a habit even once the pipeline is trusted, since a bad caption
  auto-posting to a client's account is the kind of mistake that costs the client
  relationship, not just a re-edit.

---

## 4. Quick-start checklist

1. Sign up for Metricool, start on **Starter** (~$22/mo) if you're not yet doing the
   API automation, or **Advanced** (~$54-67/mo) if you're building Option A/B now.
2. Connect your own accounts first as the test brand — validate the whole pipeline on
   yourself before touching a client's accounts.
3. Set up the Drive folder structure (one subfolder per client) and the caption
   spreadsheet.
4. Build Zap #1 (file → post) and Zap #2 (status writeback) in Zapier.
5. Run one real video through end-to-end: export from CapCut → drop in folder → write
   caption → confirm it appears queued in Metricool → let it post → check it landed
   correctly on both platforms.
6. Once trusted on your own accounts, connect client accounts one at a time (get their
   IG/FB admin access, add them as a brand in Metricool) and repeat.
