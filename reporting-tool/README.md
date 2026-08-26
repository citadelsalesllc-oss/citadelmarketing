# Monthly Performance Report Generator

Generates a clean, single-page PDF performance report per client, pulling
website data from **Google Analytics 4** and ad data from **Meta Ads
Manager**. Add a new client by dropping in one config file — no code changes
needed.

Each report includes:
- Key metrics (sessions, users, conversions, engagement rate, Meta spend,
  reach, clicks, cost per result), each with a month-over-month comparison
- Top traffic sources (source/medium) and top pages from GA4
- 2–3 plain-language takeaways explaining what the numbers mean for the
  client's business — not just the raw figures
- Your brand color and logo on every report

---

## Part 0: What you need before starting

- Python 3.9 or newer installed (`python3 --version` to check)
- Admin (or at least "Viewer") access to each client's GA4 property
- Admin access to each client's Meta Business/Ads account
- About 20–30 minutes for the one-time credential setup below. You only do
  this once per client's GA4 property; the Meta credentials are shared
  across all clients if you manage their ads from one Meta Business account
  (or once per ad account if they're separate).

---

## Part 1: Install the tool

```bash
cd reporting-tool
python3 -m venv .venv
source .venv/bin/activate        # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
```

You'll fill in `.env` in Parts 2 and 3 below.

---

## Part 2: Get GA4 API access (Google Analytics Data API)

GA4 doesn't let you pull data with just a username/password — you need a
**service account**, which is a special Google account for programs (not
people) to use.

1. **Create a Google Cloud project**
   - Go to https://console.cloud.google.com/
   - Click the project dropdown (top left) → **New Project**
   - Name it something like `citadel-reporting` → **Create**

2. **Enable the GA4 Data API**
   - With your new project selected, go to
     https://console.cloud.google.com/apis/library/analyticsdata.googleapis.com
   - Click **Enable**

3. **Create a service account**
   - Go to https://console.cloud.google.com/iam-admin/serviceaccounts
   - Click **Create Service Account**
   - Name it `ga4-reporting` → **Create and Continue** → skip the optional
     role/access steps → **Done**

4. **Create a key for the service account**
   - Click the service account you just created
   - Go to the **Keys** tab → **Add Key** → **Create new key** → choose
     **JSON** → **Create**
   - A `.json` file downloads automatically — this is your credential file.
     Move it into `reporting-tool/credentials/ga4_service_account.json`.
   - Treat this file like a password. Never commit it to git or share it.

5. **Copy the service account's email address**
   - It looks like `ga4-reporting@citadel-reporting.iam.gserviceaccount.com`
   - It's visible on the service account's details page.

6. **Give the service account access to each client's GA4 property**
   - Log into https://analytics.google.com as an admin of the client's account
   - **Admin** (bottom left gear icon) → under the **Property** column →
     **Property Access Management**
   - Click **+** → **Add users**
   - Paste the service account email, set role to **Viewer**, click **Add**
   - Repeat for every client property you want to report on.

7. **Get the GA4 Property ID for each client**
   - Still in **Admin** → **Property Settings** (under the Property column)
   - Copy the **Property ID** — it's just a number, e.g. `123456789` (not
     the "Measurement ID" that starts with `G-`)

8. **Update `.env`**
   ```
   GA4_SERVICE_ACCOUNT_JSON=./credentials/ga4_service_account.json
   ```

You'll enter each client's Property ID in their own config file in Part 4 —
you don't need a new service account or key per client, just Viewer access
granted per property.

---

## Part 3: Get Meta Marketing API access

1. **Create a Meta developer account**
   - Go to https://developers.facebook.com/ and log in with the Facebook
     account tied to your ad accounts (or one added as admin to them)
   - Accept the developer terms if prompted

2. **Create an app**
   - Go to https://developers.facebook.com/apps/ → **Create App**
   - Choose **Other** → **Business** as the app type
   - Name it `Citadel Reporting` → **Create App**

3. **Add the Marketing API product**
   - In your new app's dashboard, find **Marketing API** in the product
     list → **Set Up**

