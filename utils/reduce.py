import csv
import os

words = []
for dir in ['10b10_abstract', '10b10_concrete', '10b30']:
    for file in os.listdir(dir):
        with open(os.path.join(dir, file)) as f:
            reader = csv.DictReader(f, delimiter='\t')
            for line in reader:
                for word in [line['WordA'], line['WordB']]:
                    if word not in words:
                        words.append(word)

words = sorted(words)
with open('binned_all.txt', 'w+') as f:
    f.write('\n'.join(words))
