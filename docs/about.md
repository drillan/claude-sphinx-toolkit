# Claude Codeのカスタムスラッシュコマンドでドキュメント作業を効率化する

## はじめに

技術プロジェクトにおいて、ドキュメントの作成・更新・メンテナンスは重要な作業ですが、多くの開発者にとって煩雑で時間がかかる作業でもあります。特に、Sphinxのようなドキュメント生成ツールは高機能である反面、設定が複雑で学習コストが高いという課題があります。

本記事では、**Claude Codeのカスタムスラッシュコマンド機能**を活用して、こうした課題を解決し、効率的なドキュメント作成環境を構築する方法を紹介します。

## Claude Codeのカスタムスラッシュコマンドとは

Claude Codeは、`.claude/commands/`ディレクトリに配置したMarkdownファイルを自動的に読み込み、カスタムスラッシュコマンドとして利用できる機能を提供しています。

### 主な利点

- **プロジェクト固有の操作を標準化**: 複雑なコマンドラインや設定手順を単一のコマンドに集約
- **チーム全体での作業統一**: 同じコマンドを使うことで、メンバー間の作業方法を統一
- **学習コストの削減**: 複雑なツールの使い方を覚える必要がなく、シンプルなコマンドで操作可能
- **自動化の促進**: 手動で行っていた複数ステップの作業を自動化

### ファイル構成

このシステムは以下のファイル構成で構築されています：

```
.claude
├── commands
│   ├── sphinx-build.md
│   ├── sphinx-create.md
│   └── sphinx-update.md
├── docs
│   ├── CLAUDE.md
│   └── config
│       ├── extensions-config.md
│       └── theme-settings.md
```

- **`commands/`**: Claude Codeのカスタムスラッシュコマンド定義
- **`docs/CLAUDE.md`**: システム全体のドキュメントとガイド
- **`docs/config/`**: Sphinx設定ファイル（テーマと拡張機能）

## 実装例：Sphinxドキュメント自動化システム

本記事では、PythonのSphinxを例に、以下の3つのカスタムコマンドを実装したドキュメント自動化システムを紹介します：

### 1. `/project:sphinx-create` - プロジェクト初期化

https://github.com/drillan/claude-sphinx-toolkit/blob/main/.claude/commands/sphinx-create.md

このコマンドは以下を自動実行します：

- 必要なPythonパッケージのインストール（Sphinx、MyST Parser等）
- `pyproject.toml`からプロジェクト情報を自動取得
- Sphinxプロジェクトの初期化
- ReStructuredTextからMarkdownへの変換
- 基本的な拡張機能の有効化

### 2. `/project:sphinx-update` - 設定更新

https://github.com/drillan/claude-sphinx-toolkit/blob/main/.claude/commands/sphinx-update.md

このコマンドは以下を実行します：

- `.claude/docs/config/`の設定ファイルから設定を読み込み
- `docs/conf.py`を安全に更新
- 必要な追加パッケージを自動インストール
- 既存設定を保持しながら特定セクションのみを更新

### 3. `/project:sphinx-build` - ドキュメントビルド

https://github.com/drillan/claude-sphinx-toolkit/blob/main/.claude/commands/sphinx-build.md

このコマンドは以下を実行します：

- 依存関係の確認
- 指定形式でのドキュメントビルド（HTML、LaTeX、EPUB等）
- エラー時の詳細情報表示

## 使用方法

### 1. Claude Codeで設定を取り込み

自分のプロジェクトディレクトリで、Claude Codeを起動してメッセージを送信：

```bash
claude
```

Claude Codeが起動したら、以下のメッセージを送信：

```
https://github.com/drillan/claude-sphinx-toolkit の .claude ディレクトリを現在のプロジェクトにコピーしてください
```

Claude Codeが自動的にGitHubリポジトリから`.claude/`ディレクトリを取得して、現在のプロジェクトに設定します。

### 2. 手動でのセットアップ（オプション）

Claude Codeを使わない場合は、従来通りgit cloneでも可能です：

```bash
git clone https://github.com/drillan/claude-sphinx-toolkit.git
cp -r claude-sphinx-toolkit/.claude/ your-project/
cd your-project/
```

### 3. プロジェクト情報の設定

`pyproject.toml`にプロジェクト情報を設定します：

```toml
[project]
name = "your-project-name"
authors = [
    {name = "Your Name", email = "your.email@example.com"}
]
```

### 4. プロジェクトのCLAUDE.mdにルールを記述

プロジェクトルートの`CLAUDE.md`ファイルに、ドキュメント作成のルールを記述します：

