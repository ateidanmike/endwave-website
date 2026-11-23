"""Product page content + template. Rendered by build.py."""

CALLC = "https://callcenter.endwaveafrica.com/admin"

def I(name, cls="i"):
    return f'<svg class="{cls}"><use href="#i-{name}"/></svg>'

ARROW = I("arrow")

PRODUCTS = {
# ------------------------------------------------------------------ SMS
"sms": dict(
  file="sms.html", name="Bulk SMS", icon="sms", color="#E59A1C", svc="sms",
  title="Bulk SMS — Endwave",
  desc="Bulk SMS for Kenya, Uganda and Tanzania: registered sender IDs, a web portal, scheduling, delivery reports and a REST API for reminders, OTPs and alerts.",
  eyebrow="Bulk SMS",
  h1='One API for every message you <span class="grad-t">send customers.</span>',
  lead="Send payment reminders, one-time passwords, alerts and campaigns under your own brand name, from a web portal or straight from your systems through our API, across Kenya, Uganda and Tanzania.",
  cta2=("Talk to sales", "https://wa.me/254799611864"),
  chips=["Registered sender IDs", "Web portal & REST API", "Delivery reports", "KE, UG &amp; TZ"],
  mock=f'''<div class="win"><div class="win-b"><i></i><i></i><i></i><span>api · bulk sms</span></div><div class="win-c">
<div class="tabs-mini"><span class="on">SMS</span><span>OTP</span><span>Alerts</span><span>Campaigns</span></div>
<div class="code"><span class="k">POST</span> /v1/sms
{{ <span class="s">"from"</span>: "ENDWAVE",
  <span class="s">"to"</span>: ["+2547•••••864", "+2567•••••112"],
  <span class="s">"text"</span>: "Hi Amina, your invoice is due",
  <span class="s">"schedule"</span>: "2026-12-01T08:00" }}
<span class="c">→ 202 accepted · 2 queued</span></div>
<div class="rows" style="margin-top:12px">
<div class="row"><span class="m">+2547•••864</span>Invoice reminder<span class="r b-ok">DELIVERED</span></div>
<div class="row"><span class="m">+2567•••112</span>Invoice reminder<span class="r b-blue">SENT</span></div></div></div></div>''',
  feat_h="Everything you need to message customers at scale.",
  features=[
    ("Branded sender IDs", "Send under your business name. We handle sender ID registration with the mobile networks in each country."),
    ("Web portal", "Upload contacts, write once, personalise with names and amounts, and send or schedule campaigns from the browser."),
    ("REST API", "Send from your own apps, billing or CRM with a simple HTTP API, for OTPs, receipts and alerts."),
    ("Scheduling", "Queue messages for the right moment, like reminders the day before an invoice falls due."),
    ("Contact groups", "Organise customers into groups and lists so every campaign reaches the right people."),
    ("Delivery reports", "See what was delivered, what failed and why, per message and per campaign."),
  ],
  uses=[
    ("ISPs & billing", "Payment reminders, receipts and service notices sent automatically from Endwave Billing."),
    ("Banks, SACCOs & fintechs", "One-time passwords, transaction alerts and statements."),
    ("Retail & e-commerce", "Order confirmations, delivery updates and promotions."),
    ("Schools & institutions", "Fee reminders, announcements and emergency notices to parents and members."),
    ("Healthcare", "Appointment reminders and follow-ups that cut no-shows."),
    ("Events & campaigns", "Invitations, reminders and last-minute changes to thousands of people at once."),
  ],
  steps=[("Tell us your sender name", "Share the name you want to send under and your expected volume."),
         ("We register it", "We submit the sender ID to the mobile networks and set up your account."),
         ("Start sending", "Use the web portal or connect your systems through the API."),
         ("Track every message", "Delivery reports and usage, per message and per campaign.")],
  pricing_intro="Bulk SMS is billed per message. The rate per SMS drops as your monthly volume grows, and is quoted per country in local currency.",
  plans=[
    ("Pay as you go", "For small and occasional senders", "Per SMS", ["Web portal access", "Registered sender ID", "Delivery reports"]),
    ("Volume", "For businesses sending every month", "Per SMS, lower rate", ["Everything in Pay as you go", "REST API access", "Scheduling & contact groups"]),
    ("Enterprise", "For high-volume and critical traffic", "Custom rate", ["Everything in Volume", "Priority routing for OTPs", "Dedicated account manager"]),
  ],
  faq=[
    ("How long does sender ID registration take?", "It depends on the network and country. We submit as soon as you share your sender name and supporting documents, and keep you updated until it is approved."),
    ("Can I send to Uganda and Tanzania from one account?", "Yes. One Endwave account can send to numbers in Kenya, Uganda and Tanzania, with rates quoted per country."),
    ("Do you have an API?", "Yes. A REST API lets your apps, billing system or CRM send messages, schedule them and read delivery reports."),
    ("Does it work with Endwave Billing?", "Yes. Endwave Billing uses our SMS to send payment reminders, receipts and notices to your subscribers automatically."),
    ("Can I see which messages were delivered?", "Every message has a delivery status, and campaign reports show delivered, pending and failed messages."),
  ],
  related=["voice", "callcentre", "ecommerce"],
),
# ------------------------------------------------------------------ VOICE
"voice": dict(
  file="voice.html", name="VoIP, MMS & voice", icon="phone", color="#1DB974", svc="voice",
  title="VoIP, SIP Trunks & Hosted PBX — Endwave",
  desc="Business voice on the Endwave network: SIP trunks, hosted PBX, local numbers and number porting in Kenya, Uganda and Tanzania, with HD voice, voicemail and MMS.",
  eyebrow="VoIP, MMS & voice",
  h1='Business voice on <span class="grad-t">your own network.</span>',
  lead="Replace legacy lines with SIP trunks and a hosted PBX, keep your existing numbers and add local numbers in Kenya, Uganda and Tanzania, all carried on the same network as your internet.",
  cta2=("Talk to sales", "https://wa.me/254799611864"),
  chips=["SIP trunks", "Hosted PBX", "Number porting", "Local numbers in KE, UG &amp; TZ"],
  mock='''<div class="win"><div class="win-b"><i></i><i></i><i></i><span>hosted pbx · extensions</span></div><div class="win-c">
<div class="kpis"><div class="kpi"><small>Extensions</small><b>48</b></div><div class="kpi"><small>Live calls</small><b>7<em>●</em></b></div><div class="kpi"><small>Numbers</small><b>3</b></div></div>
<div class="rows" style="margin-top:12px">
<div class="row"><span class="m">+254 20 •••• 100</span>Main line → IVR<span class="r b-ok">ACTIVE</span></div>
<div class="row"><span class="m">ext 201</span>Reception<span class="r b-blue">ON CALL</span></div>
<div class="row"><span class="m">ext 305</span>Accounts<span class="r b-ok">AVAILABLE</span></div>
<div class="row"><span class="m">+256 41 •••• 220</span>Kampala office<span class="r b-ok">ACTIVE</span></div></div></div></div>''',
  feat_h="Everything a business phone system should do.",
  features=[
    ("SIP trunks", "Connect any IP-PBX to the public phone network with SIP channels sized to your call volume."),
    ("Hosted PBX", "Extensions, ring groups, call transfer and an auto-attendant without a box in your server room."),
    ("Local numbers", "Numbers in Kenya, Uganda and Tanzania, so customers in each market can call you locally."),
    ("Number porting", "In most cases you keep your existing numbers. We handle the porting with your current provider."),
    ("HD voice & voicemail", "Clear wideband calls and voicemail delivered to email, on desk phones, softphones and mobile apps."),
    ("MMS messaging", "Send picture and media messages alongside voice, from the same account."),
  ],
  uses=[
    ("Multi-branch businesses", "Free calls between offices and one number plan across every branch."),
    ("Banks, SACCOs & insurers", "Reliable inbound lines for customer service and branch calls."),
    ("Hotels & hospitality", "Room, reception and reservations lines on one hosted system."),
    ("Hospitals & clinics", "Departments, after-hours routing and voicemail for patient calls."),
    ("ISPs & carriers", "Resell voice to your own subscribers over SIP trunks."),
    ("Remote & hybrid teams", "Extensions that follow staff to laptops and mobiles."),
  ],
  steps=[("Tell us your setup", "How many people answer phones, your locations and the numbers you use today."),
         ("Design & quotation", "We size the trunks or PBX, plan the call flow and send one quotation."),
         ("Port & configure", "We port your numbers, set up extensions and test call quality."),
         ("Go live", "Switch over with minimal downtime, with our support team on hand.")],
  pricing_intro="Voice is quoted on what you use: SIP channels or PBX extensions, the numbers you hold and the calls you make. Quotes are in local currency.",
  plans=[
    ("SIP trunks", "For businesses with their own IP-PBX", "Per channel", ["Concurrent call channels", "Local DIDs", "Per-minute call rates"]),
    ("Hosted PBX", "For teams that want no hardware", "Per extension", ["Extensions & ring groups", "Auto-attendant & voicemail", "Softphone & mobile apps"]),
    ("Numbers", "For a local presence in each market", "Per number", ["Kenya, Uganda & Tanzania", "Porting of existing numbers", "Inbound routing to any extension"]),
  ],
  faq=[
    ("Can I keep my existing phone numbers?", "In most cases, yes. We port existing numbers onto our SIP trunks or hosted PBX and can add new local numbers in Kenya, Uganda and Tanzania."),
    ("Do I need new phones?", "Not necessarily. Most SIP desk phones work with our service, and staff can also use softphones on laptops or mobile apps."),
    ("What internet do I need for VoIP?", "A stable connection with enough capacity for your concurrent calls. Running voice over Endwave capacity keeps calls on one network end to end."),
    ("Can I connect my existing PBX?", "Yes. SIP trunks connect to most IP-PBX systems, so you keep your current setup and replace only the lines."),
    ("Does it work with the call centre?", "Yes. The Endwave Call Centre runs on the same voice platform, so numbers and queues work together."),
  ],
  related=["callcentre", "sms", "ecommerce"],
),
# ------------------------------------------------------------------ CALL CENTRE
"callcentre": dict(
  file="callcentre.html", name="Call Centre", icon="head", color="#14A894", svc="callcentre",
  title="Cloud Call Centre — Endwave",
  desc="A full contact centre in a browser tab: IVR, inbound and outbound queues, call recording and live supervisor dashboards. Seats and headsets set up on site in Kenya, Uganda and Tanzania.",
  eyebrow="Call Centre",
  h1='A full contact centre <span class="grad-t">in a browser tab.</span>',
  lead="IVR menus, inbound and outbound queues, call recording and live supervisor dashboards. Agents log in from a browser, and you can scale from five seats to five hundred.",
  cta2=("Open the call centre", CALLC),
  chips=["IVR & queues", "Call recording", "Live dashboards", "5 to 500 agents"],
  mock='''<div class="win"><div class="win-b"><i></i><i></i><i></i><span>callcenter.endwaveafrica.com</span></div><div class="win-c">
<div class="kpis"><div class="kpi"><small>In queue</small><b id="cq">2</b></div><div class="kpi"><small>Avg wait</small><b id="cw">0:18</b></div><div class="kpi"><small>Answered</small><b>412</b></div></div>
<div class="rows" style="margin-top:12px">
<div class="row"><span class="agent"><span class="av" style="--c:#14A894">W</span>Wanjiru K.</span><span class="m">Sales</span><span class="r b-ok">ON CALL</span></div>
<div class="row"><span class="agent"><span class="av" style="--c:#2980C3">B</span>Brian O.</span><span class="m">Support</span><span class="r b-blue">AVAILABLE</span></div>
<div class="row"><span class="agent"><span class="av" style="--c:#E59A1C">A</span>Aisha N.</span><span class="m">Billing</span><span class="r b-due">WRAP-UP</span></div></div></div></div>''',
  feat_h="Built for teams that answer customers all day.",
  features=[
    ("IVR menus", "Greet callers and route them to the right team with press-1 menus, business hours and holiday rules."),
    ("Inbound & outbound queues", "Fair call distribution across agents, plus outbound campaigns and callbacks."),
    ("Call recording", "Record calls for quality, training and dispute resolution, searchable by agent and date."),
    ("Live supervisor dashboards", "See queues, waiting times and agent status in real time, and listen in when needed."),
    ("Browser-based agents", "Agents work from a browser tab with a headset. No desk phones or local servers required."),
    ("Reports", "Answered, missed and abandoned calls, handling times and agent performance over any period."),
  ],
  uses=[
    ("Customer support", "Help desks for ISPs, utilities and subscription businesses."),
    ("Sales & telemarketing", "Outbound campaigns with call lists and callbacks."),
    ("Banks, SACCOs & insurers", "Member and policyholder service lines with recording."),
    ("BPOs & outsourcers", "Multi-client operations with separate queues and reports."),
    ("Hospitals & clinics", "Appointment booking and patient enquiry lines."),
    ("Government & NGOs", "Hotlines and public information lines."),
  ],
  steps=[("Tell us your team", "Number of agents, queues, hours and the numbers customers call."),
         ("Design the call flow", "We map the IVR, queues and routing, then send one quotation."),
         ("Set up on site", "We configure the platform and, if you need them, supply seats and headsets."),
         ("Go live & support", "Agents trained, calls flowing, and our team on hand as you grow.")],
  pricing_intro="The call centre is priced per agent seat each month, with numbers and call minutes on top. Setup and any equipment are quoted once.",
  plans=[
    ("Per agent seat", "Monthly, for each agent who logs in", "Per seat", ["Browser-based agent desk", "Queues & IVR", "Call recording"]),
    ("Numbers & minutes", "The lines customers call", "Usage-based", ["Local numbers in KE, UG &amp; TZ", "Toll and per-minute rates", "Number porting"]),
    ("Setup & equipment", "One-off, if you need it", "Quoted once", ["Call flow design", "Headsets & seats on site", "Agent & supervisor training"]),
  ],
  faq=[
    ("Do agents need special phones?", "No. Agents use a browser and a headset. We can supply headsets and set up seats on site if you need them."),
    ("Can I start small?", "Yes. Start with a handful of agents and add seats as your team grows, up to hundreds of agents."),
    ("Are calls recorded?", "Call recording is included and can be switched on per queue, for quality and training."),
    ("Can supervisors see what's happening live?", "Yes. Live dashboards show queues, waiting times and each agent's status, and supervisors can listen in."),
    ("Can I keep my existing customer line?", "In most cases, yes. We port your existing numbers so customers keep calling the number they know."),
  ],
  related=["voice", "sms", "ecommerce"],
  platform=CALLC,
),
# ------------------------------------------------------------------ E-COMMERCE
"ecommerce": dict(
  file="ecommerce.html", name="Integrated e-commerce", icon="cart", color="#E0533D", svc="commerce",
  title="Integrated E-commerce — Endwave",
  desc="Online stores with M-Pesa, Airtel Money and card checkout, inventory and order tracking, and SMS order updates, connected to Endwave billing.",
  eyebrow="Integrated e-commerce",
  h1='Sell online, get paid, <span class="grad-t">deliver.</span>',
  lead="An online store on your own domain with mobile money and card checkout, stock and order tracking, and SMS updates to customers at every step, connected to Endwave billing and messaging.",
  cta2=("Talk to sales", "https://wa.me/254799611864"),
  chips=["Your own domain", "M-Pesa, Airtel Money & cards", "Inventory & orders", "SMS order updates"],
  mock='''<div class="win"><div class="win-b"><i></i><i></i><i></i><span>shop.yourbrand.co.ke · orders</span></div><div class="win-c">
<div class="kpis"><div class="kpi"><small>Orders today</small><b>38</b></div><div class="kpi"><small>Revenue</small><b>KES 186K</b></div><div class="kpi"><small>Low stock</small><b>4</b></div></div>
<div class="rows" style="margin-top:12px">
<div class="row"><span class="m">#1042</span>KES 4,500 · M-Pesa<span class="r b-ok">PAID</span></div>
<div class="row"><span class="m">#1041</span>KES 12,900 · Visa<span class="r b-blue">DISPATCHED</span></div>
<div class="row"><span class="m">#1040</span>KES 2,150 · Airtel<span class="r b-ok">DELIVERED</span></div></div></div></div>''',
  feat_h="A store that runs itself between orders.",
  features=[
    ("Storefront on your domain", "A fast, mobile-first shop under your own brand and web address."),
    ("Mobile money & cards", "Checkout with M-Pesa, Airtel Money, Visa, Mastercard and American Express."),
    ("Inventory", "Track stock across products and variants, with alerts before you run out."),
    ("Order tracking", "Every order from payment to dispatch to delivery, in one dashboard."),
    ("SMS order updates", "Customers get confirmations and delivery updates by SMS automatically."),
    ("Connected to billing", "Sales, invoices and receipts flow into Endwave billing and reports."),
  ],
  uses=[
    ("Retailers & wholesalers", "Take orders online alongside your physical shop."),
    ("Brands & manufacturers", "Sell direct to customers across Kenya, Uganda and Tanzania."),
    ("ISPs", "Sell routers, packages and top-ups online to your subscribers."),
    ("Restaurants & groceries", "Orders and deliveries with mobile-money checkout."),
    ("Schools & institutions", "Uniforms, fees and event tickets paid online."),
    ("Event organisers", "Tickets with instant SMS confirmation."),
  ],
  steps=[("Tell us what you sell", "Products, payment methods and how you deliver."),
         ("We build the store", "Design, products, payments and SMS updates set up on your domain."),
         ("Test & launch", "Test orders end to end, then open to customers."),
         ("Grow", "Reports, promotions and support as orders increase.")],
  pricing_intro="E-commerce is a one-off setup to build your store, then a monthly fee to host and run it. Payment provider charges apply as set by each provider.",
  plans=[
    ("Store setup", "One-off", "Quoted once", ["Design on your domain", "Products & categories loaded", "Payments & SMS connected"]),
    ("Monthly", "Hosting, updates & support", "Per month", ["Hosting & security updates", "Order & inventory dashboard", "Support from our team"]),
    ("Add-ons", "As you grow", "Per add-on", ["Bulk SMS campaigns", "Call centre for orders", "Custom features"]),
  ],
  faq=[
    ("Which payment methods can customers use?", "M-Pesa, Airtel Money and cards (Visa, Mastercard and American Express), subject to approval by each payment provider."),
    ("Can I use my own domain?", "Yes. The store runs on your own domain. If you don't have one yet, we can help you register it."),
    ("Do customers get order updates?", "Yes. Confirmations and delivery updates go out by SMS automatically through Endwave Bulk SMS."),
    ("Can I manage stock myself?", "Yes. Add products, change prices and update stock from the dashboard at any time."),
    ("Can I sell in Uganda and Tanzania?", "Yes, with payment options and pricing set up for each market you sell in."),
  ],
  related=["sms", "callcentre", "voice"],
),
}

