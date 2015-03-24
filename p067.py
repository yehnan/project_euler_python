

# Problem 67: Maximum path sum II
# https://projecteuler.net/problem=67

from io import open

def get_triangle(filename):
    triangle = []
    with open(filename, 'r', encoding='ascii') as fin:
        for line in fin:
            triangle.append([int(n) for n in line.split()])
    return triangle

def max_path_sum(tri, row, col):
    for r in range(len(tri)-1 -1, -1, -1):
        for c in range(len(tri[r])):
            tri[r][c] += max(tri[r+1][c], tri[r+1][c+1])
    return tri[row][col]
    
def mpsii(filename):
    tri = get_triangle(filename)
    return max_path_sum(tri, 0, 0)
#
def test():
    if mpsii('p067_data_test.txt') == 23:
        return 'Pass'
    else:
        return 'Fail'
    
def main():
    return mpsii('p067_data.txt')
    
if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 2 and sys.argv[1] == 'test':
        print(test())
    else:
        print(main())

