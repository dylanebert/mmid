from shutil import copytree
import os

with open('word_lists/concrete') as f:
    cgmc = f.read().splitlines()

from_dir = '/data/nlp/gmc'
to_dir = '/data/nlp/cgmc'

for dir in ['train', 'dev', 'test']:
    from_path = os.path.join(from_dir, dir)
    to_path = os.path.join(to_dir, dir)
    if not os.path.exists(to_path):
        os.makedirs(to_path)
    for word in cgmc:
        from_filename = os.path.join(from_path, word)
        to_filename = os.path.join(to_path, word)
        copytree(from_filename, to_filename)
