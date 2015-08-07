import sys
import random

poem = []

for line in sys.stdin:
	line = line.strip()
	poem.append(line)

random.shuffle(poem)

for item in poem:
	print item