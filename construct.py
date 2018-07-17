import json
from urllib.request import urlretrieve
import os

local_path = '/home/debert/mmid'
data_path = '/data/people/debert/mmid/data'
mmid_english_urls_path = '/data/people/debert/mmid/mmid_english_urls.jsonl'

def save_images(word, links):
    path = os.path.join(data_path, word)
    if not os.path.exists(path):
        os.makedirs(path)

    broken_links_file = open(os.path.join(local_path, 'broken_links', word + '.txt'), 'w+', encoding='utf-8')
    broken_links = broken_links_file.read().splitlines()

    for i, link in enumerate(links):
        filename = os.path.join(path, str(i + 1) + '.jpg')
        if not os.path.exists(filename) and link not in broken_links:
            print('Retrieving word {0}: {1} of {2}'.format(word, i + 1, len(links)), end='\r')
            try:
                urlretrieve(link, filename)
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
