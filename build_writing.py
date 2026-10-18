# -*- coding: utf-8 -*-
import os, re, html, glob

SRC = os.path.expanduser("~/yh_stage/txt")
SITE = os.path.expanduser("~/yh_site")
OUT = os.path.join(SITE, "novels")

POEMS = """乙未回南天 乙未春游并序 二月二宴天蓬 五一潮州观感 冬之荷 刘君晓明履新赋 午时读书
卜算子·参商 卜算子·接风 卜算子·新闻 国土房管十二载之春夏秋冬 圣彼得堡晴朗月夜 增城何屋揽胜 寻梅
岭南三月 念奴娇·凭栏听雨 新春乐·自然怡然农庄 春 春日感怀 杨春曲 沁园春·夜色羊城 游九曜园 游响沙湾
游苏泊罕草原 白云三首 窗外即景 艺博馆赏八景图 花城百花开（中华新韵版） 苏幕遮 行香子·雨中上白云山
观同好吕田桂峰照片有感 观莲花山 观鄂尔多斯成吉思汗陵 记白云评审会 访王昭君陵园 识君 贺新郎 路行
踏莎行·访敦煌 与边防指挥学院朱大校宴 过圣诞 重游六榕寺 长相思 长联 颐和山庄伯齐吟社诗歌宴
题庐江书院（中华新韵版） 骤雨打新荷 麓湖春晓 文档 题莲花山 题莲花山（中华新韵版） 甲乙午未""".split()

ZAWEN = "再论三严三实 严实 认识国情 抢唛 大盘虾奖 空白".split()

EXCLUDE = ["石头", "照片", "2015年工作总结", "手机丢失情况说明", "空白（横排） 2"]

TITLE_FIX = {"文档": "咏松", "寻梅": "行摄梅花", "花城百花开（中华新韵版）": "题牡丹宴",
             "甲乙午未": "甲乙午未", "骤雨打新荷": "骤雨打新荷", "长联": "长联"}

KIND_SUB = {"甲乙午未": "长诗", "骤雨打新荷": "元曲", "长联": "长联"}

COPYRIGHT = "© 王胜（wangdw）· 版权所有｜仅供阅读，禁止复制、转载、摘编"

