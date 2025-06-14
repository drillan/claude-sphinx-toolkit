**目的:** `.claude/docs/config/`の設定ファイルに基づいて`docs/conf.py`を安全に更新します。

```markdown
---
name: sphinx-update
description: Update Sphinx configuration from .claude/config/ files
---

# Sphinx 設定更新

`.claude/docs/config/`ディレクトリの設定ファイルに基づいて、`docs/conf.py`を更新します。

## 更新内容:

1. **テーマ設定の更新**
   - `.claude/docs/config/theme-settings.md`からテーマ設定を読み込み
   - `html_theme`と`html_theme_options`を更新
   - 必要なテーマパッケージを自動インストール

2. **拡張機能の更新**
   - `.claude/docs/config/extensions-config.md`から拡張機能リストを読み込み
   - `extensions`と`myst_enable_extensions`を更新
   - 必要な拡張パッケージを自動インストール

3. **安全な更新処理**
   - 既存の`conf.py`の他の設定を保持
   - 特定のセクションのみを更新
   - バックアップ作成とエラー時の復元

## 設定ファイル形式:
設定ファイルはYAML Front Matterを使用して構造化されています。

例 - `theme-settings.md`:
```yaml
---
html_theme: furo
html_theme_options:
  sidebar_hide_name: true
  light_css_variables:
    color-brand-primary: "#336790"
---