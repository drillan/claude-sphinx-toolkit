---
html_theme: furo
html_theme_options:
  sidebar_hide_name: true
  light_css_variables:
    color-brand-primary: "#336790"
    color-brand-content: "#336790"
  dark_css_variables:
    color-brand-primary: "#E5B62F"
    color-brand-content: "#E5B62F"
html_title: "プロジェクトドキュメント"
---

# Sphinxテーマ設定

このファイルはSphinxのHTMLテーマとその設定を管理します。

## 利用可能なテーマ:

### **Furo** (推奨)
モダンで清潔なデザインのテーマ
```bash
uv add furo --group docs
```

### **Sphinx RTD Theme**
Read the Docsスタイルの定番テーマ
```bash
uv add sphinx-rtd-theme --group docs
```

### **Sphinx Book Theme**  
Jupyter Bookスタイルのテーマ
```bash
uv add sphinx-book-theme --group docs
```

## テーマ固有オプション:

上記のYAML Front Matterでテーマオプションを設定できます。
`/sphinx-update`コマンドで`conf.py`に自動反映されます。