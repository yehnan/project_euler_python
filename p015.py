

# Problem 15: Lattice paths
# https://projecteuler.net/problem=15

def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result
def main(row, col):
    return factorial(row+col) // factorial(row) // factorial(col)

print(main(2, 2))
print(main(20, 20))