ORDER = ["sms", "voice", "callcentre", "ecommerce"]


def faq_html(items):
    return '<div class="qa">' + "".join(
        f'<div class="q{"" if i else " open"}"><button type="button" aria-expanded="{"false" if i else "true"}"><small>{i+1:02d}</small><span>{q}</span><i></i></button><div class="a"><div><p>{a}</p></div></div></div>'
        for i, (q, a) in enumerate(items)) + "</div>"


def render(key):
    p = PRODUCTS[key]
    c = p["color"]
    ext = ' target="_blank" rel="noopener"' if p["cta2"][1].startswith("http") else ""
    chips = "".join(f'<span class="chip"><i class="dot" style="background:{c}"></i>{t}</span>' for t in p["chips"])
    feats = "".join(f'<div class="ad reveal"><small>{i+1:02d}</small><h4>{h}</h4><p>{t}</p></div>' for i, (h, t) in enumerate(p["features"]))
    uses = "".join(f'<div class="au"><small>{i+1:02d}</small><h4>{h}</h4><p>{t}</p></div>' for i, (h, t) in enumerate(p["uses"]))
    steps = "".join(f'<div class="step reveal"><small>{i+1:02d}</small><h4>{h}</h4><p>{t}</p></div>' for i, (h, t) in enumerate(p["steps"]))
    plans = "".join(
        f'<div class="plan reveal"><small>{n}</small><p>{sub}</p><b>{unit}</b><ul class="ticks1">'
        + "".join(f"<li>{I('check')}{x}</li>" for x in inc)
        + f'</ul><a class="btn btn-o btn-sm" href="contact.html?svc={p["svc"]}">Get pricing {ARROW}</a></div>'
        for n, sub, unit, inc in p["plans"])
    rel = "".join(
        f'<a class="relc reveal" href="{PRODUCTS[r]["file"]}" style="--c:{PRODUCTS[r]["color"]}"><span class="ic">{I(PRODUCTS[r]["icon"])}</span><b>{PRODUCTS[r]["name"].replace("&", "&amp;")}</b><p>{PRODUCTS[r]["desc"].split(":")[0].split(".")[0]}.</p><span class="link">Explore {ARROW}</span></a>'
        for r in p["related"])
    platform = ""
    if p.get("platform"):
        platform = f'<a class="link" style="margin-top:22px" href="{p["platform"]}" target="_blank" rel="noopener">Agents &amp; supervisors: log in to the call centre {I("ext")}</a>'
    return f'''<section class="phero dark prod">
  <div class="gridbg"></div><div class="glow"></div>
  <div class="wrap">
    <div>
      <div class="crumb"><a href="index.html">Home</a><span>/</span><a href="index.html#products">Products</a><span>/</span><span>{p["name"].replace("&", "&amp;")}</span></div>
      <span class="eyebrow line">{p["eyebrow"].replace("&", "&amp;")}</span>
      <h1>{p["h1"]}</h1>
      <p>{p["lead"]}</p>
      <div class="cta-row"><a class="btn btn-p" href="contact.html?svc={p["svc"]}">Get a quote {ARROW}</a><a class="btn btn-g" href="{p["cta2"][1]}"{ext}>{p["cta2"][0]}</a></div>
      <div class="chips">{chips}</div>
    </div>
    <div class="prod-mock reveal" style="--c:{c}">{p["mock"]}</div>
  </div>
</section>

<section class="sec soft">
  <div class="wrap">
    <div class="head reveal"><span class="eyebrow"><span class="n">01</span> Features</span><h2>{p["feat_h"]}</h2></div>
    <div class="adv">{feats}</div>
  </div>
</section>

<section class="sec dark">
  <div class="gridbg"></div>
  <div class="wrap">
    <div class="head reveal"><span class="eyebrow"><span class="n">02</span> Who it's for</span><h2>Where teams use it.</h2></div>
    <div class="aud reveal">{uses}</div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="head reveal"><span class="eyebrow"><span class="n">03</span> How it works</span><h2>From request to live.</h2><p class="lead">You pay once setup is agreed, never before.</p></div>
    <div class="steps">{steps}</div>
  </div>
</section>

<section class="sec soft" id="pricing">
  <div class="wrap">
    <div class="head reveal"><span class="eyebrow"><span class="n">04</span> Pricing</span><h2>How pricing works.</h2><p class="lead">{p["pricing_intro"]} Ask for a quote and we'll send rates for your country and volume within one business day.</p></div>
    <div class="plans">{plans}</div>
  </div>
</section>

<section class="sec" id="faq">
  <div class="wrap" style="max-width:900px">
    <div class="head c reveal"><span class="eyebrow"><span class="n">?</span> FAQ</span><h2>Common questions.</h2></div>
    {faq_html(p["faq"])}
  </div>
</section>

<section class="sec soft">
  <div class="wrap">
    <div class="head reveal"><span class="eyebrow"><span class="n">05</span> Better together</span><h2>Works with the rest of Endwave.</h2><p class="lead">One account, one invoice and systems that are already connected.</p></div>
    <div class="rel">{rel}</div>
  </div>
</section>

<section class="cta soft">
  <div class="wrap">
    <div class="cta-box reveal">
      <div class="gridbg"></div>
      <span class="eyebrow" style="position:relative">{p["name"].replace("&", "&amp;")}</span>
      <h2>Tell us what you need. We'll send one quotation.</h2>
      <p>Share your volumes and countries and we'll reply within one business day with pricing and next steps.</p>
      <div class="cta-row"><a class="btn btn-w" href="contact.html?svc={p["svc"]}">Get a quote {ARROW}</a><a class="btn btn-g" href="https://wa.me/254799611864" target="_blank" rel="noopener">{I("wa")} WhatsApp us</a></div>
      {platform}
    </div>
  </div>
</section>
'''
