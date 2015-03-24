

# Problem 18: Maximum path sum I
# https://projecteuler.net/problem=18

from io import open

def get_triangle(filename):
    triangle = []
    with open(filename, 'r', encoding='ascii') as fin:
        for line in fin:
            triangle.append([int(n) for n in line.split()])
    return triangle

def max_path_sum(tri, row, col):
    if row == len(tri)-1:
        return tri[row][col]
    else:
        sub = max(max_path_sum(tri, row+1, col), 
                  max_path_sum(tri, row+1, col+1))
        return tri[row][col] + sub
        
def mpsi(filename):
    tri = get_triangle(filename)
    return max_path_sum(tri, 0, 0)
#
def test():
    if mpsi('p018_data_test.txt') == 23:
        return 'Pass'
    else:
        return 'Fail'
    
def main():
    return mpsi('p018_data.txt')
    
if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 2 and sys.argv[1] == 'test':
        print(test())
    else:
        print(main())

