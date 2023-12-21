#!/bin/bash 
git pull
python3 -m venv .venv
source .venv/bin/activate
pip install discord.py
pip install asyncio
pip install firebase-admin
python3 angry-bird.py
