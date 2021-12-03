#Created by corentin the 2020-12-19 at 13:27

import itertools

operands = {
    '+' : lambda x,y: x + y,
    '*' : lambda x,y: x * y,
    '-' : lambda x,y: x - y,
    '/' : lambda x,y: x / y
}



lines = []
with open('input_day18.txt', 'r') as f:
    for line in f:
        l = line.strip().split()
        lines.append(list(itertools.chain(*[[e for e in el] for el in l])))


def calcul_line(line):
    x = 0
    operand = None
    i = 0
    while i < len(line):
        el = line[i]
        if el.isdigit(): #it's a number
            if operand is None:
                x = int(el)
            elif operand == '+':
                x = operands[operand](x, int(el))
                operand = None
            else: # part 2
                j = i + 1
                nb_open = 0
                #print(len(line[i:]))
                while j < len(line):
                    if line[j] == '(':
                        nb_open += 1
                    elif line[j] == '*' and nb_open == 0:
                        #print('ajhzfbncla,')
                        break
                    elif line[j] == ')':
                        #print('azdjkcanldkq')
                        if nb_open == 0:
                            break
                        else:
                            nb_open -= 1
                    j += 1
                print('j ici:', j, 'et i:', i)
                x = operands[operand](x, calcul_line(line[i:j]))
                i = j
                print('la j :', j)
                operand = None
                continue

        elif el in operands: # it's a operand
            operand = el

        elif el == '(': # it's a open parenthese

            nb_open = 0  ### index closing parenthese
            j = i + 1
            while j < len(line):
                if line[j] == '(':
                    nb_open += 1
                elif line[j] == ')':
                    if nb_open == 0:
                        break
                    else:
                        nb_open -= 1
                j += 1
            ###
            print('j ici:', j, 'et i:', i, 'bla')
            if operand == None:
                x = calcul_line(line[i+1:j+1])
            else:
                print('operandeuuuh !!')
                tmp = calcul_line(line[i+1:j+1])
                if operand == '*':
                    print('BLAAAAAA, le i:', i)
                    k = j + 1
                    nb_open = 0
                    # print(len(line[i:]))
                    while k < len(line):
                        print('pouet')
                        if line[k] == '(':
                            nb_open += 1
                        elif line[k] == '*' and nb_open == 0:
                            print('ajhzfbncla,')
                            break
                        elif line[k] == ')':
                            # print('azdjkcanldkq')
                            if nb_open == 0:
                                break
                            else:
                                nb_open -= 1
                        k += 1
                    print('kkkk:', k, j)
                    print(line[j+1:k])
                    x = operands[operand](x,calcul_line([str(tmp)] + line[j+1:k]))
                    j = k-1
                else:
                    x = operands[operand](x,tmp)
                operand = None
            i = j
        elif el == ')': #it's a closing parenthese
            return x
        print(x, i)
        i += 1
    return x


resultat = 0
for line in lines:
    resultat += calcul_line(line)


print(resultat)


# -------- PART 2 -------