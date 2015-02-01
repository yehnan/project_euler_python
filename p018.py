

# Problem 18: Maximum path sum I
# https://projecteuler.net/problem=18

from io import open

def max_path_sum(tri, row, col):
    if row == len(tri)-1:
        return tri[row][col]
    else:
        sub = max(max_path_sum(tri, row+1, col), 
                 max_path_sum(tri, row+1, col+1))
        return tri[row][col] + sub
        
def get_triangle(filename):
    triangle = []
    with open(filename, 'r', encoding='ascii') as fin:
        for line in fin:
            triangle.append([int(n) for n in line.split()])
    return triangle

print(max_path_sum(get_triangle('p018_triangle1.txt'), 0, 0))
print(max_path_sum(get_triangle('p018_triangle2.txt'), 0, 0))

    