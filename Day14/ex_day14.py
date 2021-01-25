#Created by taka the 2020-12-14 at 18:02


def bit_to_int(bits):
    res_int = 0
    for i,v in enumerate(bits[::-1]):
        res_int = res_int + int(v) * pow(2,i)
    return res_int


def calcul_with_mask(mask, value):
    result = ''.join([m if m == '1' or m == '0' else v for m,v in zip(mask,value)])
    return bit_to_int(result)


def part_1(inputs):
    memory = {}
    for inf, val in inputs:
        if inf == 'mask':
            mask = val
            continue
        bits = '{0:036b}'.format(int(val))
        memory[inf] = calcul_with_mask(mask, bits)

    return sum(memory.values())




def mem_key_calcul(mask, b_key):
    result = ''.join([m if m == '1' or m == 'X' else v for m, v in zip(mask, b_key)])
    iter_x = pow(2, result.count('X'))
    if 'X' in result:
        adresses = []
        for v in range(iter_x):
            v_bits = bin(v)[2:].zfill(result.count('X'))
            tmp = result
            for b in v_bits:
                tmp = tmp.replace('X',str(b),1)

            adresses.append(bit_to_int(tmp))
        return adresses
    else:
        return [bit_to_int(result)]


def part_2(inputs):
    memory = {}
    for inf,val in inputs:
        if inf == 'mask':
            mask = val
        else:
            bits_key = '{0:036b}'.format(int(inf))
            mem_adresses = mem_key_calcul(mask, bits_key)
            for addr in mem_adresses:
                memory[addr] = int(val)

    return sum(memory.values())



if __name__=="__main__":
    with open('input_day14.txt', 'r') as f:
        data = []
        for line in f:
            inf, val = line.strip().split(" = ")
            if inf == "mask":
                data.append((inf,val))
            else:
                data.append((inf[4:-1], val))

    res_1 = part_1(data)
    print('Part 1 :', res_1)

    res_2 = part_2(data)
    print('Part 2 :', res_2)