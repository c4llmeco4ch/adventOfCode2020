# PART 1

ans = 0
with open('customs.txt') as f:
    are_done = False
    lines = f.readlines()
    while not are_done:
        try:
            end = lines.index('\n')
        except ValueError:
            end = len(lines) + 1
        group = lines[:end]
        resp = set()
        for line in group:
            line = line.strip() # I learned my lesson this time...
            for ch in line: # Not thrilled about a nested loop
                resp.add(ch)
        ans += len(resp)
        lines = lines[end + 1:]
        if len(lines) < 1:
            are_done = True
print(ans)

# PART 2

ans = 0
with open('customs.txt') as f:
    are_done = False
    lines = f.readlines()
    while not are_done:
        try:
            end = lines.index('\n')
        except ValueError:
            end = len(lines)
        group = lines[:end]
        resp = {ch for ch in group[0].strip()} # Poggers
        for line in group[1:]:
            line = line.strip()
            resp = {v for v in resp if v in line}
        ans += len(resp)
        lines = lines[end + 1:]
        if len(lines) < 1:
            are_done = True
print(ans)
