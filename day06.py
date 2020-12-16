data = [
(315, 342),
(59, 106),
(44, 207),
(52, 81),
(139, 207),
(93, 135),
(152, 187),
(271, 47),
(223, 342),
(50, 255),
(332, 68),
(322, 64),
(250, 72),
(165, 209),
(129, 350),
(139, 118),
(282, 129),
(311, 264),
(216, 246),
(134, 42),
(66, 151),
(263, 199),
(222, 169),
(236, 212),
(320, 178),
(202, 288),
(273, 190),
(83, 153),
(88, 156),
(284, 305),
(131, 90),
(152, 88),
(358, 346),
(272, 248),
(317, 122),
(166, 179),
(301, 307),
(156, 128),
(261, 290),
(268, 312),
(89, 53),
(324, 173),
(353, 177),
(91, 69),
(303, 164),
(40, 221),
(146, 344),
(61, 314),
(319, 224),
(98, 143),
]

def manhattan_distance(coord_1, coord_2):
    return abs(coord_1[0] - coord_2[0]) + abs(coord_1[1] - coord_2[1])

min_x = min([coord[0] for coord in data])
max_x = max([coord[0] for coord in data])
min_y = min([coord[1] for coord in data])
max_y = max([coord[1] for coord in data])

grid = {}

for y in range(min_y - 1, max_y + 2):
    for x in range(min_x - 1, max_x + 2):
        for idx, coord in enumerate(data):
            if (x, y) not in grid:
                grid[(x, y)] = (idx, manhattan_distance((x, y), coord))
            else:
                _, distance = grid[(x, y)]
                test_distance = manhattan_distance((x, y), coord)
                if test_distance < distance:
                    grid[(x, y)] = (idx, test_distance)
                elif test_distance == distance:
                    grid[(x, y)] = (-1, test_distance)

idx_to_ignore = {-1}

for y in (min_y - 1, max_y + 1):
    for x in range(min_x - 1, max_x + 2):
        idx, _ = grid[(x, y)]
        idx_to_ignore.add(idx)

for y in range(min_y - 1, max_y + 2):
    for x in (min_x - 1, max_x + 1):
        idx, _ = grid[(x, y)]
        idx_to_ignore.add(idx)

inner_grid_count = {}
for coord in grid:
    idx, _ = grid[coord]
    if idx not in idx_to_ignore:
        if idx not in inner_grid_count:
            inner_grid_count[idx] = 1
        else:
            inner_grid_count[idx] += 1

print('Max', max(inner_grid_count[coord] for coord in inner_grid_count))


good_coords = set()
goal = 10000

for y in range(min_y , max_y + 1):
    for x in range(min_x , max_x + 1):
        total = 0
        for coord in data:
            total += manhattan_distance((x, y), coord)
            if total >= goal:
                break
        if total < goal:
            good_coords.add((x, y))

print('Good coords', len(good_coords))