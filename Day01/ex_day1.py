#Created by taka the 2020-12-01 at 11:45


import itertools


def part1(entrees):
    for val1, val2 in itertools.combinations(entrees, 2):
        if val1 + val2 == 2020:
            print(val1*val2)
            break


def part2(entrees):
    for val1, val2, val3 in itertools.combinations(entrees, 3):
        if val1 + val2 + val3== 2020:
            print(val1 * val2 * val3)
            break


if __name__ == "__main__":

    # get integer of input file in list (strip of the '\n')
    fichier = open("inputex1.txt", "r")
    entrees = fichier.readlines()
    entrees = [int(el.strip()) for el in entrees]

    part1(entrees)
    part2(entrees)