#!/usr/bin/env python

import sys


if __name__ == '__main__':

    curkey = None
    total = None
   
    for line in sys.stdin:
        key, valor = line.split("\t")
        valor = int(valor)
        
        if total is None:
          total = valor

        if key == curkey:
            
            total += valor
        else:
           
            if curkey is not None:
                
                sys.stdout.write("{} {}\n".format(curkey, total))

            curkey = key
            total = valor
     
    sys.stdout.write("{} {}\n".format(curkey, total))