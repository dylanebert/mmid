mmid_words = open('mmid_words_list.txt', encoding='utf-8').readlines()
wordsim_words = open('wordsim_words_list.txt', encoding='utf-8').readlines()

overlap = []
for word in mmid_words:
    if word in wordsim_words:
        overlap.append(word)

print(len(mmid_words))
print(len(wordsim_words))
print(len(overlap))

with open('overlap.txt', 'w', encoding='utf-8') as f:
    for word in overlap:
        f.write('{0}'.format(word))
