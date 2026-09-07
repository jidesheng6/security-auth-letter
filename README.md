# 安全测试授权书生成

本地 / GitHub Pages 可用的离线网页：填写或随机生成授权信息，预览后导出 **PNG** / **PDF**，或打印。

在线演示：https://jidesheng6.github.io/security-auth-letter/

## 使用

- **本地**：用浏览器直接打开 `index.html`
- **在线**：打开 GitHub Pages 地址

## 目录

```
security-auth-letter/
├── index.html                 # 主页面
├── rescan-custom-fonts.py     # 扫描 fonts/custom 写入下拉列表
├── fonts/
│   ├── fonts.css
│   ├── *.woff2                # 内置开源手写 / 正文黑体宋体
│   └── custom/                # 自备字体（默认不进仓库）
└── vendor/
    ├── html2canvas.min.js
    └── jspdf.umd.min.js
```

## 自备手写字体

1. 将 `.ttf` / `.otf` / `.woff2` 放入 `fonts/custom/`
2. 运行 `python rescan-custom-fonts.py`
3. 或在页面点击「导入字体」

请勿将未授权的商业字库推送到公开仓库。

## 导出

- **PNG**：按预览整页截图
- **PDF**：单页 A4
- **打印**：浏览器打印

内置字体为 Google Fonts / 悠哉等开源授权（OFL）。
