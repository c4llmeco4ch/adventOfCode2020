# Day 1 Writeup

Tl;dr:

- The Walrus Operator, what it is and how to use it
- `itertools`, an amazing module for working with iterables

## Question

"After saving Christmas five years in a row, you've decided to take a vacation at a nice resort on a tropical island. Surely, Christmas will go on without you.

The tropical island has its own currency and is entirely cash-only. The gold coins used there have a little picture of a starfish; the locals just call them stars. None of the currency exchanges seem to have heard of them, but somehow, you'll need to find fifty of these coins by the time you arrive so you can pay the deposit on your room.

To save your vacation, you need to get all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input); apparently, something isn't quite adding up.

Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

For example, suppose your expense report contained the following:

```md
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

Introduced in Python 3.8, the "Walrus Operator" (`:=`) or [the more boring "Assignment Expression"](https://www.python.org/dev/peps/pep-0572/) provides a means of assigning to a variable while other operations take place. Let's imagine we have the following code snippet:

```python
x = 5
y = 6
if x + y >= 10:
    print(f'{x + y} is at least a double-digit number')
```

Notice how we had to repeat `x + y` twice? One way to combat this repetition would be to save `x + y` to a variable, `s` and use that instead:

```python
x = 5
y = 6
s = x + y
if s >= 10:
    print(f'{s} is at least a double-digit number')
```

With the walrus operator, though, we can actually combine the third and fourth lines of the above example, consolidating our code while also avoiding repetition:

```python
x = 5
y = 6
if (s := x + y) >= 10:
    print(f'{s} is at least a double-digit number')
```

So how does this apply to our Advent of Code solution? Well, we said it would be great if we could consolidate `int(line)` to avoid repetition, which can be realized through clever use of the walrus operator:

```python
with open('{file}') as f:
    my_numbers = [num for line in f.readlines() if (num := int(line)) < 2020]
```

---

Awesome! So now we have a clean, efficent, repetition-free means of saving each of our numbers to a list. Next, we need to actually determine which pair of numbers has a sum of 2020. My first instinct when tackling this problem was to attempt a recursive divide-and-conquer solution, emphasizing the least number of jumps by sorting the provided input and attacking the problem with an algorithm similar to a binary search. This solution began to get very bogged down, however.

Around this time, I remembered a very useful library that, while possibly less efficient from a runtime perspective, would make the code vastly more concise and readable: [itertools](https://docs.python.org/3/library/itertools.html). More specifically, itertools has a function called `combinations` which forms tuples of a requested length providing all the possible combinations from the desired iterable. In our case, the iterable would be `my_numbers`, with the desired length being 2. Thus, our code transformed to be:

```python
import itertools

with open('{file}') as f:
    my_numbers = [num for line in f.readlines() if (num := int(line)) < 2020]
    my_pairs = itertools.combinations(my_numbers, 2)
```

However, we can consolidate this further by removing `my_numbers`, giving us...

```python
import itertools

with open('{file}') as f:
    my_pairs = itertools.combinations([num for line in f.readlines() if (num := int(line)) < 2020], 2)
```

Now that we have a list of pairs, we simply need to iterate over each pair and determine if the pair has a sum of 2020, saving that pair in the process. For a simple solution, this can be done using a basic for loop:

```python
for one, two in my_pairs:
    if one + two == 2020:
        # print the solution, save one and two to a variable for future use or return a result, if in a function
```

Optionally, we can use filter and a lambda function to give back the pair we desire:

```python
winner = list(filter(lambda x: sum(x) == 2020, pairs))[0] # winner is a tuple of (num1, num2)
```

Running through this problem on my provided data set and printing the pair of values, we get 447 and 1573 for a product of 703131.

## How this changes for part 2

Part 2 simply asks us to repeat the process, this time looking for 3 values whose sum is 2020 while providing the product. Ultimately, the large majority of our code remains the same. The only key difference is our `itertools.combination()` line, which needs to replace the "2" with a "3" in the second parameter:

```python
with open('{file}') as f:
    my_pairs = itertools.combinations([num for line in f.readlines() if (num := int(line)) < 2019], 3)
```

Repeating the remainder of the code and running this provides us with the valid triplet of 930, 609, and 481 for a product of 272423970.
