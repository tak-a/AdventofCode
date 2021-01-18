#Created by taka the 2020-12-04 at 11:56

valid_passport = 0

needed_key = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

def check_height(hgt):
    if hgt[-2:] == 'in' and hgt[:-2].isdigit():
        return 59 <= int(hgt[:-2]) <= 76
    elif hgt[-2:] == 'cm' and hgt[:-2].isdigit():
        return 150 <= int(hgt[:-2]) <= 193
    else:
        return False


rules = {
    'byr': lambda x : 1920 <= int(x) <= 2002,
    'iyr': lambda x : 2010 <= int(x) <= 2020,
    'eyr': lambda x : 2020 <= int(x) <= 2030,
    'hgt': check_height,
    'hcl': lambda x : x[0] == '#' and all((el.isdigit() or el.isalpha()) for el in x[1:]) and len(x) == 7,
    'ecl': lambda x : x in ['amb','blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
    'pid': lambda x : x.isdigit() and len(x) == 9,
    'cid': lambda x : True
}


def part_1(dics):
    valid = 0
    for dic in dics:
        if all((key in dic.keys() for key in needed_key)):
            valid += 1
    print('Part 1 :', valid)


def part_2(dics):
    valid = 0
    for dic in dics:
        if all((key in dic.keys() for key in needed_key)) and all(rules[key](dic[key]) for key in dic):
            valid += 1
    print('Part 2 :', valid)


if __name__ == '__main__':
    with open("input_day4.txt", 'r') as f:
        dico_pass = {}
        dics = []
        for line in f:
            if line != "\n" and line != "":
                values = line.split()
                for val in values:
                    k, v = val.split(':')
                    dico_pass[k] = v
            else:
                dics.append(dico_pass)
                dico_pass = {}
        dics.append(dico_pass)

    part_1(dics)
    part_2(dics)