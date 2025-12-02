#!/bin/bash
# エラーが発生したら即停止
set -e

echo "[*] Updating repositories..."
apt-get update
apt-get install -y software-properties-common
add-apt-repository universe
apt-get update

echo "[*] Installing Forensics Tools (Steghide, Foremost)..."
# radare2 はここから削除し、下でビルドします
apt-get install -y steghide foremost git make gcc

echo "[*] Installing Radare2 (Building from source)..."
echo "    This will take a few minutes. Please wait..."

# 作業フォルダを汚さないよう /tmp で作業
cd /tmp

# 既存の残骸があれば削除
if [ -d "radare2" ]; then
    rm -rf radare2
fi

# 公式リポジトリからクローンしてビルド
git clone https://github.com/radareorg/radare2
cd radare2
sys/install.sh

echo "[*] Installation Complete!"
echo "You can now use 'steghide', 'foremost', and 'radare2'."