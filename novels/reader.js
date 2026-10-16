(function () {
  'use strict';
  var root = document.documentElement;
  var KEY = 'dw-reader-fs';
  var MIN = 0.85, MAX = 1.35, STEP = 0.08;
  var scale = parseFloat(localStorage.getItem(KEY) || '1');
  if (isNaN(scale)) scale = 1;
  scale = Math.min(MAX, Math.max(MIN, scale));

  function apply() {
    root.style.setProperty('--fs', 'calc(clamp(1.0625rem, 0.95rem + 0.55vw, 1.1875rem) * ' + scale + ')');
    try { localStorage.setItem(KEY, String(scale)); } catch (e) {}
  }
  apply();

  var up = document.getElementById('fs-up');
  var down = document.getElementById('fs-down');
  if (up) up.addEventListener('click', function () {
    scale = Math.min(MAX, +(scale + STEP).toFixed(2));
    apply();
  });
  if (down) down.addEventListener('click', function () {
    scale = Math.max(MIN, +(scale - STEP).toFixed(2));
    apply();
  });

  var toc = document.getElementById('toc');
  var tocBtn = document.getElementById('toc-toggle');
  if (toc && tocBtn) {
    tocBtn.addEventListener('click', function () {
      var open = toc.hasAttribute('hidden');
      if (open) {
        toc.removeAttribute('hidden');
        tocBtn.setAttribute('aria-expanded', 'true');
      } else {
        toc.setAttribute('hidden', '');
        tocBtn.setAttribute('aria-expanded', 'false');
      }
    });
    toc.addEventListener('click', function (e) {
      if (e.target.tagName === 'A') {
        toc.setAttribute('hidden', '');
        tocBtn.setAttribute('aria-expanded', 'false');
      }
    });
  }

  // best-effort anti-copy
  var block = function (e) { e.preventDefault(); return false; };
  document.addEventListener('copy', block);
  document.addEventListener('cut', block);
  document.addEventListener('contextmenu', block);
  document.addEventListener('dragstart', block);
  document.addEventListener('selectstart', block);

  document.addEventListener('keydown', function (e) {
    var key = e.key && e.key.toLowerCase();
    var meta = e.ctrlKey || e.metaKey;
    if (!meta) return;
    if (key === 'c' || key === 'x' || key === 'a' || key === 's' || key === 'p' || key === 'u') {
      e.preventDefault();
      return false;
    }
  });
})();
