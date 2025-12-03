# CTF Starter Pack

Dockerベースの軽量かつ強力なCTFソルバー環境です。
Web, Pwn, Crypto, Miscなど主要ジャンルのツールがすぐに使用可能です。

## 🛠️ 推奨ホスト環境 (Host Tools)

このパック（Docker環境）に加え、Windows側に以下のGUIツールをインストールすることを強く推奨します。

1. Docker Desktop (必須)

- コンテナ実行エンジン。

2. VS Code (必須)

- エディタ。「Dev Containers」拡張機能をインストールしてください。

3. Burp Suite Community

- Web問題のプロキシ・通信改ざん用。

4. Ghidra

- Reversing問題のデコンパイル（ソースコード復元）用。

5. Wireshark

- Forensics問題のパケット解析用。

## 🚀 基本環境の起動方法 (Main Solver)

普段のCTFではこちらを使います。

1. Docker Desktop を起動します。

2. このフォルダ (CTF_Starter_Pack) を VS Code で開きます。

3. 左下の >< ボタンをクリックし、"Reopen in Container" を選択します。

4. Start Containerの文字が出ると進まなくなるのでF1キーを押した後Reload Windowをします。

5. 初回ビルドが完了し、ターミナルが root@... になれば準備完了です。

## 🧮 SageMath (Crypto) の起動手順

SageMath（高度な数学ソフト）はサイズが巨大なため、必要な時だけ別の手順で起動します。
VS Codeの中ではなく、Windowsの画面で操作してください。

### Step 1: PowerShellを開く

Windowsのスタートメニューを右クリックし、「Windows PowerShell」 または 「ターミナル」 を開きます。

### Step 2: フォルダへ移動

このパックの中にある sagemath フォルダへ移動します。
（例：デスクトップに置いた場合）

```
cd Desktop\CTF_Starter_Pack\sagemath
```

### Step 3: 起動コマンドを実行

以下のコマンドを入力します。初回はダウンロードに時間がかかります。

```
docker compose up
```

Dockerに関しての許可が求められた場合、そのまま許可してください。

### Step 4: ブラウザでアクセス（重要！）

黒い画面にたくさんの文字が流れます。最後に以下のようなURLが表示されます。

```
http://127.0.0.1:8888/?token=abcd1234...
```

1. このURLをコピーします（範囲選択して Enter または Ctrl+C）。

2. ブラウザのアドレスバーに貼り付けます。

3. 【ここが重要】 アドレスの中の 8888 を 9999 に書き換えて Enter を押します。

- 変更前: http://127.0.0.1:8888/?token=...

- 変更後: http://127.0.0.1:9999/?token=...

これで Notebook が開きます。

## 💡 ヒント

- ファイルの保存場所:
Notebook上でファイルを作成する際は、workspace フォルダの中に保存してください。そうすれば、メイン環境（VS Code）からもそのファイルが見えるようになります。

- 終了方法:
PowerShellの画面で Ctrl + C を押すと停止します。

## ⚠️ ポート設定 (Port Config)

- Web問題: ポート 1337 または 8000 の使用を推奨（Burp Suiteの 8080 と競合しないため）。

- SageMath: 上記手順の通り、ホスト側はポート 9999 を使用します。

## 📦 含まれるツール (Base)

- Python: Pwntools, PyCryptodome, Requests, Z3-Solver, Scapy

- Pwn: GDB (GEF), Checksec, ROPgadget

- Basic: Git, Curl, Vim, Netcat, Binwalk, Exiftool

## ➕ 追加機能 (Optional)

### Forensics & Reversing 拡張

Steghide, Foremost, Radare2 などの追加ツールが必要な場合は、VS Code内のターミナル で以下を実行してください。

```
bash install_tools.sh
```