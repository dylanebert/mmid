import random
import numpy as np
from scipy.spatial.distance import cosine
from matplotlib import pyplot as plt
import os
from nltk.stem.snowball import SnowballStemmer

stemmer = SnowballStemmer('english')

bin_thresholds = [-1., -.13, -.01, .11, .23, .35, .47, .59, .71, .83, 1.]
num_bins = 10
bin_size = 10

concrete = []
with open('concrete_words_list.txt') as f:
    for line in f.read().splitlines():
        concrete.append(line)

dict = {}
with open('glove_mmid.txt') as f:
    for line in f.read().splitlines():
        line_split = line.split(' ')
        word = line_split[0]
        vector = [float(v) for v in line_split[1:]]
        if word in concrete:
            dict[word] = vector

marked = []

def get_random():
    word = random.choice(list(dict.keys()))
    while word in marked:
        word = random.choice(list(dict.keys()))
    return word

def get_pair(bin):
    min_similarity = bin_thresholds[bin]
    max_similarity = bin_thresholds[bin + 1]
    sim = float('-inf')
    attempts = 0
    w1 = get_random()
    w2 = get_random()
    while sim <= min_similarity or sim > max_similarity or w1 == w2 or stemmer.stem(w1) == stemmer.stem(w2):
        attempts += 1
        if attempts >= 1000:
            attempts = 0
            w1 = get_random()
        w2 = get_random()
        sim = 1 - cosine(dict[w1], dict[w2])
    return w1, w2, sim

bins = np.empty((num_bins, bin_size), dtype=object)

for i in range(num_bins):
    print('{0} of {1}'.format(i + 1, num_bins), end='\r')
    bins[i] = [None] * bin_size
    for j in range(bin_size):
        w1, w2, sim = get_pair(i)
        marked.append(w1)
        marked.append(w2)
        bins[i, j] = (w1, w2, sim)

for i in range(num_bins):
    with open(os.path.join('10b10_concrete/', '{0}.csv'.format(i + 1)), 'w+') as f:
        f.write('WordA\tWordB\tCossim\n')
        for tuple in bins[i]:
            w1, w2, sim = tuple
            f.write('{0}\t{1}\t{2}\n'.format(w1, w2, sim))
