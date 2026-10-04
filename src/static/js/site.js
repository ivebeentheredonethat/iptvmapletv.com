/* IPTVMaple — site behaviour. No dependencies. */
(() => {
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  document.documentElement.classList.add("js");

  /* header: shadow on scroll + mobile menu */
  const header = $(".header");
  const onScroll = () => header && header.classList.toggle("is-scrolled", scrollY > 8);
  addEventListener("scroll", onScroll, { passive: true });
  onScroll();
  const menuBtn = $(".menu-btn");
  if (menuBtn) {
    const toggle = (open) => {
      document.body.classList.toggle("menu-open", open);
      menuBtn.setAttribute("aria-expanded", String(open));
      document.body.style.overflow = open ? "hidden" : "";
    };
    menuBtn.addEventListener("click", () => toggle(!document.body.classList.contains("menu-open")));
    $$(".mobile-nav a").forEach((a) => a.addEventListener("click", () => toggle(false)));
    addEventListener("keydown", (e) => e.key === "Escape" && toggle(false));
  }

  /* reveal on scroll */
  const io = "IntersectionObserver" in window && new IntersectionObserver((entries) => {
    entries.forEach((e) => { if (e.isIntersecting) { e.target.classList.add("is-in"); io.unobserve(e.target); } });
  }, { rootMargin: "0px 0px -8% 0px" });
  $$(".reveal").forEach((el) => (io ? io.observe(el) : el.classList.add("is-in")));

  /* reviews sliders: the track slides left/right one slide at a time; dots, swipe, auto-advance (paused on hover/focus) */
  $$("[data-carousel]").forEach((c) => {
    const track = $(".rv-track", c), slides = $$(".rv-slide", c), dots = $$(".rv-dots button", c);
    if (slides.length < 2) return;
    let i = 0, timer;
    const show = (n) => {
      i = (n + slides.length) % slides.length;
      track.style.transform = `translateX(calc(${-i * 100}% - ${i * 20}px))`;
      slides.forEach((s, k) => s.setAttribute("aria-hidden", String(k !== i)));
      dots.forEach((d, k) => d.setAttribute("aria-current", String(k === i)));
    };
    const play = () => { clearInterval(timer); if (!matchMedia("(prefers-reduced-motion: reduce)").matches) timer = setInterval(() => show(i + 1), 6000); };
    dots.forEach((d, k) => d.addEventListener("click", () => { show(k); play(); }));
    let x0 = null;
    c.addEventListener("touchstart", (e) => { x0 = e.touches[0].clientX; clearInterval(timer); }, { passive: true });
    c.addEventListener("touchend", (e) => {
      if (x0 === null) return;
      const dx = e.changedTouches[0].clientX - x0; x0 = null;
      if (Math.abs(dx) > 40) show(i + (dx < 0 ? 1 : -1));
      play();
    });
    c.addEventListener("mouseenter", () => clearInterval(timer));
    c.addEventListener("mouseleave", play);
    c.addEventListener("focusin", () => clearInterval(timer));
    show(0);
    play();
  });

  /* pricing: connection switcher */
  $$("[data-pricing]").forEach((root) => {
    const data = JSON.parse($("script[type='application/json']", root).textContent);
    const tabs = $$(".seg button", root);
    const render = (n) => {
      const set = data.find((d) => d.devices === n);
      tabs.forEach((t, k) => {
        const on = +t.dataset.devices === n;
        t.setAttribute("aria-selected", String(on));
        if (on) t.parentElement.style.setProperty("--i", k);
      });
      set.plans.forEach((p, i) => {
        const card = $$(".plan", root)[i];
        $(".amt", card).textContent = p.price;
        $("s", card).textContent = "$" + p.original;
        $(".per-month", card).textContent = p.months > 1 ? `≈ $${(p.price / p.months).toFixed(2)}/mo` : "Billed monthly";
        $(".plan-sub", card).textContent = `${n} simultaneous ${n > 1 ? "connections" : "connection"}`;
        $(".js-conn", card).textContent = `${n} ${n > 1 ? "devices" : "device"} at the same time`;
        const a = $(".btn", card);
        a.href = `/${p.slug}/`;
      });
    };
    tabs.forEach((t) => t.addEventListener("click", () => render(+t.dataset.devices)));
  });

  /* tabs (setup guides) */
  $$("[data-tabs]").forEach((root) => {
    const btns = $$("[role='tab']", root);
    btns.forEach((b) => b.addEventListener("click", () => {
      btns.forEach((x) => {
        const on = x === b;
        x.setAttribute("aria-selected", String(on));
        document.getElementById(x.getAttribute("aria-controls")).hidden = !on;
      });
    }));
  });

  /* channels: search + region filter */
  const chRoot = $("[data-channels]");
  if (chRoot) {
    const input = $("input[type='search']", chRoot);
    const regionBtns = $$(".region-tabs button", chRoot);
    const countries = $$(".country", chRoot);
    const groups = $$("[data-region]", chRoot);
    const empty = $(".empty", chRoot);
    let region = "all";
    const esc = (s) => s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
    const html = (s) => s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
    const apply = () => {
      const q = input.value.trim().toLowerCase();
      let shown = 0;
      countries.forEach((c) => {
        const inRegion = region === "all" || c.closest("[data-region]").dataset.region === region;
        const lis = $$("li", c);
        let hit = false;
        const nameHit = q && c.dataset.name.includes(q);
        lis.forEach((li) => {
          const t = li.dataset.t || (li.dataset.t = li.textContent);
          if (!q) { li.hidden = false; li.textContent = t; return; }
          const m = t.toLowerCase().includes(q);
          hit ||= m;
          li.hidden = !(m || nameHit);
          const safe = html(t);
          li.innerHTML = m ? safe.replace(new RegExp(esc(html(q)), "ig"), (x) => `<mark>${x}</mark>`) : safe;
        });
        const vis = inRegion && (!q || hit || nameHit);
        c.hidden = !vis;
        c.open = !!(q && vis && hit);
        if (vis) shown++;
      });
      groups.forEach((g) => (g.hidden = !$$(".country:not([hidden])", g).length));
      empty.style.display = shown ? "none" : "block";
    };
    input.addEventListener("input", apply);
    regionBtns.forEach((b) => b.addEventListener("click", () => {
      region = b.dataset.region;
      regionBtns.forEach((x) => x.setAttribute("aria-pressed", String(x === b)));
      apply();
    }));
  }

  /* order / trial / referral forms -> /api/ajax (Pages Function) */
  $$("form[data-lead-form]").forEach((form) => {
    const btn = $("button[type='submit']", form);
    const msg = $(".form-msg", form);
    const setErr = (field, text) => {
      const input = form.elements[field];
      if (!input) return;
      input.setAttribute("aria-invalid", text ? "true" : "false");
      const e = input.closest(".field").querySelector(".err");
      if (e) e.textContent = text || "";
    };
    form.addEventListener("submit", async (ev) => {
      ev.preventDefault();
      msg.className = "form-msg";
      let bad = false;
      $$("[required]", form).forEach((i) => {
        const empty = !i.value.trim();
        setErr(i.name, empty ? "Required" : "");
        bad ||= empty;
      });
      $$("input[type='email']", form).forEach((e) => {
        if (e.value && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(e.value)) { setErr(e.name, "Enter a valid email"); bad = true; }
      });
      $$("input[type='tel']", form).forEach((t) => {
        if (t.value && t.value.replace(/\D/g, "").length < 7) { setErr(t.name, "Enter a valid phone number"); bad = true; }
      });
      if (bad) { $("[aria-invalid='true']", form)?.focus(); return; }

      btn.disabled = true; btn.classList.add("is-loading");
      try {
        const fd = new FormData(form);
        fd.set("current_url", location.href);
        const res = await fetch("/api/ajax", { method: "POST", body: fd });
        const json = await res.json();
        if (!json.success || !json.data || json.data.success === false) throw new Error(json.data?.message || "Something went wrong");
        const type = form.dataset.leadForm;
        try {
          window.gtag && gtag("event", "generate_lead", { form_type: type, value: +form.dataset.value || 0, currency: "USD" });
          window.rdt && rdt("track", "Lead");
        } catch (_) {}
        if (json.data.url) { location.href = json.data.url; return; }
        form.reset();
        const card = form.closest(".order-card"), done = card && $("[data-success]", card);
        if (done) {
          $("[data-success-hide]", card).hidden = true;
          done.hidden = false;
          card.scrollIntoView({ behavior: "smooth", block: "center" });
          done.focus({ preventScroll: true });
          return;
        }
        msg.textContent = json.data.message;
        msg.className = "form-msg is-ok";
      } catch (err) {
        msg.textContent = "Sorry — we couldn't send your details. Please try again or message us on WhatsApp.";
        msg.className = "form-msg is-error";
      } finally {
        btn.disabled = false; btn.classList.remove("is-loading");
      }
    });
    $$("input, select", form).forEach((i) => i.addEventListener("input", () => setErr(i.name, "")));
  });

  /* big confirmation panel -> back to the form */
  $$("[data-success-again]").forEach((b) => b.addEventListener("click", () => {
    const card = b.closest(".order-card");
    $("[data-success]", card).hidden = true;
    $("[data-success-hide]", card).hidden = false;
    $("input:not([type=hidden])", card)?.focus();
  }));

  /* referral: reveal form */
  $$("[data-show]").forEach((b) => b.addEventListener("click", () => {
    const t = document.getElementById(b.dataset.show);
    t.hidden = false;
    t.scrollIntoView({ behavior: "smooth", block: "start" });
    setTimeout(() => $("input:not([type=hidden])", t)?.focus({ preventScroll: true }), 500);
  }));

  /* recent real purchases: shows only entries the owner has added via /api/orders-admin; nothing is shown when the feed is empty */
  (() => {
    const skip = /^\/(thank-you|landing\d?)\//.test(location.pathname);
    let hidden = false;
    try { hidden = sessionStorage.getItem("sn-off") === "1"; } catch (e) {}
    if (skip || hidden) return;
    const ago = (iso) => {
      const m = Math.max(1, Math.round((Date.now() - Date.parse(iso)) / 60000));
      if (m < 60) return m + " min ago";
      const h = Math.round(m / 60);
      if (h < 24) return h + (h === 1 ? " hour ago" : " hours ago");
      const d = Math.round(h / 24);
      return d + (d === 1 ? " day ago" : " days ago");
    };
    /* sample names are shown only on a device where the owner switched preview on at /sales-demo/ (never to visitors) */
    const SAMPLE = () => [
      { first: "Sarah", place: "Ontario", plan: "12 Months", at: new Date(Date.now() - 2 * 3600e3).toISOString() },
      { first: "James", place: "Texas", plan: "6 Months", at: new Date(Date.now() - 35 * 60e3).toISOString() },
      { first: "Olivia", place: "Sydney", plan: "12 Months", at: new Date(Date.now() - 5 * 3600e3).toISOString() },
      { first: "Klaus", place: "Germany", plan: "3 Months", at: new Date(Date.now() - 90 * 60e3).toISOString() },
    ];
    const start = async () => {
      let preview = false;
      try { preview = localStorage.getItem("sn-preview") === "1"; } catch (e) {}
      let items = window.__SALE_DEMO || (preview ? SAMPLE() : []);
      if (!items.length) { try { items = await (await fetch("/api/recent-orders")).json(); } catch (e) { return; } }
      if (!Array.isArray(items) || !items.length) return;
      const card = document.createElement("aside");
      card.className = "sale-toast";
      card.setAttribute("role", "status");
      card.setAttribute("aria-live", "polite");
      card.innerHTML = '<span class="sale-dot" aria-hidden="true"></span><div><p class="sale-line"></p><p class="sale-time"></p></div><button type="button" aria-label="Close">×</button>';
      document.body.appendChild(card);
      const line = card.querySelector(".sale-line"), time = card.querySelector(".sale-time");
      let i = 0, shown = 0, timer;
      const show = () => {
        if (shown >= Math.min(items.length * 2, 6)) return;
        const x = items[i++ % items.length];
        line.textContent = "";
        const b = document.createElement("b");
        b.textContent = x.first;
        line.append(b, " from " + x.place + " purchased ", Object.assign(document.createElement("b"), { textContent: x.plan }));
        time.textContent = ago(x.at) + (window.__SALE_DEMO || preview ? " · preview sample" : "");
        card.classList.add("is-on");
        shown++;
        timer = setTimeout(() => { card.classList.remove("is-on"); timer = setTimeout(show, window.__SALE_DEMO || preview ? 4000 : 14000); }, 6500);
      };
      card.querySelector("button").addEventListener("click", () => {
        clearTimeout(timer); card.classList.remove("is-on"); shown = 99;
        try { sessionStorage.setItem("sn-off", "1"); } catch (e) {}
      });
      card.addEventListener("mouseenter", () => card.classList.add("is-paused"));
      card.addEventListener("mouseleave", () => card.classList.remove("is-paused"));
      setTimeout(show, window.__SALE_DEMO || preview ? 2500 : 7000);
    };
    "requestIdleCallback" in window ? requestIdleCallback(start, { timeout: 4000 }) : setTimeout(start, 2500);
  })();
  // ---------- M3U playlist checker (/iptv-checker/): parses pasted text locally, nothing is sent anywhere
  (() => {
    const box = $("[data-m3u-check]");
    if (!box) return;
    const input = $("#m3u-input", box), out = $("[data-m3u-out]", box);
    const attr = (line, name) => { const m = line.match(new RegExp(name + '="([^"]*)"', "i")); return m ? m[1].trim() : ""; };
    const el = (tag, text, cls) => { const e = document.createElement(tag); if (text != null) e.textContent = text; if (cls) e.className = cls; return e; };
    const run = () => {
      const lines = input.value.replace(/\r/g, "").split("\n").map((l) => l.trim()).filter(Boolean);
      out.textContent = "";
      if (!lines.length) { out.append(el("p", "Paste a playlist first.", "m3u-warn")); return; }
      const header = lines[0].toUpperCase().startsWith("#EXTM3U");
      const epg = header ? (attr(lines[0], "url-tvg") || attr(lines[0], "x-tvg-url")) : "";
      const items = []; let cur = null;
      for (const l of lines) {
        if (l.toUpperCase().startsWith("#EXTINF")) cur = { info: l };
        else if (!l.startsWith("#") && cur) { cur.url = l; items.push(cur); cur = null; }
      }
      const groups = new Map(), urls = new Map();
      let live = 0, movies = 0, series = 0, noId = 0, noLogo = 0, catchup = 0;
      for (const it of items) {
        const g = attr(it.info, "group-title") || "(no group)";
        groups.set(g, (groups.get(g) || 0) + 1);
        urls.set(it.url, (urls.get(it.url) || 0) + 1);
        if (/\/movie\//i.test(it.url)) movies++; else if (/\/series\//i.test(it.url)) series++; else live++;
        if (!attr(it.info, "tvg-id")) noId++;
        if (!attr(it.info, "tvg-logo")) noLogo++;
        if (/catchup|tvg-rec|timeshift/i.test(it.info)) catchup++;
      }
      const dupes = [...urls.values()].reduce((n, c) => n + (c > 1 ? c - 1 : 0), 0);
      const fmt = (n) => n.toLocaleString("en-CA");
      const rows = [
        ["Valid #EXTM3U header", header ? "Yes" : "No: most apps will reject this list", !header],
        ["Entries", fmt(items.length), !items.length],
        ["Groups", fmt(groups.size)],
        ["Live channels", fmt(live)], ["Movies", fmt(movies)], ["Series episodes", fmt(series)],
        ["EPG link in header", epg || "None: add your provider’s EPG link in the player", !epg],
        ["Entries without tvg-id (no guide)", fmt(noId), noId > 0],
        ["Entries without a logo", fmt(noLogo)],
        ["Duplicate stream URLs", fmt(dupes), dupes > 0],
        ["Entries with catch-up tags", fmt(catchup)],
      ];
      const table = el("table"), tb = el("tbody");
      for (const [k, v, warn] of rows) { const tr = el("tr"); tr.append(el("td", k), el("td", v, warn ? "m3u-warn" : "")); tb.append(tr); }
      table.append(tb); out.append(table);
      const top = [...groups.entries()].sort((a, b) => b[1] - a[1]).slice(0, 8);
      if (top.length) {
        out.append(el("p", "Largest groups:", "m3u-sub"));
        const ul = el("ul");
        top.forEach(([g, n]) => ul.append(el("li", g + ": " + fmt(n))));
        out.append(ul);
      }
      if (!items.length) out.append(el("p", "No #EXTINF entries followed by a stream URL were found.", "m3u-warn"));
    };
    $("[data-m3u-run]", box).addEventListener("click", run);
    $("[data-m3u-file]", box).addEventListener("change", (e) => {
      const f = e.target.files && e.target.files[0];
      if (!f) return;
      f.text().then((t) => { input.value = t; run(); });
    });
  })();
})();
