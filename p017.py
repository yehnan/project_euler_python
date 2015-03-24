

# Problem 17: Number letter counts
# https://projecteuler.net/problem=17

d3 = {1: 'one thousand'}
d2a = { 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen',
        14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
        17: 'seventeen', 18: 'eighteen', 19: 'nineteen' }
d2b = { 2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty',
        6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety' }
d1 = { 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
       6: 'six', 7: 'seven', 8: 'eight', 9: 'nine' }

def i2s(i): # from 1 to 1000
    a4 = i // 1000
    a3 = (i % 1000) // 100
    a2 = (i % 100) // 10
    a1 = i % 10
    result = []
    if a4 == 1:
        result.append('one thousand')
        if a3 != 0 or a2 != 0 or a1 != 0:
            result.append(' and ')
    if a3 != 0:
        result.append(d1[a3])
        result.append(' hundred')
        if a2 != 0 or a1 != 0:
            result.append(' and ')
    if a2 == 1:
        result.append(d2a[a2*10 + a1])
    elif a2 >= 2:
        result.append(d2b[a2])
        if a1 != 0:
            result.append('-')
    if a2 != 1 and a1 != 0:
        result.append(d1[a1])
    return ''.join(result)
    
def nlc(n, m=None):
    if m is None:
        m = n
    result = 0
    for i in range(n, m+1):
        s = i2s(i)
        s = s.replace(' ', '').replace('-', '')
        result += len(s)
    return result

#
def test():
    if nlc(342) == 23 and nlc(115) == 20:
        return 'Pass'
    else:
        return 'Fail'
    
def main():
    return nlc(1, 1000)
    
if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 2 and sys.argv[1] == 'test':
        print(test())
    else:
        print(main())

