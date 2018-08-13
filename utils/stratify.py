import random
import numpy as np
from scipy.spatial.distance import cosine
from matplotlib import pyplot as plt
import os

bin_thresholds = [-.25, -.15, -.05, .05, .15, .25, .35, .45, .55, .65, .75]

dict = {}
with open('glove_mmid.txt') as f:
    for line in f.read().splitlines():
        line_split = line.split(' ')
        word = line_split[0]
        vector = [float(v) for v in line_split[1:]]
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
    while sim <= min_similarity or sim > max_similarity or w1 == w2:
        attempts += 1
        if attempts >= 100:
            attempts = 0
            w1 = get_random()
        w2 = get_random()
        sim = 1 - cosine(dict[w1], dict[w2])
    return w1, w2, sim

bins = np.empty((10, 30), dtype=object)

for i in range(10):
    print('{0} of 10'.format(i + 1), end='\r')
    bins[i] = [None] * 30
    for j in range(30):
        w1, w2, sim = get_pair(i)
        marked.append(w1)
        marked.append(w2)
        bins[i, j] = (w1, w2, sim)

for i in range(10):
    with open(os.path.join('10b30/', '{0}.csv'.format(i + 1)), 'w+') as f:
        f.write('WordA\tWordB\tCossim\n')
        for tuple in bins[i]:
            w1, w2, sim = tuple
            f.write('{0}\t{1}\t{2}\n'.format(w1, w2, sim))
