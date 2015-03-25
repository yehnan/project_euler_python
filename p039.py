

# Problem 39: Integer right triangles
# https://projecteuler.net/problem=39

# brute force
def irt_bf(p_upperbound):
    p_max = 0
    t_max = 0
    for p in range(4, p_upperbound+1):
        t = 0
        for b in range(1, p):
            for a in range(1, b+1):
                c = p - a - b
                if a <= b < c and a**2 + b**2 == c**2:
                    print(a, b, c, p)
                    t += 1
        if t > t_max:
            t_max = t
            p_max = p
            
    return p_max
    
#
def irt(p_upperbound):
    p_max = 0
    t_max = 0
    for p in range(p_upperbound//4*2, p_upperbound+1, 2):
        t = 0
        for a in range(2, int(p / (2**0.5+1)) + 1):
            if p * (p-2*a) % (2* (p-a)) == 0:
                t += 1
        if t > t_max:
            t_max = t
            p_max = p
    
    return p_max

#
def test():
    return 'No test'
    
def main():
    return irt(1000)

if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 2 and sys.argv[1] == 'test':
        print(test())
    else:
        print(main())