4. **Get a System User access token (recommended — doesn't expire)**
   - Go to https://business.facebook.com/settings/system-users (Business
     Settings → Users → System Users)
   - Click **Add** → name it `reporting-bot` → role **Admin** → **Create System User**
   - Click **Add Assets** → select **Apps** → choose the app you created in
     step 2 → give it **Full Control**
   - Click **Add Assets** again → select **Ad Accounts** → check each
     client ad account you want to report on → give **View Performance** access
     (or Advertiser if that's not enough)
   - Click **Generate New Token**
     - Select the app you created
     - Under permissions, check **ads_read**
     - Click **Generate Token**
   - Copy the token immediately — it's shown only once. Paste it somewhere
     safe temporarily.

   > A regular personal access token (from Graph API Explorer) expires in
   > about 60 days. A System User token from a Business Manager doesn't
   > expire unless you revoke it, so it's the better choice for a recurring
   > report you'll run monthly.

5. **Get your App ID and App Secret**
   - In your app dashboard → **Settings** → **Basic**
   - Copy the **App ID** and **App Secret** (click "Show" for the secret)

6. **Get each client's Ad Account ID**
   - Go to https://adsmanager.facebook.com/ for that client's account
   - The Ad Account ID is shown near the account name/top of the page,
     formatted like `123456789012345` — the tool expects it prefixed with
     `act_`, e.g. `act_123456789012345`

7. **Update `.env`**
   ```
   META_ACCESS_TOKEN=paste-your-system-user-token-here
   META_APP_ID=paste-your-app-id-here
   META_APP_SECRET=paste-your-app-secret-here
   ```

---

## Part 4: Add a client

1. Copy the example config:
   ```bash
   cp config/clients.example.json config/clients/acme_dental.json
   ```
   Use a short, filesystem-safe name for the file (no spaces) — this is
   the `--client` value you'll pass on the command line.

2. Edit `config/clients/acme_dental.json`:
   ```json
   {
     "client_name": "Acme Dental",
     "ga4_property_id": "123456789",
     "meta_ad_account_id": "act_1234567890",
     "meta_result_action_type": "lead",
     "brand": {
       "primary_color": "#0B5FFF",
       "secondary_color": "#1A1A2E",
       "logo_path": "assets/logos/acme_dental.png"
     }
   }
   ```
   - `ga4_property_id`: from Part 2, step 7
   - `meta_ad_account_id`: from Part 3, step 6 (include the `act_` prefix)
   - `meta_result_action_type`: which Meta "result" to report cost-per-result
     on. Common values: `lead` (lead ads/forms), `purchase`, `onsite_conversion.messaging_conversation_started_7d`
     (Messenger), or `link_click`. Check what the client's campaigns are
     actually optimizing for in Ads Manager if unsure.
   - `primary_color` / `secondary_color`: the client's brand hex colors
   - `logo_path`: path to a PNG or JPG logo file, relative to
     `reporting-tool/`. Drop the logo file in `assets/logos/`. If omitted or
     the file doesn't exist, the report just skips the logo.

3. Repeat for each client — each gets its own file in `config/clients/`.

---

## Part 5: Generate a report

```bash
python main.py --client acme_dental --start 2026-07-01 --end 2026-07-31
```

This automatically compares against the previous same-length period (in
this example, June 1–30) and writes the PDF to:

```
output/acme_dental_2026-07-01_to_2026-07-31.pdf
```

Use `--output path/to/file.pdf` to control where it's saved instead.

To run it for every client at month-end, repeat the command with each
client's config name and the same date range.

---

## Troubleshooting

- **`PERMISSION_DENIED` from GA4`** — the service account email hasn't been
  added to that GA4 property (Part 2, step 6), or was added to the wrong
  property.
- **`Invalid OAuth access token` from Meta** — the token expired (if you
  used a personal token instead of a System User token) or was typed/pasted
  incorrectly. Regenerate it per Part 3, step 4.
- **`(#100) Object does not exist` from Meta** — the ad account ID is
  wrong, or the System User wasn't granted access to that specific ad
  account (Part 3, step 4).
- **Logo doesn't appear on the report** — check `logo_path` in the client's
  config is correct and relative to the `reporting-tool/` folder, and that
  the file is a `.png` or `.jpg`.
- **Numbers look like zero everywhere** — double check the `--start`/`--end`
  dates actually had traffic/ad activity, and that the GA4 property or ad
  account ID belongs to the right client.

---

## Security notes

- `.env`, everything in `credentials/`, and everything in `config/clients/`
  (except the `.example.json`) are git-ignored by default — don't remove
  those `.gitignore` entries, since they hold live credentials and client IDs.
- Never paste your Meta access token or the GA4 service account JSON into
  chat, email, or a shared doc. Store them only in this local `.env` /
  `credentials/` setup.
- If a token or key is ever exposed, revoke/regenerate it immediately (Meta:
  Business Settings → System Users → regenerate token; Google: delete the
  key on the service account and create a new one).
