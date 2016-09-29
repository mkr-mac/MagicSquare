import sys
from itertools import permutations, imap
#@profile
def magic(size, power):
	"""Today we find some magic squares! Quickly! At least for size 3 power 1!"""
	#Get the number of boxes
	numbox = size ** 2
	sizepp = size + 1
	sizemm = size - 1
	sizedu = size * 2
	sizedo = sizedu + 1
	numboxpp = numbox + 1
	numboxmm = numbox - 1
	fsize  = sizedu + 2
	halfbox = numbox/2
	#Sets initial values for the list
	a = range(1,numboxpp)
	f = [0] * (sizedu+2)
	#Magical permutation function
	q = permutations(a,numbox)
	zz = xrange(size)
	print "Searching..."
	"""~~~Main Loop~~~"""
	for i in q:
		#Half of the numbers is enough
		if halfbox < i[0]: break
		#Do some fancy list stuff
		i = [t**power for t in i]
		for n in zz:
			f[n] = i[size*n:size*(n+1)]
			f[size+n] = i[n::size]
		f[sizedu] = i[::sizepp]
		f[sizedo] = i[sizemm:numboxmm:sizemm]
		#Are all our additions the same?
		lastf = sum(f[sizedo])
		for y in imap(sum, f):
			if (y != lastf):
				break
		else:
			#We did it!
			print "SOLUTION!"
			print i
			#The reverse is also true
			print "SOLUTION!"
			print i[::-1]

	return "END"

print(magic(int(sys.argv[1]), int(sys.argv[2])))