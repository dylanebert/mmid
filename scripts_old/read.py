import csv
import numpy as np

dict_reader = csv.DictReader(open('concreteness.txt', 'r', encoding='utf-8'), delimiter='\t')
concreteness_dict = {}
for row in dict_reader:
    concreteness_dict[row['Word']] = float(row['Conc.M'])

wordsim_words = open('wordsim_words_list.txt', 'r', encoding='utf-8').read().splitlines()

with open('mmid_words_list.txt', 'r', encoding='utf-8') as f:
    words = [word for word in f.read().splitlines() if word in concreteness_dict and word not in wordsim_words]
    words_sorted = sorted(words, key=lambda word: concreteness_dict[word])
    open('concrete_words_list.txt', 'w', encoding='utf-8').write('\n'.join(words_sorted[-1000:]))
    open('abstract_words.list.txt', 'w', encoding='utf-8').write('\n'.join(words_sorted[:1000]))
