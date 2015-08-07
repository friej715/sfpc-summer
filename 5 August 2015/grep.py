import sys

for line in sys.stdin:
	line = line.strip()
	if 'rose' in line:
		print line
	