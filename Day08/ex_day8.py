#Created by taka the 2020-12-08 at 11:34

def part_1(instructions):
    acc = 0
    i = 0
    visited_index = []
    while True :
        visited_index.append(i)
        ins, val = instructions[i]
        if ins == 'jmp':
            i += int(val)
        elif ins == 'acc':
            acc += int(val)
            i += 1
        else:
            i += 1
        if i in visited_index:
            break

    print('Part 1 :', acc)


def part_2(instructions):
    ins_only = [el[0] for el in instructions]

    occ_nop = [i for i, x in enumerate(ins_only) if x == "nop"]
    occ_jmp = [i for i, x in enumerate(ins_only) if x == "jmp"]

    occs = occ_nop + occ_jmp

    for ind in occs:
        index_inst = 0
        visited = []
        finish = False
        accumulator = 0
        while True:
            if index_inst in visited:
                break
            elif index_inst >= len(instructions):
                finish = True
                break
            elem = instructions[index_inst]
            if index_inst == ind:
                if elem[0] == 'jmp':
                    visited.append(index_inst)
                    index_inst += 1
                elif elem[0] == 'acc':
                    accumulator += int(elem[1])
                    visited.append(index_inst)
                    index_inst += 1
                elif elem[0] == 'nop':
                    visited.append(index_inst)
                    index_inst += int(elem[1])
            else:
                if elem[0] == 'acc':
                    accumulator += int(elem[1])
                    visited.append(index_inst)
                    index_inst += 1
                elif elem[0] == 'jmp':
                    visited.append(index_inst)
                    index_inst += int(elem[1])
                else:
                    visited.append(index_inst)
                    index_inst += 1
        if finish:
            print('Part 2 :', accumulator)
            break


if __name__ == '__main__':
    with open("input_day8.txt", 'r') as f:
        instructions = [line.strip().split() for line in f]

    part_1(instructions)
    part_2(instructions)