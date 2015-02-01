

# Problem 16: Power digit sum
# https://projecteuler.net/problem=16

def main(n):
    num = 2 ** n
    result = 0
    for d in str(num):
        result += int(d)
    return result

print(main(15))
print(main(1000))
