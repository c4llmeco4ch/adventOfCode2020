# PART 1

def calc_adjacents(grid, v, h):
    adj_occ = 0
    if h > 0:
        if v > 0 and grid[v - 1][h - 1] == '#':
            adj_occ += 1
        if grid[v][h - 1] == '#':
            adj_occ += 1
        if v < len(grid) - 1 and grid[v + 1][h - 1] == '#':
            adj_occ += 1
    if v > 0 and grid[v - 1][h] == '#':
        adj_occ += 1
    if v < len(grid) - 1 and grid[v + 1][h] == '#':
        adj_occ += 1
    if h < len(grid[v]) - 1:
        if v > 0 and grid[v - 1][h + 1] == '#':
            adj_occ += 1
        if grid[v][h + 1] == '#':
            adj_occ += 1
        if v < len(grid) - 1 and grid[v + 1][h + 1] == '#':
            adj_occ += 1
    return adj_occ

def determine_swaps(g):
    swap_grid = []
    for vert, line in enumerate(g):
        swap_grid.append([])
        for horiz, char in enumerate(line):
            if char == '.':
                swap_grid[vert].append(False)
            elif (ca := calc_adjacents(g, vert, horiz)) == 0 and char == 'L':
                swap_grid[vert].append(True)
            elif char == '#' and ca >= 4:
                swap_grid[vert].append(True)
            else:
                swap_grid[vert].append(False)
    return swap_grid

with open('seating.txt') as f:
    text = f.readlines()
    grid = [[v for v in line.strip()] for line in text]
    swap = [[]]
    are_done = False
    while not are_done:
        swap = determine_swaps(grid)
        flat = [val for line in swap for val in line]
        if not any(flat):
            are_done = True
        else:
            for v, l in enumerate(swap):
                for h, b in enumerate(l):
                    if grid[v][h] == '.':
                        continue
                    if b:
                        grid[v][h] = '#' if grid[v][h] == 'L' else 'L'
print(sum(map(lambda x: x.count('#'), grid)))

# PART 2

def find_first(grid, v, h, dy, dx):
    v += dy
    h += dx
    while v >= 0 and v < len(grid) and h >= 0 and h < len(grid[0]):
        if grid[v][h] != '.':
            return grid[v][h]
        v += dy
        h += dx
    return '.'


def calc_adjacents(grid, v, h):
    adj_occ = 0
    if h > 0:
        if v > 0 and find_first(grid, v, h, -1, -1) == '#':
            adj_occ += 1
        if find_first(grid, v, h, 0, -1) == '#':
            adj_occ += 1
        if v < len(grid) - 1 and find_first(grid, v, h, 1, -1) == '#':
            adj_occ += 1
    if v > 0 and find_first(grid, v, h, -1, 0) == '#':
        adj_occ += 1
    if v < len(grid) - 1 and find_first(grid, v, h, 1, 0) == '#':
        adj_occ += 1
    if h < len(grid[v]) - 1:
        if v > 0 and find_first(grid, v, h, -1, 1) == '#':
            adj_occ += 1
        if find_first(grid, v, h, 0, 1) == '#':
            adj_occ += 1
        if v < len(grid) - 1 and find_first(grid, v, h, 1, 1) == '#':
            adj_occ += 1
    return adj_occ

def determine_swaps(g):
    swap_grid = []
    for vert, line in enumerate(g):
        swap_grid.append([])
        for horiz, char in enumerate(line):
            if char == '.':
                swap_grid[vert].append(False)
            elif (ca := calc_adjacents(g, vert, horiz)) == 0 and char == 'L':
                swap_grid[vert].append(True)
            elif char == '#' and ca >= 5:
                swap_grid[vert].append(True)
            else:
                swap_grid[vert].append(False)
    return swap_grid

with open('seating.txt') as f:
    text = f.readlines()
    grid = [[v for v in line.strip()] for line in text]
    swap = [[]]
    are_done = False
    while not are_done:
        swap = determine_swaps(grid)
        flat = [val for line in swap for val in line]
        if not any(flat):
            are_done = True
        else:
            for v, l in enumerate(swap):
                for h, b in enumerate(l):
                    if grid[v][h] == '.':
                        continue
                    if b:
                        grid[v][h] = '#' if grid[v][h] == 'L' else 'L'
print(sum(map(lambda x: x.count('#'), grid)))

