# PART 1

ones = 0
threes = 0
last = 0
with open('adapters.txt') as f:
    lines = sorted([int(l.strip()) for l in f.readlines()])
    lines.append(max(lines) + 3)
    for val in lines:
        if (diff := val - last) == 1:
            ones += 1
        elif diff == 3:
            threes += 1
        last = val
print((ones, threes))
print(ones * threes)

# PART 2

last = 0
with open('adapt_test.txt') as f:
    lines = sorted([int(l.strip()) for l in f.readlines()])
    lines.append(max(lines) + 3)
    