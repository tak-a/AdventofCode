#Created by taka the 2020-12-13 at 14:00
import math

def extended_euclide(a, b):

    r, u, v, rp, up, vp = a, 1, 0, b, 0, 1
    while rp != 0:
        q = r//rp
        r, u, v, rp, up, vp = rp, up, vp, r-q*rp, u-q*up, v-q*vp

    return(v)


def part_1(a_time, bus):
    bus_time = list(map(lambda x: x-(a_time % x), bus))
    earliest = min(bus_time)
    earliest_bus = bus[bus_time.index(earliest)]

    return earliest*earliest_bus


def part_2(bus):
    # ----- PART 2 : theoreme reste chinois -----
    indice_and_id = [(i, busid) for i, busid in enumerate(bus) if busid != 'x']
    indices, busids = list(zip(*indice_and_id))

    indices = [int(i) for i in indices]
    busids = [int(busid) for busid in busids]

    M = 1
    for i in busids:
        M = M * i

    ms = [M // busid for busid in busids]

    ts = 0
    for i, bus in enumerate(busids):
        pb = ms[i]
        inv = pb * extended_euclide(bus, pb)
        ts -= indices[i] * inv

    return ts%M


if __name__=="__main__":
    with open("input_day13.txt", 'r') as f:
        lines = [line.strip() for line in f]

    arriving_time = int(lines[0])
    bus = (lines[1]).split(',')
    list_bus = [int(b) for b in bus if b != 'x']
    res_1 = part_1(arriving_time, list_bus)
    print('Part 1 :', res_1)

    res_2 = part_2(bus)
    print('Part 2 :', res_2)