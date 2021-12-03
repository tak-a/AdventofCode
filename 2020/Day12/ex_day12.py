#Created by taka the 2020-12-12 at 13:18
directions = ['N', 'E', 'S', 'W']


def part_1(instructions, facing):
    dirs = {d:0 for d in directions}

    for ins, numb in instructions:
        if ins in 'NESW':
            dirs[ins] = dirs[ins] + int(numb)
        elif ins == 'L':
            facing = directions[(directions.index(facing) - int(int(numb)/90)) % 4]
        elif ins == 'R':
            facing = directions[(directions.index(facing) + int(int(numb)/90)) % 4]
        else:
            dirs[facing] = dirs[facing] + int(numb)

    return ( abs(dirs['N'] - dirs['S']) + abs(dirs['E'] - dirs['W']))


def rotate_waypoint(wp_x, wp_y,ins, numb):
    if numb == 180:
        wp_x, wp_y = -wp_x, -wp_y
    elif (ins,numb) in [('L', 90), ('R', 270)]:
        wp_x, wp_y = -wp_y, wp_x
    elif(ins, numb) in [('L', 270), ('R', 90)]:
        wp_x, wp_y = wp_y, -wp_x

    return wp_x, wp_y

def move_waypoint(wp_x,wp_y, ins, numb):
    if ins == 'N':
        return wp_x, wp_y + numb
    elif ins == 'S':
        return wp_x, wp_y - numb
    elif ins == 'E':
        return wp_x + numb, wp_y
    else:
        return wp_x - numb, wp_y

def part_2(instructions, waypoint):
    wp_x, wp_y = waypoint
    boat_x, boat_y = 0, 0
    for ins, numb in instructions:
        if ins in 'NESW':
            wp_x,wp_y = move_waypoint(wp_x, wp_y, ins, int(numb))
        elif ins in 'LR':
            wp_x, wp_y = rotate_waypoint(wp_x, wp_y, ins, int(numb))
        else:
            boat_x = boat_x + int(numb)*wp_x
            boat_y = boat_y + int(numb)*wp_y

    return abs(boat_x) + abs(boat_y)

if __name__=="__main__":
    with open("input_day12.txt", 'r') as f:
        commands = [line.strip() for line in f]
        commands = [(c[0], c[1:]) for c in commands]

    res_1 = part_1(commands, 'E')
    print('Part 1 :', res_1)

    res_2 = part_2(commands, (10,1))

    print('Part 2 :', res_2)

