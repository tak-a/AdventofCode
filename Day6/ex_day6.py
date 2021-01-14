#Created by taka the 2020-12-06 at 12:48

def part_1(groups):
    somme = 0
    for grp in groups:
        tmp = "".join(grp)
        somme += len(set(tmp))

    print('Part 1 :', somme)

def part_2(groups):
    somme = 0
    for grp in groups:
        for el in grp[0]:
            if all(el in g for g in grp):
                somme += 1

    print('Part 2 :', somme)


if __name__  == '__main__':
    groups = []
    with open("input_day6.txt", 'r') as f:
        file = f.read()
        groups = file.split('\n\n')
        groups = [grp.split('\n') for grp in groups]

    part_1(groups)
    part_2(groups)

