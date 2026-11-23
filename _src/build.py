#!/usr/bin/env python3
"""Assemble Endwave site pages from shared shell + page bodies."""
import pathlib, sys, hashlib

SRC = pathlib.Path(__file__).parent / "pages"
OUT = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else pathlib.Path(__file__).resolve().parent.parent

BILLING = "https://demo.endwaveafrica.com/login"
PPPOE = "https://demo.endwaveafrica.com/pppoe"
CAPACITY = "https://capacity.endwaveafrica.com/"
CALLC = "https://callcenter.endwaveafrica.com/admin"

def I(name, cls="i"):
    return f'<svg class="{cls}"><use href="#i-{name}"/></svg>'

SPRITE = """<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>
<symbol id="i-globe" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.6 3.8 5.6 3.8 9s-1.3 6.4-3.8 9c-2.5-2.6-3.8-5.6-3.8-9S9.5 5.6 12 3z"/></symbol>
<symbol id="i-phone" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2z"/></symbol>
<symbol id="i-head" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"><path d="M4 15v-3a8 8 0 0 1 16 0v3"/><rect x="3" y="14" width="4" height="6" rx="1.5"/><rect x="17" y="14" width="4" height="6" rx="1.5"/></symbol>
<symbol id="i-sms" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M4 5h16v11H9l-5 4z"/><path d="M8 9h8M8 12h5"/></symbol>
<symbol id="i-bill" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"><rect x="5" y="3" width="14" height="18" rx="2"/><path d="M9 8h6M9 12h6M9 16h3"/></symbol>
<symbol id="i-cart" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M3 4h2l2.4 11h10.2L20 8H6.4"/><circle cx="9" cy="19" r="1.4"/><circle cx="17" cy="19" r="1.4"/></symbol>
<symbol id="i-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></symbol>
<symbol id="i-ext" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M7 17L17 7M9 7h8v8"/></symbol>
<symbol id="i-tower" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"><circle cx="12" cy="6" r="1.6"/><path d="M8.5 3.5a5 5 0 0 0 0 5M15.5 3.5a5 5 0 0 1 0 5M12 8l-3.5 13M12 8l3.5 13M9.5 16h5"/></symbol>
<symbol id="i-build" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"><rect x="3" y="7" width="8" height="13" rx="1"/><path d="M14 20v-7l3.5-3 3.5 3v7z"/><path d="M6 11h2M6 15h2"/></symbol>
<symbol id="i-users" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"><circle cx="9" cy="8" r="3.2"/><circle cx="17" cy="9" r="2.6"/><path d="M3 20c.5-3.5 3-5.5 6-5.5s5.5 2 6 5.5M15 14.6c2.8-.2 5 1.6 5.6 4.9"/></symbol>
<symbol id="i-check" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12l5 5L20 7"/></symbol>
<symbol id="i-chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M6 9l6 6 6-6"/></symbol>
<symbol id="i-server" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"><rect x="3.5" y="4" width="17" height="7" rx="2"/><rect x="3.5" y="13" width="17" height="7" rx="2"/><path d="M7 7.5h.01M7 16.5h.01M11 7.5h6M11 16.5h6"/></symbol>
<symbol id="i-plug" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M9 3v5M15 3v5M6 8h12v3a6 6 0 0 1-12 0zM12 17v4"/></symbol>
<symbol id="i-sat" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M13 7l4 4-3 3-4-4zM10 10l-4 4M14 14l-1 1M6 14l4 4-2 2-4-4zM16 3l5 5M15 16a5 5 0 0 0 3-3M17 20a9 9 0 0 0 5-5"/></symbol>
<symbol id="i-radio" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"><circle cx="12" cy="12" r="2"/><path d="M8.2 8.2a5.4 5.4 0 0 0 0 7.6M15.8 8.2a5.4 5.4 0 0 1 0 7.6M5.4 5.4a9.3 9.3 0 0 0 0 13.2M18.6 5.4a9.3 9.3 0 0 1 0 13.2"/></symbol>
<symbol id="i-mail" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3.5 6.5l8.5 6 8.5-6"/></symbol>
<symbol id="i-pin" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21s-7-6.2-7-11.5a7 7 0 0 1 14 0C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/></symbol>
<symbol id="i-clock" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></symbol>
<symbol id="i-net" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"><circle cx="12" cy="5" r="2"/><circle cx="5" cy="18" r="2"/><circle cx="19" cy="18" r="2"/><circle cx="12" cy="13" r="2"/><path d="M12 7v4M10.5 14.3l-4 2.6M13.5 14.3l4 2.6"/></symbol>
<symbol id="i-target" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.5" fill="currentColor"/></symbol>
<symbol id="i-eye" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><path d="M2 12s3.6-7 10-7 10 7 10 7-3.6 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/></symbol>
<symbol id="i-wa" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.6.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.2-.4.7-1.4.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6a2.7 2.7 0 0 0 1.8-1.2 2.2 2.2 0 0 0 .1-1.3c0-.1-.2-.2-.5-.3z"/></symbol>
<symbol id="i-shield" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l8 3v6c0 4.5-3.4 8.2-8 9-4.6-.8-8-4.5-8-9V6z"/><path d="M8.5 12l2.5 2.5 4.5-5"/></symbol>
<symbol id="i-gauge" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"><path d="M4 17a8 8 0 1 1 16 0"/><path d="M12 17l4-5"/><circle cx="12" cy="17" r="1.3" fill="currentColor"/></symbol>
</defs></svg>"""

