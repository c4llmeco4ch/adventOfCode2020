# Day 1 Writeup

## Question

"After saving Christmas five years in a row, you've decided to take a vacation at a nice resort on a tropical island. Surely, Christmas will go on without you.

The tropical island has its own currency and is entirely cash-only. The gold coins used there have a little picture of a starfish; the locals just call them stars. None of the currency exchanges seem to have heard of them, but somehow, you'll need to find fifty of these coins by the time you arrive so you can pay the deposit on your room.

To save your vacation, you need to get all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input); apparently, something isn't quite adding up.

Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

For example, suppose your expense report contained the following:
```
1721
979
366
299
675
1456
```
In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.

Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply them together?"

## Process

The solution for both parts of day 1's problem is effectively repeated, so we'll focus on the steps needed to reach part 1 and do a quick review on what (if anything) changes for part 1.

As we see in our provided data set from the prompt, the input is a set of numbers, 1 per line. Thus, the first step is to:

1) Get all the lines from the list, then...
2) Change all the numbers from strings (remember, this is a text file) to integers

First, let's deal with getting each line from the text file. This is in itself pretty simple:

```python
with open('{text file name}') as {variable name, 'f' works here}:
    lines = f.readlines()
```

Then, in order to obtain each number from `lines`, we could use a for-loop:

```python
my_numbers = []
for line in lines:
    num = int(line)
    my_numbers.append(num)
```

This works fine, but there is a much better solution in Python: list comprehension! We can take those 4 lines and bring them to a single line: `my_numbers = [int(line) for line in lines]`. This would bring our full `with` clause to:
```python
with open('{file}') as f:
    lines = f.readlines()
    my_numbers = [int(line) for line in lines]
```

But we can be sneakier! Do we even need `lines`? It's not being manipulated at all, so we can actually just replace our use of the variable in our list comprehension with `f.readlines()`:

```python
with open('{file}') as f:
    my_numbers = [int(line) for line in f.readlines()]
```

Now we're getting somewhere. But let's say a number in our data set is 2025. Do we need to retain it? Won't that just slow down later calculations? So, let's remove those values by tacking an if statement to the back-end of our comprehension: `my_numbers = [int(line) for line in f.readlines() if int(line) >= 2020]`. While this is great, there is some repetition on the form of `int(line)`. Is there any way to remove this repetition...?

### The Walrus Operator

Introduced in Python 3.8, the "Walrus Operator" or the more boring "Assignment Expression"