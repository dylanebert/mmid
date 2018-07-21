import json
import os
import urllib.request
import datetime

local_path = '/home/debert/mmid'
data_path = '/data/people/debert/mmid/data'
mmid_english_urls_path = '/data/people/debert/mmid/mmid_english_urls.jsonl'

def save_images(word, links):
    path = os.path.join(data_path, word)
    if not os.path.exists(path):
        os.makedirs(path)

    broken_links_file = open(os.path.join(local_path, 'broken_links', word + '.txt'), 'r+', encoding='utf-8')
    broken_links = broken_links_file.read().splitlines()

    for i, link in enumerate(links):
        filename = os.path.join(path, str(i + 1) + '.jpg')
        if not os.path.exists(filename) and link not in broken_links:
            print('{0} Retrieving word {1}: {2} of {3}'.format(datetime.datetime.now(), word, i + 1, len(links)))
            try:
                response = urllib.request.urlopen(link, timeout=.5)
                with open(filename, 'wb') as f:
                    f.write(response.read())
            except:
                broken_links.append(link)

    broken_links_file.write('\n'.join(broken_links))

    print('Finished retrieving word {0}\t\t\t'.format(word))

words = open(os.path.join(local_path, 'test_word_list.txt'), 'r', encoding='utf-8').read().splitlines()
idx = 1
with open(mmid_english_urls_path, encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        obj = json.loads(line)
        word = obj['word_string']
        if word in words:
            print('{0} of {1}'.format(idx, len(words)))
            idx += 1
            save_images(word, obj['images'].values())
