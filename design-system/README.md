# 海洋系列 · 设计系统

门户与四盘子站的视觉源文件。本仓库托管在 GitHub Pages 根域，兄弟仓库请 **直接链接线上 CSS**，不要复制一份 tokens。

## 兄弟仓库怎么接入

在页面 `<head>` 中引入（用户站 `wangdw.xyz` 根路径）：

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="http://wangdw.xyz/design-system/tokens.css">
<link rel="stylesheet" href="http://wangdw.xyz/design-system/nav.css">
```

也可用站点根绝对路径（仅本仓库页面）：

```html
<link rel="stylesheet" href="/design-system/tokens.css">
<link rel="stylesheet" href="/design-system/nav.css">
```

活样式指南：<http://wangdw.xyz/design-system/>

## 三套主题

| 选择器 | 用途 |
|---|---|
| 默认 `:root`（日光海） | 产品壳：门户、四盘看板 |
| `[data-theme="deep"]` | 地图 / 节点图 / 沉浸分析 |
| `[data-theme="gazette"]` | 仅 `marine-weekly` 红头周报体裁 |

语义色（成功 / 警告 / 危险 / 行情红涨绿跌）在浅色与深海中保持对齐；不要把机关红 `--primary` 用到看板壳上。

## 四盘强调色

- `--pan-a` 家底蓝 → [广海汇](http://wangdw.xyz/guangzhou-marine-enterprises/)
- `--pan-b` 经营青 → [监测站](http://wangdw.xyz/marine-monitor/)
- `--pan-c` 质量琥珀 → [信号灯](http://wangdw.xyz/guangzhou-ocean-dashboard/)
- `--pan-d` 底座红 → [周报档案](http://wangdw.xyz/marine-weekly/)
