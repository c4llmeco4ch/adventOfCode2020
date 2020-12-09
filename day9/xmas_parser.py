import itertools

with open('xmas_cipher.txt') as f:
    lines = f.readlines()
    sum_dict = init_map(lines[:25])
    for front, val in enumerate(lines[25:]):
        if val not in sum_dict.keys():
            print(f'found the answer: {val}')
        sum_dict = drop(int(lines[front]), sum_dict)
        for num in lines[front + 1: front + 25]:
            sum_dict = sum_dict.get(num + int(val), []).append((val, num))