#Created by taka the 2020-12-07 at 11:11

def can_have_shiny_gold(bag):
    global shiny_count, visited
    to_check = [sac for sac in dico if list(zip(*dico[sac])) and bag in list(zip(*dico[sac]))[1]]

    for el in to_check:
        if dico[el] and el not in visited:
            visited.append(el)
            shiny_count += 1
            can_have_shiny_gold(el)


def part_1(to_search):
    can_have_shiny_gold(to_search)
    print('Part 1 :', shiny_count)


def compte_sac(sac):
    res = 0
    for el in dico[sac[1]]:
        res = res + el[0] * compte_sac(el)
        res = res + el[0]

    return res


def part_2():
    print('Part 2 :', compte_sac((1, "shiny gold")))


if __name__ == '__main__':
    dico = dict()

    #dictionnary with name of bag as key,
    # list of tuple(nb_bags, bag_name) as value
    with open("input_day7.txt", 'r') as f:
        for line in f:
            sentence = line.split()
            bags_infos = []
            for ind in range(len(sentence)):
                if "bag" in sentence[ind]:
                    if "contain" in sentence[ind:]:
                        bags_infos.append((sentence[ind - 2] + " " + sentence[ind - 1]))
                    elif (sentence[ind - 3]).isdigit():
                        bags_infos.append((sentence[ind - 3] + " " + sentence[ind - 2] + " " + sentence[ind - 1]))
            k = bags_infos[0]
            v = [(int(e[0]), e[2:]) for e in bags_infos[1:]]
            dico[k] = v
        #print(dico)


    shiny_count = 0
    visited = []

    part_1("shiny gold")
    part_2()