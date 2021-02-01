# Created by taka the 2020-12-17 at 13:44


def parse_inputs(inputs):
    rules, my_ticket, tickets = inputs.split('\n\n')

    my_ticket = [int(val) for val in my_ticket.split('\n')[1].split(',')]

    tickets = list(map(lambda x: [int(val) for val in x.split(',')], tickets.split('\n')[1:]))

    rules_dic = {}
    rules = rules.split('\n')
    for r in rules:
        k, v = r.split(": ")
        range1, range2 = v.split(" or ")
        sr1, er1 = range1.split("-")
        sr2, er2 = range2.split("-")

        rules_dic[k] = lambda x, sr1=sr1, er1=er1, sr2=sr2, er2=er2: int(sr1) <= x <= int(er1) \
                                                                     or int(sr2) <= x <= int(er2)

    return rules_dic, my_ticket, tickets


def part_1(rules, tickets):
    valid_tickets = []
    error_rate = 0

    for t in tickets:
        tmp = error_rate
        for value in t:
            # if not any(value in rules[k] for k in rules):
            if not any(rules[k](value) for k in rules):
                error_rate += value

        if tmp == error_rate:
            valid_tickets.append(t)

    return error_rate, valid_tickets


def part_2(rules, valid_tickets, my_ticket):
    fields = {k: [i for i in range(len(valid_tickets[0]))] for k in rules}

    for t in valid_tickets:
        for i, val in enumerate(t):
            for k in rules:
                if not rules[k](val) and i in fields[k]:  # if this val doesn't work for this field, remove the index from fields
                    fields[k].remove(i)

    done = False
    visited = []

    while not done:
        key = ""
        val = None
        for k in fields:
            if len(fields[k]) == 1 and k not in visited:
                key = k
                val = fields[k][0]
                visited.append(k)
                break

        for k in fields:
            if k != key and val in fields[k]:
                fields[k].remove(val)

        if all(len(fields[k]) == 1 for k in fields):
            done = True

    result = 1
    for i,k in enumerate(fields):
        if i > 5:
            break
        result *= my_ticket[fields[k][0]]

    return result

if __name__ == '__main__':

    file = open('input_day16.txt', 'r').read()
    rules, my_ticket, tickets = parse_inputs(file)

    res_1, valids = part_1(rules, tickets)

    print('Part 1 :', res_1)

    res_2 = part_2(rules, valids, my_ticket)

    print('Part 2 :', res_2)