TPL = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow, noarchive">
<meta name="copyright" content="%%COPY%%">
<title>%%TITLE%% · 德王府</title>
<style>
:root { --paper:#f7f1e6; --ink:#3b3428; --line:#d8cdb8; --accent:#8a6d3b; }
* { margin:0; padding:0; box-sizing:border-box; }
body {
  background:var(--paper); color:var(--ink);
  font-family:"Songti SC","STSong","SimSun",serif; line-height:2;
  -webkit-user-select:none; -moz-user-select:none; -ms-user-select:none; user-select:none;
  -webkit-touch-callout:none;
}
.container { max-width:640px; margin:0 auto; padding:56px 24px 80px; }
header { text-align:center; margin-bottom:44px; }
.back { display:inline-block; font-size:13px; color:#9a8a6e; text-decoration:none; margin-bottom:24px; letter-spacing:1px; }
h1 { font-size:26px; font-weight:normal; letter-spacing:6px; }
.subtitle { margin-top:10px; font-size:13px; color:#9a8a6e; letter-spacing:2px; }
.body { font-size:17px; }
.body p { text-indent:2em; margin-bottom:12px; text-align:justify; }
.body .poem { text-align:center; text-indent:0; margin-bottom:8px; }
.notice { text-align:center; margin-top:56px; padding-top:20px; border-top:1px solid var(--line); font-size:12px; color:#a08d6a; letter-spacing:2px; line-height:1.9; }
.toast { position:fixed; left:50%; bottom:28px; transform:translateX(-50%) translateY(20px); background:#3b3428; color:#f7f1e6; font-size:13px; letter-spacing:1px; padding:10px 18px; border-radius:4px; opacity:0; pointer-events:none; transition:.25s; }
.toast.show { opacity:.94; transform:translateX(-50%) translateY(0); }
img { -webkit-user-drag:none; pointer-events:none; }
</style>
</head>
<body>
<div class="container">
  <header>
    <a class="back" href="%%BACK%%">← %%BACKTEXT%%</a>
    <h1>%%TITLE%%</h1>
    <p class="subtitle">%%SUB%%</p>
  </header>
  <div class="body">
%%BODY%%
  </div>
  <p class="notice">%%COPY%%<br>未经作者书面许可，不得以任何形式复制、转载、摘编或用于商业用途。</p>
</div>
<div class="toast" id="toast">版权所有，仅供阅读</div>
<script>
(function(){
  var t=document.getElementById('toast');
  function warn(){ if(!t) return; t.classList.add('show'); setTimeout(function(){ t.classList.remove('show'); }, 1600); }
  ['contextmenu','copy','cut','dragstart','selectstart'].forEach(function(k){
    document.addEventListener(k, function(e){ e.preventDefault(); if(k==='copy') warn(); });
  });
  document.addEventListener('keydown', function(e){
    if((e.ctrlKey||e.metaKey) && ['c','x','s','p','a','u'].indexOf(e.key.toLowerCase())>=0){ e.preventDefault(); warn(); }
  });
})();
</script>
</body>
</html>
"""

INDEX_TPL = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow, noarchive">
<meta name="copyright" content="%%COPY%%">
<title>%%TITLE%% · 德王府</title>
<style>
:root { --paper:#f7f1e6; --ink:#3b3428; --line:#d8cdb8; --accent:#8a6d3b; }
* { margin:0; padding:0; box-sizing:border-box; }
body {
  background:var(--paper); color:var(--ink);
  font-family:"Songti SC","STSong","SimSun",serif; line-height:1.9;
  -webkit-user-select:none; -moz-user-select:none; -ms-user-select:none; user-select:none;
}
.container { max-width:560px; margin:0 auto; padding:48px 22px 70px; }
header { text-align:center; margin-bottom:30px; }
.back { display:inline-block; font-size:13px; color:#9a8a6e; text-decoration:none; margin-bottom:22px; letter-spacing:1px; }
h1 { font-size:26px; font-weight:normal; letter-spacing:6px; }
.subtitle { margin-top:9px; font-size:13px; color:#9a8a6e; letter-spacing:2px; }
h2 { font-size:15px; font-weight:normal; color:var(--accent); letter-spacing:3px; margin:34px 0 6px; padding-bottom:8px; border-bottom:1px solid var(--line); }
h2 span { font-size:12px; color:#9a8a6e; letter-spacing:1px; margin-left:8px; }
.essay { display:flex; align-items:baseline; gap:10px; padding:12px 14px; text-decoration:none; color:var(--ink); border-bottom:1px solid var(--line); }
.essay:hover { background:rgba(255,255,255,.4); }
.essay__name { font-size:17px; color:var(--ink); white-space:nowrap; }
.essay__desc { font-size:13px; color:#9a8a6e; flex:1; }
.essay__go { font-size:13px; color:var(--accent); white-space:nowrap; }
.notice { text-align:center; margin-top:40px; padding-top:18px; border-top:1px solid var(--line); font-size:12px; color:#a08d6a; letter-spacing:2px; }
</style>
</head>
<body>
<div class="container">
  <header>
    <a class="back" href="%%BACK%%">← %%BACKTEXT%%</a>
    <h1>%%TITLE%%</h1>
    <p class="subtitle">%%SUB%%</p>
  </header>
%%LIST%%
  <p class="notice">%%COPY%%</p>
</div>
</body>
</html>
"""

def read_txt(p):
    with open(p, encoding="utf-8", errors="replace") as f:
        return f.read().replace("\r\n", "\n").replace("\r", "\n")

def norm(s):
    return re.sub(r"\s+", " ", s).strip()

def nkey(s):
    return re.sub(r"[\s·・]", "", s)

POEM_KEYS = [nkey(x) for x in POEMS]
ZAWEN_KEYS = [nkey(x) for x in ZAWEN]

def match(k, keys):
    if k in keys:
        return True
    for p in keys:
        if len(p) == len(k) and sum(1 for a, b in zip(p, k) if a != b) <= 1:
            return True
        if abs(len(p) - len(k)) <= 1 and (p.endswith(k) or k.endswith(p)):
            return True
    return False

def title_of(fn, text):
    base = os.path.splitext(fn)[0]
    if base in TITLE_FIX:
        return TITLE_FIX[base]
    for line in text.split("\n"):
        line = norm(line).strip("#").strip()
        if line:
            t = line[:40]
            if "中华新韵版" in base and "新韵" not in t:
                t = t + "（中华新韵版）"
            if base == "杨春曲" and t.startswith("阳春曲"):
                return "阳春曲"
            return t
    return base

def classify(base):
    if base in EXCLUDE:
        return None
    k = nkey(base)
    if match(k, POEM_KEYS):
        return "poem"
    if k in ZAWEN_KEYS:
        return "zawen"
    return "essay"

def gen_page(kind, title, text, out_path, back, backtext, idx):
    lines = [norm(l) for l in text.split("\n")]
    lines = [l for l in lines if l and l != title]
    if lines and re.fullmatch(r"(长诗|元曲|长联)：", lines[0]):
        lines = lines[1:]
    if kind == "poem":
        body = "\n".join('<p class="poem">%s</p>' % html.escape(l) for l in lines)
        sub = KIND_SUB.get(title)
        if not sub:
            sub = "词" if ("·" in title or title in ["念奴娇·凭栏听雨","卜算子·参商","卜算子·接风","卜算子·新闻","行香子·雨中上白云山","踏莎行·访敦煌","苏幕遮","贺新郎","长相思","沁园春·夜色羊城","新春乐·自然怡然农庄"]) else "诗"
            sub = sub + " · " + ("七言" if any(len(re.sub(r"[，。！？、；：“”‘’（）]", "", l)) >= 7 for l in lines) else "五言")
    else:
        body = "\n".join("<p>%s</p>" % html.escape(l) for l in lines)
        n = len(re.sub(r"\s", "", text))
        sub = ("杂文" if kind == "zawen" else "随笔") + " · 约 %d 字" % n
    doc = (TPL.replace("%%TITLE%%", html.escape(title))
              .replace("%%SUB%%", html.escape(sub))
              .replace("%%BODY%%", body)
              .replace("%%BACK%%", back)
              .replace("%%BACKTEXT%%", html.escape(backtext))
              .replace("%%COPY%%", html.escape(COPYRIGHT)))
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(doc)

def main():
    files = sorted(glob.glob(os.path.join(SRC, "*.txt")))
    groups = {"poem": [], "essay": [], "zawen": []}
    for p in files:
        base = os.path.splitext(os.path.basename(p))[0]
        kind = classify(base)
        if not kind:
            continue
        text = read_txt(p)
        groups[kind].append((base, title_of(base, text), text))

    labels = {"poem": ("poems", "诗歌", "诗余"), "essay": ("essays", "随笔", "随笔"), "zawen": ("zawen", "杂文", "杂文")}
    meta = {}
    for kind, items in groups.items():
        d, name, backtext = labels[kind]
        os.makedirs(os.path.join(OUT, d), exist_ok=True)
        lst = []
        for i, (base, title, text) in enumerate(items, 1):
            fn = "%s%02d.html" % (d[0], i)
            gen_page(kind, title, text, os.path.join(OUT, d, fn), "/novels/%s/" % d, name, i)
            n = len(re.sub(r"\s", "", text))
            lst.append((title, fn, n))
        # 分类索引
        rows = "\n".join(
            '<a class="essay" href="/novels/%s/%s"><span class="essay__name">%s</span><span class="essay__desc">%s</span><span class="essay__go">阅读 →</span></a>'
            % (d, fn, html.escape(t), ("%d 字" % n))
            for t, fn, n in lst)
        idx = (INDEX_TPL.replace("%%TITLE%%", name)
                        .replace("%%SUB%%", "共 %d 篇 · 点击阅读" % len(lst))
                        .replace("%%LIST%%", rows)
                        .replace("%%BACK%%", "/novels/essay.html")
                        .replace("%%BACKTEXT%%", "创作")
                        .replace("%%COPY%%", html.escape(COPYRIGHT)))
        with open(os.path.join(OUT, d, "index.html"), "w", encoding="utf-8") as f:
            f.write(idx)
        meta[kind] = (name, d, len(lst))

    # 总入口 /novels/essay.html：三分栏
    def block(kind):
        name, d, n = meta[kind]
        rows = "\n".join(
            '<a class="essay" href="/novels/%s/%s%02d.html"><span class="essay__name">%s</span><span class="essay__desc">%s</span><span class="essay__go">阅读 →</span></a>'
            % (d, d[0], i, html.escape(t), ("%d 字" % len(re.sub(r"\s", "", tx))))
            for i, (b, t, tx) in enumerate(groups[kind][:6], 1)
        )
        more = '<a class="essay" href="/novels/%s/"><span class="essay__name">全部 %d 篇</span><span class="essay__desc">%s总目</span><span class="essay__go">进入 →</span></a>' % (d, n, name)
        return '<h2>%s<span>%d 篇</span></h2>\n%s\n%s' % (name, n, rows, more)

    FEATURED = [
        ("nanyuetian.html", "南粤天", "五言绝句"),
        ("qingchun-lieche.html", "青春列车", "携子返乡随笔"),
        ("tanqin-1.html", "探亲（一）", "携子探亲 · 说走就走"),
        ("tanqin-2.html", "探亲（二）", "小镇夜市 · 稻收时节"),
        ("tanqin-3.html", "探亲（三）", "汉江河岸 · 小座驾"),
        ("zhai-xigua.html", "摘西瓜", "童谣"),
        ("shangban.html", "上班", "新单位一周记"),
        ("meimei.html", "媒霉", "时评 · 郭美美与红会"),
        ("xianshu.html", "闲书", "中山图书馆书评"),
    ]
    feat_rows = "\n".join(
        '<a class="essay" href="/novels/essays/%s"><span class="essay__name">%s</span><span class="essay__desc">%s</span><span class="essay__go">阅读 →</span></a>'
        % (fn, html.escape(t), html.escape(d)) for fn, t, d in FEATURED)
    featured = '<h2>精选<span>%d 篇</span></h2>\n%s' % (len(FEATURED), feat_rows)

    hub = (INDEX_TPL.replace("%%TITLE%%", "创作")
                    .replace("%%SUB%%", "诗歌 %d · 随笔 %d · 杂文 %d" % (meta["poem"][2], meta["essay"][2], meta["zawen"][2]))
                    .replace("%%LIST%%", featured + "\n" + block("poem") + "\n" + block("essay") + "\n" + block("zawen"))
                    .replace("%%BACK%%", "https://wangdw.xyz/life.html")
                    .replace("%%BACKTEXT%%", "生活")
                    .replace("%%COPY%%", html.escape(COPYRIGHT)))
    with open(os.path.join(OUT, "essay.html"), "w", encoding="utf-8") as f:
        f.write(hub)

    print("诗歌 %d / 随笔 %d / 杂文 %d" % (meta["poem"][2], meta["essay"][2], meta["zawen"][2]))
    for k in ("poem", "essay", "zawen"):
        print(" ", k, [t for _, t, _ in groups[k]][:8])

if __name__ == "__main__":
    main()
