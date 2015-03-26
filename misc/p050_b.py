



def euler(n):
    candidates = range(n+1)
    fin = int(n**0.5)
    for i in xrange(2, fin+1):
        if not candidates[i]:
            continue
        candidates[2*i::i] = [None] * (n//i - 1)
    return [i for i in candidates[2:] if i]

def main():
    primes = euler(1000000)
    largest = 0
    chain = []
    for start in range(10):      # why 10?
        seq = primes[start:]
        i = 0
        total = 0
        for prime in seq:
            total += prime
            if total > 1000000:
                break
            i += 1
            if total in primes:
                c = seq[:i]
                if len(c) > len(chain):
                    chain = c
    print sum(chain)

main()

