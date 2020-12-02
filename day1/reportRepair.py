import itertools

# PART 1

with open('expenses.txt') as f:
   pairs = itertools.combinations(
            [val for price in f.readlines() if (val := int(price)) < 2020], 2)

winner = list(filter(lambda x: sum(x) == 2020, pairs))[0]
print(f'The pair of numbers is {winner[0]}, {winner[1]} with a sum of {sum(winner)}.')
print(f'The product is {winner[0] * winner[1]}')

# PART 2

with open('expenses.txt') as f:
    triplets = itertools.combinations(
                [val for price in f.readlines() if (val := int(price)) < 2019], 3)

winner = list(filter(lambda x: sum(x) == 2020, triplets))[0]
print(f'The set of numbers is {winner[0]}, {winner[1]}, {winner[2]} with a sum of {sum(winner)}.')
print(f'The product is {winner[0] * winner[1] * winner[2]}')