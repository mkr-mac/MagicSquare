import sys
from itertools import permutations

def magic(size, power):
        """Today we find some magic squares! Quickly!"""
	#Get the number of boxes
	numbox = size ** 2
	#Sets initial values for the list
	a = [x for x in xrange(1, numbox+1)]
	fsize = (2*size)+2
	#Main loop
	print("Starting...")
        preq = permutations(a,numbox)
        print("Permutations Complete!")
	print("Searching...")
	for i in preq:
                #addemup(item, size, power)
                f = [0] * fsize
                #Do some fancy list stuff
                for m in xrange(size):
                        for n in xrange(size):
                                f[m] += i[(size*m)+n] ** power
                                f[m+size] += i[m+(n*size)] ** power
                        f[2*size] += i[((m+1)*size)-(m+1)] ** power
                        f[(2*size)+1] += i[(m*size)+m] ** power
                
                allf = f[0]
                #Are all our additions the same?
                for y in f:
                        if (y != allf):
                                break
                else:
                        #We did it!
                        print("SOLUTION!!!")
                        for o in i:
                                print(o)

	return "END"

print(magic(int(sys.argv[1]), int(sys.argv[2])))
