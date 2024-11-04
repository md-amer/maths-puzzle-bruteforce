from itertools import permutations
from time import time

start = time()

perm = permutations(range(1,10))

perm = list(perm)

for j in range(l):
	combo = perm[j]
	a = combo[0]
	b = combo[1]
	c = combo[2]
	d = combo[3]
	e = combo[4]
	f = combo[5]
	g = combo[6]
	h = combo[7]
	i = combo[8]
	
	if 9+a-6 == b-3:
		if 4+d*5-f == 6:
			if 8-5 == g-h*2:
				if c+1+7-4 == 8:
					if 7 == e*3-i-2:
						if 9-4/8*c == 7:
							if a == d+5-1-e:
								if 6-5+g-7 == 3:
									if b == f-h-4+i:
										if 3*6-2*8 == 2:
											print ('Solution: ')
											print(combo)

end = time()
print(end - start)
