def is_prime2(num):
    if num < 2:
        return False
    # if num % 2 == 0:
    if not num & 1:       
        return num == 2
    div = 3
    while div * div <= num:
        if num % div == 0:
            return False
        div += 2
    return True

def primes(n):
    sieve = [True] * (n//2)
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1) / (2*i)+1)
    return [2] + [2*i+1 for i in range(1, n//2) if sieve[i]]

def euler50():
   N = 10000
   Primes = primes(N)
   Found = 0
   for Len in xrange(550, 21, -1):        # magic number?
      for Offset in xrange(1, 549+1):     # magic number?
         PP = sum([Primes[J] for J in xrange(Offset+1,Offset+Len+1)])
         if PP < 1000000 and is_prime2(PP):
            Found = PP
            break
      if Found:
         break
   return Found
print(euler50())