def nav(active):
    def on(p): return ' class="on"' if p == active else ""
    return f"""<header class="nav" id="nav"><div class="wrap">
  <a class="brand" href="index.html" aria-label="Endwave home"><img src="assets/endwave-logo-light.png" alt="Endwave NextGen Worldwide" width="202" height="34"></a>
  <ul class="menu" id="menu">
    <li><a href="index.html"{on('home')}>Home</a></li>
    <li class="dd"><button type="button" aria-expanded="false">Products {I('chev','chev')}</button>
      <div class="drop mega">
        <h6>Platforms you can log in to</h6>
        <div class="grid">
          <a class="di" href="{BILLING}" target="_blank" rel="noopener"><span class="ic" style="--c:#2980C3;background:#2980C3">{I('bill')}</span><span><b>Endwave Billing <span class="tag-live">LIVE</span></b><small>ISP billing, M-Pesa collections &amp; CRM</small></span></a>
          <a class="di" href="{CAPACITY}" target="_blank" rel="noopener"><span class="ic" style="--c:#15B0E3;background:#15B0E3">{I('gauge')}</span><span><b>Wholesale Operations <span class="tag-live">LIVE</span></b><small>Capacity orders, links &amp; utilisation</small></span></a>
          <a class="di" href="{PPPOE}" target="_blank" rel="noopener"><span class="ic" style="--c:#6F6BE8;background:#6F6BE8">{I('net')}</span><span><b>PPPoE Manager</b><small>Subscriber sessions, plans &amp; routers</small></span></a>
          <a class="di" href="{CALLC}" target="_blank" rel="noopener"><span class="ic" style="--c:#14A894;background:#14A894">{I('head')}</span><span><b>Call Centre <span class="tag-live">LIVE</span></b><small>Queues, IVR, agents &amp; recordings</small></span></a>
        </div>
        <h6>Communications &amp; commerce</h6>
        <div class="grid">
          <a class="di" href="index.html#sms"><span class="ic" style="--c:#E59A1C;background:#E59A1C">{I('sms')}</span><span><b>Bulk SMS</b><small>Sender IDs, portal &amp; REST API</small></span></a>
          <a class="di" href="index.html#voice"><span class="ic" style="--c:#1DB974;background:#1DB974">{I('phone')}</span><span><b>VoIP, MMS &amp; voice</b><small>SIP trunks, hosted PBX &amp; numbers</small></span></a>
          <a class="di" href="index.html#commerce"><span class="ic" style="--c:#E0533D;background:#E0533D">{I('cart')}</span><span><b>Integrated e-commerce</b><small>Storefronts with mobile money &amp; cards</small></span></a>
        </div>
      </div></li>
    <li class="dd"><button type="button" aria-expanded="false">Services {I('chev','chev')}</button>
      <div class="drop list">
        <a class="di" href="capacity.html"><span><b>Wholesale internet capacity</b><small>Dedicated 50 Mbps – 100 Gbps, BGP &amp; IP transit</small></span></a>
        <a class="di" href="capacity.html#delivery"><span><b>Fibre, Starlink &amp; point-to-point</b><small>Three ways to land capacity at your site</small></span></a>
        <a class="di" href="capacity.html#datacentres"><span><b>Data centres &amp; colocation</b><small>Five carrier-neutral sites in KE, UG &amp; TZ</small></span></a>
        <a class="di" href="capacity.html#pricing"><span><b>Capacity pricing</b><small>Per-Mbps rates in KES, UGX &amp; TZS</small></span></a>
        <a class="di" href="capacity.html#coverage"><span><b>Our network</b><small>Coverage, routes and AS329846</small></span></a>
      </div></li>
    <li><a href="about.html"{on('about')}>About</a></li>
    <li><a href="contact.html"{on('contact')}>Contact</a></li>
    <li class="nav-cta"><a class="btn btn-p btn-sm" href="contact.html">Talk to us</a></li>
  </ul>
  <button class="burger" id="burger" type="button" aria-label="Open menu"><span></span></button>
</div></header>"""

