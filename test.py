import csv

wordsim_words = {}
with open('wordsim_words_list.txt') as f:
    for line in f.read().splitlines():
        wordsim_words[line] = {}

with open('concreteness.txt') as f:
    dict_reader = csv.DictReader(f, delimiter='\t')
    for row in dict_reader:
        word = row['Word']
        if word in wordsim_words:
            wordsim_words[word]['Concreteness'] = row['Conc.M']
