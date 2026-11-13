/* =========================================================
   Endwave — site interactions
   ========================================================= */

/* ---------------------------------------------------------
   CONFIG — edit rates, currencies and the form endpoint here
   --------------------------------------------------------- */
const CONFIG = {
  // Indicative price per Mbps per month, in USD, by band.
  // Replace with Endwave's approved rate card before launch.
  bands: [
    { name: "Starter",    min: 50,   max: 149,   usd: 1.60 },
    { name: "Growth",     min: 150,  max: 299,   usd: 1.45 },
    { name: "Pro",        min: 300,  max: 599,   usd: 1.35 },
    { name: "Premium",    min: 600,  max: 999,   usd: 1.25 },
    { name: "Enterprise", min: 1000, max: 10000, usd: 1.10 },
  ],
  // Local currency per country and the FX rate used to convert from USD.
  countries: {
    ke: { name: "Kenya",    cur: "KES", fx: 129,  round: 1,
          cities: "Nairobi · Mombasa · Kisumu", currency: "KES or USD",
          delivery: "Fibre hand-off at tower, PoP or data centre" },
    ug: { name: "Uganda",   cur: "UGX", fx: 3650, round: 50,
          cities: "Kampala · Gulu · Mbarara", currency: "UGX or USD",
          delivery: "Fibre hand-off via Kenya cross-border routes" },
    tz: { name: "Tanzania", cur: "TZS", fx: 2650, round: 10,
          cities: "Dar es Salaam · Arusha · Dodoma · Mwanza", currency: "TZS or USD",
          delivery: "Fibre hand-off at coastal and inland sites" },
  },
  // Set to your form handler (Formspree, Netlify, your own API…).
  // Leave empty to show the success state without sending.
  formEndpoint: "",
};

const $ = (s, el = document) => el.querySelector(s);
const $$ = (s, el = document) => [...el.querySelectorAll(s)];
let currentCountry = "ke";

/* ---------- Year ---------- */
$("#year").textContent = new Date().getFullYear();

/* ---------- Nav: scrolled state, burger, active link ---------- */
const nav = $("#nav");
const burger = $("#burger");
const navLinks = $("#navLinks");

window.addEventListener("scroll", () => nav.classList.toggle("is-scrolled", window.scrollY > 10), { passive: true });

burger.addEventListener("click", () => {
  const open = burger.getAttribute("aria-expanded") === "true";
  burger.setAttribute("aria-expanded", String(!open));
  navLinks.classList.toggle("is-open", !open);
});
$$("a", navLinks).forEach(a => a.addEventListener("click", () => {
  burger.setAttribute("aria-expanded", "false");
  navLinks.classList.remove("is-open");
}));

const sectionObserver = new IntersectionObserver(entries => {
  entries.forEach(e => {
    if (!e.isIntersecting) return;
    $$(".nav__links a").forEach(a => a.classList.toggle("is-active", a.getAttribute("href") === "#" + e.target.id));
  });
}, { rootMargin: "-45% 0px -50% 0px" });
["model", "coverage", "pricing", "process", "faq"].forEach(id => sectionObserver.observe(document.getElementById(id)));

/* ---------- Reveal on scroll (with stagger for siblings) ---------- */
const revealObserver = new IntersectionObserver(entries => {
  entries.forEach(e => {
    if (!e.isIntersecting) return;
    const el = e.target;
    const siblings = [...el.parentElement.children].filter(c => c.classList.contains("reveal"));
    const idx = Math.max(0, siblings.indexOf(el));
    el.style.transitionDelay = Math.min(idx * 80, 400) + "ms";
    el.classList.add("is-in");
    revealObserver.unobserve(el);
  });
}, { threshold: 0.12, rootMargin: "0px 0px -40px 0px" });
$$(".reveal").forEach(el => revealObserver.observe(el));

// CTA waves draw-in
const ctaObs = new IntersectionObserver(([e]) => { if (e.isIntersecting) e.target.classList.add("is-in"); }, { threshold: .3 });
ctaObs.observe($(".cta__inner"));

/* ---------- Counters ---------- */
const countObs = new IntersectionObserver(entries => {
  entries.forEach(e => {
    if (!e.isIntersecting) return;
    const el = e.target;
    const target = parseFloat(el.dataset.count);
    const dec = parseInt(el.dataset.decimals || "0", 10);
    const suffix = el.dataset.suffix || "";
    const start = performance.now();
    const dur = 1600;
    const tick = now => {
      const t = Math.min((now - start) / dur, 1);
      const eased = 1 - Math.pow(1 - t, 3);
      el.textContent = (target * eased).toFixed(dec) + suffix;
      if (t < 1) requestAnimationFrame(tick);
    };
    requestAnimationFrame(tick);
    countObs.unobserve(el);
  });
}, { threshold: .6 });
$$("[data-count]").forEach(el => countObs.observe(el));

