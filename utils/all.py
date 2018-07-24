import csv

concreteness_words = []
dict_reader = csv.DictReader(open('concreteness.txt', 'r', encoding='utf-8'), delimiter='\t')
for row in dict_reader:
    concreteness_words.append(row['Word'])

overlap = []
with open('mmid_words_list.txt', encoding='utf-8') as f:
    for word in f.read().splitlines():
        if word in concreteness_words:
            overlap.append(word)

with open('mmid_concreteness_all.txt', 'w+', encoding='utf-8') as f:
    f.write('\n'.join(overlap))
