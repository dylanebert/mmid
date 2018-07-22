import json
import os
import urllib.request
import datetime
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--data_path', help='data path in which to save mmid data', type=str, default='/data/people/debert/mmid/data')
parser.add_argument('--broken_links_dir', help='directory in which to store broken links records', type=str, default='/home/debert/mmid/broken_links')
parser.add_argument('--urls_path', help='json file storing image urls', type=str, default='/data/people/debert/mmid/mmid_english_urls.jsonl')
parser.add_argument('--word_list_path', help='path to list of words to retrieve', type=str, default='/home/debert/mmid/test_word_list.txt')
args = parser.parse_args()

data_path = args.data_path
broken_links_dir = args.broken_links_dir
urls_path = args.urls_path
word_list_path = args.word_list_path

def save_images(word, links):
    path = os.path.join(data_path, word)
    broken_links_path = os.path.join(broken_links_dir, word + '.txt')
    if not os.path.exists(path):
        os.makedirs(path)
    if not os.path.exists(broken_links_path):
        broken_links_file = open(broken_links_path, 'w+', encoding='utf-8')
    else:
        broken_links_file = open(broken_links_path, 'r+', encoding='utf-8')
    broken_links = broken_links_file.read().splitlines()

    for i, link in enumerate(links):
        timestamp = datetime.datetime.now()
        filename = os.path.join(path, str(i + 1) + '.jpg')
        if not os.path.exists(filename):
            if link not in broken_links:
                print('{0} Retrieving word {1}: {2} of {3}'.format(timestamp, word, i + 1, len(links)))
                try:
                    response = urllib.request.urlopen(link, timeout=.5)
                    with open(filename, 'wb') as f:
                        f.write(response.read())
                except:
                    broken_links.append(link)

    broken_links_file.write('\n'.join(broken_links))
    broken_links_file.close()

words = open(word_list_path, 'r', encoding='utf-8').read().splitlines()
idx = 1
with open(urls_path, encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        obj = json.loads(line)
        word = obj['word_string']
        if word in words:
            print('{0} of {1}'.format(idx, len(words)))
            idx += 1
            save_images(word, obj['images'].values())