```markdown
# CLAUDE.md

## ドキュメント作成ルール

### 基本方針
- Sphinxドキュメントシステムを使用する
- 新しいドキュメントファイル作成後は必ず `/project:sphinx-update` を実行
- ビルド前に `/project:sphinx-build` でエラーがないか確認

### 依存関係管理
- ドキュメント関連パッケージは `uv add --group docs` で管理
- 設定変更後は必ず `uv sync --group docs` を実行

### 利用可能なコマンド
- `/project:sphinx-create` - 新規Sphinxプロジェクトの初期化
- `/project:sphinx-update` - 設定更新
- `/project:sphinx-build` - ドキュメントビルド
```

このルールにより、Claude Codeが常に適切な手順でドキュメント作業を行うようになります。

### 5. Claude Codeでコマンドを実行

Claude Codeを起動し、プロジェクトディレクトリで以下のコマンドを実行：

```bash
# 初期化
/project:sphinx-create

# 設定更新
/project:sphinx-update

# ビルド
/project:sphinx-build
```

## 他の言語・ツールへの応用

この手法は、Python/Sphinxに限らず、様々な言語やドキュメントツールに応用可能です：

### 応用例

- **Node.js + JSDoc**: JavaScript/TypeScriptプロジェクトのAPI文書生成
- **Go + Hugo**: Goプロジェクトの静的サイト生成
- **Java + Maven Site**: Javaプロジェクトのサイト生成
- **Ruby + YARD**: Rubyプロジェクトのドキュメント生成
- **Rust + mdBook**: RustプロジェクトのBook形式ドキュメント

### 応用のポイント

1. **コマンドの標準化**: 言語に関係なく、`/project:doc-create`、`/project:doc-build`等の統一命名
2. **設定の外部化**: プロジェクト固有の設定を`.claude/config/`に分離
3. **依存関係管理**: 各言語のパッケージマネージャーに対応した自動インストール

## 関係者が得られる利益

### 開発者
- **時短効果**: 複雑なコマンドを覚える必要がなく、作業時間を大幅短縮
- **品質向上**: 統一された手順により、ドキュメントの品質が安定
- **ストレス軽減**: 設定ミスやコマンド間違いによるエラーを削減

### チームリーダー・プロジェクトマネージャー
- **品質管理**: 全メンバーが同じ手順でドキュメントを作成するため、品質のバラツキを削減
- **オンボーディング効率化**: 新メンバーの学習コストを大幅に削減
- **メンテナンス性向上**: 標準化された手順により、長期的なメンテナンスが容易

### 組織・企業
- **知識の属人化防止**: 標準化により、特定の人に依存しない体制を構築
- **生産性向上**: ドキュメント作成の効率化により、開発リソースをより重要な作業に集中
- **品質保証**: 一貫した品質のドキュメントにより、顧客満足度や開発効率が向上

## まとめ

Claude Codeのカスタムスラッシュコマンド機能を活用することで、複雑なドキュメント作成プロセスを大幅に簡素化できます。本記事で紹介したSphinx自動化システムは、そのまま使用することも、他のツールに応用することも可能です。

プロジェクトの特性に合わせてカスタムコマンドを作成し、チーム全体の生産性向上とドキュメント品質の向上を実現してください。

## 詳細な設定ファイル

システムの詳細な設定は、以下のファイルで管理されています：

### テーマ設定
https://github.com/drillan/claude-sphinx-toolkit/blob/main/.claude/docs/config/theme-settings.md

Sphinxのテーマとテーマオプションを管理するファイルです。Furo、Sphinx RTD Theme、Sphinx Book Themeなどの設定が可能です。

### 拡張機能設定
https://github.com/drillan/claude-sphinx-toolkit/blob/main/.claude/docs/config/extensions-config.md

Sphinxの拡張機能とその設定を管理するファイルです。MyST Parser、Autodoc、Napoleon、Intersphinxなどの設定が含まれています。

### Pythonパッケージ管理ガイド
https://github.com/drillan/claude-sphinx-toolkit/blob/main/.claude/python-package.md

uvを使用したモダンなPythonパッケージ管理の包括的なガイドです。

### ドキュメントシステム概要
https://github.com/drillan/claude-sphinx-toolkit/blob/main/.claude/docs/CLAUDE.md

アーキテクチャ、開発用コマンド、技術スタックの詳細説明です。

:::message
この記事で紹介したコード例は、[GitHub リポジトリ](https://github.com/drillan/claude-sphinx-toolkit)で公開しています。実際のファイル構成や詳細な設定については、リポジトリをご確認ください。
:::
