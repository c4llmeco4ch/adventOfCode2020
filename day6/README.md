# Day 6 Write-up

Tl;dr:

- T
- B
- D

## Problem

As your flight approaches the regional airport where you'll switch to a much larger plane, customs declaration forms are distributed to the passengers.

The form asks a series of 26 yes-or-no questions marked a through z. All you need to do is identify the questions for which anyone in your group answers "yes". Since your group is just you, this doesn't take very long.

However, the person sitting next to you seems to be experiencing a language barrier and asks if you can help. For each of the people in their group, you write down the questions for which they answer "yes", one per line. For example:

```md
abcx
abcy
abcz
```

In this group, there are 6 questions to which anyone answered "yes": a, b, c, x, y, and z. (Duplicate answers to the same question don't count extra; each question counts at most once.)

Another group asks for your help, then another, and eventually you've collected answers from every group on the plane (your puzzle input). Each group's answers are separated by a blank line, and within each group, each person's answers are on a single line. For example:

```md
abc

a
b
c

ab
ac

a
a
a
a

b
```

This list represents answers from five groups:

The first group contains one person who answered "yes" to 3 questions: a, b, and c.
The second group contains three people; combined, they answered "yes" to 3 questions: a, b, and c.
The third group contains two people; combined, they answered "yes" to 3 questions: a, b, and c.
The fourth group contains four people; combined, they answered "yes" to only 1 question, a.
The last group contains one person who answered "yes" to only 1 question, b.
In this example, the sum of these counts is 3 + 3 + 3 + 1 + 1 = 11.

For each group, count the number of questions to which anyone answered "yes". What is the sum of those counts?

## Process

When dealing with summation, products, or general count-keeping, the first thing we need is a running total. For this problem, that will simply be `ans = 0`. With that out of the way, we need to read in all the lines. As usual, that looks like...

```python
with open('{file}') as f:
    lines = f.readlines()
```

So, we have all of our lines. In my mind, the next step is to figure out which group is "next", evaluate that group, then add its count to `ans`. To do that, we need to figure out how many times to repeat that process. In my case, I decided to use a while loop. To maintain the loop, a simple placeholder boolean is sufficient:

```python
are_done = False
while not are_done:
    # code
```

Now, we need to establish what set of lines we need to review for a particular group. Luckily, we have a solid indicator in a blank link (one where the only character is `\n`). Thus, because `lines` is a list, we have access to `end = lines.index('\n')`. Now, we can take a sublist of lines ranging from the beginning to `end`: `group = lines[:end]`. Putting everything we have so far together, we get:

```python
ans = 0
with open('{file}') as f:
    lines = f.readlines()
    are_done = False
    while not are_done:
        end = lines.index('\n')
        group = lines[:end]
```

Awesome. We have our group, so now we need to determine how many unique questions are being asked. Luckily for us, there is a perfect way to hold unique values: [a set](https://realpython.com/python-sets/). Starting off, we have no questions registered, so we initialize an empty set using `response = set()`.

Now, we have our group, and we have a way to keep track of the unique questions in that group. Next up is reviewing each person's questions and seeing what is available. A for-each loop can suffice here, with my version being `for line in group:`. Now, how do we determine which new questions are in `line`? A simple approach might involve using a nested for loop over each letter, adding it to `response` as `set.add()` does nothing if the value is in the set:

```python
for line in group:
    for question in line:
        response.add(question)
```

However, there is an even better way to approach this issue. Sets have two special operations: intersect and union. Without diving too far into set theory, intersection takes two sets and returns only the values that are in both (put a pin in this for later). Union, on the other hand, returns the unique values that are in both sets. For this part, union seems like a perfect fit. There are two ways of utilizing this function in Python: `set.union()` and the union operator (`|`). By casting `line` as a set, we can simply write `response = response | set(line)`.

With the for loop, `for line in group:`, completed, we now have every unique response from that group stored in `response`. All we have to do is add how many responses we have to `ans`: `ans += len(response)`. 

Finally, we need to recalibrate `lines` for our next group. 