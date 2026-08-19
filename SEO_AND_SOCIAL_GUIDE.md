# SEO & Social Media Guide — Full Curriculum

Companion to ROADMAP.md. This is the "what SEO actually includes, end to end" reference,
plus what's currently working on social for trades (with sources), plus UTM/redirect
links explained plainly. Written 2026-08-19.

---

## Part 1 — SEO, all of it, organized by what actually moves rankings

SEO for a local trade business breaks into five buckets. They are **not equally
important** — trying to do all five at once, evenly, is why it feels overwhelming.
Per Whitespark's 2026 Local Search Ranking Factors study (the most-cited annual survey
in this industry), Google Business Profile signals alone account for ~32% of map-pack
ranking weight, and reviews add another ~20% — so GBP + reviews are roughly *half* the
game before you've touched a backlink. Work in this order:

### 1. Google Business Profile signals (biggest lever, do this first)
- Every field filled out completely — a complete profile gets ~7x more clicks than an
  incomplete one.
- **Primary category** is, individually, the single most important ranking factor
  Whitespark measures out of 187 factors tracked. Pick the most specific accurate
  category ("Plumber," not "Contractor"), and only add secondary categories that are
  genuinely true.
- Weekly GBP posts (offers, projects, updates — reuses content you already shoot).
- Photos added regularly, real job-site photos over stock.
- Q&A section seeded with real questions ("Do you offer emergency service?").
- Services list filled out with descriptions, not just names.

### 2. Reviews (second-biggest lever)
- Volume matters, but **recency matters just as much** — a steady trickle of new
  reviews outranks a pile of old ones. This is why a review-request system (Section 3
  of ROADMAP.md) is SEO infrastructure, not just reputation management.
- Respond to every review, good and bad, within 48 hours — response behavior itself is
  a factor Google tracks.
- Never buy or incentivize reviews — it violates Google's policy and profiles get
  suspended over it.

### 3. On-page / content signals
- **Service + city pages**: one dedicated page per service per city served
  ("Water Heater Repair — Coeur d'Alene," "Water Heater Repair — Post Falls"), not one
  generic "Services" page. This is the actual mechanism behind ranking for multiple
  nearby towns.
- Title tag and meta description on every page, written for a human first (what it is
  + city), keyword second.
