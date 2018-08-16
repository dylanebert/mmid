import numpy as np
from scipy.spatial.distance import cosine
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--filename', help='path to input', type=str, required=True)
parser.add_argument('-o', '--output', help='path to output', type=str, default='pairs.csv')
args = parser.parse_args()

dict = {}
with open(args.filename) as f:
    for line in f.read().splitlines():
        line_split = line.split(' ')
        dict[line_split[0]] = np.array(line_split[1:], dtype=float)

keys = list(dict.keys())
with open(args.output, 'w+') as f:
    for i, x in enumerate(keys):
        print('{0} of {1}'.format(i+1, len(keys)), end='\r')
        for j, y in enumerate(keys[(i+1):]):
            sim = 1 - cosine(dict[x], dict[y])
            f.write('{0}\t{1}\t{2}\n'.format(x, y, sim))
