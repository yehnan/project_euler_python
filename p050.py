

# Problem 50: Consecutive prime sum
# https://projecteuler.net/problem=50

def prime_sieve(n):
    sieve = [True] * (n//2)
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1) // (2*i)+1)
    return [2] + [2*i+1 for i in range(1, n//2) if sieve[i]]

def cumulative_sum(li):
    result = [0]
    tmp = 0
    for e in li:
        if tmp > 1000000:     # !
            break             # !
        tmp += e
        result.append(tmp)
    return result
    
def cps(m):
    primes = prime_sieve(m)
    primes_set = set(primes)
    primes_sum = cumulative_sum(primes)
    
    p_max = 2
    p_len_max = 1
    for i in range(p_len_max, len(primes_sum)):
        for j in range(i-1-p_len_max, -1, -1):
            p = primes_sum[i] - primes_sum[j]
            if p > m:
                break
            if p in primes_set and p > p_max:
                p_max = p
                p_len_max = i - j
    
    return (p_max, p_len_max)
    
#
def test():
    if cps(100) == (41, 6) and cps(1000) == (953, 21):
        return 'Pass'
    else:
        return 'Fail'

def main():
    return cps(1 * 1000 * 1000)[0]

if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 2 and sys.argv[1] == 'test':
        print(test())
    else:
        print(main())

