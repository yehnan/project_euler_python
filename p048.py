

# Problem 48: Self powers
# https://projecteuler.net/problem=48

# 
def sp(n):
    result = 0
    for i in range(1, n+1):
        result += i ** i
    return result

print(sp(10))
print(len(str(sp(10))))

result_s = str(sp(1000))
result_len = len(result_s)
print(result_s)
print(result_len)

print(result_s[-10:])









