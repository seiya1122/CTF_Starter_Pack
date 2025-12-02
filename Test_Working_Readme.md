# 動作確認手順書 (Testing Manual)

CTF Starter Pack のセットアップ完了後、各機能が正常に動作しているかを確認するためのチェックリストです。

## ✅ チェック 1: 基本環境の起動 (Main Environment)

- Docker Desktop が起動している（タスクバーにクジラのアイコンがある）。

- VS Codeでフォルダを開き、左下の >< ボタンから "Reopen in Container" を実行できた。

- ターミナルのプロンプトが root@...:/workspace# に変わった。
(root@...:/CTF_Starter_Pack# の場合 cd workspace/)

## ✅ チェック 2: 主要ツールの動作テスト

コンテナ内のターミナルで以下のコマンドを実行し、エラーが出ないか確認してください。

1. Python & Pwntools の確認

同梱されているテストスクリプトを実行します。

```
python3 hello_ctf.py
```

- [+] CTF Starter Pack is ready. と表示された。

- エラー（ModuleNotFoundErrorなど）が出ていない。

2. GDB (デバッガ) の確認
```
gdb -v
```

- バージョン情報が表示される。

- GDBを起動 (gdb -q) した際、GEFのカラフルなプロンプトが表示される。(q を入力すると終了可能)

3. 一般ツールの確認

```
checksec --help
ropper --version
```

- checksec のヘルプ（使用法）が表示される。

- ropper のバージョン情報が表示される。

## ✅ チェック 3: 追加機能のインストール (Optional)

コンテナ内のターミナルで以下のコマンドを実行します。(continueとか言われたらENTER押してください)

```
bash install_tools.sh
```

- インストールが最後まで完了し、Installation Complete! と表示された。

- その後、radare2 -v を実行してバージョンが表示される。

## ✅ チェック 4: SageMath (Crypto) の起動

注意: この手順は Windows側の PowerShell で行います。(一回閉じて、もう一度VSCodeのターミナルでPowerShellがおすすめ)

1. sagemath フォルダに移動し、docker compose up を実行する。

2. 表示されたURLをブラウザに貼り付け、ポートを 8888 から 9999 に変更する。

3. Notebookの画面（ファイル一覧）が表示される。

4. New ボタンから SageMath ノートブックを作成できる。

5. ノートブックで 1 + 1 を実行し、2 と表示される。

## ✅ チェック 5: ファイル同期の確認

1. **[コンテナ側]** VS Codeのターミナルで touch test_sync.txt を実行する。

2. **[Windows側]** エクスプローラーで workspace フォルダを開く。

3. ``test_sync.txt`` が即座に表示されればOK。

## ✅ チェック 6: welcome_program.pyの実行

コンテナ内のターミナルで
```
python3 welcome_program.py
```

### 全てのチェックが完了すれば、環境は完璧です。
Let's Hack!!!