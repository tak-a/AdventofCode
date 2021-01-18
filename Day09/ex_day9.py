#Created by taka the 2020-12-09 at 11:12

import itertools

def part_1(values):
    i = 0
    while True:
        if values[i+25] not in list(map(lambda x: sum(list(x)),itertools.combinations(values[i:i+25], 2))):
            return values[i+25]
        i += 1

def slidding_window(values, size):
    return [values[i:i+size] for i in range(len(values))]

def part_2(values,val):
    size = 3
    found = False
    while not found:
        sw = slidding_window(values, size)
        for el in sw:
            if sum(el) == val:
                print('Part 2 :', min(el)+max(el))
                found = True
                break
        size += 1


if __name__ == "__main__":

    with open("input_day9.txt", 'r') as f:
        values = [int(val.strip()) for val in f]

    val = part_1(values)
    print('Part 1 :', val)

    part_2(values, val)