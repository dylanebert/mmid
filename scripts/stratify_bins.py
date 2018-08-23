import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', help='input file', required=True)
args = parser.parse_args()

with open(args.input) as f:
    words = f.read().splitlines()
