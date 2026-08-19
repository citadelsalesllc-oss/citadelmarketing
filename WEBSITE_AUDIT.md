# Website Audit — citadelsales.co

Audited 2026-08-19 from the live page source (Durable-built Next.js site). Snapshot in
time — re-audit after making changes, since Durable may push platform-level updates
independently.

## What's already right
- Unique, descriptive `<title>` and meta description on every page (Home, About,
  Services, Contact) — no duplicate titles.
- Single clear `<h1>` on the homepage ("Your Work Is Built to Last. Now Build a
  Presence That Does Too."), followed by correctly nested H2s and H3s.
- Full Open Graph + Twitter Card tags filled in — link previews will render properly.
- Canonical tag present and correct.
- GA4 installed and firing (`G-DDQ7EREBFF`).
- Real named team bios (Logan Romero, Morgan Boring) — genuine trust/credibility signal.
- Honest "new agency, real numbers" framing instead of fabricated testimonials —
  matches the brand voice and is the right call this early.
- Mobile nav, social links (Facebook, Instagram) present and correctly linked.

## Fix now (quick, high value)
1. **Footer contact info isn't clickable.** "208-660-4438 - citadelsalesllc@gmail.com"
   in the footer is plain text — no `tel:`/`mailto:` href. Costs a tap-to-call on
   mobile, where most local search traffic lives.
2. **Legal footer links are placeholders.** Privacy Policy, Terms of Service, and
   Cookie Policy all point to `/` instead of real pages. Build three short real pages
   or remove the links until you do — dead links read as unfinished.
3. **Calendly booking link isn't UTM-tagged anywhere.** Same untagged URL on every
   button (homepage, presumably Instagram bio, texts). Tag each placement per the UTM
   guide (`utm_source=instagram&utm_medium=social`, `utm_source=sms&utm_medium=text`,
   etc.) so GA4 can actually attribute which channel books calls.

## Real SEO gaps
4. **Schema is generic `Organization`, not `LocalBusiness`.** Missing telephone,
   geo-coordinates, opening hours, service area — the fields Google's local pack
   actually reads. The head-injected Durable schema block is also oddly populated with
   AI-agent-discovery fields (llms.txt, agents.md, openapi.json) rather than real local
   business data.
5. **No `FAQPage` structured data**, despite a full, well-written FAQ section on every
   page. Cheap to add, can earn expandable rich snippets in search results.
6. **Only one generic `/services` page — no per-service or per-city pages.** The #1
   on-page lever from SEO_AND_SOCIAL_GUIDE.md is unbuilt on your own site. Build 2-3
   pages (e.g. "Google Business Profile Management — Coeur d'Alene," "Social Media for
   Trades — North Idaho") — doubles as SEO and as a portfolio page to show prospects.
7. **Hero image is a desk/monitor photo, not a job site.** A visiting plumber or
   excavator owner should see themselves in the hero immediately. Swap in one of the
   job-site/excavator shots already in the carousel.

## Verify yourself (needs account access I don't have)
- [pagespeed.web.dev](https://pagespeed.web.dev) — the page ships a large amount of
  inline CSS (Durable platform trait); check the real mobile Performance score.
- Google Search Console — confirm sitemap submitted and pages indexed (couldn't reach
  robots.txt/sitemap.xml directly to verify from here).
