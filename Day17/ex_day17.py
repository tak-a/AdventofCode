# Created by Taka the 2020-12-18 at 20:20

from itertools import product


def neighbours(coordinate, dim):
    if dim == 3:
        coords =[(i,j,k) for i,j,k in product([-1,0,1], repeat=dim)]
        coords.remove((0,0,0))
        x,y,z = coordinate
        return [(x + i, y + j, z + k) for i, j, k in coords]
    else:
        coords = [(i, j, k, l) for i, j, k, l in product([-1, 0, 1], repeat=dim)]
        coords.remove((0, 0, 0, 0))
        w, x, y, z = coordinate
        return [(w + i, x + j, y + k, z + l) for i, j, k, l in coords]


def count_active(dic):
    return len([v for v in dic.values() if v == '#'])


def problem(p_dic, cycles, dim):
    for _ in range(cycles):
        dic_copy = p_dic.copy()

        for coor in dic_copy:
            active = 0

            for neigh in neighbours(coor,dim):
                if neigh in dic_copy and dic_copy[neigh] == '#':
                    active += 1
                elif sum([1 for el in neighbours(neigh, dim) if el in dic_copy and dic_copy[el] == '#']) == 3:
                    p_dic[neigh] = '#'
                else:
                    p_dic[neigh] = '.'

            if dic_copy[coor] == '#' and active != 2 and active != 3:
                p_dic[coor] = '.'
            elif dic_copy[coor] == '.' and active == 3:
                p_dic[coor] = '#'

    return count_active(p_dic)


if __name__ == "__main__":
    puzzle = open("input_day17.txt", 'r').read()
    example = open("example.txt", 'r').read()

    inputs = list(map(lambda x: [el for el in x], puzzle.split('\n')))

    puzzle_dic = {}
    for i in range(len(inputs)):
        for j in range(len(inputs[i])):
            puzzle_dic[(i,j,0)] = inputs[i][j]

    res_1 = problem(puzzle_dic, 6, 3)
    print('Part 1 :', res_1)

    puzzle_dic = {}
    for i in range(len(inputs)):
        for j in range(len(inputs[i])):
            puzzle_dic[(i, j, 0, 0)] = inputs[i][j]

    res_2 = problem(puzzle_dic, 6, 4)
    print('Part 2 :', res_2)

