/* Endwave NextGen Worldwide — site script */
(() => {
const $ = (s, r = document) => r.querySelector(s), $$ = (s, r = document) => [...r.querySelectorAll(s)];
const fmt = n => Math.round(n).toLocaleString('en-US');
const ico = n => `<svg class="i"><use href="#i-${n}"/></svg>`;

/* ---------- nav ---------- */
const nav = $('#nav');
const onScroll = () => nav.classList.toggle('scrolled', scrollY > 20 || nav.classList.contains('mob'));
addEventListener('scroll', onScroll, { passive: true }); onScroll();
$('#burger').addEventListener('click', () => { nav.classList.toggle('mob'); document.body.style.overflow = nav.classList.contains('mob') ? 'hidden' : ''; onScroll(); });
const dds = $$('.menu .dd');
const closeAll = except => dds.forEach(d => { if (d !== except) { d.classList.remove('open'); d.querySelector('button').setAttribute('aria-expanded', 'false'); } });
const desk = () => matchMedia('(min-width:1081px)').matches;
dds.forEach(d => {
  const b = d.querySelector('button'); let t;
  b.addEventListener('click', e => { e.stopPropagation(); const o = !d.classList.contains('open'); closeAll(d); d.classList.toggle('open', o); b.setAttribute('aria-expanded', o); });
  d.addEventListener('mouseenter', () => { if (!desk()) return; clearTimeout(t); closeAll(d); d.classList.add('open'); b.setAttribute('aria-expanded', 'true'); });
  d.addEventListener('mouseleave', () => { if (!desk()) return; t = setTimeout(() => { d.classList.remove('open'); b.setAttribute('aria-expanded', 'false'); }, 160); });
});
document.addEventListener('click', e => { if (!e.target.closest('.dd')) closeAll(); });
document.addEventListener('keydown', e => { if (e.key === 'Escape') closeAll(); });
$$('.menu a').forEach(a => a.addEventListener('click', () => { nav.classList.remove('mob'); document.body.style.overflow = ''; closeAll(); }));

/* ---------- reveal & counters ---------- */
const io = new IntersectionObserver(es => es.forEach(en => {
  if (!en.isIntersecting) return; en.target.classList.add('in'); io.unobserve(en.target);
  $$('[data-count]', en.target).forEach(count);
}), { threshold: .12, rootMargin: '0px 0px -40px 0px' });
function count(el) { const end = +el.dataset.count; let s = null; const tick = ts => { s = s || ts; const p = Math.min(1, (ts - s) / 1200); el.textContent = Math.round(end * (1 - Math.pow(1 - p, 3))); if (p < 1) requestAnimationFrame(tick); }; requestAnimationFrame(tick); }
const watch = () => $$('.reveal:not(.in)').forEach(el => io.observe(el));
['.bento', '.svc', '.ways', '.adv', '.dcs', '.vals', '.combos', '.steps', '.req', '.launch'].forEach(sel => $$(sel).forEach(g => [...g.children].forEach((c, i) => c.style.transitionDelay = (i % 6) * 70 + 'ms')));

/* ---------- hero orbit ---------- */
const orbit = $('#orbit');
if (orbit) {
  const nodes = [['Capacity', 'globe', 50, 4, '#15B0E3'], ['Billing', 'bill', 90, 28, '#2980C3'], ['Call centres', 'head', 88, 74, '#14A894'], ['Bulk SMS', 'sms', 50, 96, '#E59A1C'], ['VoIP & voice', 'phone', 12, 74, '#1DB974'], ['E-commerce', 'cart', 10, 28, '#E0533D'], ['PPPoE', 'net', 73, 50, '#6F6BE8'], ['Colocation', 'server', 27, 50, '#3B7BD8']];
  const svg = $('#orbitLines');
  nodes.forEach(([l, ic, x, y, c], i) => {
    svg.insertAdjacentHTML('beforeend', `<line x1="50" y1="50" x2="${x}" y2="${y}" vector-effect="non-scaling-stroke"/><line class="p" x1="${x}" y1="${y}" x2="50" y2="50" vector-effect="non-scaling-stroke" style="animation-delay:${i * .45}s"/>`);
    const small = i > 5;
    orbit.insertAdjacentHTML('beforeend', `<div class="node" style="left:${x}%;top:${y}%;--c:${c};animation-delay:${i * .7}s">${y > 60 && !small ? '' : ''}<i style="${small ? 'width:44px;height:44px;border-radius:13px' : ''}">${ico(ic)}</i><span>${l}</span></div>`);
  });
}

/* ---------- logo strip ---------- */
const track = $('#track');
if (track) {
  const items = [['pay-mpesa.png', 'M-Pesa', 30], ['pay-airtel.svg', 'Airtel Money', 34], ['pay-visa.png', 'Visa', 20], ['pay-mastercard.png', 'Mastercard', 32], ['pay-amex.png', 'American Express', 34], ['dc-icolo.png', 'iColo', 26], ['dc-raxio.svg', 'Raxio', 24], ['dc-adc.png', 'Africa Data Centres', 30], ['logo-starlink.svg', 'Starlink', 54], ['logo-mikrotik.png', 'MikroTik', 24]];
  const one = items.map(([f, a, h]) => `<img src="assets/${f}" alt="${a}" style="height:${h}px" loading="lazy">`).join('') + '<span>BGP · AS329846</span>';
  track.innerHTML = one + one;
  $$('img', track).forEach((im, i) => { if (i >= items.length + 0 && i < items.length * 2) im.alt = ''; });
}

/* ---------- product mocks ---------- */
const bars = $('#bars');
if (bars) bars.innerHTML = [38, 48, 44, 58, 62, 56, 70, 76, 68, 82, 78, 92].map((h, i) => `<i style="height:${h}%;animation-delay:${i * .06}s"></i>`).join('');
if ($('#cq')) setInterval(() => { $('#cq').textContent = Math.floor(Math.random() * 4); $('#cw').textContent = '0:' + String(10 + Math.floor(Math.random() * 20)); }, 3000);

/* ---------- network map ---------- */
const cities = [
  ['Gulu', 150, 58, 'ug', 'm', 12, 4], ['Kampala', 160, 150, 'ug', 'core', -66, 4], ['Mbarara', 88, 198, 'ug', 'm', -18, 22],
  ['Kisumu', 250, 160, 'ke', 'm', 10, -10], ['Nairobi', 340, 205, 'ke', 'core', 12, -10], ['Mombasa', 446, 312, 'ke', 'land', -78, -6],
  ['Mwanza', 186, 238, 'tz', 'm', -62, 18], ['Arusha', 322, 282, 'tz', 'm', 12, 4], ['Dodoma', 282, 356, 'tz', 'm', -64, 4],
  ['Dar es Salaam', 428, 378, 'tz', 'core', -110, 22], ['Mbeya', 196, 408, 'tz', 'm', -56, 4]];
const links = [[0, 1], [1, 2], [1, 3], [3, 4], [4, 5], [4, 7], [7, 8], [8, 9], [5, 9], [6, 3], [6, 8], [8, 10], [1, 6]];
$$('#netmap').forEach(svg => {
  const P = i => cities[i];
  let h = `<defs><radialGradient id="lk" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#16345F"/><stop offset="1" stop-color="#0D2140"/></radialGradient></defs>`;
  h += `<g fill="none" stroke="rgba(140,170,230,.06)">${Array.from({ length: 12 }, (_, i) => `<path d="M0 ${i * 38} H520"/>`).join('')}${Array.from({ length: 14 }, (_, i) => `<path d="M${i * 40} 0 V430"/>`).join('')}</g>`;
  h += `<path d="M520 230 C 488 262, 470 320, 462 380 L460 430 L520 430Z" fill="rgba(21,110,190,.10)"/>`;
  h += `<text class="mo" x="494" y="300" font-family="JetBrains Mono" font-size="8.5" fill="#3D5F8C" letter-spacing="2" transform="rotate(90 494 300)">INDIAN OCEAN</text>`;
  h += `<ellipse cx="208" cy="196" rx="50" ry="40" fill="url(#lk)" stroke="rgba(95,208,245,.12)"/><text class="mo" x="178" y="200" font-family="JetBrains Mono" font-size="7.5" fill="#4C78A8" letter-spacing="1">L. VICTORIA</text>`;
  h += [['UGANDA', 60, 112, 'ug'], ['KENYA', 372, 128, 'ke'], ['TANZANIA', 238, 318, 'tz']].map(([t, x, y, c]) => `<text class="cl" data-c="${c}" x="${x}" y="${y}" font-family="Plus Jakarta Sans" font-weight="800" font-size="15" fill="#24375C" letter-spacing="4">${t}</text>`).join('');
  h += `<path d="M520 296 L${P(5)[1]} ${P(5)[2]}" stroke="#3FD493" stroke-opacity=".55" stroke-width="1.6" class="route" fill="none"/><path d="M520 392 L${P(9)[1]} ${P(9)[2]}" stroke="#3FD493" stroke-opacity=".55" stroke-width="1.6" class="route" fill="none"/>`;
  h += `<text class="mo" x="474" y="286" font-family="JetBrains Mono" font-size="8" fill="#3FD493" opacity=".8">SUBSEA</text>`;
  h += links.map(([a, b]) => `<path class="lk" data-a="${P(a)[3]}" data-b="${P(b)[3]}" d="M${P(a)[1]} ${P(a)[2]} L${P(b)[1]} ${P(b)[2]}" stroke="rgba(95,208,245,.28)" stroke-width="1.4" fill="none"/>`).join('');
  h += links.filter((_, i) => i % 2 === 0).map(([a, b], i) => `<path d="M${P(a)[1]} ${P(a)[2]} L${P(b)[1]} ${P(b)[2]}" stroke="#5FD0F5" stroke-width="2" fill="none" class="route" style="animation-duration:${10 + i * 2}s"/>`).join('');
  h += cities.map(([n, x, y, c, t, dx, dy]) => {
    const col = t === 'core' ? '#15B0E3' : t === 'land' ? '#3FD493' : '#8D9AB8';
    const r = t === 'm' ? 4.5 : 6.5;
    const pulse = t !== 'm' ? `<circle cx="${x}" cy="${y}" r="${r}" fill="${col}" class="pulse-dot"/>` : '';
    return `<g class="city" data-c="${c}">${pulse}<circle cx="${x}" cy="${y}" r="${r + 4}" fill="${col}" opacity=".14"/><circle cx="${x}" cy="${y}" r="${r}" fill="${col}" stroke="#040914" stroke-width="2"/><text x="${x + dx}" y="${y + dy}" font-family="Plus Jakarta Sans" font-size="11.5" font-weight="${t === 'm' ? 600 : 700}" fill="${t === 'm' ? '#9AA8C6' : '#fff'}">${n}</text></g>`;
  }).join('');
  svg.innerHTML = h;
});

/* ---------- coverage ---------- */
const cov = {
  ke: [['Key cities', 'Nairobi · Mombasa · Kisumu'], ['Billing currency', 'KES or USD'], ['Data centres', 'ADC Kenya · iColo NBO1 · iColo NBO2'], ['Delivery', 'Fibre, Starlink or point-to-point'], ['Capacity', '50 Mbps – 100 Gbps']],
  ug: [['Key cities', 'Kampala · Gulu · Mbarara'], ['Billing currency', 'UGX or USD'], ['Data centres', 'Raxio Uganda'], ['Delivery', 'Fibre, Starlink or point-to-point'], ['Capacity', '50 Mbps – 100 Gbps']],
  tz: [['Key cities', 'Dar es Salaam · Arusha · Mwanza · Dodoma'], ['Billing currency', 'TZS or USD'], ['Data centres', 'Raxio Tanzania'], ['Delivery', 'Fibre, Starlink or point-to-point'], ['Capacity', '50 Mbps – 100 Gbps']]
};
if ($('#covKv')) {
  const setCov = c => {
    $('#covKv').innerHTML = cov[c].map(([k, v]) => `<div><dt>${k}</dt><dd>${v}</dd></div>`).join('');
    $$('#covTabs button').forEach(b => b.classList.toggle('on', b.dataset.c === c));
    $$('#netmap .city').forEach(g => g.style.opacity = g.dataset.c === c ? 1 : .35);
    $$('#netmap .cl').forEach(t => t.setAttribute('fill', t.dataset.c === c ? '#5FD0F5' : '#24375C'));
  };
  $$('#covTabs button').forEach(b => b.addEventListener('click', () => setCov(b.dataset.c)));
  setCov('ke');
}

/* ---------- data centres ---------- */
if ($('#dcs')) {
  const dcs = [['KE · NBO', 'ADC Kenya', 'Nairobi', 'dc-adc.png'], ['KE · NBO1', 'iColo NBO1', 'Nairobi', 'dc-icolo.png'], ['KE · NBO2', 'iColo NBO2', 'Nairobi', 'dc-icolo.png'], ['UG · KLA', 'Raxio Uganda', 'Kampala', 'dc-raxio.svg'], ['TZ · DAR', 'Raxio Tanzania', 'Dar es Salaam', 'dc-raxio.svg']];
  $('#dcs').innerHTML = dcs.map(([c, n, l, logo], i) => `<div class="dc reveal" style="transition-delay:${i * 70}ms"><div class="top"><span>${c}</span><span class="dot"></span></div><div class="logo"><img src="assets/${logo}" alt="${n}" loading="lazy"></div><h6>${n}</h6><p>${l}</p><div class="tags"><span>Colocation</span><span>Cross-connect</span></div></div>`).join('');
}

/* ---------- pricing calculator ---------- */
if ($('#slider')) {
  const bands = [['Starter', 50, 199, '50 – 199 Mbps', 100], ['Growth', 200, 500, '200 – 500 Mbps', 300], ['Pro', 501, 999, '501 – 999 Mbps', 700], ['Carrier', 1000, 100000, '1 Gbps and above', 2000]];
  const cur = {
    Kenya: { code: 'KES', rates: [190, 180, 170, 160], activation: 11600 },
    Uganda: { code: 'UGX', rates: [5200, 4950, 4700, 4400], activation: 320000 },
    Tanzania: { code: 'TZS', rates: [3600, 3420, 3230, 3040], activation: 220000 }
  };
  const stops = [50, 100, 200, 500, 1000, 10000, 100000];
  let mbps = 100, country = 'Kenya';
  const toSlider = v => { for (let i = 0; i < 6; i++) { if (v <= stops[i + 1]) { const a = Math.log(stops[i]), b = Math.log(stops[i + 1]); return (i + (Math.log(v) - a) / (b - a)) * 100; } } return 600; };
  const fromSlider = s => { const i = Math.min(5, Math.floor(s / 100)), t = s / 100 - i; const v = Math.exp(Math.log(stops[i]) + t * (Math.log(stops[i + 1]) - Math.log(stops[i]))); return v < 1000 ? Math.max(50, Math.round(v / 10) * 10) : v < 10000 ? Math.round(v / 100) * 100 : Math.round(v / 1000) * 1000; };
  const label = v => v >= 1000 ? (v / 1000).toLocaleString('en-US', { maximumFractionDigits: 1 }) + ' Gbps' : v + ' Mbps';
  $('#bands').innerHTML = bands.map((b, i) => `<div class="band" data-i="${i}" role="button" tabindex="0"><h6>${b[0]}</h6><small>${b[3]}</small><b><span class="bc">KES</span> <span class="br">${cur.Kenya.rates[i]}</span> <em>/Mbps</em></b></div>`).join('');
  const render = fromInput => {
    mbps = Math.max(50, Math.min(100000, mbps));
    const bi = bands.findIndex(b => mbps <= b[2]), i = bi < 0 ? bands.length - 1 : bi, b = bands[i], c = cur[country], rate = c.rates[i];
    $('#cur').textContent = c.code;
    if ($('#actFee')) $('#actFee').textContent = `${c.code} ${fmt(c.activation)}`;
    $$('.band').forEach((el, j) => { $('.bc', el).textContent = c.code; $('.br', el).textContent = fmt(c.rates[j]); el.classList.toggle('on', j === i); });
    $('#total').textContent = fmt(mbps * rate);
    $('#note').innerHTML = `<b>${c.code} ${fmt(rate)}</b> per Mbps per month · <b>${b[0]}</b> tier (${b[3]}) · plus <b>${c.code} ${fmt(c.activation)}</b> one-time port activation. Indicative until feasibility is confirmed${country !== 'Kenya' ? `; ${country} quotes can also be billed in USD` : ''}.`;
    $('#sideTitle').textContent = `${label(mbps)} · ${country}`;
    $('#reqCap').href = `contact.html?svc=capacity&mbps=${mbps}&country=${country}#request`;
    const s = toSlider(mbps), sl = $('#slider'); if (!fromInput) sl.value = s; sl.style.setProperty('--p', s / 6 + '%');
    const u = +$('#unit').value; if (document.activeElement !== $('#mbps')) $('#mbps').value = +(mbps / u).toFixed(u > 1 ? 1 : 0);
  };
  $('#slider').addEventListener('input', e => { mbps = fromSlider(+e.target.value); render(true); });
  $('#mbps').addEventListener('input', e => { const v = +e.target.value * +$('#unit').value; if (v >= 50) { mbps = v; render(); } });
  $('#mbps').addEventListener('blur', () => render());
  $('#unit').addEventListener('change', () => { $('#mbps').blur(); render(); });
  const step = d => { const inc = mbps < 1000 || (d < 0 && mbps <= 1000) ? 50 : mbps < 10000 ? 500 : 10000; mbps += d * inc; render(); };
  $('#plus').addEventListener('click', () => step(1)); $('#minus').addEventListener('click', () => step(-1));
  $$('.band').forEach(el => { const go = () => { mbps = bands[+el.dataset.i][4]; render(); }; el.addEventListener('click', go); el.addEventListener('keydown', e => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); go(); } }); });
  $$('#calcTabs button').forEach(b => b.addEventListener('click', () => { country = b.dataset.c; $$('#calcTabs button').forEach(x => x.classList.toggle('on', x === b)); render(); }));
  render();
}

