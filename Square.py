import sys
from itertools import permutations

def magic(size, power):
        """Today we find some magic squares! Quickly!"""
	#Get the number of boxes
	numbox = size ** 2
	#Sets initial values for the list
	a = range(1,numbox+1)
	fsize = (2*size)+2
	#Main loop
	print("Starting...")
	#Magical permutation function
        preq = permutations(a,numbox)
        print("Permutations Complete!")
	print("Searching...")
	for i in preq:
                #addemup(item, size, power)
                f = [0] * fsize
                #Do some fancy list stuff
                for n in xrange(size):
                        f[n] = sum(i[size*(n):size*(n+1)])
                        f[size+n] = sum(i[n::size])
                f[2*size] = sum(i[::size+1])
                f[2*size+1] = sum(i[size-1:numbox-1:size-1])
                
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
