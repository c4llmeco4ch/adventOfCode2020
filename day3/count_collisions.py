# PART 1

x = 0
trees = 0
with open('slope.txt') as f:
    for line in f.readlines()[1:]:
        line = line.strip()
        x = (x + 3) % len(line)
        print(f'{line[:x]}[{line[x]}]{line[x+1:]} | {x}')
        if line[x] == '#':
            trees += 1
print(trees)

# PART 2
xSpeed = [1, 3, 5, 7, 1]
ySpeed = [1, 1, 1, 1, 2]
x = [0] * len(xSpeed)
trees = [0] * len(xSpeed)

with open('slope.txt') as f:
    for pos, line in enumerate(f.readlines()[1:]):
        line = line.strip()
        shouldNotSkip = [(pos - 1) % yS == 0 for yS in ySpeed]
        x = [(x[j] + (xS if shouldNotSkip[j] else 0)) % len(line) for j, xS in enumerate(xSpeed)]
        trees = [trees[p] + (1 if line[i] == '#' and shouldNotSkip[p] else 0) for p, i in enumerate(x)]
total = 1
print(trees)
for val in trees:
    total *= val
print(total)