FOOTER = f"""<footer><div class="wrap">
  <div class="f-top">
    <div class="f-brand"><img src="assets/endwave-logo-light.png" alt="Endwave NextGen Worldwide" width="260" height="44">
      <p>Capacity, voice, call centres, bulk SMS, billing and e-commerce for operators and businesses across Kenya, Uganda and Tanzania.</p>
      <q>Six services. One network for Africa.</q></div>
    <div><h6>Platforms</h6><ul>
      <li><a class="ext" href="{BILLING}" target="_blank" rel="noopener">Endwave Billing</a></li>
      <li><a class="ext" href="{PPPOE}" target="_blank" rel="noopener">PPPoE Manager</a></li>
      <li><a class="ext" href="{CAPACITY}" target="_blank" rel="noopener">Wholesale Operations</a></li>
      <li><a class="ext" href="{CALLC}" target="_blank" rel="noopener">Call Centre</a></li></ul></div>
    <div><h6>Services</h6><ul>
      <li><a href="capacity.html">Internet capacity</a></li>
      <li><a href="index.html#voice">VoIP, MMS &amp; voice</a></li>
      <li><a href="index.html#callcentre">Call centres</a></li>
      <li><a href="index.html#sms">Bulk SMS</a></li>
      <li><a href="index.html#billing">Billing system</a></li>
      <li><a href="index.html#commerce">E-commerce</a></li></ul></div>
    <div><h6>Network</h6><ul>
      <li><a href="capacity.html#coverage">Coverage</a></li>
      <li><a href="capacity.html#datacentres">Data centres</a></li>
      <li><a href="capacity.html#pricing">Capacity pricing</a></li>
      <li><a href="about.html">About us</a></li>
      <li><a href="contact.html#faq">FAQ</a></li></ul></div>
    <div><h6>Get in touch</h6><ul>
      <li><a href="mailto:kenya@endwaveafrica.com">kenya@endwaveafrica.com</a></li>
      <li><a href="mailto:uganda@endwaveafrica.com">uganda@endwaveafrica.com</a></li>
      <li><a href="mailto:tz@endwaveafrica.com">tz@endwaveafrica.com</a></li>
      <li><a href="tel:+254799611864">+254 799 611 864</a></li>
      <li><a href="contact.html">Contact page</a></li></ul></div>
  </div>
  <div class="f-big" aria-hidden="true">ENDWAVE</div>
  <div class="f-bot"><span>© 2026 Endwave NextGen Worldwide. All rights reserved.</span><span class="mono">AS329846 · Kenya · Uganda · Tanzania</span>
    <div class="f-soc"><a href="mailto:kenya@endwaveafrica.com" aria-label="Email">{I('mail')}</a><a href="https://wa.me/254799611864" target="_blank" rel="noopener" aria-label="WhatsApp">{I('wa')}</a></div></div>
</div></footer>"""

def page(title, desc, active, body):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#040914">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="assets/endwave-logo-stacked.png">
<link rel="icon" href="assets/endwave-mark.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&amp;family=JetBrains+Mono:wght@400;500;600&amp;display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css?v={VER}">
</head>
<body data-page="{active}">
{SPRITE}
{nav(active)}
<main>
{body}
</main>
{FOOTER}
<script src="script.js?v={VER}"></script>
</body>
</html>
"""

PAGES = {
  "index.html": ("Endwave — Six services. One network for Africa.", "Wholesale internet capacity, VoIP, call centres, bulk SMS, billing and e-commerce across Kenya, Uganda and Tanzania — from one provider on one network.", "home"),
  "capacity.html": ("Wholesale Internet Capacity — Endwave", "Dedicated, uncontended capacity from 50 Mbps to 100 Gbps over fibre, Starlink or point-to-point in Kenya, Uganda and Tanzania. Per-Mbps pricing in KES, UGX and TZS.", "capacity"),
  "about.html": ("About Endwave NextGen Worldwide", "Endwave runs its own network (AS329846) and the platforms that operators and businesses across Kenya, Uganda and Tanzania build on.", "about"),
  "contact.html": ("Contact Endwave — Request capacity, a demo or a quote", "Request wholesale capacity, a billing system demo or a quote for voice, call centres, bulk SMS and e-commerce in Kenya, Uganda and Tanzania.", "contact"),
}

VER = hashlib.md5((OUT / "styles.css").read_bytes() + (OUT / "script.js").read_bytes()).hexdigest()[:8]
ctx = dict(I=I, BILLING=BILLING, PPPOE=PPPOE, CAPACITY=CAPACITY, CALLC=CALLC)
for fn, (t, d, a) in PAGES.items():
    src = (SRC / fn).read_text()
    body = eval('f"""' + src.replace('"""', '\\"\\"\\"') + '"""', ctx)
    (OUT / fn).write_text(page(t, d, a, body))
    print("built", fn, len(body))
