#!/bin/bash
source ~/tensorflow-gpu/bin/activate
cd ~/mmid
python3 -u construct.py --word_list_path /home/debert/mmid/concrete_words_list.txt
