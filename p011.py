

# Problem 11: Largest product in a grid
# https://projecteuler.net/problem=11

from io import open

grid = []
with open('p011_data.txt', 'r', encoding='ascii') as fin:
    for line in fin:
        grid.append(list(map(int, line.split())))

#
def product(li):
    result = 1
    for n in li:
        result *= n
    return result
    
def product_max(li, count):
    max = 0
    for i in range(0, len(li)-count + 1):
        m = product(li[i:i+count])
        if m > max:
            max = m
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
        if m > max:
            max = m
    for col in range(len(grid[0])):
        m = product_max(diag(grid, 0, col, 1), count)
        if m > max:
            max = m
    for col in range(len(grid[0])):
        m = product_max(diag(grid, 0, col, -1), count)
        if m > max:
            max = m
    return max

def lpiad(grid, count):
    m = find_max(grid, count)
    grid_rotated = list(zip(*grid))
    mr = find_max(grid_rotated, count)
    return max(m, mr)

#
def test():
     return 'No test'
    
def main():
    return lpiad(grid, 4)
    
if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 2 and sys.argv[1] == 'test':
        print(test())
    else:
        print(main())

