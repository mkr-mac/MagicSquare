def magic(size, power):
	numbox = initval = size ** 2
	a = [1] * numbox
	maxsize = 10
	for i in range(0,numbox):
		a[i] = initval
		initval -= 1
		print a[i]
	
	a[0] -= 1
	while (a[numbox-1] < maxsize):
		a[0] += 1
		a = rollover(a, numbox, maxsize)
		if (checkem(a, numbox)):
			continue
		
	return "END"

def rollover(a, numbox, maxsize):
	for l in range(0,numbox):
		if (a[l] > maxsize):
			a[l] = 1
			a[l+1] += 1
	return a

def checkem(a, numbox):
	for j in range(0,numbox):
		for k in range(0,numbox):
			if (a[j] == a[k]):
				return True
				print "continue"

	
print(magic(3, 2))
