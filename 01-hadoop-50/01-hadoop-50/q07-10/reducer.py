import sys

if __name__ == '__main__':
   
    for line in sys.stdin:

        concat,key,fecha,valor= line.split("\t")
        valor=int(valor)

        sys.stdout.write("{}   {}   {}\n".format(key,fecha ,valor))
            