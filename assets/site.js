// Stage rail (tracks which part of the chain is on screen) + scene-frame corner ticks.
(function () {
  document.documentElement.classList.add('js');
  if (!('IntersectionObserver' in window)) {
    document.querySelectorAll('.frame').forEach(function (f) { f.classList.add('in'); });
    return;
  }

  var frames = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting) { e.target.classList.add('in'); frames.unobserve(e.target); }
    });
  }, { threshold: 0.25 });
  document.querySelectorAll('.frame').forEach(function (f) { frames.observe(f); });

  var links = {};
  document.querySelectorAll('.rail a').forEach(function (a) { links[a.getAttribute('href').slice(1)] = a; });
  var current = null;
  var spy = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (!e.isIntersecting) return;
      var id = e.target.id;
      if (id === current || !links[id]) return;
      if (current && links[current]) links[current].removeAttribute('aria-current');
      links[id].setAttribute('aria-current', 'true');
      current = id;
    });
  }, { rootMargin: '-45% 0px -50% 0px' });
  Object.keys(links).forEach(function (id) {
    var el = document.getElementById(id);
    if (el) spy.observe(el);
  });
})();

// Light / dark toggle: flips the effective theme and remembers it in this browser.
(function () {
  var btn = document.querySelector('[data-theme-toggle]');
  if (!btn) return;
  btn.addEventListener('click', function () {
    var root = document.documentElement;
    var now = root.dataset.theme || (window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark');
    var next = now === 'light' ? 'dark' : 'light';
    root.dataset.theme = next;
    try { localStorage.setItem('theme', next); } catch (e) {}
  });
})();
