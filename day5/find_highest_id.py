# PART 1

def key_to_bin(key: str) -> int:
    b = ['0'] * len(key)
    for pos, val in enumerate(key):
        if val == 'B' or val == 'R':
            b[pos] = '1'
    return int(''.join(b), base=2)

top_id = 0
with open('id_list.txt') as f:
    for line in f.readlines():
        line = line.strip()
        row, col = key_to_bin(line[:7]), key_to_bin(line[7:])
        top_id = seat if (seat := (row * 8) + col) > top_id else top_id
print(top_id)

# PART 2
import itertools

def calc_all_options():
    valid_ids = {}
    for key in itertools.product(itertools.product('BF', repeat=7), itertools.product('RL', repeat=3)):
        boarding_id = ''.join([''.join(key[0]), ''.join(key[1])])
        valid_ids[boarding_id] = (key_to_bin(''.join(key[0])) * 8) + key_to_bin(''.join(key[1]))
    return valid_ids

possibilities = calc_all_options()
with open('id_list.txt') as f:
    all_ids = set()
    for line in f.readlines():
        line = line.strip()
        row, col = key_to_bin(line[:7]), key_to_bin(line[7:])
        seat = (row * 8) + col
        all_ids.add(seat)
for i in range(min(all_ids), max(all_ids)):
    if i - 1 in all_ids and i + 1 in all_ids and i not in all_ids and i in possibilities.values():
        print(f'try {i}')
