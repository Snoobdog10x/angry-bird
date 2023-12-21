#!/bin/bash 
git pull
python3 -m venv .venv
source .venv/bin/activate
python3 angry-bird.py
