

def fact(n):
    result = 1
    for i in range(1, n):
        result *= i
    return result

def main(n):
    s = str(fact(n))
    result = 0
    for c in s:
        result += int(c)
    return result

print(main(10))
print(main(100))
