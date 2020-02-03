#! /usr/bin/env python
import sys
if __name__ == "__main__":

    
    for line in sys.stdin:
        letra=line.split(' ')[0]
        cant=line.split(' ')[6]
        cant=float(cant)
        sys.stdout.write("{}\t{}\n".format(letra,cant))