#!/bin/bash
source ~/tensorflow-gpu/bin/activate
cd ~/mmid
python3 -u -l gpus=1 construct.py
