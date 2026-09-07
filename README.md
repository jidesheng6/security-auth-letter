# 安全测试授权书生成

本地 / CDN 可用的离线网页：填写或随机生成授权信息，预览后导出 **PNG** / **PDF**，或打印。

## 在线访问（国内无需代理）

推荐用国内可访问的 GitHub 文件 CDN（同步本仓库 `main` 分支）：

**https://cdn.jsdmirror.com/gh/jidesheng6/security-auth-letter@main/index.html**

备用（海外或已开代理时）：

- GitHub Pages：https://jidesheng6.github.io/security-auth-letter/
- 仓库：https://github.com/jidesheng6/security-auth-letter

> 说明：GitHub Pages / github.io 在大陆常需代理。jsDMirror 走公共 CDN，一般可直连；若偶发失败可多刷一次或换网络。若要更稳的独立域名托管，可用 Zeabur（`*.zeabur.app`）或腾讯云 EdgeOne Pages / CloudBase（需自行注册账号绑定仓库）。

## 本地使用

用浏览器直接打开 `index.html`（无需联网）。

## 目录

```
security-auth-letter/
├── index.html
├── rescan-custom-fonts.py
├── fonts/           # 内置开源 woff2；custom/ 放自备字体（默认不进仓库）
└── vendor/          # html2canvas、jspdf
```

## 自备手写字体

1. 将 `.ttf` / `.otf` / `.woff2` 放入 `fonts/custom/`
2. 运行 `python rescan-custom-fonts.py`
3. 或在页面点击「导入字体」

请勿将未授权的商业字库推送到公开仓库。

## 导出

- **PNG** / **PDF** / **打印**：均按右侧预览整页

内置字体为 Google Fonts / 悠哉等开源授权（OFL）。
