#! /usr/bin/env python
import sys
#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
if __name__ == "__main__":

    for line in sys.stdin:


        valor = int(line.split("	")[0])
        valor = "{:03.0f}".format(valor)
        letras = (line.split("	")[1].rstrip("\r\n")).split(",")
        for letra in letras:
            sys.stdout.write("{}\t{}\n".format(letra,valor))