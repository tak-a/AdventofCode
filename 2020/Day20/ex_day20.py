#Created by corentin the 2020-12-23 at 20:38

cardinals = ['North', 'East', 'South', 'West']
tiles = {}

#final image
image = []
for _ in range(12):
    image.append(['0000'] * 12)

#get from tje input file the different tiles in the tiles dictionnary
with open("input_day20.txt", 'r') as f:
    tile = []
    for line in f:
        l = line.strip()
        if 'Tile' in l:
            key = line.split()[1].strip(':')
        elif l != "":
            tile.append(l)
        else:
            tiles[key] = tile
            tile = []


borders = {}
for t in tiles.keys():
    border = []
    border.append(tiles[t][0])
    east = [l[-1] for l in tiles[t]]
    border.append(''.join(east))
    border.append(tiles[t][-1])
    west = [l[0] for l in tiles[t]]
    border.append(''.join(west))
    borders[t] = border


bordure_id = {}
for t in tiles.keys():
    edges = []
    for i,border in enumerate(borders[t]):
        is_edge = True
        for ti in borders.keys():
            if ti != t and (border in borders[ti] or border[::-1] in borders[ti]):
                is_edge = False
        if is_edge:
            if i == 0:
                edges.append('N')
            elif i == 1:
                edges.append('E')
            elif i == 2:
                edges.append('S')
            else:
                edges.append('W')
    if len(edges) == 2:
        bordure_id[t] = edges

print(bordure_id)

resultat = 1
for bid in bordure_id:
    resultat = resultat * int(bid)

print('Part 1 solution:',resultat,'\n')

print('There are', len(tiles), 'tiles')
print('Corner tile id :')
print(bordure_id)
for t in tiles:
    for bt in [bt for bt in borders.keys() if bt != t]:
        for i,b in enumerate(borders[t]):
            if b in borders[bt]:
                print('The border', cardinals[i], 'of tile', t,'equals border', cardinals[borders[bt].index(b)],'of tile',bt)


def rotate_tile(tile):
    return zip(*tile[::-1])


#order tile in image
a = 0 # index for image

for t in tiles:
    if t in bordure_id: # tile is a border of image
        nb_rotate = 0
        if a == 0: # top left corner
            nb_rotate = 4 - max([cardinals.index(a) for a in bordure_id[t]])
            for _ in range(nb_rotate):
                tiles[t] = rotate_tile(tiles[t])
        elif a == 11: # top right corner

        elif a == 132: # bottom left corner

        elif a == 143: #bottom left corner

        index_last = min([cardinals.index()])