import json
import os
import urllib.request
import datetime
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', help='path to input word list file', type=str, required=True)
parser.add_argument('-o', '--output', help='path to output directory', type=str, required=True)
parser.add_argument('--broken_links', help='directory in which to store broken links', type=str, default='broken_links/')
parser.add_argument('--urls', help='mmid url file', type=str, default='backup/urls.jsonl')
args = parser.parse_args()

def save_images(word, links):
    path = os.path.join(args.output, word)
    broken_links_path = os.path.join(args.broken_links, word + '.txt')
    if not os.path.exists(path):
        os.makedirs(path)
    if not os.path.exists(broken_links_path):
        broken_links_file = open(broken_links_path, 'w+', encoding='utf-8')
    else:
        broken_links_file = open(broken_links_path, 'r+', encoding='utf-8')
    broken_links = broken_links_file.read().splitlines()

    for i, link in enumerate(links):
        timestamp = datetime.datetime.now()
        _, ext = os.path.splitext(link)
        filename = os.path.join(path, str(i + 1) + ext)
        if not os.path.exists(filename):
            if link not in broken_links:
                print('{0} Retrieving word {1}: {2} of {3}'.format(timestamp, word, i + 1, len(links)))
                try:
                    with urllib.request.urlopen(link, timeout=.5) as response:
                        info = response.info()
                        if(info.get_content_maintype() == 'image'):
                            with open(filename, 'wb') as f:
                                f.write(response.read())
                except:
                    broken_links.append(link)

    broken_links_file.write('\n'.join(broken_links))
    broken_links_file.close()

words = open(args.input, 'r', encoding='utf-8').read().splitlines()
idx = 1
with open(args.urls, encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        obj = json.loads(line)
        word = obj['word_string']
        if word in words:
            print('{0} of {1}'.format(idx, len(words)))
            idx += 1
            save_images(word, obj['images'].values())
