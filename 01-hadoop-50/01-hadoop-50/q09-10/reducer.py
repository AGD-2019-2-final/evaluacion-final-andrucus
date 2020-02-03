import sys
#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#

if __name__ == '__main__':

    curkey = None
    total = 0
    i=0

    for line in sys.stdin:
    	if i<6:
	        texto,key,fecha,valor = line.split("\t")
	        valor = int(valor)
	        sys.stdout.write("{}\t{}\t{}\n".format(key, fecha,valor))
	        i+=1

    #sys.stdout.write("{},{}\n".format(curkey, total))