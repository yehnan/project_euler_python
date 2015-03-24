

# Problem 6: Sum square difference
# https://projecteuler.net/problem=6

def ssd(n):
    sum_sq = sum(i**2 for i in range(1, n+1))
    sq_sum = sum(range(1, n+1)) ** 2
    return sq_sum - sum_sq

#
def test():
    if ssd(10) == 2640:
        return 'Pass'
    else:
        return 'Fail'
    
def main():
    return ssd(100)
    
if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 2 and sys.argv[1] == 'test':
        print(test())
    else:
        print(main())

