

# Problem 42: Coded triangle numbers
# https://projecteuler.net/problem=42

from io import open

def tn(n):
    return n * (n+1) // 2
memo = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
def is_tn(n):
    mn = len(memo)
    mmax = memo[-1]
    while n > mmax:
        mmax = tn(mn)
        memo.append(mmax)
        mn += 1
    if n in memo:
        return True
    return False

def word_value(word):
    value = 0
    for c in word:
        value += ord(c) - ord('A') + 1
    return value

def main(filename):
    result = 0
    with open('p042_words.txt', 'r', encoding='ascii') as fin:
        words = eval(''.join(('[', fin.read(), ']')))
        for word in words:
            if is_tn(word_value(word)):
                result += 1
    return result

# print(word_value('SKY'))
print(main('p042_words.txt'))

