# PART 1

from typing import List, Tuple, Dict

invalid_num = -1

def init_map(nums: List[str]) -> Dict[int, List[Tuple[int, int]]]:
    my_map = {}
    for i in nums:
        i = int(i.strip())
        for j in nums[i + 1:]:
            j = int(j.strip())
            print(my_map.get(i + j, []))
            if not my_map.get(i + j):
                my_map[i + j] = []
            my_map[i + j].append((i, j))
    return my_map

def drop(val: int, d: Dict[int, List[Tuple[int, int]]]) -> Dict[int, List[Tuple[int, int]]]:
    for k in d.keys():
      for tup in d[k]:
          if val in tup:
              d[k].remove(tup)
              break
    return d

with open('xmas_cipher.txt') as f:
    lines = f.readlines()
    sum_dict = init_map(lines[:25])
    for front, val in enumerate(lines[25:]):
        val = int(val)
        if not sum_dict.get(val):
            print(f'found the answer: {val}')
            invalid_num = val
        sum_dict = drop(lines[front], sum_dict)
        for num in lines[front + 1: front + 25]:
            num = int(num)
            if not sum_dict.get(num + val):
                sum_dict[num + val] = []
            sum_dict[num + val].append((val, num))

# PART 2
with open('xmas_cipher.txt') as f:
    lines = f.readlines()
    for pos, line in enumerate(lines):
        total = line = int(line)
        offset = 0
        while total < invalid_num:
            offset += 1
            total += int(lines[pos + offset])
        if total == invalid_num:
            weakness = (line, int(lines[pos + offset]))
            print(f'Found it. {(line, int(lines[pos + offset]))}')
            r = [int(x) for x in lines[pos: pos + offset + 1]]
            break
print(min(r) + max(r))
