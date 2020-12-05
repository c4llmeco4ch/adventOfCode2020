# PART 1

def bin_search(key: str, low = 0, high = 127) -> int:
    for val in key:
        current = (high + low) // 2
        if val == 'F' or val == 'L':
            high = current
        elif val == 'B' or val == 'R':
            low = current
    return current

top_id = 0
with open('id_list.txt') as f:
    for line in f.readlines():
        row, col = bin_search(line[:7]), bin_search(line[7:], high=7)
        top_id = seat if (seat := (row * 8) + col) > top_id else top_id
print(top_id)

# PART 2

with open('id_list.txt') as f:
    all_ids = set()
    for line in f.readlines():
        row, col = bin_search(line[:7]), bin_search(line[7:], high=7)
        seat = (row * 8) + col
        all_ids.add(seat)
all_ids = sorted(list(all_ids))
for pos, val in enumerate(all_ids[:-1]):
    if all_ids[pos + 1] != val + 1:
        print(f'Am id {val}, next is {all_ids[pos + 1]}')