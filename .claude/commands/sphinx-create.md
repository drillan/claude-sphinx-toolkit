---
name: sphinx-create
description: Initialize new Sphinx project with MyST Markdown support
---

# Sphinx プロジェクト初期化

新しいSphinxドキュメントプロジェクトを作成し、MyST Markdownサポートを自動設定します。

## 前提条件

- パッケージはuvで管理する
- ドキュメント関連のパッケージは `uv add` コマンドのオプションに `--group docs` をつける

## 実行内容:

1. **環境準備**
   ```bash
   # 必要なパッケージをインストール
   uv add sphinx --group docs
   uv add "myst-parser" --group docs

2. プロジェクト情報取得

PROJECT_NAME:

- pyproject.tomlからproject.nameとauthors[0].nameを取得
- 取得できない場合は `basename $PWD` (プロジェクトルートのディレクトリ名)から取得

AUTHOR_NAME:

- pyproject.tomlからauthors[0].nameを取得
- 取得できない場合は次の優先順位で取得
  - `git config --get user.name` (Gitのユーザ名)
  - `$USER` (OSのユーザ名)から取得

3. Sphinxプロジェクト作成

`sphinx-quickstart -q -p "PROJECT_NAME" -a "AUTHOR_NAME" ./docs`

4. Markdownへ変換

```bash
uvx --from "rst-to-myst[sphinx]" rst2myst convert docs/index.rst
rm docs/index.rst
```

5. 初期設定適用

- .claude/docs/config/の設定ファイルから初期テーマを適用
- 基本的な拡張機能を有効化

6. MyST拡張機能 (デフォルト):

- amsmath (数式サポート)
- attrs_inline (インライン属性)
- colon_fence (コロンコードブロック)
- deflist (定義リスト)
- dollarmath (ドル記号数式)
- fieldlist (フィールドリスト)
- html_admonition (HTML警告)
- html_image (HTML画像)
- linkify (自動リンク)
- replacements (テキスト置換)
- smartquotes (スマートクォート)
- strikethrough (取り消し線)
- substitution (置換)
- tasklist (タスクリスト)

linkifyを使う場合、次のコマンドでパッケージを追加する

`uv add linkify linkify-it-py --group docs`

7. ビルドのテスト

ドキュメントのビルドは @.claude/commands/sphinx-build.md に従って実行します