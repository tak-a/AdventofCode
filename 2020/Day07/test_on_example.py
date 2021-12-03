#Created by corentin the 2020-12-07 at 14:12


dico = dict()

res = 0

def compte_sac(sac):
    res = 0
    #res = res + sum([e[0] for e in dico[sac[1]]])
    for el in dico[sac[1]]:
        res = res + el[0] * compte_sac(el)
        res = res + el[0]

        print("sac[1] : ", sac[1], "res : ", res)
    #res = res + sum([e[0] for e in dico[sac[1]]])
    return res

with open("example.txt", 'r') as f:
    for line in f:
        sentence = line.split()
        bags_infos = []
        for ind in range(len(sentence)):
            if "bag" in sentence[ind]:
                if "contain" in sentence[ind:]:
                #bags_infos.append((sentence[ind-2] + " " + sentence[ind-1])) #part 1 : without number of bags
                    bags_infos.append((sentence[ind - 2] + " " + sentence[ind - 1]))
                elif (sentence[ind-3]).isdigit():
                    bags_infos.append((sentence[ind-3] + " " + sentence[ind - 2] + " " + sentence[ind - 1]))
            #print(bags_infos)
        k = bags_infos[0]
        v = [(int(e[0]), e[2:]) for e in bags_infos[1:]]
        dico[k] = v

print(dico)


result = compte_sac((1,"shiny gold"))

print(result)