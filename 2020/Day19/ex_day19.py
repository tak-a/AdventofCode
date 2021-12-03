#Created by corentin the 2020-12-20 at 00:36


rules = {} #all the rules
messages = [] #all messages
acceptables_solutions = [] # messages that would match the rule 0



on_rules = True #True if we read the rules, False if it's the messages
with open("input_day19.txt", 'r') as f:
    for line in f:
        if line == "\n":
            on_rules = False
            continue
        if on_rules:
            id, val = line.strip().split(':')
            values = [v.split() for v in val.strip().strip("\"").split('|')]

            rules[id] = tuple(values)
        else:
            messages.append(line.strip())




def find_messages(rule, mess, liste):
    r = rule[0] #first val in rule list
    v = rules[r] #value corresponding in the rules dict


    if v[0][0] == 'a' or v[0][0] == 'b':  # it's a letter of the message
        mess += v[0][0]

        if len(rule) == 1: # if it was the last rule in the list
            liste.append(mess)
        else: # continue with the rest
            find_messages(rule[1:], mess, liste)

    else:
        for val in v:
            find_messages(val + rule[1:], mess, liste)


#print(messages)
#print(rules)

# ----- PART 2 -----
#rules['8'] = (['42'], ['42', '8'])
#rules['11'] = (['42', '31'],['42', '11', '31',])

poss_42 = []
find_messages(['42'], "", poss_42)
print(poss_42)

poss_31 = []
find_messages(['31'], "", poss_31)
print(poss_31)

print([a for a in poss_31 if a in poss_42])
#find_messages(['0'], "",acceptables_solutions)


#print(acceptables_solutions)
n_m = []
a_s = []
for m in messages:
    tmp = m
    c1 = 0
    c2 = 0
    found = True
    while found:
        found = False
        if tmp[:8] in poss_42 and len(tmp) > 8:# and tmp[8:16] in poss_42 and tmp[16:24] in poss_42:
            found = True
            tmp = tmp[8:]
            c1 += 1

    found = True
    while found:
        found = False
        if len(tmp) == len(m): # there was no 42
            break
        if tmp[:8] in poss_31 and len(m) > 8:# and tmp[-16:-8] in poss_31:
            found = True
            tmp = tmp[8:]
            c2 += 1
    if c2 < c1:
        n_m.append(tmp)

# for acc in acceptables_solutions:
#     tmp = acc
#     found = True
#     while found:
#         found = False
#         if tmp[:8] in poss_42 and tmp[8:16] in poss_42 and tmp[16:24] in poss_42:
#             found = True
#             tmp = tmp[8:]
#
#     found = True
#     while found:
#         found = False
#         if tmp[-8:] in poss_31 and tmp[-16:-8] in poss_31:
#             found = True
#             tmp = tmp[:-8]
#
#     a_s.append(tmp)

compteur = 0
second_c = 0
for m in n_m:
    if m in acceptables_solutions:
        compteur += 1
    if m == '':
        second_c += 1


print(second_c)

print(compteur)


