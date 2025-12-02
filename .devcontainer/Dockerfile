# ベースイメージ
FROM ubuntu:22.04

# 設定
ENV DEBIAN_FRONTEND=noninteractive
ENV LANG C.UTF-8

# 1. 安定しているメインリポジトリのツールのみをインストール
# ※ エラー回避のため Universeリポジトリや重いツール(SageMath等)は除外
RUN apt-get update && apt-get install -y \
    build-essential \
    gdb \
    git \
    curl \
    wget \
    vim \
    nano \
    netcat-openbsd \
    iputils-ping \
    libssl-dev \
    libffi-dev \
    python3 \
    python3-pip \
    python3-dev \
    bsdmainutils \
    file \
    binutils \
    nasm \
    binwalk \
    exiftool \
    && rm -rf /var/lib/apt/lists/*

# 2. Pythonライブラリ (安定版)
# SageMathの代用として z3-solver や pycryptodome を搭載
RUN pip3 install --no-cache-dir \
    pwntools \
    pycryptodome \
    requests \
    ipykernel \
    tqdm \
    z3-solver \
    scapy \
    ropper

# 3. GDB GEF (デバッグ画面の強化プラグイン)
RUN wget -O ~/.gdbinit-gef.py -q https://gef.blah.cat/py \
    && echo "source ~/.gdbinit-gef.py" >> ~/.root_gdbinit \
    && echo "source ~/.gdbinit-gef.py" >> ~/.gdbinit

WORKDIR /workspace
CMD ["/bin/bash"]