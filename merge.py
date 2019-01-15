#! /usr/bin/env python
import argparse

parser = argparse.ArgumentParser(description='Merge textfiles to a single file without duplicates')
parser.add_argument('filenames', metavar='F', nargs='*', type=str, help='a file or list of files for merging')
parser.add_argument('master', metavar='M', type=str, help='name of the output file')
parser.add_argument('-s', '--sort', action="store_true", default=False, help="sort the output")

args = parser.parse_args()
outlines = []

for fname in args.filenames:
    with open(fname) as infile:
        for line in infile:
            line = line.strip("\n")
            if line not in outlines:
                outlines.append(line)

if args.sort:
    outlines.sort()

with open(args.master, 'w') as outfile:
    for line in outlines:
        outfile.write(line+'\n')

print("merged to '" + str(args.master) + "'")
