/* EmbryoGenesis website · interactions · TechnoTaau Team
   Progressive enhancement: every page is fully readable without this file. */
(function () {
  'use strict';
  var d = document;
  d.documentElement.classList.add('js');
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* sticky header: only .site-head sticks (the utility bar and strip scroll away).
     --header-h / --jump-h feed html{scroll-padding-top}, so anchors, jump buttons and
     keyboard focus never land under the sticky bars. */
  var hw = d.getElementById('headwrap'), sh = d.querySelector('.site-head') || hw, root = d.documentElement;
  var jumpBar = d.querySelector('.jump');
  function onScroll() { if (sh) sh.classList.toggle('scrolled', window.scrollY > 8); }
  function setH() {
    if (sh) root.style.setProperty('--header-h', sh.offsetHeight + 'px');
    var jh = jumpBar && getComputedStyle(jumpBar).position === 'sticky' ? jumpBar.offsetHeight : 0;
    root.style.setProperty('--jump-h', jh + 'px');
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  window.addEventListener('resize', setH);
  onScroll(); setH();
  if (d.fonts && d.fonts.ready) d.fonts.ready.then(setH);

  /* mobile menu */
  var mb = d.getElementById('menuBtn'), nav = d.getElementById('siteNav');
  function closeMenu(focusBtn) { if (!nav || !nav.classList.contains('open')) return; nav.classList.remove('open'); mb.setAttribute('aria-expanded', 'false'); if (focusBtn) mb.focus(); }
  if (mb && nav) {
    mb.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      mb.setAttribute('aria-expanded', String(open));
    });
    d.addEventListener('click', function (e) { if (!nav.contains(e.target) && !mb.contains(e.target)) closeMenu(false); });
  }

  /* dropdowns (disclosure pattern): click/Enter/Space toggles, ArrowDown opens and moves in,
     Escape closes and returns focus, leaving the group closes it. Hover opening is CSS-only on
     hover-capable desktops. */
  function ddSet(dd, open) { dd.classList.toggle('open', open); dd.querySelector('button').setAttribute('aria-expanded', String(open)); }
  d.querySelectorAll('.nav .dd').forEach(function (dd) {
    var b = dd.querySelector('button'), items = function () { return Array.prototype.slice.call(dd.querySelectorAll('.ddmenu a')); };
    b.addEventListener('click', function () { ddSet(dd, !dd.classList.contains('open')); });
    dd.addEventListener('keydown', function (e) {
      var list = items(), i = list.indexOf(d.activeElement);
      if (e.key === 'ArrowDown') { e.preventDefault(); ddSet(dd, true); (list[i + 1] || list[0]).focus(); }
      else if (e.key === 'ArrowUp' && i > -1) { e.preventDefault(); (list[i - 1] || b).focus(); }
      else if (e.key === 'Escape' && dd.classList.contains('open')) { e.stopPropagation(); ddSet(dd, false); b.focus(); }
    });
    dd.addEventListener('focusout', function (e) { if (e.relatedTarget && !dd.contains(e.relatedTarget)) ddSet(dd, false); });
  });
  d.addEventListener('click', function (e) {
    d.querySelectorAll('.nav .dd.open').forEach(function (dd) { if (!dd.contains(e.target)) ddSet(dd, false); });
  });
  d.addEventListener('keydown', function (e) { if (e.key === 'Escape') closeMenu(true); });

  /* tabs: [role=tablist][data-group] with [data-tab] buttons and .tpanel[data-group] panels */
  d.querySelectorAll('[role="tablist"][data-group]').forEach(function (list) {
    var g = list.dataset.group, tabs = Array.prototype.slice.call(list.querySelectorAll('[data-tab]'));
    function select(t) {
      tabs.forEach(function (x) { var on = x === t; x.setAttribute('aria-selected', String(on)); x.tabIndex = on ? 0 : -1; });
      d.querySelectorAll('.tpanel[data-group="' + g + '"]').forEach(function (p) { p.hidden = p.id !== t.dataset.tab; });
    }
    tabs.forEach(function (t, i) {
      t.addEventListener('click', function () { select(t); });
      t.addEventListener('keydown', function (e) {
        var n = e.key === 'ArrowRight' ? tabs[(i + 1) % tabs.length] : e.key === 'ArrowLeft' ? tabs[(i - 1 + tabs.length) % tabs.length]
          : e.key === 'Home' ? tabs[0] : e.key === 'End' ? tabs[tabs.length - 1] : null;
        if (n) { e.preventDefault(); n.focus(); select(n); }
      });
    });
  });

  /* filter chips: [data-filter-group] buttons filter [data-cat] items inside the same <main> */
  d.querySelectorAll('[data-filter-group]').forEach(function (bar) {
    var scope = bar.closest('main') || d;
    bar.querySelectorAll('button').forEach(function (b) {
      b.addEventListener('click', function () {
        bar.querySelectorAll('button').forEach(function (x) { x.setAttribute('aria-pressed', String(x === b)); });
        var f = b.dataset.filter;
        scope.querySelectorAll('[data-cat]').forEach(function (c) { c.hidden = !(f === 'all' || c.dataset.cat.split(' ').indexOf(f) > -1); });
      });
    });
  });

  /* jump links: scroll (html scroll-padding keeps the target clear of the sticky bars),
     move keyboard focus to the target, and mark the section currently in view */
  var jumps = Array.prototype.slice.call(d.querySelectorAll('[data-jump]'));
  jumps.forEach(function (b) {
    b.addEventListener('click', function () {
      var t = d.getElementById(b.dataset.jump);
      if (!t) return;
      setH();
      t.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth', block: 'start' });
      if (!t.hasAttribute('tabindex')) t.setAttribute('tabindex', '-1');
      t.focus({ preventScroll: true });
    });
  });
  if (jumps.length && 'IntersectionObserver' in window) {
    var seen = {};
    var jio = new IntersectionObserver(function (es) {
      es.forEach(function (e) { seen[e.target.id] = e.isIntersecting; });
      var cur = null;
      jumps.forEach(function (b) { if (!cur && seen[b.dataset.jump]) cur = b; });
      jumps.forEach(function (b) { if (b === cur) b.setAttribute('aria-current', 'true'); else b.removeAttribute('aria-current'); });
    }, { rootMargin: '-30% 0px -55% 0px' });
    jumps.forEach(function (b) { var t = d.getElementById(b.dataset.jump); if (t) jio.observe(t); });
  }

  /* hero slider: .slides > .slide, .dots buttons */
  d.querySelectorAll('.slides').forEach(function (wrap) {
    var slides = wrap.querySelectorAll('.slide'), dots = wrap.querySelectorAll('.dots button'), i = 0, timer, started = false;
    if (slides.length < 2) return;
    function show(n) {
      i = (n + slides.length) % slides.length;
      slides.forEach(function (s, k) { s.hidden = k !== i; s.classList.toggle('is-in', started && k === i); });
      dots.forEach(function (b, k) { b.setAttribute('aria-current', String(k === i)); });
    }
    function play() { stop(); timer = setInterval(function () { if (!d.hidden) show(i + 1); }, 6000); }
    function stop() { clearInterval(timer); }
    var paused = reduce, dotbar = wrap.querySelector('.dots');
    var ctl = d.createElement('button');
    ctl.type = 'button'; ctl.className = 'slidectl';
    function label() {
      ctl.setAttribute('aria-label', paused ? 'Play slideshow' : 'Pause slideshow'); ctl.textContent = paused ? '\u25B6' : '\u275A\u275A';
      wrap.setAttribute('aria-live', paused ? 'polite' : 'off');
    }
    ctl.addEventListener('click', function () { paused = !paused; label(); if (paused) stop(); else play(); });
    if (dotbar) { dotbar.appendChild(ctl); label(); }
    var resume = function () { if (!paused) play(); };
    dots.forEach(function (b, k) { b.addEventListener('click', function () { show(k); resume(); }); });
    wrap.addEventListener('mouseenter', stop); wrap.addEventListener('mouseleave', resume);
    wrap.addEventListener('focusin', stop); wrap.addEventListener('focusout', resume);
    show(0); started = true; resume();
  });

  /* reveal on scroll; children of card grids get a short stagger via --rv-i (see add-qc.css) */
  var rv = d.querySelectorAll('.reveal'), GRID = '.cards,.cards3,.cards4,.care,.pgrid,.tgrid,.centres3,.duo,.duo2,.aca-hub,.aca-cgrid,.keyfacts,.gallery';
  function staggered(el) {
    var gs = Array.prototype.slice.call(el.querySelectorAll(GRID)); if (el.matches(GRID)) gs.push(el);
    var kids = []; gs.forEach(function (g) { Array.prototype.forEach.call(g.children, function (c, k) { kids.push([c, k]); }); });
    return kids;
  }
  function revealIn(el) {
    el.classList.add('in');
    var kids = staggered(el);
    /* drop the stagger once it has played so hover transitions are not delayed */
    setTimeout(function () { kids.forEach(function (x) { x[0].style.removeProperty('--rv-i'); }); }, reduce ? 0 : 1400);
  }
  if ('IntersectionObserver' in window && !reduce) {
    rv.forEach(function (el) { staggered(el).forEach(function (x) { x[0].style.setProperty('--rv-i', Math.min(x[1], 6)); }); });
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { revealIn(e.target); io.unobserve(e.target); } });
    }, { rootMargin: '0px 0px -8% 0px' });
    rv.forEach(function (el) { io.observe(el); });
  } else { rv.forEach(function (el) { el.classList.add('in'); }); }

  /* forms: until a backend is connected (WordPress Forminator / CRM), show a confirmation.
     Set data-endpoint on a form to POST it as FormData. */
  d.querySelectorAll('form[data-lead]').forEach(function (f) {
    f.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!f.checkValidity()) { f.reportValidity(); return; }
      var msg = f.querySelector('.form-msg');
      var done = function () { if (msg) { msg.hidden = false; msg.focus && msg.focus(); } f.querySelectorAll('button[type=submit]').forEach(function (b) { b.disabled = true; }); };
      if (f.dataset.endpoint) {
        fetch(f.dataset.endpoint, { method: 'POST', body: new FormData(f) }).then(done, done);
      } else { done(); }
    });
  });

  /* current year */
  d.querySelectorAll('[data-year]').forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();
