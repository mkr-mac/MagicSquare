import sys
from itertools import permutations, imap

def magic(size, power):
	"""Today we find some magic squares! Quickly!"""
	#Get the number of boxes
	numbox = size ** 2
	sizepp = size + 1
	sizemm = size - 1
	sizedu = size * 2
	sizedo = sizedu + 1
	numboxpp = numbox + 1
	numboxmm = numbox - 1
	fsize  = sizedu + 2
	#Sets initial values for the list
	a = range(1,numboxpp)
	forig = [0] * (sizedu+2)
	#Main loop
	print "Starting..."
	#Magical permutation function
	q = permutations(a,numbox)
	print "Permutations Complete!"
	print "Searching..."
	for i in q:
		if numbox/2 < i[0]: break
		f = forig
		#Do some fancy list stuff
		for n in xrange(size):
			f[n] = i[size*n:size*(n+1)]
			f[size+n] = i[n::size]
		f[sizedu] = i[::sizepp]
		f[sizedo] = i[sizemm:numboxmm:sizemm]
		#Are all our additions the same?
		allf = sum(f[sizedo])
		for y in imap(sum, f):
			if (y != allf):
				break
		else:
			#We did it!
			print "SOLUTION!"
			print i
			print "SOLUTION!"
			print i[::-1]

	return "END"

print(magic(int(sys.argv[1]), int(sys.argv[2])))
