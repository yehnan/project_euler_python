

# Problem 28: Number spiral diagonals
# https://projecteuler.net/problem=28

def main(size):
    result = 1  # center
    for i in range(3, size+2, 2):
        result += i**2   # top-right
        tmp = (i-2)**2 + 1 + i - 2
        result += tmp   # bottom-right
        result += tmp + i - 1   # bottom-left
        tmp = tmp + i - 1
        result += tmp + i - 1   # top-left
    return result
print(main(5))
print(main(1001))

