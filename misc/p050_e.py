from math import sqrt

def is_prime(n): 
    n = int(n) 
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False 
    if n < 9: return True 
    if n%3 == 0: return False
    r = int(sqrt(n)) 
    f = 5 
    while f <= r:
        if n%f == 0: return False 
        if n%(f+2) == 0: return False 
        f +=6
    return True
    
def prime_sieve(n):
    sieve = [True] * (n//2)
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1) // (2*i)+1)
    return [2] + [2*i+1 for i in range(1, n//2) if sieve[i]]

max = 1000000
primes = prime_sieve(max)
prime_sum = [0]

sum = 0
count = 0
while sum < max:               # can we do this?
    sum += primes[count]
    prime_sum.append(sum)
    count += 1
#
terms = 1
for i in range(count):
    for j in range(i+terms, count):
        n = prime_sum[j] - prime_sum[i]
        if j-i > terms and is_prime(n):
            terms, max_prime = j-i, n

print "Project Euler 50 Solution = ", max_prime, " with ", terms, " terms"
