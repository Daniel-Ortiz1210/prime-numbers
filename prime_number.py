import math

n = 84

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def prime_factors(n):
    factors = []
    prime_factors = []
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i  == 0:
            factors.append(i)
    for n in factors:
        if is_prime(n):
            prime_factors.append(n)                
    
    return sorted(prime_factors)

print(prime_factors(n))