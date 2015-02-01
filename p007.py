

# Problem 7: 10001st prime
# https://projecteuler.net/problem=7

#
def prime(n_th):
    primes = [2]
    def is_prime(n):
        for i in primes:
            if n % i == 0:
                return False
        return True
    for i in range(n_th-len(primes)):
        p = primes[-1]
        while True:
            p += 1
            if is_prime(p):
                primes.append(p)
                break
    return primes

print(prime(6)[-1])
print(prime(10001)[-1])

