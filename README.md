# Darul Ahbaab — Website Deploy Package

Everything here is ready to drop onto a static host. Put all these files together in
one folder (the site "root").

## Files
- **index.html** — the whole site (now ~91KB, down from 195KB — logo is defined once and reused)
- **og-image.jpg** — the 1200×630 preview image shown when the link is shared (WhatsApp, iMessage, etc.)
- **robots.txt** — tells Google it can index the site
- **sitemap.xml** — lists the page for Google
- **_headers** — security headers (works on Cloudflare Pages AND Netlify)
- **_redirects** — placeholder for future redirect rules (HTTPS is automatic)

## ⚠️ Before you go live: replace the placeholder domain
I used `https://darulahbaab.com/` as a placeholder. After you register your real
domain, find-and-replace `darulahbaab.com` with your actual domain in these files:
- index.html  (the og:url, canonical, twitter:image, structured data)
- robots.txt  (the Sitemap: line)
- sitemap.xml (the <loc> line)

## Deploy in 4 steps (Cloudflare Pages — recommended)
1. Put this folder on GitHub (git init, commit, push).
2. Go to Cloudflare Pages → "Connect to Git" → pick the repo → Deploy.
   (Build command: none. Output directory: /  — it's plain HTML.)
3. Cloudflare gives you a free HTTPS URL immediately (yourname.pages.dev).
4. Add your custom domain under the project's "Custom domains" tab.

Netlify works identically, or you can drag this folder onto app.netlify.com/drop.

## After launch
- Add the site to **Google Search Console** and submit sitemap.xml (speeds up showing in Google).
- Consider a professional email (info@yourdomain) — Zoho Mail has a free tier.
- The contact form opens the visitor's email app pointed at Axbaabta1@gmail.com — watch that inbox.

## Still worth doing later (optional)
- Replace the traced logo with the ORIGINAL vector file if the designer has one (sharpest possible).
- Wire the contact form to Formspree/Getform for real submissions instead of mailto.
