#! /usr/bin/env python

import sys

args = sys.argv
fullmedialist = args[args.index(str("-i"))+1]
config = args[args.index("-c")+1]
output = args[args.index("-o")+1]

print fullmedialist, "\n", config, "\n", output

outputfile = open(output, "w")
outputfile.write("Success!")
