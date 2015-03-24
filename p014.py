

# Problem 14: Longest Collatz sequence
# https://projecteuler.net/problem=14

memo = {1: 1}
def collatz(n):
    if n not in memo:
        if n % 2 == 0:
            memo[n] = 1 + collatz(n // 2)
        else:
            memo[n] = 1 + collatz(3 * n + 1)
    return memo[n]

def lcs(m):
    n = 1
    n_len = 1
    for i in range(2, m+1):
        i_len = collatz(i)
        if n_len < i_len:
            n = i
            n_len = i_len
    return n

#
def test():
    if collatz(13) == 10:
        return 'Pass'
    else:
        return 'Fail'
    
def main():
    return lcs(1 * 1000 * 1000)
    
if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 2 and sys.argv[1] == 'test':
        print(test())
    else:
        print(main())

