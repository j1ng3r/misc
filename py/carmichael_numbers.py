import math

C = [561,1105,1729,2465,2821,6601,8911,10585,15841,
 29341,41041,46657,52633,62745,63973,75361,101101,
 115921,126217,162401,172081,188461,252601,278545,
 294409,314821,334153,340561,399001,410041,449065,
 488881,512461]

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 
83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499]
def getSmallestPrimeFactor(x):
	for p in primes:
		if x % p == 0:
			return p

primes = [2, 3]
def generate_primes(x):
	d = primes[-1] + 2
	while d**2 < x:
		d_is_prime = True
		for p in primes:
			if d % p == 0:
				d_is_prime = False
			if p**2 > d:
				break
		if d_is_prime:
			primes.append(d)
		
		d += 2

smallestPrimes = []
i = 0
for c in C:
	generate_primes(c)
	sp = getSmallestPrimeFactor(c)
	while sp >= primes[i]:
		smallestPrimes.append(c)
		i += 1
		
print(smallestPrimes)
