# wangdwn 站点分类

门户：<https://wangdw.xyz/>

本文件是根域目录的分类源。门户为两层结构：`index.html` 展示四个栏目卡片；学习／生活／工作为分栏卡片门户（第二层再进目录），飞轮仍为列表。每个 **活 Pages URL 只出现在一个栏目**（顶栏 / 页脚的设计系统快捷入口除外）。

视觉：门户自有 Apple 风壳（`portal.css`）+ [`/design-system/`](https://wangdw.xyz/design-system/)（`tokens.css`）。兄弟仓库请直接链接线上 CSS，不要复制一份 tokens。

栏目顺序：**学习 → 生活 → 工作 → 飞轮**。

---

## 1. 学习（learn.html）

学习栏为分栏门户（与生活栏同构）：五个卡片（地球科学 / 高考学科馆 / 心理学馆 / 精读书架 / 读书笔记）。分栏入口在仓库根目录：`/learn-ieso.html` 等；正文仍在 `learn/` 与兄弟 Pages。

| 分栏 | 入口 | 收录 |
|---|---|---|
| 地球科学 | [/learn-ieso.html](https://wangdw.xyz/learn-ieso.html) | [ieso-learning-site](https://wangdw.xyz/ieso-learning-site/) |
| 高考学科馆 | [/learn-gaokao.html](https://wangdw.xyz/learn-gaokao.html) | [gaokao 馆壳](https://wangdw.xyz/learn/gaokao/) · 英数物化地子页 |
| 心理学馆 | [/learn-psychology.html](https://wangdw.xyz/learn-psychology.html) | [psychology](https://wangdw.xyz/learn/psychology/) · 生活里的心理小故事 |
| 精读书架 | [/learn-english.html](https://wangdw.xyz/learn-english.html) | [english-bite](https://wangdw.xyz/learn/english-bite/) · 星级沉浸短文 |
| 读书笔记 | [/learn-notes.html](https://wangdw.xyz/learn-notes.html) | [reading-notes](https://wangdw.xyz/learn/reading-notes/)（不进马斯克知识库） |

### 高考学科馆（分栏内）

| 站点 | 备注 | Pages |
|---|---|---|
| 高考学科馆壳 | 英数物化地统一入口；暑假卡／母题已分类 | [gaokao](https://wangdw.xyz/learn/gaokao/) |
| 英语子页 | 词根馆深链；阅读见精读书架 | [english](https://wangdw.xyz/learn/gaokao/english.html) |
| 词根馆（ieso-vocab） | 88 根 · 约 3500 词 · 只练根 | [ieso-vocab](https://wangdw.xyz/ieso-vocab/) |
| 数学子页 | 知识卡片 · RPG · 成绩打怪 · 暑假卡／母题 | [math](https://wangdw.xyz/learn/gaokao/math.html) |
| 物理子页 | 暑假卡 8 张 · 母题地图／卷 | [physics](https://wangdw.xyz/learn/gaokao/physics.html) |
| 化学子页 | 母题地图 + 22 题母题卷（暑假卡待补） | [chemistry](https://wangdw.xyz/learn/gaokao/chemistry.html) |
| 地理子页 | 暑假卡 15 张 · IESO 衔接 | [geography](https://wangdw.xyz/learn/gaokao/geography.html) |
| 钰霖暑假学习卡 | 数物地 + 学习法 · 支持 ?cat= 分科 | [summer-cards](https://wangdw.xyz/gaozhong-shuxue-card/summer-cards.html) |
| 母题地图 · 母题卷 | 数学／物理／化学 · 高一–高二 | [muti](https://wangdw.xyz/gaozhong-shuxue-card/muti.html) |
| 高中数学知识卡片 | 人教 A 版必修一二 | [gaozhong-shuxue-card](https://wangdw.xyz/gaozhong-shuxue-card/) |
| 数学答题 RPG | 副本闯关 + 卡片联动 | [math-rpg](https://wangdw.xyz/math-rpg/) |
| 成绩打怪 · 进阶版 | 分数战报 · 本机存储 | [gaokao.github.io](https://wangdw.xyz/gaokao.github.io/) |

## 2. 生活（life.html）

生活栏为分栏门户：六个卡片（小说 / 日记 / 随笔 / 诗歌 / 阅读 / 城市与日常）+ 实验归档。因 GitHub Pages 上 `life.html` 与 `life/` 目录撞名，分栏入口放在仓库根目录：`/life-novels.html` 等；`life/` 下旧路径保留为 meta-refresh。诗经迁至根目录 `/shijing/`。正文仍在 `novels/`，旧文章 URL 不变。

| 分栏 | 入口 | 收录 |
|---|---|---|
| 小说 | [/life-novels.html](https://wangdw.xyz/life-novels.html) | 《木棉泣血》→ [/novels/mucian-qixue.html](https://wangdw.xyz/novels/mucian-qixue.html) |
| 日记 | [/life-diary.html](https://wangdw.xyz/life-diary.html) | 《小子日记》→ [/novels/diary.html](https://wangdw.xyz/novels/diary.html) |
| 随笔 | [/life-essays.html](https://wangdw.xyz/life-essays.html) | 生活记 + 随笔 e01–e20 + 杂文 z01–z06（各只列一次；旧 `novels/essays/` · `novels/zawen/` 索引跳转至此） |
| 诗歌 | [/life-poetry.html](https://wangdw.xyz/life-poetry.html) | 短章 + 自作 p01–p51（各只列一次；旧 `novels/poems/` 索引跳转至此） |
| 阅读 | [/life-reading.html](https://wangdw.xyz/life-reading.html) | 《闲书》书评 + 诗经两册（`/shijing/`）；读书笔记仍在学习栏 |
| 城市与日常 | [/life-city.html](https://wangdw.xyz/life-city.html) | 城脉千年 · 装机优化工具 |

### 城市与日常（分栏内）

| 站点 | 备注 | Pages |
|---|---|---|
| 数字广州 · 城脉千年 | 历代城图与城市考古 | [chengmai-qiannian](https://wangdw.xyz/chengmai-qiannian/) |
| 装机优化工具 | | [pc-setup-tool](https://wangdw.xyz/pc-setup-tool/) |

### 实验与归档（生活页默认折叠）

| 站点 | 说明 | Pages |
|---|---|---|
| Pro Split-Flap Clock | 实验时钟 | [ipad.clock.github.io](https://wangdw.xyz/ipad.clock.github.io/) |
| Pro Split-Flap Clock (iclock) | 实验时钟 | [ipad.iclock.github.io](https://wangdw.xyz/ipad.iclock.github.io/) |
| Tech-Noir Clock iPad2 | 实验时钟 | [clock.ipad2.github.io](https://wangdw.xyz/clock.ipad2.github.io/) |
| Pro Split-Flap Clock (ipad) | 实验时钟 | [iclock-ipad-github.io](https://wangdw.xyz/iclock-ipad-github.io/) |
| 蔚蓝之城：珠江口传奇 | 游戏 | [web.game.github.io](https://wangdw.xyz/web.game.github.io/) |
| 中秋音乐卡 | 一次性节日页 | [zhongqiu-card](https://wangdw.xyz/zhongqiu-card/) |


## 3. 工作（work.html）

工作栏为分栏门户（与生活／学习同构）：五个卡片（家底盘 / 经营盘 / 质量盘 / 周报底座 / 专业工具）。分栏入口：`/work-assets.html` 等。

| 分栏 | 入口 | 收录 |
|---|---|---|
| 家底盘 | [/work-assets.html](https://wangdw.xyz/work-assets.html) | [广海汇](https://wangdw.xyz/guangzhou-marine-enterprises/) · [节点地图](https://wangdw.xyz/ocean-node-map/) |
| 经营盘 | [/work-ops.html](https://wangdw.xyz/work-ops.html) | [结构判断台](https://wangdw.xyz/structure.html) · [监测站](https://wangdw.xyz/marine-monitor/) · [深度分析](https://wangdw.xyz/gz-marine-analysis/) · [招标雷达](https://wangdw.xyz/geo-ocean-bidding/) |
| 质量盘 | [/work-quality.html](https://wangdw.xyz/work-quality.html) | [海洋经济信号灯](https://wangdw.xyz/guangzhou-ocean-dashboard/) |
| 周报底座 | [/work-weekly.html](https://wangdw.xyz/work-weekly.html) | [海洋周报](https://wangdw.xyz/marine-weekly/) |
| 专业工具 | [/work-tools.html](https://wangdw.xyz/work-tools.html) | 奖励申报 · 论文库 · GeoLibre · 土地测算 |

### 海洋系列 · 三盘一底座（分栏明细）

把海洋经济当成一家「巨型企业」的数字镜像：家底 / 经营 / 质量 / 政策底座。

| 盘 | 主站 | 子站 / 并入 | Pages |
|---|---|---|---|
| A 家底 | 广海汇·企业全景看板 | 涉海创新节点地图 | [guangzhou-marine-enterprises](https://wangdw.xyz/guangzhou-marine-enterprises/) · [ocean-node-map](https://wangdw.xyz/ocean-node-map/) |
| B 经营 | 结构判断台 | 监测站、深度分析、招标雷达 | [structure.html](https://wangdw.xyz/structure.html) · [marine-monitor](https://wangdw.xyz/marine-monitor/) · [gz-marine-analysis](https://wangdw.xyz/gz-marine-analysis/) · [geo-ocean-bidding](https://wangdw.xyz/geo-ocean-bidding/) |
| C 质量 | 海洋经济信号灯 | — | [guangzhou-ocean-dashboard](https://wangdw.xyz/guangzhou-ocean-dashboard/) |
| D 底座 | 海洋周报·时间序列档案 | — | [marine-weekly](https://wangdw.xyz/marine-weekly/) |

本仓库内的 `/funding/`、`/map/` 是跳转到经营盘对应页的快捷入口，不算独立站点。

### 需定期刷新数据

- **A 家底**：企业名录 / 三表画像 / 节点地图采集
- **B 经营**：政策口径、产业数据、招标雷达
- **C 质量**：海温 / 港口 / AIS / 灾害 / 企业风险信号
- **D 底座**：按期写周报并归档


### 内容健康检查（2026-10-17）

- **结构判断台** `data/structure_judgment.json` 与 `marine-monitor/app/public/data/structure_judgment.json` 对齐（含游艇盘）。
- **涉海创新节点地图** 已切到广海汇名录 roster 模式（672 节点）；政采 discovery 仍可用 scraper 另行刷新。
- **质量盘** 已接库内证据包（专项资金/政策/招标/名录 sector/NOAA 海温）；格子=有迹/无迹，非景气随机灯。港口吞吐量·AIS·灾害预警仍未接入。产业树代表企业仍为结构样例。
- **`/funding/`、`/map/`** 快捷入口改为站内相对跳转至 `marine-monitor`。

### 专业工具

| 站点 | 备注 | Pages |
|---|---|---|
| 地海测·科技奖励申报指南 | **内容会过期，需定期刷新** | [awards-guide](https://wangdw.xyz/awards-guide/) |
| 高端论文数据库 | **内容会过期，需定期刷新** | [paper-db](https://wangdw.xyz/paper-db/) |
| GeoLibre 使用手册 | 学术工具 | [geolibre-manual](https://wangdw.xyz/geolibre-manual/) |
| 土地出让测算与监测校准 | | [parcel-decision-workbench](https://wangdw.xyz/parcel-decision-workbench/) |

---

## 4. AI 飞轮（flywheel.html）

| 站点 | 备注 | Pages |
|---|---|---|
| AI 智学工坊 | | [ai-learning-hub](https://wangdw.xyz/ai-learning-hub/) |
| 马斯克知识库 | | [muskpedia](https://wangdw.xyz/muskpedia/) |
| 极简 Markdown 编辑器 | 知识飞轮写作工具 | [md-viewer](https://wangdw.xyz/md-viewer/) |
| 命理实验室 | 八字／铁板学术小工具；Pages 已开；robots 仍 Disallow（软私密，未改） | [mingli-lab](https://wangdw.xyz/mingli-lab/) |
| 设计系统 | 同时出现在顶栏；目录卡片在本栏 | [design-system](https://wangdw.xyz/design-system/) |

---

## 5. 私密（不对外）

以下仓库不对外公开，门户不放卡片、不列 Pages URL。此处只记仓库名。

| 仓库 | 状态 |
|---|---|
| `wangdwn/classics` | private |
| `wangdwn/3D` | private |
| `wangdwn/cehui.github.io` | private |

---

## 仓库但无强 Pages 入口

| 仓库 | 说明 |
|---|---|
| [sites](https://github.com/wangdwn/sites) | 旧版站点索引，功能已由本仓库门户取代 |
| [tg-relay](https://github.com/wangdwn/tg-relay) | Telegram API relay，非 Pages 产品 |
| [telegram-bot](https://github.com/wangdwn/telegram-bot) | 机器人，非 Pages 产品 |

根域仓库本身：本站（[wangdwn.github.io](https://github.com/wangdwn/wangdwn.github.io)）。

---

## 维护约定

1. **新站点**：先写入本文件对应栏目，再在对应栏目 HTML 加入口；同一 URL 不要出现在两个栏目。
2. **海洋系列新子站**：挂在工作页 A/B/C/D 对应宫格的「子模块 / 并入」行，不要再在其他栏目重复。
3. **时钟 / 一次性实验**：默认进生活页「实验与归档」，用 `<details>` 收起。
4. **刷新节奏**：四盘 + `awards-guide` + `paper-db` 视为内容型站点，资料或数据过期时优先更新这几处。
5. **私密仓库**：只记仓库名，不写公开 Pages URL，也不在门户放卡片。
6. **数字人文**：新专题先进生活栏；古地图类须先过地图审图与图源授权，未过审的只留本地离线版，不上线。

- 十八里铺（长篇小说）：[shibali](http://wangdw.xyz/shibali/) · 归入 生活 → 小说 · 只读 + 版权声明
