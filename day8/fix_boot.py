# PART 1

with open('boot_instr.txt') as f:
    lines = f.readlines()
    acc = 0
    seen_lines = set()
    pos = 0
    are_done = False
    while not are_done:
        if pos in seen_lines:
            print(f'Acc in P1: {acc}')
            are_done = True
            continue
        seen_lines.add(pos)
        line = lines[pos]
        op, num = (l := line.split())[0], int(l[1].strip())
        if op == 'jmp':
            pos += num
            continue
        elif op == 'acc':
            acc += num
        pos += 1

# PART 2, god help us all

import asyncio # time to take the plunge
from typing import Tuple, List

async def boot_up(changed: int, lines: List[str]) -> Tuple[int, bool]:
    acc = 0
    seen_lines = set()
    pos = 0
    are_done = False
    terminated = False
    while not are_done:
        if pos == len(lines):
            are_done = True
            terminated = True
            print(f'Changing L{changed} worked with an acc of {acc}')
            continue
        elif pos in seen_lines:
            are_done = True
            continue
        seen_lines.add(pos)
        line = lines[pos]
        op, num = (l := line.split())[0], int(l[1].strip())
        if op == 'jmp':
            pos += num
            continue
        elif op == 'acc':
            acc += num
        pos += 1
    return (acc, terminated)

async def calc_all_options():
    with open('boot_instr.txt') as f:
        lines = f.readlines()
        changes = []
        for pos, line in enumerate(lines):
            temp = lines.copy()
            op, num = tuple(line.split())
            if op == 'jmp':
                temp[pos] = line.replace('jmp', 'nop')
            elif op == 'nop' and int(num) != 0:
                temp[pos] = line.replace('nop', 'jmp')
            else:
                continue
            changes.append((pos, asyncio.ensure_future(boot_up(pos, temp))))
    await asyncio.gather(*changes)


asyncio.run(calc_all_options())
