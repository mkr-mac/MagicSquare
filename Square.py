import sys
from itertools import permutations

def magic(size, power):
	#Get the number of boxes
	#and a value for giving a starting value to the boxes
	numbox = initval = size ** 2
	#The main list of the boxes
	a = [0] * (numbox)
	#Sets initial values for the list
	a = [x for x in xrange(1, 1000)]
	#Main loop
	print("Starting...")
        preq = permutations(a,9)
        print("Permutations Complete!")
	#q = set(preq)
	#print("Sets Ready!")
	print("Searching...")
	for i in preq:
                #addemup(item, size, power)
                f = [0] * ((size * 2) + 2)
                #Do some fancy list stuff
                for m in xrange(size):
                        for n in xrange(size):
                                f[m] += i[(size*m)+n] ** power
                                f[m+size] += i[m+(n*size)] ** power
                        f[2*size] += i[((m+1)*size)-(m+1)] ** power
                        f[(2*size)+1] += i[(m*size)+m] ** power
                
                if(allsame(f)):
                        #We did it!
                        print("SOLUTION!!!")
                        for o in i:
                                print(o)

	return "END"

def allsame(f):
	allf = f[0]
	#Are all our additions the same?
	for y in f:
		if (y != allf):
			return False
	return True

print(magic(int(sys.argv[1]), int(sys.argv[2])))
