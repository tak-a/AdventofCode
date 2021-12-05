# Created by taka the 04-12-2021 at 10:57

f = open('./input.txt', 'r')
lines = f.readlines()
lines = [line.strip('\n') for line in lines]


# Part 1
def minAndMax(linesList):
    '''

    :param linesList: list, lines of the valid bit values
    :return: (string, string) : both bit values for least common and most common bit
    '''
    el = ['', '', '', '', '', '', '', '', '', '', '', '']
    for l in linesList:
        for i in range(len(l)):
            el[i] += l[i]

    mini = ''.join(['1' if e.count('1') < e.count('0') else '0' for e in el])
    maxi = ''.join(['1' if e.count('1') >= e.count('0') else '0' for e in el])
    return mini, maxi


epsilon, gamma = minAndMax(lines)
print("Part 1 :", int(gamma, 2)*int(epsilon, 2))


# Part 2

def oxy_and_co2(linesList, minSearch=True):
    '''
    calculate oxygen or co2 values depending on param minSearch
    :param linesList: list of values still valid for this search
    :param minSearch: True if we try to find co2 (least common bit), False if oxygen(most common)
    :return: the bit value corresponding to the search
    '''
    res = linesList
    i = 0
    while len(res) != 1:
        mini, maxi = minAndMax(res)
        if minSearch:
            res = [e for e in res if e[i] == mini[i]]
        else:
            res = [e for e in res if e[i] == maxi[i]]
        i += 1
    return res[0]


oxygen = oxy_and_co2(lines, False)
co2 = oxy_and_co2(lines)

print("Part 2 :", int(oxygen, 2)*int(co2, 2))

