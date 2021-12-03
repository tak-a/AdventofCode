#Created by taka the 2020-12-02 at 12:09



def parse_data(input_file):
    lines = []
    with open(input_file, 'r') as f:
        for line in f:
            minmax, letter, pw = line.split()
            minOcc, maxOcc = minmax.split('-')
            letter = letter.strip(':')
            lines.append([minOcc, maxOcc, letter, pw])
    return lines


def part_1(infos):
    good_pw = 0
    for line in infos:
        minOcc, maxOcc, letter, pw = line
        occ = pw.count(letter)
        if occ >= int(minOcc) and occ <= int(maxOcc):
            good_pw +=1

    print('Part 1:', good_pw)


#second part
def part_2(infos):
    good_pw = 0
    for line in infos:
        pos1, pos2, letter, pw = line
        if (pw[int(pos1)-1],pw[int(pos2)-1]).count(letter) == 1:
            good_pw +=1

    print('Part 2:',good_pw)


if __name__ == '__main__':
    data = parse_data('input_day2.txt')
    part_1(data)
    part_2(data)