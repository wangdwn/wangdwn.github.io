/* 英语碎片精读 · 会话引擎（点词 + 多样轻题） */
(function (global) {
  'use strict';

  function esc(s) {
    return String(s == null ? '' : s)
      .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  function init(data) {
    const GLOSS = data.gloss || {};
    const ACTIVITIES = data.activities || [];
    const glossEl = document.getElementById('gloss');
    const prog = document.getElementById('prog');
    let activeGw = null;
    const results = [];

    function showGloss(key, el) {
      const g = GLOSS[key];
      if (!g) return;
      if (activeGw) activeGw.classList.remove('is-on');
      activeGw = el || null;
      if (activeGw) activeGw.classList.add('is-on');
      document.getElementById('g-word').textContent = key;
      let wsp = document.getElementById('g-wspeak');
      if (!wsp) { wsp = document.createElement('button'); wsp.id='g-wspeak'; wsp.type='button'; wsp.className='gloss__speak'; wsp.textContent='\uD83D\uDD0A'; wsp.setAttribute('aria-label','读单词'); document.getElementById('g-word').insertAdjacentElement('afterend', wsp); }
      wsp.onclick = ev => { ev.stopPropagation(); biteSpeak(key, wsp); };
      document.getElementById('g-ph').textContent = g.ph || '';
      document.getElementById('g-cn').textContent = g.cn || '';
      const exEl = document.getElementById('g-ex');
      exEl.textContent = '';
      if (g.ex) {
        const sb = document.createElement('button');
        sb.type = 'button'; sb.className = 'gloss__speak'; sb.textContent = '\uD83D\uDD0A';
        sb.setAttribute('aria-label', '读例句');
        sb.addEventListener('click', ev => { ev.stopPropagation(); biteSpeak(g.ex, sb); });
        exEl.appendChild(sb);
        exEl.appendChild(document.createTextNode(' ' + g.ex));
      }
      let exzh = document.getElementById('g-exzh');
      if (!exzh) {
        exzh = document.createElement('div');
        exzh.id = 'g-exzh'; exzh.className = 'gloss__exzh';
        exEl.insertAdjacentElement('afterend', exzh);
      }
      exzh.textContent = g.exzh || '';
    const rootEl = document.getElementById('g-root');
    if (rootEl) {
      if (g.root) {
        rootEl.hidden = false;
        rootEl.innerHTML = '词根馆 · <a href="https://wangdw.xyz/ieso-vocab/#root=' + encodeURIComponent(g.root) + '" target="_blank" rel="noopener">' + g.root + (g.rootMeaning ? '（' + g.rootMeaning + '）' : '') + '</a>';
      } else {
        rootEl.hidden = true;
        rootEl.innerHTML = '';
      }
    }
      const badge = document.getElementById('g-badge');
      if (badge) badge.hidden = !g.gaokao;
      glossEl.classList.add('show');
      glossEl.setAttribute('aria-hidden', 'false');
    }
    function hideGloss() {
      glossEl.classList.remove('show');
      glossEl.setAttribute('aria-hidden', 'true');
      if (activeGw) activeGw.classList.remove('is-on');
      activeGw = null;
      document.querySelectorAll('.b-wordtag.is-on').forEach(t => t.classList.remove('is-on'));
    }

    document.querySelectorAll('.gw').forEach(el => {
      el.addEventListener('click', e => {
        e.stopPropagation();
        const key = el.getAttribute('data-w');
        if (glossEl.classList.contains('show') && activeGw === el) hideGloss();
        else showGloss(key, el);
      });
    });
    const closeBtn = document.getElementById('gloss-close');
    if (closeBtn) closeBtn.addEventListener('click', hideGloss);
    document.addEventListener('click', e => {
      if (!glossEl.contains(e.target) && !e.target.classList.contains('gw') && !e.target.closest('.b-wordtag')) hideGloss();
    });

    const grid = document.getElementById('wordgrid');
    if (grid) {
      Object.keys(GLOSS).forEach(k => {
        const g = GLOSS[k];
        const btn = document.createElement('button');
        btn.type = 'button';
        btn.className = 'b-wordtag' + (g.gaokao ? ' gaokao' : '');
        const short = (g.cn || '').split('；')[0].split('（')[0];
        btn.innerHTML = esc(k) + ' <small>' + esc(short) + '</small>';
        btn.addEventListener('click', e => {
          e.stopPropagation();
          document.querySelectorAll('.b-wordtag.is-on').forEach(t => t.classList.remove('is-on'));
          btn.classList.add('is-on');
          const gw = document.querySelector('.gw[data-w="' + k + '"]');
          showGloss(k, gw);
          if (gw) gw.scrollIntoView({ behavior: 'smooth', block: 'center' });
        });
        grid.appendChild(btn);
      });
    }

    const quizRoot = document.getElementById('quiz');
    const doneEl = document.getElementById('done');
    const doneMsg = document.getElementById('done-msg');
    const retryBtn = document.getElementById('retry');

    function markDone(idx, ok) {
      results[idx] = ok;
      maybeFinish();
    }
    function scoredCount() {
      return results.filter(r => r === true || r === false).length;
    }
    function scoredTotal() {
      return ACTIVITIES.filter(a => a.type !== 'reflect').length;
    }
    function maybeFinish() {
      if (scoredCount() < scoredTotal()) return;
      const n = results.filter(r => r === true).length;
      const total = scoredTotal();
      const gaokao = Object.keys(GLOSS).filter(k => GLOSS[k].gaokao);
      if (doneMsg) {
        doneMsg.textContent =
          '记词与理解题对了 ' + n + '/' + total + '。' +
          (gaokao.length ? '朱砂词可抄：' + gaokao.join(' / ') + '。' : '') +
          '下一篇回书架继续。';
      }
      if (doneEl) {
        doneEl.classList.add('show');
        doneEl.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      }
    }

    function renderMcq(item, idx, card) {
      const opts = document.createElement('div');
      opts.className = 'q-opts';
      let answered = false;
      item.opts.forEach((text, oi) => {
        const b = document.createElement('button');
        b.type = 'button';
        b.className = 'q-opt';
        b.innerHTML = '<span class="mark">' + String.fromCharCode(65 + oi) + '</span><span>' + esc(text) + '</span>';
        b.addEventListener('click', () => {
          if (answered) return;
          answered = true;
          opts.querySelectorAll('.q-opt').forEach((x, i) => {
            x.disabled = true;
            if (i === item.ans) x.classList.add('is-right');
            if (i === oi && oi !== item.ans) x.classList.add('is-wrong');
            if (i === oi) x.classList.add('is-pick');
          });
          const fb = card.querySelector('[data-fb]');
          fb.textContent = (oi === item.ans ? '✓ 对了。' : '✗ 再看一眼原文。') + ' ' + (item.why || '');
          fb.classList.add('show');
          markDone(idx, oi === item.ans);
        });
        opts.appendChild(b);
      });
      card.appendChild(opts);
    }

    function renderMatch(item, idx, card) {
      const pairs = item.pairs.slice();
      const left = pairs.map((p, i) => ({ i, cn: p.cn }));
      const right = pairs.map((p, i) => ({ i, en: p.en })).sort(() => Math.random() - 0.5);
      let pickL = null, pickR = null, matched = 0, locked = false;
      const hint = document.createElement('p');
      hint.className = 'act-hint';
      hint.textContent = '先点中文，再点对应英文（或反过来）。';
      card.appendChild(hint);
      const row = document.createElement('div');
      row.className = 'match-row';
      const colL = document.createElement('div');
      colL.className = 'match-col';
      const colR = document.createElement('div');
      colR.className = 'match-col';
      left.forEach(x => {
        const b = document.createElement('button');
        b.type = 'button';
        b.className = 'match-chip';
        b.dataset.side = 'l';
        b.dataset.i = String(x.i);
        b.textContent = x.cn;
        colL.appendChild(b);
      });
      right.forEach(x => {
        const b = document.createElement('button');
        b.type = 'button';
        b.className = 'match-chip';
        b.dataset.side = 'r';
        b.dataset.i = String(x.i);
        b.textContent = x.en;
        colR.appendChild(b);
      });
      row.appendChild(colL);
      row.appendChild(colR);
      card.appendChild(row);
      const fb = card.querySelector('[data-fb]');

      function clearPick() {
        row.querySelectorAll('.match-chip.is-pick').forEach(c => c.classList.remove('is-pick'));
        pickL = pickR = null;
      }
      function tryPair() {
        if (pickL == null || pickR == null || locked) return;
        const ok = pickL === pickR;
        const bl = row.querySelector('.match-chip[data-side="l"][data-i="' + pickL + '"]');
        const br = row.querySelector('.match-chip[data-side="r"][data-i="' + pickR + '"]');
        if (ok) {
          bl.classList.add('is-done');
          br.classList.add('is-done');
          bl.disabled = br.disabled = true;
          matched++;
          clearPick();
          if (matched >= pairs.length) {
            fb.textContent = '✓ 配对完成。语境里再扫一遍这些词会更牢。';
            fb.classList.add('show');
            markDone(idx, true);
          }
        } else {
          bl.classList.add('is-miss');
          br.classList.add('is-miss');
          locked = true;
          setTimeout(() => {
            bl.classList.remove('is-miss');
            br.classList.remove('is-miss');
            clearPick();
            locked = false;
          }, 450);
        }
      }
      row.addEventListener('click', e => {
        const b = e.target.closest('.match-chip');
        if (!b || b.disabled || locked) return;
        const side = b.dataset.side;
        const i = +b.dataset.i;
        if (side === 'l') {
          row.querySelectorAll('[data-side="l"].is-pick').forEach(c => c.classList.remove('is-pick'));
          b.classList.add('is-pick');
          pickL = i;
        } else {
          row.querySelectorAll('[data-side="r"].is-pick').forEach(c => c.classList.remove('is-pick'));
          b.classList.add('is-pick');
          pickR = i;
        }
        tryPair();
      });
    }

    function renderCloze(item, idx, card) {
      const wrap = document.createElement('div');
      wrap.className = 'cloze-body';
      const blanks = [];
      const parts = item.text.split(/\{\{(\d+)\}\}/g);
      parts.forEach((part, pi) => {
        if (pi % 2 === 0) {
          wrap.appendChild(document.createTextNode(part));
        } else {
          const sel = document.createElement('select');
          sel.className = 'cloze-sel';
          sel.dataset.bi = String(blanks.length);
          const opt0 = document.createElement('option');
          opt0.value = '';
          opt0.textContent = '…';
          sel.appendChild(opt0);
          const bank = item.bank.slice().sort(() => Math.random() - 0.5);
          bank.forEach(w => {
            const o = document.createElement('option');
            o.value = w;
            o.textContent = w;
            sel.appendChild(o);
          });
          blanks.push(sel);
          wrap.appendChild(sel);
        }
      });
      card.appendChild(wrap);
      const check = document.createElement('button');
      check.type = 'button';
      check.className = 'b-btn b-btn--ghost act-check';
      check.textContent = '核对填空';
      card.appendChild(check);
      const fb = card.querySelector('[data-fb]');
      let done = false;
      check.addEventListener('click', () => {
        if (done) return;
        let ok = true;
        blanks.forEach((sel, i) => {
          const want = item.answers[i];
          if (sel.value === want) {
            sel.classList.add('is-right');
            sel.classList.remove('is-wrong');
          } else {
            ok = false;
            sel.classList.add('is-wrong');
            sel.classList.remove('is-right');
          }
          sel.disabled = true;
        });
        done = true;
        check.disabled = true;
        fb.textContent = (ok ? '✓ 填对了。' : '✗ 有空错了，答案是：' + item.answers.join(' / ') + '。') + ' ' + (item.why || '');
        fb.classList.add('show');
        markDone(idx, ok);
      });
    }

    function renderUsage(item, idx, card) {
      const opts = document.createElement('div');
      opts.className = 'q-opts';
      let answered = false;
      item.sents.forEach((text, oi) => {
        const b = document.createElement('button');
        b.type = 'button';
        b.className = 'q-opt';
        b.innerHTML = '<span class="mark">' + String.fromCharCode(65 + oi) + '</span><span>' + esc(text) + '</span>';
        b.addEventListener('click', () => {
          if (answered) return;
          answered = true;
          opts.querySelectorAll('.q-opt').forEach((x, i) => {
            x.disabled = true;
            if (i === item.ans) x.classList.add('is-right');
            if (i === oi && oi !== item.ans) x.classList.add('is-wrong');
            if (i === oi) x.classList.add('is-pick');
          });
          const fb = card.querySelector('[data-fb]');
          fb.textContent = (oi === item.ans ? '✓ 这句用法对。' : '✗ 再比一下语境。') + ' ' + (item.why || '');
          fb.classList.add('show');
          markDone(idx, oi === item.ans);
        });
        opts.appendChild(b);
      });
      card.appendChild(opts);
    }

    function renderRecall(item, idx, card) {
      const prompt = document.createElement('p');
      prompt.className = 'recall-prompt';
      prompt.innerHTML = '中文提示：<b>' + esc(item.cn) + '</b>';
      card.appendChild(prompt);
      const timer = document.createElement('div');
      timer.className = 'recall-timer';
      timer.textContent = '准备…';
      card.appendChild(timer);
      const opts = document.createElement('div');
      opts.className = 'q-opts';
      opts.hidden = true;
      card.appendChild(opts);
      const fb = card.querySelector('[data-fb]');
      const choices = item.choices.slice().sort(() => Math.random() - 0.5);
      let answered = false;
      let left = item.seconds || 30;
      const startBtn = document.createElement('button');
      startBtn.type = 'button';
      startBtn.className = 'b-btn b-btn--ghost act-check';
      startBtn.textContent = '开始 ' + left + ' 秒回忆';
      card.insertBefore(startBtn, opts);

      function endTimer() {
        timer.textContent = '时间到，选出英文词';
        opts.hidden = false;
        startBtn.hidden = true;
      }

      startBtn.addEventListener('click', () => {
        startBtn.disabled = true;
        timer.textContent = left + ' 秒';
        const iv = setInterval(() => {
          left--;
          if (left <= 0) {
            clearInterval(iv);
            endTimer();
          } else {
            timer.textContent = left + ' 秒';
          }
        }, 1000);
      });

      choices.forEach(w => {
        const b = document.createElement('button');
        b.type = 'button';
        b.className = 'q-opt';
        b.innerHTML = '<span class="mark">·</span><span>' + esc(w) + '</span>';
        b.addEventListener('click', () => {
          if (answered || opts.hidden) return;
          answered = true;
          const ok = w === item.ans;
          opts.querySelectorAll('.q-opt').forEach(x => {
            x.disabled = true;
            if (x.textContent.trim() === item.ans || x.querySelector('span:last-child').textContent === item.ans) {
              x.classList.add('is-right');
            }
          });
          b.classList.add(ok ? 'is-pick' : 'is-wrong');
          fb.textContent = (ok ? '✓ 记得住。' : '✗ 答案是 ' + item.ans + '。') + ' ' + (item.why || '');
          fb.classList.add('show');
          markDone(idx, ok);
        });
        opts.appendChild(b);
      });
    }

    function renderReflect(item, card) {
      const ta = document.createElement('textarea');
      ta.className = 'reflect-ta';
      ta.rows = 3;
      ta.placeholder = item.prompt || '用一两句中文写下你想到的（只存本机，可不填）。';
      card.appendChild(ta);
      const save = document.createElement('button');
      save.type = 'button';
      save.className = 'b-btn b-btn--ghost act-check';
      save.textContent = '记下（可选）';
      card.appendChild(save);
      const key = 'bite-reflect-' + (data.id || location.pathname);
      try {
        const prev = localStorage.getItem(key);
        if (prev) ta.value = prev;
      } catch (e) {}
      const fb = card.querySelector('[data-fb]');
      save.addEventListener('click', () => {
        try { localStorage.setItem(key, ta.value || ''); } catch (e) {}
        fb.textContent = ta.value.trim() ? '已记在本机。想改随时再写。' : '空着也没关系，回书架即可。';
        fb.classList.add('show');
      });
    }

    const typeLabel = {
      match: '配对记词',
      cloze: '语境填空',
      usage: '用法辨识',
      recall: '限时回忆',
      mcq: '读懂了吗',
      reflect: '随手一想（可选）'
    };

    function renderAll() {
      quizRoot.innerHTML = '';
      results.length = 0;
      ACTIVITIES.forEach(() => results.push(null));
      if (doneEl) doneEl.classList.remove('show');
      ACTIVITIES.forEach((item, idx) => {
        const card = document.createElement('div');
        card.className = 'q-card';
        const label = typeLabel[item.type] || '练习';
        card.innerHTML =
          '<div class="q-type">' + esc(label) + '</div>' +
          '<div class="q">' + (item.type === 'reflect' ? '' : (idx + 1) + '. ') + esc(item.q || '') + '</div>';
        const fb = document.createElement('div');
        fb.className = 'q-fb';
        fb.dataset.fb = '1';
        if (item.type === 'mcq') renderMcq(item, idx, card);
        else if (item.type === 'match') renderMatch(item, idx, card);
        else if (item.type === 'cloze') renderCloze(item, idx, card);
        else if (item.type === 'usage') renderUsage(item, idx, card);
        else if (item.type === 'recall') renderRecall(item, idx, card);
        else if (item.type === 'reflect') renderReflect(item, card);
        card.appendChild(fb);
        quizRoot.appendChild(card);
      });
    }

    if (retryBtn) retryBtn.addEventListener('click', renderAll);
    renderAll();

    function onScroll() {
      const el = document.getElementById('article');
      if (!el || !prog) return;
      const rect = el.getBoundingClientRect();
      const total = el.offsetHeight - window.innerHeight * 0.35;
      const scrolled = Math.min(Math.max(-rect.top, 0), Math.max(total, 1));
      const p = Math.min(100, Math.round((scrolled / Math.max(total, 1)) * 100));
      prog.style.width = p + '%';
    }
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  global.BiteSession = { init: init };
})(window);

/* 朗读：站点内预生成英语音频，手机不需要安装英语语音 */
var __biteAudio = null;
var __biteMap = null;
var __biteMapPromise = null;
var __biteToken = 0;
function loadBiteAudioMap() {
  if (__biteMap) return Promise.resolve(__biteMap);
  if (__biteMapPromise) return __biteMapPromise;
  __biteMapPromise = fetch('/learn/english-bite/audio/index.json')
    .then(function (r) { if (!r.ok) throw new Error('audio index'); return r.json(); })
    .then(function (j) { __biteMap = j; return j; })
    .catch(function (e) { __biteMapPromise = null; throw e; });
  return __biteMapPromise;
}
function biteAudioHit(map, text) {
  if (!map || !text) return null;
  var t = String(text).trim();
  if (map.words && map.words[t]) return { kind: 'w', id: map.words[t] };
  if (map.sentences && map.sentences[t]) return { kind: 's', id: map.sentences[t] };
  if (map.passages && map.passages[t]) return { kind: 'p', id: map.passages[t] };
  var lower = t.toLowerCase();
  if (map.wordsLower && map.wordsLower[lower]) return { kind: 'w', id: map.wordsLower[lower] };
  return null;
}
function freshBiteAudio() {
  if (__biteAudio) {
    try { __biteAudio.pause(); } catch (e) {}
  }
  var audio = __biteAudio || new Audio();
  audio.setAttribute('playsinline', '');
  audio.setAttribute('webkit-playsinline', '');
  __biteAudio = audio;
  try { audio.play(); } catch (e) {}
  return audio;
}
function playBiteSrc(audio, src, btn, onended) {
  audio.onended = onended || function () { if (btn) btn.classList.remove('is-on'); };
  audio.onerror = function () {
    if (btn) { btn.classList.remove('is-on'); btn.classList.add('is-bad'); }
  };
  audio.src = src;
  audio.load();
  var play = audio.play();
  if (play && play.catch) {
    play.catch(function () {
      if (btn) { btn.classList.remove('is-on'); btn.classList.add('is-bad'); }
    });
  }
}
function biteSpeak(text, btn) {
  if (!text) return;
  var token = ++__biteToken;
  document.querySelectorAll('.b-speak.is-on,.gloss__speak.is-on,#read-all.is-on,.b-speak.is-bad,.gloss__speak.is-bad,#read-all.is-bad').forEach(function (b) {
    b.classList.remove('is-on');
    b.classList.remove('is-bad');
  });
  if (btn) btn.classList.add('is-on');
  var audio = freshBiteAudio();
  loadBiteAudioMap().then(function (map) {
    if (token !== __biteToken) return;
    var hit = biteAudioHit(map, text);
    if (!hit) throw new Error('missing audio');
    playBiteSrc(audio, '/learn/english-bite/audio/' + hit.kind + '/' + hit.id + '.mp3', btn);
  }).catch(function () {
    if (btn) { btn.classList.remove('is-on'); btn.classList.add('is-bad'); }
  });
}
function biteSpeakAll() {
  var btn = document.getElementById('read-all');
  var token = ++__biteToken;
  var paras = Array.prototype.map.call(document.querySelectorAll('.b-en .b-para'), function (p) {
    return p.getAttribute('data-en') || '';
  }).filter(Boolean);
  document.querySelectorAll('.b-speak.is-on,.gloss__speak.is-on,#read-all.is-on').forEach(function (b) {
    b.classList.remove('is-on');
  });
  if (btn) btn.classList.add('is-on');
  var i = 0;
  var audio = freshBiteAudio();
  function next() {
    if (token !== __biteToken) return;
    if (i >= paras.length) {
      if (btn) btn.classList.remove('is-on');
      return;
    }
    var text = paras[i++];
    loadBiteAudioMap().then(function (map) {
      if (token !== __biteToken) return;
      var hit = biteAudioHit(map, text);
      if (!hit) throw new Error('missing audio');
      playBiteSrc(audio, '/learn/english-bite/audio/' + hit.kind + '/' + hit.id + '.mp3', btn, next);
    }).catch(function () {
      if (btn) { btn.classList.remove('is-on'); btn.classList.add('is-bad'); }
    });
  }
  next();
}
loadBiteAudioMap().catch(function () {});
function biteToggleZh() {
  document.body.classList.toggle('show-zh');
  var b = document.getElementById('toggle-zh');
  if (b) b.classList.toggle('is-on', document.body.classList.contains('show-zh'));
}
