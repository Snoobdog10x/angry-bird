#!/bin/bash
cd /home/duythanh/projects/bots/angry-bird
echo '[INFO] git update project'
git restore --staged .
git restore .
git pull
python3 -m venv .venv
source .venv/bin/activate
echo '[INFO] install discord.py'
pip install discord.py --quiet
echo '[INFO] install discord.py[voice]'
python3 -m pip install -U "discord.py[voice]"
echo '[INFO] install asyncio'
pip install asyncio --quiet
echo '[INFO] install firebase-admin'
pip install firebase-admin --quiet
echo '[INFO] install g4f'
pip install g4f==0.1.9.3 --quiet
echo '[INFO] install redis'
pip install redis --quiet

python3 angry-bird.py
