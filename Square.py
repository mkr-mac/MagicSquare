import sys

def magic(size, power):
	numbox = initval = size ** 2
	a = [1] * (numbox + 1)
	f = [0] * ((size * 2) + 2)
	maxsize = (size ** 2)
	print("Searching...")
	for i in range(0,numbox):
		a[i] = initval
		initval -= 1
	
	a[0] -= 1
	while (a[numbox-1] < maxsize):
		a[0] += 1
		rollover(a, numbox, maxsize)
		if (checkdubs(a, numbox)):
			continue
		addemup(a, f, size, power, numbox)
		
	return "END"

def rollover(a, numbox, maxsize):
	for l in range(0,numbox):
		if (a[l] > maxsize):
			a[l] = 1
			a[l+1] += 1

def checkdubs(a, numbox):
	seen = []
	for x in range(0,numbox):
		if a[x] in seen:
			a[0] -= 1
			a[seen.index(a[x])] += 1
			return True
		seen.append(a[x])
	return False

def addemup(a, f, size, power, numbox):	
	
	#print a[8]
	f = [0] * ((size * 2) + 2)
	for m in range(0, size):
		for n in range(0, size):
			f[m] += a[(size*m)+n] ** power
			f[m+size] += a[m+(n*size)] ** power
		f[2*size] += a[((m+1)*size)-(m+1)] ** power
		f[(2*size)+1] += a[(m*size)+m] ** power
	
	if(allsame(f)):
		print("SOLUTION!!!")
		for o in range(0, size**2):
			print(a[o])

def allsame(f):
	seeni = set()
	seeni.add(f[0])
	for y in f:
		if y not in seeni:
			return False
	return True

print(magic(int(sys.argv[1]), int(sys.argv[2])))
