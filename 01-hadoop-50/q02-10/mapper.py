#! /usr/bin/env python
import sys
#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
if __name__ == "__main__":
	for line in sys.stdin:
		arr = line.split(',')
		purpose = arr[3]
		valor = arr[4]
		sys.stdout.write("{}\t{}\n".format(purpose,valor))