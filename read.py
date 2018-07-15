import json

words = []
with open('mmid_english_urls.jsonl', encoding='utf-8') as f:
    lines = f.readlines()
    length = len(lines)
    for i, line in enumerate(lines):
        if i % 100 == 0:
            print('Reading word {0} of {1}'.format(i, length), end='\r')
        obj = json.loads(line)
        words.append(obj['word_string'])
    print('Finished reading words')

with open('mmid_words_list.txt', 'w', encoding='utf-8') as f:
    for word in words:
        f.write('{0}\n'.format(word))
