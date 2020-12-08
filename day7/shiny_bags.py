# PART 1

bag_holders = 0

with open('rules.txt') as f:
    lines = f.readlines()
    valid_holders = ['shiny gold bag']
    pos = 0
    while pos < len(valid_holders):
        waldo = valid_holders[pos]
        for line in lines:
            line = line.strip()
            if waldo in (holder := line.split(' contain '))[1]:
                if holder[0][:-1] not in valid_holders:
                    bag_holders += 1
                    valid_holders.append(holder[0][:-1])
        pos += 1
print(bag_holders)

# PART 2
import re

bag_cache = {}

def count_inner_bags(bag: str, rules: str) -> int:
    """Determine the number of bags inside "bag"

    Args:
        bag (str): The bag we are finding the count of
        lines (List[str]): All the rules provided

    Returns:
        int: The count of bags inside "bag"
    """
    for line in rules:
        line = line.strip()
        if not line.startswith(bag):
            continue
        # m = re.match(rf'{bag}s contain ([0-9]? .* .* .*[.,])+', rules, re.IGNORECASE) python please...
        if (others := line.split(' contain ')[1]) == 'no other bags.':
            bag_cache[bag] = 1
            return 1
        others = others[:-1].split(', ')
        total = 0
        for b in others:
            num, color = re.match(r'([0-9]+) (.*)', b).groups()
            color = color.rstrip('s') # take out the 's' from 'bags'
            total += int(num) * bag_cache.get(color, count_inner_bags(color, rules))
        bag_cache[bag] = total + 1
        return total

with open('rules.txt') as f:
    lines = f.readlines()
    print(count_inner_bags('shiny gold bag', lines))
