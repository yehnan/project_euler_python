

# Problem 11: Largest product in a grid
# https://projecteuler.net/problem=11

from io import open

grid = []
with open('p011_grid.txt', 'r', encoding='ascii') as fin:
    for line in fin:
        grid.append(list(map(int, line.split())))

# print(grid)
def product(li):
    result = 1
    for n in li:
        result *= n
    return result
    
def product_max(li, count):
    max = 0
    for i in range(0, len(li)-count + 1):
        m = product(li[i:i+4])
        max = m if m > max else max
    return max

def diag(grid, row, col, slant):
    d = []
    while True:
        try:
            d.append(grid[row][col])
            row += 1
            col += slant
        except IndexError:
            break
    return d

def find_max(grid, count):
    max = 0
    for row in grid:
        m = product_max(row, count)
        max = m if m > max else max
    for col in range(len(grid[0])):
        m = product_max(diag(grid, 0, col, 1), count)
        max = m if m > max else max
    for col in range(len(grid[0])):
        m = product_max(diag(grid, 0, col, -1), count)
        max = m if m > max else max
    return max

max_ = find_max(grid, 4)
grid_rotated = list(zip(*grid))
max_rotated = find_max(grid_rotated, 4)
print(max(max_, max_rotated))
