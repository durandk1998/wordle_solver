from distutils.command.build import build
from patterns import letter_counts

def load_dict(filename):
    words = []
    with open(filename, 'r') as f:
        for line in f:
            words.append(line.strip())
    return words

def filter_dict(d, word, pattern):
    pass
