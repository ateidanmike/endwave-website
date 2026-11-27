# Endwave — Six services. One network for Africa.

Website for **Endwave NextGen Worldwide**: wholesale internet capacity, VoIP & voice, call centres, bulk SMS, billing and integrated e-commerce across Kenya, Uganda and Tanzania.

Live preview: https://ateidanmike.github.io/endwave-website/

## Pages

| File | Page |
|---|---|
| `index.html` | Home: platforms, network, services |
| `capacity.html` | Wholesale capacity: delivery, coverage, data centres, pricing calculator |
| `about.html` | About Endwave |
| `contact.html` | Service request, billing demo request, FAQ |
| `sms.html`, `voice.html`, `callcentre.html`, `ecommerce.html` | Product pages (content in `_src/products.py`) |
| `privacy.html`, `terms.html` | Privacy policy and terms of use |

Shared files: `styles.css`, `script.js`, `assets/`.

## Internal tools

| Path | Tool |
|---|---|
| `tools/content-studio/` | Content studio: 11 social post templates (service spotlight, promo, tip carousel, go-live, network notice, event, coverage, testimonial, milestone, hiring, holiday) in four sizes with captions, plus an email signature generator and an A4 capacity quote. PDF and .zip downloads load jsPDF and JSZip from cdnjs. |
| `tools/partnership-generator/` | Partnership announcement generator: square, portrait, story and LinkedIn/X posts as PNG, plus platform captions. Self-contained and works offline. Not linked from the site and marked `noindex`. |

## Platform links

- Billing: https://demo.endwaveafrica.com/login
- PPPoE: https://demo.endwaveafrica.com/pppoe
- Wholesale Operations: https://capacity.endwaveafrica.com/
- Call Centre: https://callcenter.endwaveafrica.com/admin

## Run locally

```bash
python3 -m http.server 8000
```

---

Built by [Atei DevOps](https://ateidevops.co.ke).

## Editing pages

Page bodies live in `_src/pages/`; the shared nav, footer and icons are in `_src/build.py`. After editing, run `python3 _src/build.py` to regenerate the HTML.
