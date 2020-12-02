from typing import Tuple
import re
# PART 1

'''My initial implementation of breaking each line's key down into easy-to-use parts
def parse_key(k: str) -> Tuple[int, int, str]:
    """Given a key in the format '{num}-{num} {letter}, return the three values as a tuple

    Args:
        k (str): The provided key to compare against a password

    Returns:
        Tuple[int, int, str]: The small and big numbers, as well as the char to search for
    """
    nums, ch = k.split()
    small, big = int((s := nums.split('-'))[0]), int(s[1])
    return small, big, ch
'''

with open('passwords.txt') as f:
    correct = 0
    for line in f.readlines():
        small, big, ch, pw = int((s := re.split('[-: ]', line))[0]), int(s[1]), s[2], s[4]
        if (c := pw.count(ch)) >= small and c <= big:
            correct += 1
    print(correct)

# PART 2

with open('passwords.txt') as f:
    correct = 0
    for line in f.readlines():
        small, big, ch, pw = int((s := re.split('[-: ]', line))[0]), int(s[1]), s[2], s[4]
        if (pw[small - 1] == ch or pw[big - 1] == ch) and pw[small - 1] != pw[big - 1]:
            correct += 1
    print(correct)
