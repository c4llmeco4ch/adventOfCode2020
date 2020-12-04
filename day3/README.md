# Day 3 Write-up

Tl;dr:

- Ternary operators condense short if-else blocks into a single line
- List comprehension is one of the best features in Python. Use it.
- `enumerate()` combines the benefits of traditional for loops with those of a for-each loop
- `reduce()` helps combine values together using the same operation

## The Question

With the toboggan login problems resolved, you set off toward the airport. While travel by toboggan might be easy, it's certainly not safe: there's very minimal steering and the area is covered in trees. You'll need to see which angles will take you near the fewest trees.

Due to the local geology, trees in this area only grow on exact integer coordinates in a grid. You make a map (your puzzle input) of the open squares (.) and trees (#) you can see. For example:
```md
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
```
These aren't the only trees, though; due to something you read about once involving arboreal genetics and biome stability, the same pattern repeats to the right many times:
```md
..##.........##.........##.........##.........##.........##.......  --->
#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....  --->
.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........#.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...##....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#  --->
```
You start on the open square (.) in the top-left corner and need to reach the bottom (below the bottom-most row on your map).

The toboggan can only follow a few specific slopes (you opted for a cheaper model that prefers rational numbers); start by counting all the trees you would encounter for the slope right 3, down 1:

From your starting position at the top-left, check the position that is right 3 and down 1. Then, check the position that is right 3 and down 1 from there, and so on until you go past the bottom of the map.

The locations you'd check in the above example are marked here with O where there was an open square and X where there was a tree:
```md
..##.........##.........##.........##.........##.........##.......  --->
#..O#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....X..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#O#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..X...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.X#.......#.##.......#.##.......#.##.......#.##.....  --->
.#.#.#....#.#.#.#.O..#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........X.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.X#...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...#X....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...X.#.#..#...#.#.#..#...#.#.#..#...#.#  --->
```
In this example, traversing the map using this slope would cause you to encounter 7 trees.

Starting at the top-left corner of your map and following a slope of right 3 and down 1, how many trees would you encounter?

## Process

The goal for this first part was to simply keep track of the column we are moving to, move down to the next row, reevaluate our column, then determine if a tree is in our way. To this end, we need to start with 2 variables: `x`, which holds the column we are in and `trees`, the total number of trees we have seen thus far. These both start at 0, so our first two lines can be:

```python
x = 0
trees = 0
```

After that, we read from the file and engage with its contents line by line. This should be familiar to those who have kept up with the previous write-ups, but to reiterate, we use...

```python
with open('{file}') as f:
    for line in f.readlines():
        # code goes here
```

Luckily for us, we know that the first line is safe, so we can actually skip it by taking a sublist of `f.readlines()`, changing the second line to `for line in f.readlines()[1:]:`. One thing to be aware of (that I personally got burned by) is potential whitespace at the end of each line, depending on how the file is copied. If this is a problem, `str.strip()` will solve it.

Afterwards, we need to move to correct column. For part 1, we move 3 columns to the right. This would be a simple `x += 3`. However, we need to keep in mind that the row extends infinitely to the right. This means we need to implement "wrapping" to bring our `x` value back to the beginning of the line. A simple way to implement this is through the use of modulo: `(x + 3) % len(line)`. To this point, our code looks like...

```python
x = 0
trees = 0
with open('{file}') as f:
    for line in f.readlines()[1:]:
        line = line.strip()
        x = (x + 3) % len(line)
```

Now that we have moved to the correct column, we want to determine if the space we are on is a tree and, if so, increment `trees`:

```python
if line[x] == '#':
    trees += 1
```

Putting this all together, we get...

```python
x = 0
trees = 0
with open('{file}') as f:
    for line in f.readlines()[1:]:
        line = line.strip()
        x = (x + 3) % len(line)
        if line[x] == '#':
            trees += 1
```

Running this code against my input data, we get 209 trees.

## How this changes for part 2

Unlike days 1 and 2, day 3 begins to sees larger additions between parts 1 and 2. For part 2, we are asked to solve not just 1 problem but 5. Then, once the 5 situations have been solved, we must take the product of each situation's tree count for our answer. The 5 calculations we must track are...

- Right 1, down 1.
- Right 3, down 1. (This is the slope calculated in part 1)
- Right 5, down 1.
- Right 7, down 1.
- Right 1, down 2.

There are two main ways to approach part 2. The first is to repeat the reading process 5 times, once per slope, and calculate each tree count separately. The second is to read the file once and keep track of each tree count and x position at the same time. I chose to pursue the latter. To this end, we need to alter `x` from being an integer to being a list of integers, 1 per slope: `x = [0] * 5`. The same thing can be done for trees. Finally, to calculate how often and by how much we need to alter `x`, we create two lists for the x and y speeds:

```python
x_speed = [1, 3, 5, 7, 1]
y_speed = [1, 1, 1, 1, 2]
```

Now, unlike before where we can just iterate through each line in our input, we now need to be conscious of *which* line we are on so we can properly assess whether to shift over based on our `y` speed. To do this we are going to use a nifty Python function called `enumerate()`.

### Enumerate(), or "For loops in Python are a lie"

In programming, there are 2 types of for loops, traditional C-style for loops and for-each loops. An example of each in other programming languages is as follows:

```java
//traditional for loop
for(int i = 0; i < carDealerships.length; i++){
    // code
}
//for-each loop
for(String word : sentence){
    //code
}
```

The benefit of the former is in its generality. You can use it to both read from an array and write to indecies in said array. This makes it applicable to effectively any problem where a for loop is reasonable. On the other hand, a for-each loop is a bit more specialized in its uses. Depending on the language, altering `word` in the above example would not actually change the version of `word` inside `sentence`. Phrased another way, they give us direct access to each value (as opposed to writing `sentence[i]`) at the expense of being *read-only*.

Python is a bit of an oddball, though. Writing a traditional C-style for loop is typically taught using the `range()` function:

```python
for i in range(len(carDealerships)):
    # code
```

But what does `range()` actually do? [According to the official documentation](https://docs.python.org/3.8/library/stdtypes.html#typesseq-range), the function creates an immutable sequence similar to a tuple or list. So really, the above code snippet is actually picking individual values from a sequence. Further exploration might lead someone to realize that altering `i` will also not affect the values inside the iterable. This means that in Python, all for loops are *in fact* for-each loops. 

`enumerate()`, however, allows for the creation of a for loop that has the benefits of *both* a traditional for loop and a for-each loop. [By iterating over tuples](https://docs.python.org/3.8/library/functions.html#enumerate) of the position and value of items in an list, we are given easy read access *and* easy write access in a nice, Pythonic package.

So, to ensure we know which line we are reviewing in part 2, we can rewrite our code thusly:

```python
with open('{file}') as f:
    for pos, line in enumerate(f.readlines()):
```

### List Comprehension

Now that we know which lines we are on, we need to move each of our x positions to the corresponding spot. We could write that code using a simple for loop (using our new `enumerate` tool):

```python
for pos, val in enumerate(x):
    x[pos] = (val + 3) % len(line)
```

But Python has an even better way: [list comprehension](https://www.w3schools.com/python/python_lists_comprehension.asp)! We can shrink those two lines of code down into a single line by writing `x = [(x[j] + xS) % len(line) for j, xS in enumerate(x_speed)]`. Hold on, though! We have a problem. We do not necessarily want to move horizontally if our y slope is greater than 1. As such, we need to figure out, for each slope, whether we can move based on `pos`: `should_not_skip = [pos % yS == 0 for yS in y_speed]`. This way, we could use an if statement to determine whether or not to proceed to move horizontally:

```python
for pos, val in enumerate(x):
    if should_not_skip[pos]:
        x[pos] = (val + 3) % len(line)
```

But, much like in other languages, we can use a neat tool called a [ternary operator](https://www.geeksforgeeks.org/ternary-operator-in-python/) to implant our if statement inside a list comprehension:

```python
x = [(x[j] + (xS if should_not_skip[j] else 0)) % len(line) for j, xS in enumerate(x_speed)]
```

Furthermore, we can continue this trend and similarly update our condition to determine if a tree is in our way:

```python
trees = [trees[p] + (1 if line[i] == '#' and should_not_skip[p] else 0) for p, i in enumerate(x)]
```

This brings our full piece of code t...

```python
x_speed = [1, 3, 5, 7, 1]
y_speed = [1, 1, 1, 1, 2]
x = [0] * len(x_speed)
trees = [0] * len(x_speed)

with open('slope.txt') as f:
    for pos, line in enumerate(f.readlines()[1:]):
        line = line.strip()
        should_not_skip = [(pos - 1) % yS == 0 for yS in y_speed]
        x = [(x[j] + (xS if should_not_skip[j] else 0)) % len(line) for j, xS in enumerate(x_speed)]
        trees = [trees[p] + (1 if line[i] == '#' and should_not_skip[p] else 0) for p, i in enumerate(x)]
```

### Bringing it all together (literally) with reduce()

Normally, this would be the point in the code where I'd explain that I did indeed run the code and got a final answer. However, there is a simple way and a more complicated but interesting way to perform this operation of finding the product from a list of numbers.

First the simple way: we create a running total variable and give it a value of 1. After that, we iterate over our tree values and mulitply them by the running total, having our answer afterwards:

```python
ans = 1
for tree in trees:
    ans *= tree
```

While passable, we can gain a lot from learning how to use the `reduce()` function. Unlike `filter()`, which plucks out values we do want, and `map()`, which alters all numbers by some calculation, `reduce()` [combines all values in an iterable](https://docs.python.org/3/library/functools.html#functools.reduce) by keeping a running total and using that total to help iterate over the remaining values, repeating until we have a combined total based on the operation:

```python
ans = reduce(lambda x, y: x * y, trees)
```

Coupled with a lambda function, `reduce`, like it's siblings `map` and `filter`, can be a hyper-powerful tool for writing concise code, so it's something to keep in mind for future problems.

And yes, when run against this data set, we receive a value of 1,574,890,240.

---

[Find me on Twitter](https://twitter.com/c4llmeco4ch)