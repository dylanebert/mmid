import json
from urllib.request import urlretrieve
import os

def save_images(word, links):
    path = os.path.join('/data/people/debert/mmid/data', word)
    if not os.path.exists(path):
        os.makedirs(path)
    for i, link in enumerate(links):
        try:
            urlretrieve(link, os.path.join(path, str(i + 1) + '.jpg'))
            print('Retrieved {0}'.format(link))
        except:
            print('Failed to retrieve {0}'.format(link))

words = open('overlap.txt', 'r', encoding='utf-8').read().splitlines()
links = []
with open('/data/people/debert/mmid_english_urls.jsonl', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        obj = json.loads(line)
        word = obj['word_string']
        if word in words:
            save_images(word, obj['images'].values())
