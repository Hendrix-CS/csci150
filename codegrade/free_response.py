import json
import sys
import argparse

parser = argparse.ArgumentParser(description='Check a free-response question')

parser.add_argument('md_file', type=str)
parser.add_argument('--words', type=int)
parser.add_argument('--blank', type=str)
parser.set_defaults(words=50)
parser.set_defaults(blank="Replace")

args = parser.parse_args()

word_count = 0
with open(args.md_file) as f:
    for line in f.readlines():
        if args.blank in line:
            print("Answer seems to be incomplete")
            sys.exit(1)
        elif 'CodeGrade Tag' not in line:
            word_count += len(line.split())

if word_count < args.words:
    print(f"Only {word_count} words, at least {args.words} required")
    sys.exit(1)
