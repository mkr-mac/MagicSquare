def magic(size, power):
	numbox = initval = size ** 2
	a = [1] * numbox
	f = [0] * ((size * 2) + 2)
	maxsize = (size ** 2)
	print("Searching...")
	for i in range(0,numbox):
		a[i] = initval
		initval -= 1
	
	a[0] -= 1
	while (a[numbox-1] < maxsize):
		a[0] += 1
		a = rollover(a, numbox, maxsize)
		if (checkdubs(a)):
			continue
		addemup(a, f, size, power, numbox)
		
	return "END"

def rollover(a, numbox, maxsize):
	for l in range(0,numbox):
		if (a[l] > maxsize):
			a[l] = 1
			a[l+1] += 1
	return a
def checkdubs(a):
      try:
         iterator = iter(a)
         first = next(iterator)
         return all(first == rest for rest in iterator)
      except StopIteration:
         return True

def addemup(a, f, size, power, numbox):	
	f = [0] * ((size * 2) + 2)
	for m in range(0, size):
		for n in range(0, size):
			f[m] += a[m+n] ** power
			f[m+size] += a[m+(n*size)] ** power
		f[2*size] += a[(m*size)+(size+-m+-1)] ** power
		f[(2*size)+1] += a[(m*size)+m] ** power
	
	if(allsame(f)):
		print("SOLUTION!!!")
		for o in range(0, size**2):
			print(a[o])

def allsame(f):
	return all(x == f[0] for x in f)

print(magic(3, 1))
