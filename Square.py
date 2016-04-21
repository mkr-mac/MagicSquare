def magic(size, power):
	numbox = initval = size **power
	a = [1] * numbox
	maxsize = 102
	for i in range(0,numbox):
		a[i] = initval
		initval -= 1
		print a[i]
	
	a[0] -= 1
	while (a[numbox-1] < maxsize):
		for j in range(0,numbox):
			
	return "END"

	
print(magic(3, 2))
