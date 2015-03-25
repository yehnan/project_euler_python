

# Problem 29: Distinct powers
# https://projecteuler.net/problem=29

def dp(al, ah, bl, bh):
    ps = set()
    for a in range(al, ah+1):
        for b in range(bl, bh+1):
            ps.add(a**b)
    return len(ps)

#
def test():
    if dp(2, 5, 2, 5) == 15:
        return 'Pass'
    else:
        return 'Fail'
    
def main():
    return dp(2, 100, 2, 100)

if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 2 and sys.argv[1] == 'test':
        print(test())
    else:
        print(main())

