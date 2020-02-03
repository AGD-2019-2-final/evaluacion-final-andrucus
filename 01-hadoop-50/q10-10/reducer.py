#!/usr/bin/env python
import sys
#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
if __name__ == '__main__':

    curkey = None
    numbers = ""


    for line in sys.stdin:
        key, val = line.split("\t")
        val = str(int(val))


        if key == curkey:

            numbers = numbers + "," + val
        else:

            if curkey is not None:

                sys.stdout.write("{}\t{}\n".format(curkey, numbers))

            curkey = key
            numbers = val
    sys.stdout.write("{}\t{}\n".format(curkey, numbers))