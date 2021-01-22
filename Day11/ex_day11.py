#Created by taka the 2020-12-11 at 11:39
import copy

directions = [(-1,-1),(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0,-1)]

def nb_adjacent_occupied(layout, row, col, part=1):
    r_length = len(layout)
    c_length = len(layout[0])
    nb_adj = 0

    for y,x in directions:
        r = row+y
        c = col+x

        if part == 1:
            if 0<= r <r_length and 0<= c <c_length and layout[r][c] == '#':
                nb_adj += 1
        else:
            while 0<= r <r_length and 0<= c <c_length:
                if layout[r][c] == '#':
                    nb_adj += 1
                    break
                elif layout[r][c] == 'L':
                    break
                r = r + y
                c = c + x

    return nb_adj


def nb_occupied(layout):
    return sum(r.count('#') for r in layout)


def solve_problem(layout, tolerance, part):
    c_layout = copy.deepcopy(layout)
    same = False
    while not same:
        same = True
        for r,line in enumerate(layout):
            for c,seat in enumerate(line):
                if seat == 'L' and nb_adjacent_occupied(layout, r, c, part) == 0:
                    c_layout[r][c] = '#'
                    same = False
                elif seat == '#' and nb_adjacent_occupied(layout, r, c, part) >= tolerance:
                    c_layout[r][c] = 'L'
                    same = False
        layout = copy.deepcopy(c_layout)
        for k in layout:
            for l in k:
                print(l, end='')
            print('\n')
        print('\n\n')

    occupied = nb_occupied(layout)
    return occupied


if __name__=="__main__":

    with open("input_day11.txt", 'r') as f:
        seats = [[el for el in line.strip()] for line in f]

    result_1 = solve_problem(seats, 4, 1)

    print('Part 1 :', result_1)

    result_2 = solve_problem(seats, 5, 2)

    print('Part 2 :', result_2)