/* ---------- Timeline progress ---------- */
const timeline = $(".timeline");
const steps = $$(".timeline__step");
function updateTimeline() {
  const r = timeline.getBoundingClientRect();
  const vh = window.innerHeight;
  const progress = Math.min(Math.max((vh * 0.6 - r.top) / r.height, 0), 1);
  timeline.style.setProperty("--progress", (progress * 100).toFixed(1) + "%");
  steps.forEach(s => {
    const sr = s.getBoundingClientRect();
    s.classList.toggle("is-in", sr.top < vh * 0.6 || s.classList.contains("is-in") && sr.top < vh);
  });
}
window.addEventListener("scroll", updateTimeline, { passive: true });
updateTimeline();

/* ---------- Country sync (coverage map + calculator + form) ---------- */
function setCountry(code) {
  currentCountry = code;
  const c = CONFIG.countries[code];

  // tabs
  $$(".tab").forEach(t => {
    const on = t.dataset.country === code;
    t.classList.toggle("is-active", on);
    t.setAttribute("aria-selected", on);
  });
  $$(".seg__btn").forEach(b => b.classList.toggle("is-active", b.dataset.country === code));

  // panel
  const panel = $("#countryPanel");
  panel.classList.add("is-switching");
  setTimeout(() => {
    $('[data-field="cities"]', panel).textContent = c.cities;
    $('[data-field="currency"]', panel).textContent = c.currency;
    $('[data-field="delivery"]', panel).textContent = c.delivery;
    panel.classList.remove("is-switching");
  }, 220);

  // map
  $$("#map [data-c]").forEach(el => el.classList.toggle("is-on", el.dataset.c === code));

  // form
  $("#fCountry").value = code;

  renderCalc();
}
$$(".tab").forEach(t => t.addEventListener("click", () => setCountry(t.dataset.country)));
$$(".seg__btn").forEach(b => b.addEventListener("click", () => setCountry(b.dataset.country)));
$("#fCountry").addEventListener("change", e => setCountry(e.target.value));

/* ---------- Pricing calculator ---------- */
// Slider positions 0–1000 map piecewise onto the bands so each band gets equal width.
const STOPS = [
  { p: 0,    v: 50 },
  { p: 200,  v: 150 },
  { p: 400,  v: 300 },
  { p: 600,  v: 600 },
  { p: 800,  v: 1000 },
  { p: 1000, v: 10000 },
];
const range = $("#calcRange");
let mbps = 100;

function posToMbps(p) {
  for (let i = 1; i < STOPS.length; i++) {
    const a = STOPS[i - 1], b = STOPS[i];
    if (p <= b.p) {
      const v = a.v + (b.v - a.v) * ((p - a.p) / (b.p - a.p));
      return v >= 1000 ? Math.round(v / 100) * 100 : Math.round(v / 10) * 10;
    }
  }
  return 10000;
}
function mbpsToPos(v) {
  for (let i = 1; i < STOPS.length; i++) {
    const a = STOPS[i - 1], b = STOPS[i];
    if (v <= b.v) return a.p + (b.p - a.p) * ((v - a.v) / (b.v - a.v));
  }
  return 1000;
}
const bandFor = v => CONFIG.bands.find(b => v >= b.min && v <= b.max) || CONFIG.bands.at(-1);
const localRate = (band, c) => Math.round((band.usd * c.fx) / c.round) * c.round;
const fmt = n => n.toLocaleString("en-US");

function animateNumber(el, to) {
  const from = parseInt(el.textContent.replace(/,/g, ""), 10) || 0;
  const start = performance.now();
  cancelAnimationFrame(el._raf);
  const step = now => {
    const t = Math.min((now - start) / 500, 1);
    const e = 1 - Math.pow(1 - t, 3);
    el.textContent = fmt(Math.round(from + (to - from) * e));
    if (t < 1) el._raf = requestAnimationFrame(step);
  };
  el._raf = requestAnimationFrame(step);
}

