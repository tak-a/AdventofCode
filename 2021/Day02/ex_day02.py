f = open('./input.txt', 'r')
lines = f.readlines()

# Part 1
horizontal = 0
depth = 0
for l in lines:
    dir, val = l.split()
    if dir == 'forward':
        horizontal += int(val)
    elif dir == 'up':
        depth -=int(val)
    else:
        depth += int(val)

print('Part 1 :', horizontal*depth)


# Part 2
horizontal = 0
depth = 0
aim = 0
for l in lines:
    dir, val = l.split()
    if dir == 'forward':
        horizontal += int(val)
        depth += aim*int(val)
    elif dir == 'up':
        aim -= int(val)
    else:
        aim += int(val)

print('Part 2 :', horizontal*depth)