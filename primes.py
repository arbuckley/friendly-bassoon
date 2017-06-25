#Prime number calculator for friendly bassoon 

def is_prime(x): 
	prime = True
	for i in range(2, x): 
		if (x % i) == 0:
			prime = False 
	return prime 

print is_prime(10) 
print is_prime(17)
print is_prime(27)
print is_prime(31)
