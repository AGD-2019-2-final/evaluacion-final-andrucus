#!/usr/bin/env python

import sys


if __name__ == '__main__':

    curkey = None
    total = None
    total_minimo = None
   
    for line in sys.stdin:
        key, valor = line.split("\t")
        valor = float(valor)
        
        if total is None:
          total = valor

        if total_minimo is None:
          total_minimo = valor

        if key == curkey:
            
            total = max(total,valor)
            total_minimo = min(total_minimo, valor)
        else:
           
            if curkey is not None:
                
                sys.stdout.write("{}\t{}\t{}\n".format(curkey, total, total_minimo))

            curkey = key
            total = valor
            total_minimo = valor
     
    sys.stdout.write("{}\t{}\t{}\n".format(curkey, total, total_minimo))