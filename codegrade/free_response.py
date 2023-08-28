import json
import sys
import argparse

parser = argparse.ArgumentParser(description='Check a free-response question')

parser.add_argument('md_file', type=str)
parser.add_argument('--words', type=int)
parser.set_defaults(words=50)

args = parser.parse_args()

word_count = 0
with open(args.md_file) as f:
    for line in f.readlines():
        if '*Replace' in line:
            print("Answer seems to be blank")
            sys.exit(1)
        elif 'CodeGrade Tag' not in line:
            word_count += len(line.split())

if word_count < args.words:
    print(f"Only {word_count} words, at least {args.words} required")
    sys.exit(1)
