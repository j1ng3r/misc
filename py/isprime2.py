import math

def is_pseudo_prime(x, base):
	if x == 2: return True
	bits = x - 1
	prod = 1
	while bits:
		if bits & 1:
			prod = (prod * base) % x
		base = (base * base) % x
		bits >>= 1
	return prod == 1

primes = [2, 3]
def is_prime(x):
	if x < 2: return False
	if x == 2: return True
	
	lim = math.floor(math.sqrt(x))
	for p in primes:
		if x % p == 0: return False
		if p**2 > x: return True
	
	d = primes[-1] + 2
	while True:
		if x % d == 0: return False
		if d**2 > x: return True
		
		d_is_prime = True
		for p in primes:
			if d % p == 0:
				d_is_prime = False
			if p**2 > d:
				break
		if d_is_prime:
			primes.append(d)
		
		d += 2

def is_totally_pseudo_prime(x, k):
	for p in primes:
		if not is_pseudo_prime(x, p):
			return False
		k -= 1
		if k == 0: return True

N = []
k = 1

x = 2
while k < 30:
	if not is_prime(x) and is_totally_pseudo_prime(x, k):
		N.append(x)
		k += 1
	else:
		x += 1

print(N)
print(primes)
