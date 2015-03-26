


def prime_sieve(n):
    sieve = [True] * (n//2)
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1) / (2*i)+1)
    return [2*i+1 for i in range(1, n//2) if sieve[i]]

P = prime_sieve(1000001)

seq=[3]

for i in P:
    if seq[0]+i>1000000:
        break
    seq.insert(0, seq[0]+i)
    
for i in range(10):
    print(P[i], seq[len(seq)-1-i])

Max=0
for n in range(0, 4):
    for t in seq:
        if t-P[n] in P:
            Max = max(Max, t-P[n])
            break
print(Max)