/* ---------- FAQ ---------- */
if ($('#qa')) {
  const faq = [
    ['Can I buy just one service?', 'Yes. Every service can be taken on its own. Combining them simply means one account, one invoice and systems that are already connected.'],
    ['Who is wholesale capacity for?', 'ISPs, WISPs, fibre operators, carriers and ICT companies that resell bandwidth or run their own networks, plus enterprises that need dedicated, uncontended internet for their sites.'],
    ['Is the capacity shared or throttled?', 'Neither. The bandwidth you buy is dedicated to your network, backed by 99.9% guaranteed uptime and monitored 24/7 by our NOC, so it performs the same at peak hours as it does off-peak.'],
    ['What do I need at my site before activation?', 'Active last-mile fibre pulled to your BTS location; a router that supports BGP or static routing with a free optical port (for example an SFP-enabled MikroTik); SFP modules, 1.25G 10 km (Huawei, Sopto or BIDI one-core); a splicing technician on standby once the site is confirmed; and power redundancy, strongly recommended. Activation is a one-time KES 11,600 port fee.'],
    ['Do you offer BGP, IP addresses and colocation?', 'Yes. We run our own network (AS329846) and support BGP sessions, IP transit and address allocation, with colocation and cross-connects in five carrier-neutral data centres.'],
    ['Can I try the billing system first?', 'Yes. The Endwave Billing demo, including PPPoE management, is open at demo.endwaveafrica.com, and we can set up a separate demo environment for your own network on request.'],
    ['Can I keep my existing phone numbers?', 'In most cases, yes. We port existing numbers onto our SIP trunks or hosted PBX and can add new local numbers in Kenya, Uganda and Tanzania.'],
    ['Do you set up the call centre equipment?', 'Yes. We design the IVR and queues, supply seats and headsets if you need them, and set everything up on site with your team.'],
    ['How do I get a sender ID for bulk SMS?', 'Tell us the name you want to send under and we handle registration with the networks. Once approved, you can send from the web portal or through our API.'],
    ['Does the billing system work with M-Pesa?', 'Yes. Payments from M-Pesa, Airtel Money and cards reconcile automatically, and receipts and reminders go out by SMS and email.'],
    ["What if there's no fibre at my site?", 'We can deliver over Starlink satellite or licensed point-to-point radio instead, and combine either with fibre later as a backup path.']];
  $('#qa').innerHTML = faq.map(([q, a], i) => `<div class="q${i ? '' : ' open'}"><button type="button" aria-expanded="${!i}"><small>${String(i + 1).padStart(2, '0')}</small><span>${q}</span><i></i></button><div class="a"><div><p>${a}</p></div></div></div>`).join('');
  $$('.q button').forEach(b => b.addEventListener('click', () => { const q = b.parentElement, o = !q.classList.contains('open'); $$('.q').forEach(x => { x.classList.remove('open'); $('button', x).setAttribute('aria-expanded', 'false'); }); if (o) { q.classList.add('open'); b.setAttribute('aria-expanded', 'true'); } }));
}