function renderTiers() {
  const c = CONFIG.countries[currentCountry];
  const active = bandFor(mbps);
  $("#tiers").innerHTML = CONFIG.bands.map((b, i) => `
    <div class="tier ${b === active ? "is-active" : ""}" data-i="${i}">
      <div class="tier__name">${b.name}</div>
      <div class="tier__range">${b.min >= 1000 ? "1 Gbps +" : `${b.min} – ${b.max} Mbps`}</div>
      <div class="tier__rate">${c.cur} <b>${fmt(localRate(b, c))}</b>/Mbps</div>
    </div>`).join("");
  $$(".tier").forEach(t => t.addEventListener("click", () => {
    const b = CONFIG.bands[+t.dataset.i];
    setMbps(b.min === 50 ? 100 : b.min);
  }));
}

function renderCalc() {
  const c = CONFIG.countries[currentCountry];
  const band = bandFor(mbps);
  const rate = localRate(band, c);

  const big = mbps >= 1000;
  $("#calcVal").textContent = big ? (mbps / 1000).toFixed(mbps % 1000 ? 1 : 0) : mbps;
  $("#calcUnit").textContent = big ? "Gbps" : "Mbps";
  $("#calcCur").textContent = c.cur;
  animateNumber($("#calcPrice"), rate * mbps);
  $("#calcRate").textContent = `${c.cur} ${fmt(rate)}`;
  $("#calcTier").textContent = band.name;

  const pos = mbpsToPos(mbps);
  range.value = pos;
  range.style.setProperty("--p", pos / 10 + "%");
  renderTiers();
}

function setMbps(v) {
  mbps = Math.min(Math.max(v, 50), 10000);
  renderCalc();
}

range.addEventListener("input", () => {
  mbps = posToMbps(+range.value);
  renderCalc();
});
$$(".stepper__btn").forEach(btn => btn.addEventListener("click", () => {
  const dir = +btn.dataset.step;
  const inc = mbps >= 1000 ? 500 : mbps >= 300 ? 50 : 10;
  const next = mbps + dir * inc;
  setMbps(dir < 0 && mbps > 1000 && next < 1000 ? 1000 : next);
}));

// Carry calculator values into the request form
$("#calcCta").addEventListener("click", () => {
  $("#fCapacity").value = mbps;
  $("#fCountry").value = currentCountry;
});

/* ---------- FAQ: only one open at a time ---------- */
$$(".acc").forEach(d => d.addEventListener("toggle", () => {
  if (d.open) $$(".acc").forEach(o => { if (o !== d) o.open = false; });
}));

/* ---------- Request form ---------- */
const form = $("#requestForm");
const status = $("#formStatus");
const success = $("#formSuccess");

const validators = {
  capacity: v => +v >= 50 || "Capacity must be at least 50 Mbps",
  site: v => v.trim().length > 2 || "Tell us where the capacity should go",
  name: v => v.trim().length > 1 || "Your name",
  email: v => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v) || "A valid email",
  phone: v => v.replace(/\D/g, "").length >= 9 || "A valid mobile number",
};

form.addEventListener("submit", async e => {
  e.preventDefault();
  const data = Object.fromEntries(new FormData(form));
  const missing = [];
  Object.entries(validators).forEach(([key, fn]) => {
    const ok = fn(data[key] || "");
    const field = form.elements[key].closest(".field");
    field.classList.toggle("is-invalid", ok !== true);
    if (ok !== true) missing.push(ok);
  });

  if (missing.length) {
    status.textContent = "Still needed: " + missing.join(" · ");
    status.classList.add("is-error");
    form.querySelector(".is-invalid input, .is-invalid select")?.focus();
    return;
  }

  status.classList.remove("is-error");
  status.textContent = "Sending…";
  const btn = form.querySelector('button[type="submit"]');
  btn.disabled = true;

  try {
    if (CONFIG.formEndpoint) {
      const res = await fetch(CONFIG.formEndpoint, {
        method: "POST",
        headers: { "Content-Type": "application/json", Accept: "application/json" },
        body: JSON.stringify({ ...data, countryName: CONFIG.countries[data.country].name }),
      });
      if (!res.ok) throw new Error("Request failed");
    } else {
      await new Promise(r => setTimeout(r, 700));
      console.info("Endwave capacity request (no endpoint set):", data);
    }
    status.textContent = "";
    success.hidden = false;
  } catch (err) {
    status.textContent = "Something went wrong. Please email sales@endwave.africa.";
    status.classList.add("is-error");
  } finally {
    btn.disabled = false;
  }
});

form.addEventListener("input", e => e.target.closest(".field")?.classList.remove("is-invalid"));
$("#formReset").addEventListener("click", () => {
  form.reset();
  success.hidden = true;
  setCountry(currentCountry);
});

/* ---------- Init ---------- */
setCountry("ke");
setMbps(100);
