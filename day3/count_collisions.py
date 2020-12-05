# PART 1

x = 0
trees = 0
with open('slope.txt') as f:
    for line in f.readlines()[1:]:
        line = line.strip()
        x = (x + 3) % len(line)
        if line[x] == '#':
            trees += 1
print(trees)

# PART 2

x_speed = [1, 3, 5, 7, 1]
y_speed = [1, 1, 1, 1, 2]
x = [0] * len(x_speed)
trees = [0] * len(x_speed)

with open('slope.txt') as f:
    for pos, line in enumerate(f.readlines()[1:]):
        line = line.strip()
        should_not_skip = [(pos - 1) % yS == 0 for yS in y_speed]
        x = [(x[j] + (xS if should_not_skip[j] else 0)) % len(line) for j, xS in enumerate(x_speed)]
        trees = [trees[p] + (1 if line[i] == '#' and should_not_skip[p] else 0) for p, i in enumerate(x)]

from functools import reduce
print(reduce(lambda x, y: x * y, trees))