- One H1 per page that matches page intent; H2s for sub-sections.
- Image alt text describing the actual photo ("tankless water heater install,
  Hayden ID"), not stuffed keywords.
- Internal links between service pages and from blog content back to service pages.

### 4. Technical SEO
- **Site speed / Core Web Vitals** — check any page for free at
  [pagespeed.web.dev](https://pagespeed.web.dev). Large uncompressed job-site photos
  are the #1 thing that tanks trade-business sites — compress before upload (TinyPNG,
  or your website builder's built-in image optimization).
- Mobile-friendly, since the large majority of "plumber near me" searches happen on a phone.
- HTTPS (padlock in the browser bar) — table stakes, most builders handle this automatically.
- XML sitemap submitted in Google Search Console.
- Schema markup (LocalBusiness / Service schema) — most modern builders (GoHighLevel,
  Webflow, Duda) generate basic schema automatically; verify with
  [Google's Rich Results Test](https://search.google.com/test/rich-results).

### 5. Off-page / backlinks & citations
This is real, but it's the smallest of the five levers for local trades — link signals
add credibility but carry less weight than GBP or reviews per the same study. Don't
spend disproportionate time here relative to sections 1–2.

**What a good local backlink looks like for a trade business:**
- Chamber of commerce membership (often paid, includes a directory listing + link)
- Home Builders Association / trade association membership listing
- Supplier/manufacturer "find a contractor" pages (you have real relationships here
  from Consolidated Supply — this is a genuine unlock most competitors don't have)
- Local news coverage (a press release for a milestone — new hire, big project,
  anniversary — sent to local outlets)
- Sponsorship of a local team/event, listed on their site
- **NAP citation consistency**: identical Name/Address/Phone across GBP, website,
  Facebook, Yelp, Angi, BBB, and any directory. Inconsistency actively hurts — this is
  a quick, mechanical thing to audit and fix.

**What actively hurts:** bought link packages ("1,000 backlinks for $50" on Fiverr/etc.),
link farms, directory-spam submissions. These aren't neutral — Google can penalize a
site for them. If it's cheap and instant, it's not a real backlink strategy.

### Geotagging, specifically
Two separate things get called "geotagging":
1. **GPS metadata (EXIF) embedded in photo files** — most phone camera photos already
   carry this automatically if location services are on for the camera app; check your
   phone's camera settings. Drone footage sometimes needs it added manually with a free
   tool like GeoImgr. This is a minor, supporting signal — not something to over-invest in.
2. **Geo-keyword file naming** before upload ("hayden-id-water-heater-install.jpg"
   instead of "IMG_4021.jpg") — cheap to do, genuinely helps image search and
   reinforces location relevance when combined with alt text.

Treat geotagging as a 10-minute habit you build into your existing photo workflow, not
a separate project — it rides along with content you're already shooting.

---

## Part 2 — Social media for trades: what's actually working right now

Grounded in current industry data (sources at the bottom — treat these as directional
industry benchmarks from marketing-industry research, not peer-reviewed studies, but
they're consistent with what shows up across multiple independent sources):

- **Facebook is still the primary channel for residential/service trades** — around
  65% of plumbing/home-service companies use it as their primary marketing channel, and
  it converts inquiries better because its user base skews toward homeowners.
- **Instagram gets more engagement per post** (roughly 1.2x Facebook) for project
  photos, and is a growing discovery channel — about a third of consumers now use
  Instagram to find and vet local businesses, with TikTok close behind for younger
  homeowners.
- **Video beats static, consistently** — video posts generate roughly 80% more
  engagement than photo posts across trade categories. This plays directly to what
  you already do best (photo/video/drone) — lead with video, not photo carousels.
- **Paid social is genuinely cheap for this niche** — cost-per-lead on Facebook lead
  campaigns for contractors runs a fraction of paid search cost, which is a real
  argument for small-budget Meta ad tests once a client's organic/GBP is solid.
- **Response speed is a ranking factor of its own** for paid leads — the
  highest-performing contractor ad accounts pair video creative with fast (sub-5-minute)
  lead response. Worth telling clients: the ad only works if they answer the phone/text fast.
- **Realistic lead mix for a healthy trade business in 2026**: roughly 40% paid
  (Google/Local Service Ads), 30% organic + GBP, 20% referral/repeat, 10% other
  (social, email, SMS). Social's real job in this mix is trust-building and discovery,
  not carrying the whole funnel by itself — set that expectation with clients up front
  so a slow month on Instagram doesn't read as failure.

**For your channel-by-persona playbook (service vs. new-construction) from the nightly
board artifact — this data supports it as-is**: homeowner-facing service trades lean
Facebook + Instagram + video + fast response; new-construction/commercial leans
LinkedIn + portfolio + referral, and paid social plays a smaller supporting role there.

---

## Part 3 — UTM links & redirects, explained plainly

You're not missing anything complicated — this is a small mechanical skill.

**What a UTM link is:** normal URL + tags on the end that tell Google Analytics exactly
where a click came from. Without it, GA4 just says "social" or "direct" — with it, you
can say "that spike came from the Tuesday Instagram Reel, not the Facebook post."

**The four tags you'll actually use:**
- `utm_source` — where it was posted (`facebook`, `instagram`, `newsletter`)
- `utm_medium` — the channel type (`social`, `email`, `cpc`)
- `utm_campaign` — what this specific push is (`fall_review_push`, `spring_promo`)
- `utm_content` (optional) — lets you A/B two versions of the same post (`video` vs `photo`)

**Example, built by hand:**
```
https://clientsite.com/?utm_source=instagram&utm_medium=social&utm_campaign=fall_review_push
```

**Don't build these by hand — use the free builder:**
[Google's Campaign URL Builder](https://ga-dev-tools.google/campaign-url-builder/) —
paste the base URL, fill in the three fields, it generates the full link for you.

**Why you also need a redirect/shortener:** a raw UTM link is ugly and too long for an
Instagram bio or a text message. So you:
1. Build the full UTM link with the tool above
2. Run it through a shortener/redirect — [Bitly](https://bitly.com) (free tier is
   plenty) or, if the client's website has room, a clean redirect on their own domain
   (`clientsite.com/spring` → forwards to the full tagged link)
3. Post/share the short link — it still tracks in GA4 exactly like the long one would

**Where you check the results:** GA4 → Reports → Acquisition → Traffic acquisition,
filter or sort by Session source/medium. That's where "did the Instagram push actually
drive traffic" gets answered with a number instead of a guess.

**Practice plan on your own site:** tag every link you post about Citadel for the next
two weeks (source/medium/campaign for each platform), then check GA4 after two weeks —
that's the whole skill, repetition is what makes it automatic.

---

## Part 4 — Closing the "didn't go to school for this" gap

Free, real credentials you can add to your leave-behind and website — this solves two
problems at once (you actually learn the material, and you get a badge that's
legitimate proof for a skeptical prospect):

- **Google Skillshop** (search.google.com/skillshop) — free: Google Ads certification,
  Google Analytics (GA4) certification
- **HubSpot Academy** (academy.hubspot.com) — free: SEO certification, Social Media
  certification, Content Marketing certification
- **Moz's Beginner's Guide to SEO** (moz.com/beginners-guide-to-seo) — not a
  certification, but the single best free deep-dive if you want to go past this document

Certifications on this branch of Tier 3 (Google Ads, email) directly unlock selling
those services with real confidence instead of a guess — tie this into the Friday
"learning block" in your weekly rhythm.

---

## Part 5 — Website audit

Send the live URL and I'll audit what's checkable from the public site directly:
title tags/meta descriptions, header structure, image alt text, mobile rendering,
schema markup presence, internal linking, and obvious technical issues.

For the deepest audit (actual load-speed scores, indexing status, keyword rankings),
also pull these yourself and share the numbers — they require access I don't have to
your accounts:
- [pagespeed.web.dev](https://pagespeed.web.dev) — paste your URL, screenshot the
  Performance/SEO scores
- Google Search Console → Pages report (any pages not indexed) and Performance report
  (what you already rank for)

---

### Sources
- [Local SEO for Home Service Businesses: 2026 Complete Guide](https://hookagency.com/blog/local-seo-for-home-service-businesses/)
- [Local SEO Statistics For Home Service Contractors: 35+ Data Points For 2026](https://gridworkmarketing.com/blog/local-seo-statistics-contractors/)
- [Local SEO 2026: Real-World Ranking Factors for Contractors](https://www.fitzdesignz.com/blog/local-seo-in-action-how-2026-ranking-factors-compare-to-what-we-see-on-the-ground)
- [HVAC Social Media Marketing Stats (2026)](https://www.webtonic.io/blog/heating-ventilation-social-media-marketing-statistics)
- [31 home services marketing statistics every contractor needs to know in 2026](https://www.callrail.com/blog/home-services-marketing-statistics)
- [Home Services Marketing Statistics: Ads, SEO & Leads (2026)](https://click-vision.com/home-services-marketing-statistics)
