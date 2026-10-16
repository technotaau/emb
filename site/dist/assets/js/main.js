/* EmbryoGenesis website · interactions · TechnoTaau Team
   Progressive enhancement: every page is fully readable without this file. */
(function () {
  'use strict';
  var d = document;
  d.documentElement.classList.add('js');
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* sticky header shadow + header height for sticky sub-bars */
  var hw = d.getElementById('headwrap');
  function onScroll() { if (hw) hw.classList.toggle('scrolled', window.scrollY > 8); }
  function setH() { if (hw) d.documentElement.style.setProperty('--header-h', hw.offsetHeight + 'px'); }
  window.addEventListener('scroll', onScroll, { passive: true });
  window.addEventListener('resize', setH);
  onScroll(); setH();

  /* mobile menu */
  var mb = d.getElementById('menuBtn'), nav = d.getElementById('siteNav');
  if (mb && nav) {
    mb.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      mb.setAttribute('aria-expanded', String(open));
    });
    d.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && nav.classList.contains('open')) { nav.classList.remove('open'); mb.setAttribute('aria-expanded', 'false'); mb.focus(); }
    });
  }

  /* dropdowns */
  d.querySelectorAll('.nav .dd > button').forEach(function (b) {
    b.addEventListener('click', function () {
      var dd = b.parentElement, open = dd.classList.toggle('open');
      b.setAttribute('aria-expanded', String(open));
    });
  });
  d.addEventListener('click', function (e) {
    d.querySelectorAll('.nav .dd.open').forEach(function (dd) {
      if (!dd.contains(e.target)) { dd.classList.remove('open'); dd.querySelector('button').setAttribute('aria-expanded', 'false'); }
    });
  });

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
        var k = e.key === 'ArrowRight' ? 1 : e.key === 'ArrowLeft' ? -1 : 0;
        if (k) { e.preventDefault(); var n = tabs[(i + k + tabs.length) % tabs.length]; n.focus(); select(n); }
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

  /* jump links */
  d.querySelectorAll('[data-jump]').forEach(function (b) {
    b.addEventListener('click', function () {
      var t = d.getElementById(b.dataset.jump);
      if (t) t.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth', block: 'start' });
    });
  });

  /* hero slider: .slides > .slide, .dots buttons */
  d.querySelectorAll('.slides').forEach(function (wrap) {
    var slides = wrap.querySelectorAll('.slide'), dots = wrap.querySelectorAll('.dots button'), i = 0, timer;
    if (slides.length < 2) return;
    function show(n) {
      i = (n + slides.length) % slides.length;
      slides.forEach(function (s, k) { s.hidden = k !== i; });
      dots.forEach(function (b, k) { b.setAttribute('aria-current', String(k === i)); });
    }
    function play() { if (!reduce) { stop(); timer = setInterval(function () { show(i + 1); }, 6000); } }
    function stop() { clearInterval(timer); }
    dots.forEach(function (b, k) { b.addEventListener('click', function () { show(k); play(); }); });
    wrap.addEventListener('mouseenter', stop); wrap.addEventListener('mouseleave', play);
    wrap.addEventListener('focusin', stop); wrap.addEventListener('focusout', play);
    show(0); play();
  });

  /* reveal on scroll */
  var rv = d.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && !reduce) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
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
