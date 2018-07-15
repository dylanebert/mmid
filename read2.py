import csv

words = []
with open('combined.csv') as f:
    for row in csv.reader(f):
        for word in row[:1]:
            if word not in words:
                words.append(word)

with open('wordsim_words_list.txt', 'w', encoding='utf-8') as f:
    for word in words:
        f.write('{0}\n'.format(word))
