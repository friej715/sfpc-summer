import sys
import random

for line in sys.stdin:
	line = line.strip()
	words = line.split(" ")
	random.shuffle(words)
	recombined = " ".join(words)
	print recombined