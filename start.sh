#!/bin/bash
cd /home/duythanh/projects/bots/angry-bird
git pull
python3 -m venv .venv
source .venv/bin/activate
pip install g4f==0.1.9.3
python3 angry-bird.py
