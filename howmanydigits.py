from math import log10, floor, pi,e
import sys
for line in sys.stdin.readlines():
	n = int(line)
	if n == 0 or n == 1:
		print(1)
		continue
	val  = ((n * log10(n/e) + log10(2*pi*n)/2.0))
	print(floor(val)+1)
