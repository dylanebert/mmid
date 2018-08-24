import argparse
import os
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', help='input pairs file', required=True)
parser.add_argument('-o', '--output', help='directory to dump bins', required=True)
args = parser.parse_args()

if not os.path.exists(args.output):
    os.makedirs(args.output)

k = 10
h = 100

min = float(subprocess.check_output(['head', '-1', args.input]).decode('utf-8').rstrip().split('\t')[2])
max = float(subprocess.check_output(['tail', '-{0}'.format(h+1), args.input]).decode('utf-8').splitlines()[0].rstrip().split('\t')[2])
step = (max - min) / (k - 1)

with open(args.input) as f:
    i = 0
    j = 0
    bin = []
    for line in f:
        if float(line.rstrip().split('\t')[2]) >= min + step * i:
            if j < h:
                bin.append(line)
                j += 1
            else:
                i += 1
                j = 0
                with open(os.path.join(args.output, str(i)), 'w+') as r:
                    for b in bin:
                        r.write(b)
                print('Wrote bin {0} of {1}'.format(i, k))
                bin = []
