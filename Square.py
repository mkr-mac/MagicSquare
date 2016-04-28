import sys

def magic(size, power):
	#Get the number of boxes
	#and a value for giving a starting value to the boxes
	numbox = initval = size ** 2
	#The main list of the boxes
	a = [0] * (numbox)
	#Highest number to be run through
	maxsize = (numbox)**power
	print("Searching...")
	#Sets initial values for the list
	for i in xrange(numbox):
		a[i] = initval
		initval -= 1
	
	a[0] -= 1
	#Main loop
	while (a[numbox-1] < maxsize):
		a[0] += 1
		for l in xrange(numbox-1):
			if (a[l] > maxsize):
				a[l] = 1
				a[l+1] += 1

		#Duplicates restart the loop
		if (checkdubs(a)):
			continue
		#Check for solution
		addemup(a, size, power)
		
	return "END"

def checkdubs(a):
	seen = []
	indx = seen.index
	for x in a:
		#See if we've seen x before
		if x in seen:
			#If so, advance the first of the numbers
			a[0] -= 1
			a[indx(x)] += 1
			return True
		#Else Add it to our list
		seen += [x]
	return False

def addemup(a, size, power):
	f = [0] * ((size * 2) + 2)
	#Do some fancy list stuff
	for m in xrange(size):
		for n in xrange(size):
			f[m] += a[(size*m)+n] ** power
			f[m+size] += a[m+(n*size)] ** power
		f[2*size] += a[((m+1)*size)-(m+1)] ** power
		f[(2*size)+1] += a[(m*size)+m] ** power
	
	if(allsame(f)):
		#We did it!
		print("SOLUTION!!!")
		for o in a:
			print(o)

def allsame(f):
	allf = f[0]
	#Are all our additions the same?
	for y in f:
		if (y != allf):
			return False
	return True

print(magic(int(sys.argv[1]), int(sys.argv[2])))
