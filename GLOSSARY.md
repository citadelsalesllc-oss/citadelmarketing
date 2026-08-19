# Plain-English Glossary

Every term from ROADMAP.md, SEO_AND_SOCIAL_GUIDE.md, and WEBSITE_AUDIT.md, explained
without more jargon. Written 2026-08-19.

## Invisible stuff in your website's code

**Schema markup** — Your webpage handed to Google as a filled-out form instead of a
paragraph. Without it, Google has to guess which part of your text is your phone
number or your hours. Schema markup labels each piece directly in the code: "this is
the phone number," "this is the address." Invisible to a normal visitor — it only
exists for Google to read.

**LocalBusiness schema** — Not all schema is the same template. There's a generic
"Organization" form and a more specific "LocalBusiness" form built for businesses like
yours, with dedicated fields for phone, hours, and service area that the generic one
leaves out.

**Geo-coordinates** — Your exact GPS pin (latitude/longitude). Writing "Coeur d'Alene"
in a sentence tells a human where you are; putting the actual coordinates in schema
tells Google's map system precisely where, which is what powers "near me" search.

**Alt text** — A written description attached to a photo, invisible unless you look at
the code. Google can't see a picture — alt text is you describing it in words
("excavator at a job site in Hayden, ID") so Google knows what it's looking at.

**Title tag / Meta description** — The blue clickable headline and gray sentence under
it in a Google search result (and the title also shows in the browser tab). Neither is
written anywhere visible on the page itself — both live only in the code.

**Canonical tag** — A note in the code saying "this is the official version of this
page," used when the same content could technically load at more than one web address,
so Google doesn't think you have duplicate pages.

**H1 / H2 / H3 (headings)** — Like a book's chapter and section titles, in order of
importance. One H1 per page (the main title), H2s for major sections, H3s for
sub-points. Helps both readers and Google understand a page's structure at a glance.

## Being findable locally

**NAP** — Acronym for **N**ame, **A**ddress, **P**hone. These three things need to be
written *identically* everywhere your business appears online — your site, Google,
Facebook, Yelp. Small inconsistencies ("St" vs "Street") can quietly hurt your ranking.

**Backlink** — Another website linking to yours. Google treats it like a vote of
confidence — if the Chamber of Commerce links to you, that's a real business vouching
for you.

**Citation** — Your business's name/address/phone listed somewhere online (a directory
like Yelp or BBB), even without a clickable link. Reinforces that you're a real
business at a real location, separate from backlinks.

**GBP (Google Business Profile)** — The free listing on Google Maps and in the "map
pack" of three businesses shown when someone searches "plumber near me." The thing you
already know how to set up and manage.

## Tracking where visitors come from

**UTM parameters** — Small tags added to the end of a link (`?utm_source=instagram`)
so that when someone clicks it, Google Analytics can tell you exactly which post or
platform sent them, instead of just "someone showed up."

**GA4 (Google Analytics)** — Free tool tracking who visits your site, where they came
from, and what they clicked. Already installed on citadelsales.co.

**Google Search Console** — A separate free Google tool from Analytics. Shows how
Google itself sees your site: what you rank for, whether pages are indexed, and any
errors found.

**Indexed** — Means Google has found and filed your page in its library. An
un-indexed page cannot appear in search results at all, no matter how good it is.

**Sitemap.xml** — A plain list of every page on your site, handed directly to Google
so nothing gets missed.

**Robots.txt** — A small file telling search engine crawlers which parts of your site
they're allowed to look at.

**Core Web Vitals / PageSpeed** — Google's score for how fast and smooth a site feels
to load and use. A slow site ranks worse and loses visitors who give up waiting.

**FAQPage schema** — Same idea as LocalBusiness schema, but the template for FAQ
content. Tells Google "these are questions and answers," which can make them appear as
an expandable dropdown directly inside your search result.
