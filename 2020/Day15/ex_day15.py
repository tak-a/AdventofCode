# Created by taka the 2020-12-16 at 16:27


# val => list :
# 1 - spoken before or not
# 2 - last turn it was spoken
# 3 - last turn before the last turn
def problem(starting_numb, nb_turn):
    numb_infos = {}
    turn = len(starting_numb) + 1
    last_spoken = starting_numb[-1]

    for numb in starting_numb:
        numb_infos[numb] = [False, starting_numb.index(numb) + 1, 0]

    while turn <= nb_turn:
        if not numb_infos[last_spoken][0]:  # was first time it was spoken
            last_spoken = 0
        else:
            diff = numb_infos[last_spoken][1] - numb_infos[last_spoken][2]
            last_spoken = diff

        if last_spoken in numb_infos.keys():
            numb_infos[last_spoken] = [True, turn, numb_infos[last_spoken][1]]
        else:
            numb_infos[last_spoken] = [False, turn, 0]

        turn += 1

    return last_spoken


if __name__ == "__main__":
    inputs = [1, 2, 16, 19, 18, 0]

    part_1_solution = problem(inputs, 2020)

    print('Part 1 :', part_1_solution)

    part_2_solution = problem(inputs, 30000000)

    print('Part 2 :', part_2_solution)
