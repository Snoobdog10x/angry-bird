#!/bin/bash
cd /home/duythanh/projects/bots/angry-bird
git pull
python3 -m venv .venv
source .venv/bin/activate
pip install discord.py
pip install asyncio
pip install firebase-admin
pip install g4f==0.1.9.3
python3 angry-bird.py
