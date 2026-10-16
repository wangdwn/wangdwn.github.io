# wangdwn 站点分类

门户：<https://wangdw.xyz/>

本文件是根域目录的分类源。门户为两层结构：`index.html` 展示四个栏目卡片；各栏目页（`learn.html` / `life.html` / `work.html` / `flywheel.html`）列出该栏站点。每个 **活 Pages URL 只出现在一个栏目**（顶栏 / 页脚的设计系统快捷入口除外）。

视觉：门户自有 Apple 风壳（`portal.css`）+ [`/design-system/`](https://wangdw.xyz/design-system/)（`tokens.css`）。兄弟仓库请直接链接线上 CSS，不要复制一份 tokens。

栏目顺序：**学习 → 生活 → 工作 → 飞轮**。

---

## 1. 学习（learn.html）

| 站点 | 备注 | Pages |
|---|---|---|
| IESO 地球科学奥林匹克学习平台 | | [ieso-learning-site](https://wangdw.xyz/ieso-learning-site/) |
| IESO 英语词汇学习 | | [ieso-vocab](https://wangdw.xyz/ieso-vocab/) |
| 高中数学知识卡片 | | [gaozhong-shuxue-card](https://wangdw.xyz/gaozhong-shuxue-card/) |
| 数学答题 RPG | | [math-rpg](https://wangdw.xyz/math-rpg/) |
| 成绩打怪 · 进阶版 | | [gaokao.github.io](https://wangdw.xyz/gaokao.github.io/) |

---

## 2. 生活（life.html）

文学创作并入本栏。

| 站点 | 备注 | Pages |
|---|---|---|
| 诗经·风雅颂穿越指南 | 文学；页面托管在 `ieso-learning-site` 的 `shijing.html` | [shijing.html](https://wangdw.xyz/ieso-learning-site/shijing.html) |
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

---

## 3. 工作（work.html）

### 海洋系列 · 三盘一底座（工作页英雄区）

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
| 设计系统 | 同时出现在顶栏；目录卡片在本栏 | [design-system](https://wangdw.xyz/design-system/) |

---

## 5. 私密（不对外）

以下仓库不对外公开，门户不放卡片、不列 Pages URL。此处只记仓库名。

| 仓库 | 状态 |
|---|---|
| `wangdwn/classics` | private |
| `wangdwn/3D` | private |
| `wangdwn/cehui.github.io` | private |
| `wangdwn/mingli-lab` | private |

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
