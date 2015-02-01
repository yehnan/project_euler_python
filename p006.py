

# Problem 6: Sum square difference
# https://projecteuler.net/problem=6

def main(n):
    sum_sq = sum([i**2 for i in range(1, n+1)])
    sq_sum = sum(range(1, n+1)) ** 2
    return sq_sum - sum_sq

print(main(10))
print(main(100))
