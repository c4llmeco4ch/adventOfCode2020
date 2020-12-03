# Day 2 Write-up

Tl;dr:

- Regular expressions are a thing. Learn the dark magic, rule the world (of string manipulation).
- The walrus (operator) rears its head once again
- XOR (^) takes a 3-boolean-operator condition and reduces it to 1

## Question

Your flight departs in a few days from the coastal airport; the easiest way down to the coast from here is via toboggan.

The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day. "Something's wrong with our computers; we can't log in!" You ask if you can take a look.

Their password database seems to be a little corrupted: some of the passwords wouldn't have been allowed by the Official Toboggan Corporate Policy that was in effect when they were chosen.

To try to debug the problem, they have created a list (your puzzle input) of passwords (according to the corrupted database) and the corporate policy when that password was set.

For example, suppose you have the following list:

```md
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
```

Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no instances of b, but needs at least 1. The first and third passwords are valid: they contain one a or nine c, both within the limits of their respective policies.

How many passwords are valid according to their policies?

## Process

Much like day 1, our first task is to pull each line and break it up into the parts we need. As seen [in my day one write-up](https://github.com/c4llmeco4ch/adventOfCode2020/blob/main/day1/README.md), the reading part is fairly simple:

```python
with open('{file}') as f:
    lines = f.readlines()
    for line in lines:
        # do the thing
```

Now, we want to look at each line and determine if it is a valid password. A simple way to achieve this result would be to break the line up into a left and right side (or a "key" and a "password"): `key, pw = tuple(line.split(':'))`. Afterward, we can break up the key into its 3 parts: the minimum, the maximum, and the character we are searching for:

```python
nums, ch = key.split()
small, big = int((s := nums.split('-'))[0]), int(s[1])
```

If you have never seen the `(s := nums.split...` portion of that code snippet, I gave a good review of it [in yesterday's write-up](https://github.com/c4llmeco4ch/adventOfCode2020/blob/main/day1/README.md#the-walrus-operator). To briefly recap, the walrus operator (:=) allows for assigning to a variable in the middle of an expression. Because we would otherwise need to repeat `nums.split('-')` to calculate `big`, assigning the split to `s` allows for us to avoid repetition when possible.

Moving on, we now have the min-max range, the character we are searching for. Now we just need to tie it all together to calculate the number of valid passwords. We will first employ a new variable, `count`, which is initialized before the for loop. Inside the for loop, we will then utilize the [count function](https://www.tutorialspoint.com/python/string_count.htm) to help determine the number of times `ch` exists within the password and check that `small <= pw.count(ch) <= big`:

```python
open('{file}') as f:
    lines = f.readlines()
    count = 0
    for line in lines:
        key, pw = tuple(line.split(':'))
        nums, ch = key.split()
        small, big = int((s := nums.split('-'))[0]), int(s[1])
        if small <= pw.count(ch) <= big:
            count += 1
```

For my data, running this code resulted in 398 valid passwords.

But can we do better? Can we condense this code further? Let us consider this snippet from the above code:

```python
key, pw = tuple(line.split(':'))
nums, ch = key.split()
small, big = int((s := nums.split('-'))[0]), int(s[1])
```

Wouldn't it be great if we could do this whole thing in one line? If we could somehow split by the colon, space, and dash at once, that would do it. The problem is, `str.split()` only works on one string at a time. Luckily for us, there does exist such a way; however, to achieve this, I must introduce you to the dark magic that is...

### Regular Expressions

[Regular expressions](https://en.wikipedia.org/wiki/Regular_expression) are one of the best tools for interacting with strings. Python has its own [regular expressions module](https://docs.python.org/3/library/re.html) that we will be using to help cut the above expression to one line. While I cannot fully explain regular expressions here, I can showcase here a basic use case for it. Much like how we used `str.split()` earlier, we will be using `re.split()` to solve this problem.

First, when working with regular expressions, a pattern needs to be created through which the `re` function can compare the string against. In this case, our pattern is "either `-`, `:`, or `{space}`." When asking to split by any from a selection, we use brackets ("[]"), with the possible options inside. This means our pattern would be `'[-: ]'`. This means our new split function would look like `re.split(r'[-: ]')`. If our practice line is, for example, `1-4 s: abcsfdsg`, we are left with a list: `['1', '4', 's', '', 'abcsfdsg']`. Thus, we can condense the 3 lines from before by assinging `small`, `big`, `ch`, and `pw` to their respective positions in the list:

```python
small, big, ch, pw = int((s := re.split(r'[-: ]', line)))[0], int(s[1]), s[2], s[4]
```

Bringing it all together, we are left with...

```python
open('{file}') as f:
    lines = f.readlines()
    count = 0
    for line in lines:
        small, big, ch, pw = int((s := re.split(r'[-: ]', line)))[0], int(s[1]), s[2], s[4]
        if small <= pw.count(ch) <= big:
            count += 1
```

## How this changes for part 2

This time, part 2 changes up the formula for what defines a valid password. Instead of `small` and `big` representing a range of occurences, it represents positions. More specifically, we must find the given character at the `small`th or `big`th position, starting from 1 (unlike starting from 0 that we are used to). Luckily, this only affects the if condition. We need to verify that `ch` exists in at least one of those positions but not both. One means of accomplishing this would be `if (pw[small - 1] == ch or pw[big - 1] == ch) and (pw[small - 1] != pw[big - 1])`. However, we can do better using a less well-known boolean operator: bitwise XOR.

### XOR

For those not in the know, let's briefly review XOR's more popular siblings, AND and OR.

AND is true if both the value to the left and right are true:

A | B | AND
--- | --- | ---
T | T | T
T | F | F
F | T | F
F | F | F

OR is true so long as *at least* one value is true:

A | B | OR
--- | --- | ---
T | T | T
T | F | T
F | T | T
F | F | F

XOR, on the other hand, is short for "exclusive or". This means the condition is true if *only* one value is true:

A | B | XOR
--- | --- | ---
T | T | F
T | F | T
F | T | T
F | F | F

To use XOR in Python (and most languages), a carrot (`^`) is used. With this, we can shorten our condition to `if (pw[small - 1] == ch) ^ (pw[big - 1] == ch)`. 

Thus, the full code for this part is...

```python
with open('passwords.txt') as f:
    correct = 0
    for line in f.readlines():
        small, big, ch, pw = int((s := re.split(r'[-: ]', line))[0]), int(s[1]), s[2], s[4]
        if (pw[small - 1] == ch) ^ (pw[big - 1] == ch):
            correct += 1
```

Run against my data set, the provided result is 562 valid passwords.
