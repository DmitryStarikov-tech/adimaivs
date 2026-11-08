#!/bin/bash

echo "Welcome to AdimAI Installer"

INSTALL_DIR="$HOME/adimai"
mkdir -p "$INSTALL_DIR"
cd "$INSTALL_DIR" || exit

curl -s -o run_project.py https://raw.githubusercontent.com/DmitryStarikov-tech/adimaivs/main/run_project.py
curl -s -o sandbox.py https://raw.githubusercontent.com/DmitryStarikov-tech/adimaivs/main/sandbox.py

pip install --upgrade pip -q
pip install torch transformers accelerate bitsandbytes huggingface_hub matplotlib pandas datasets -q

echo "3. Starting AdimAI Terminal..."
python3 run_project.py
