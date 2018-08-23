import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', help='input filter word list', required=True)
args = parser.parse_args()

with open(args.input) as f:
    words = f.read().splitlines()

with open('backup/pairs') as f:
    with open('{0}_pairs'.format(args.input), 'w+') as r:
        i = 0
        for line in f:
            i += 1
            if i % 1000 == 0:
                print(i, end='\r')
            w1, w2, _ = line.split('\t')
            if w1 in words and w2 in words:
                r.write(line)
