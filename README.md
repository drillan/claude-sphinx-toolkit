# claude-sphinx-toolkit

Claude Code Sphinx管理システム

## 使用ワークフロー

### 前提条件

このプロジェクトの開発には以下が必要です：
- `uv`がインストールされていること
- `uv init`などでpyproject.tomlが作成されていること(推奨)

### 初期セットアップ

```bash
# 1. プロジェクト初期化
/project:sphinx-create

# 2. 設定のカスタマイズ（必要に応じて）
# .claude/config/theme-settings.md を編集
# .claude/config/extensions-config.md を編集

# 3. 設定の適用
/project:sphinx-update

# 4. ドキュメントのビルド
/project:sphinx-build
```

### 日常的な開発ワークフロー

```bash
# 1. ドキュメント編集
# docs/*.md ファイルを編集

# 2. 設定変更時（テーマや拡張機能）
/project:sphinx-update

# 4. ビルド
/project:sphinx-build
```

### 本番デプロイ前

```bash
# 1. クリーンビルド
/project:sphinx-build clean

# 2. 他の形式での出力（必要に応じて）
/project:sphinx-build latex  # PDF用
/project:sphinx-build epub   # EPUB用
```