/* ---------- forms ---------- */
const mails = { Kenya: 'kenya@endwaveafrica.com', Uganda: 'uganda@endwaveafrica.com', Tanzania: 'tz@endwaveafrica.com' };
const bad = (el, isBad) => { el.classList.toggle('err', isBad); return isBad; };
const req = $('#reqForm');
if (req) {
  const capOn = () => $('input[data-k="capacity"]').checked;
  const sync = () => $$('.capf').forEach(el => el.classList.toggle('hide', !capOn()));
  $$('input[name="svc"]').forEach(c => c.addEventListener('change', () => { sync(); $('#svcPick').classList.remove('err'); }));
  const p = new URLSearchParams(location.search);
  if (p.get('svc')) { const c = $(`input[data-k="${p.get('svc')}"]`); if (c) c.checked = true; }
  if (p.get('mbps')) $('#fCap').value = p.get('mbps');
  if (p.get('country') && mails[p.get('country')]) $('#fCountry').value = p.get('country');
  sync();
  if (p.get('svc') && !location.hash) setTimeout(() => $('#request').scrollIntoView({ behavior: 'smooth' }), 300);
  req.addEventListener('submit', e => {
    e.preventDefault();
    let ok = true;
    const svcs = $$('input[name="svc"]:checked').map(c => c.value);
    if (bad($('#svcPick'), !svcs.length)) ok = false;
    ['fSite', 'fName', 'fPhone'].forEach(id => { if (bad($('#' + id), !$('#' + id).value.trim())) ok = false; });
    if (bad($('#fEmail'), !/^\S+@\S+\.\S+$/.test($('#fEmail').value))) ok = false;
    if (capOn() && bad($('#fCap'), +$('#fCap').value < 50)) ok = false;
    if (!ok) { const f = $('.err', req); if (f) { f.scrollIntoView({ block: 'center', behavior: 'smooth' }); if (f.focus) f.focus({ preventScroll: true }); } return; }
    const c = $('#fCountry').value, to = mails[c];
    const lines = [`Services: ${svcs.join(', ')}`, `Country: ${c}`];
    if (capOn()) lines.push(`Capacity: ${$('#fCap').value} Mbps`, `Preferred delivery: ${$('#fDel').value}`);
    lines.push(`Site: ${$('#fSite').value}`); if ($('#fMore').value.trim()) lines.push(`Notes: ${$('#fMore').value.trim()}`);
    lines.push('', `Name: ${$('#fName').value}`); if ($('#fCo').value.trim()) lines.push(`Company: ${$('#fCo').value}`); lines.push(`Email: ${$('#fEmail').value}`, `Mobile: ${$('#fPhone').value}`);
    const body = lines.join('\n');
    $('#summary').textContent = body; $('#toMail').textContent = to;
    $('#mailBtn').href = `mailto:${to}?subject=${encodeURIComponent('Service request — ' + svcs.join(', '))}&body=${encodeURIComponent(body)}`;
    $('#formBody').style.display = 'none'; $('#done').classList.add('show'); $('#request').scrollIntoView({ behavior: 'smooth' });
  });
  $$('input,textarea,select', req).forEach(el => el.addEventListener('input', () => el.classList.remove('err')));
  $('#editBtn').addEventListener('click', () => { $('#done').classList.remove('show'); $('#formBody').style.display = ''; });
  $('#copyBtn').addEventListener('click', async e => { try { await navigator.clipboard.writeText(`To: ${$('#toMail').textContent}\n\n` + $('#summary').textContent); e.target.textContent = 'Copied ✓'; } catch (_) { e.target.textContent = 'Select & copy above'; } setTimeout(() => e.target.textContent = 'Copy request', 2200); });
}
const demo = $('#demoForm');
if (demo) {
  demo.addEventListener('submit', e => {
    e.preventDefault();
    let ok = true;
    ['dName', 'dCo', 'dPhone'].forEach(id => { if (bad($('#' + id), !$('#' + id).value.trim())) ok = false; });
    if (bad($('#dEmail'), !/^\S+@\S+\.\S+$/.test($('#dEmail').value))) ok = false;
    if (!ok) { $('.err', demo).focus(); return; }
    const v = id => $('#' + id).value.trim();
    const body = [`Company / ISP: ${v('dCo')}`, `Subscribers: ${v('dSubs')}`, `Gateways / routers: ${v('dRouters') || '—'}`, `Service type: ${v('dType')}`, `Current billing platform: ${v('dCur') || '—'}`, v('dMore') ? `Notes: ${v('dMore')}` : '', '', `Name: ${v('dName')}`, `Email: ${v('dEmail')}`, `Phone: ${v('dPhone')}`].filter((l, i) => l || i === 6).join('\n');
    location.href = `mailto:kenya@endwaveafrica.com?subject=${encodeURIComponent('Billing demo request — ' + v('dCo'))}&body=${encodeURIComponent(body)}`;
    $('#demoMsg').innerHTML = 'Your email app should open with the request filled in. If it doesn\'t, email <a class="link" href="mailto:kenya@endwaveafrica.com">kenya@endwaveafrica.com</a>.';
  });
  $$('input', demo).forEach(el => el.addEventListener('input', () => el.classList.remove('err')));
}

watch();
})();
