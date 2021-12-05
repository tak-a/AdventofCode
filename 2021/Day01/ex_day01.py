f = open('./input.txt', 'r')
lines = f.readlines()

# Part 1
depth = int(lines[0])
res = 0
# go through all depths and count if depth N+1 is > that depth N
for l in lines[1:]:
    if int(l) > depth:
        res +=1
    depth = int(l)

print("Part 1 :", res)


# Part 2
sum_depths = sum(map(int, lines[:3]))
res_part2 = 0
# for all depths sum from depth N to N+2 and check if it is > than sum from N-1 to N+1
for l in range(len(lines[1:])):
    if sum(map(int, lines[l:l+3])) > sum_depths:
        res_part2 += 1
    sum_depths = sum(map(int, lines[l:l+3]))

print("Part 2 :", res_part2)