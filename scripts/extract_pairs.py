import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', help='input filter word list', required=True)
parser.add_argument('-f', '--filename', help='pairs filename', default='backup/pairs')
parser.add_argument('-o', '--output', help='output filename', default='extracted_pairs')
args = parser.parse_args()

with open(args.input) as f:
    words = f.read().splitlines()

with open(args.filename) as f:
    with open(args.output, 'w+') as r:
        i = 0
        for line in f:
            i += 1
            if i % 1000 == 0:
                print(i, end='\r')
            w1, w2, _ = line.split('\t')
            if w1 in words and w2 in words:
                r.write(line)
