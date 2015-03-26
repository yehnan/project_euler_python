
from math import sqrt

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

sum = 0
prime_list = []
for i in xrange(2, 1000000):
    if isPrime(i):
        sum += i
        prime_list.append(sum)
    if sum > 1000000:               # can we do this?
        break
prime_list[-1:]=[]

def GetConsecutivePrimeSum():
    for span in xrange(len(prime_list)-1, 0, -1):
        for begin_p in range(0, len(prime_list)-span):
            sum = prime_list[begin_p+span] - prime_list[begin_p];
            if isPrime(sum):
                yield sum

answer = GetConsecutivePrimeSum();
print answer.next()
