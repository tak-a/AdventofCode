#Created by taka the 2020-12-05 at 18:11

def dichotomie_row(lettres, mini, maxi):
    lettre = lettres.pop(0)
    if len(lettres) == 0:
        if lettre == 'F':
            return int(mini)
        else:
            return int(maxi)
    else:
        if lettre == 'F':
            maxi = int((maxi+mini)/2)
        else:
            mini = int((maxi+mini)/2)+1

        return dichotomie_row(lettres, mini, maxi)

def dichotomie_columns(lettres, mini, maxi):
    lettre = lettres.pop(0)
    if len(lettres) == 0:
        if lettre == 'L':
            return mini
        else:
            return maxi
    else:
        if lettre =='L':
            maxi = int((maxi+mini)/2)
        else:
            mini = int((maxi+mini)/2)+1

        return dichotomie_columns(lettres, mini, maxi)


existing = []

def part_1(data):
    global existing
    highest_seatid = 0
    for d in data:
        row = dichotomie_row(list(d)[:7],0, 127)
        col = dichotomie_columns(list(d)[7:], 0, 7)
        seatid = int(row) * 8 + int(col)
        existing.append(seatid)
        if seatid > highest_seatid: highest_seatid = seatid

    print('Part 1 :',highest_seatid)

def part_2():
    global existing
    seatids = [r * 8 + c for r in range(0, 128) for c in range(0, 8)]
    for id in seatids:
        if id not in existing and id-1 in existing and id+1 in existing:
            print('Part 2 :', id)
            break


if __name__ == '__main__':
    with open("input_day5.txt", 'r') as f:
        lines = [l.strip() for l in f]

    part_1(lines)
    part_2()