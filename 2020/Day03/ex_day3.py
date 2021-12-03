#Created by taka the 2020-12-03 at 11:36

def part_1(grid):
    x,y = 0,0
    nb_tree = 0
    length = len(grid[0])
    for line in grid:
        if grid[y][x] == '#':
            nb_tree += 1
        y += 1
        x =(x+3)%(len(grid[0]))

    print('Part 1:', nb_tree)


def part_2(grid):
    total = 1
    for (addx, addy) in [(1,1), (3, 1), (5,1), (7,1), (1,2)]:
        x, y = 0, 0
        nb_tree = 0
        while y < len(grid):
            if grid[y][x] == '#':
                nb_tree +=1
            x = (x+addx)%(len(grid[0]))
            y += addy
        total *= nb_tree

    print('Part 2:',total)


if __name__ == '__main__':
    grid = []
    with open("input_day3.txt", 'r') as f:
        for line in f:
            grid.append([el for el in line.strip()])

    part_1(grid)
    part_2(grid)
