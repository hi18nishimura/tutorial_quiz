# 🎉 Simple Quiz App

このリポジトリは、FastAPI をバックエンドに、Streamlit をフロントエンドに用いたシンプルなクイズアプリです。

---

## 📋 ディレクトリ構成

```
quiz_app/
├─ backend/
│  └─ main.py          # FastAPI サーバー
├─ frontend/
│  └─ app.py           # Streamlit アプリ
├─ requirements.txt    # 必要ライブラリ一覧
└─ README.md           # 本ファイル
```

---

## 🔧 必要環境

### 🐍 仮想環境の作成

#### Conda の場合

```bash
# 新しい仮想環境の作成
conda create -n quiz_app python=3.13.5
# 仮想環境を有効化
conda activate quiz_app
```

#### pyenv + pyenv-virtualenv の場合

```bash
# （初回のみ）使用したい Python バージョンをインストール
pyenv install 3.13.5
# 仮想環境の作成
pyenv virtualenv 3.13.5 quiz_app_env
# 仮想環境を有効化
pyenv activate quiz_app_env
```

## 📦 ライブラリのインストール

```bash
# プロジェクトルートで実行
pip install -r requirements.txt
```

---

## 🚀 バックエンド起動（FastAPI）

1. `quiz_app` に移動
2. 以下コマンドを実行

```bash
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

3. ブラウザや API クライアントで `http://localhost:8000/quiz` にアクセスすると、クイズ一覧が JSON 形式で取得できます。

---

## 🚀 フロントエンド起動（Streamlit）

1. `quiz_app` に移動
2. 以下コマンドを実行

```bash
streamlit run frontend/app.py
```

3. ブラウザで `http://localhost:8501` にアクセスして、クイズアプリを操作できます。

---

## 🎮 使い方

1. プルダウンからクイズ問題を選択
2. 自分の回答を入力
3. 「Submit Answer」ボタンを押す
4. 正誤判定と正解が表示されます

---
