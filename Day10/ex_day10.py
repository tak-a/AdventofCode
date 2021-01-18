#Created by taka the 2020-12-10 at 11:46

from collections import defaultdict

def part_1(adapters):
    diff_1, diff_3 = 0, 0
    for i in range(len(adapters)-1):
        if adapters[i+1] - adapters[i] == 1:
            diff_1 += 1
        else:
            diff_3 += 1

    print('Part 1 :', diff_1*diff_3)


def part_2(adapters):
    dico = defaultdict(lambda: 0, {0: 1})
    for a in adapters[1:]:
        dico[a] = sum(dico[i] for i in range(a-3, a))

    print('Part 2 :', dico[adapters[-1]])


if __name__ == "__main__":
    with open("input_day10.txt", 'r') as f:
        adapters = [int(line.strip()) for line in f]

    adapters.extend([0, max(adapters)])
    adapters.sort()

    part_1(adapters)
    part_2(adapters)

