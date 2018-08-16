import enchant
import csv

d = enchant.Dict('en_US')

concreteness_words = []
with open('concreteness.txt') as f:
    for line in csv.DictReader(f, delimiter='\t'):
        concreteness_words.append(line['Word'])

overlap = []
with open('glove.txt') as f1:
    with open('mmid_words_list.txt') as f2:
        mmid_words = f2.read().splitlines()
        lines = f1.readlines()
        n = len(lines)
        for i, line in enumerate(lines):
            if i % 1000 == 0:
                print('{0} of {1}'.format(i, n), end='\r')
            line_split = line.split(' ')
            word = line_split[0]
            if word in mmid_words and word in concreteness_words and d.check(word):
                overlap.append(line)

with open('glove_mmid.txt', 'w+') as f:
    for line in overlap:
        f.write(line)
