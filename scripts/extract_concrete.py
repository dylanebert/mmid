import os

with open('word_lists/nouns') as f:
    gmc_words = f.read().splitlines()
concreteness = {}
with open('concreteness/nouns') as f:
    for line in f:
        k, v = line.rstrip().split('\t')
        concreteness[k] = float(v)

cgmc = []
for word in gmc_words:
    if word in concreteness and concreteness[word] >= 4.:
        print(word)
