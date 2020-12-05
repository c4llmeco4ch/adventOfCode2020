# PART 1

fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'}
valid_passports = 0
with open('passports.txt') as f:
    lines = f.readlines()
    while len(lines) > 1:
        try:
            end = lines.index('\n')
        except ValueError:
            end = len(lines)
        passport = set()
        is_valid = True
        for line in lines[:end]:
            words = line.split()
            for word in words:
                w = word[:3]
                if w in passport or w not in fields:
                    is_valid = False
                    break
                passport.add(w)
            if not is_valid:
                break
        if is_valid and (passport == fields or len(passport) == len(fields) - 1 and 'cid' not in passport):
                valid_passports += 1
        lines = lines[end + 1:]

print(valid_passports)

# PART 2

import re
fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'}
valid_measurements = ['in', 'cm']
valid_passports = 0
with open('passports.txt') as f:
    lines = f.readlines()
    while len(lines) > 1:
        try:
            end = lines.index('\n')
        except ValueError:
            end = len(lines)
        passport = set()
        is_valid = True
        for line in lines[:end]:
            words = line.split()
            for word in words:
                w = word[:3]
                val = word[4:]
                if len(val) == 0:
                    is_valid = False
                    break
                elif w == 'byr' and (not val.isdigit() or int(val) < 1920 or int(val) > 2002):
                    is_valid = False
                elif w == 'iyr' and (not val.isdigit() or int(val) < 2010 or int(val) > 2020):
                    is_valid = False
                elif w == 'eyr' and (not val.isdigit() or int(val) < 2020 or int(val) > 2030):
                    is_valid = False
                elif w == 'hgt':
                    m = val[-2:]
                    try:
                        amount = int(val[:-2])
                    except ValueError:
                        is_valid = False
                        break
                    if m not in valid_measurements or (m == 'in' and (amount < 59 or amount > 76)) or (m == 'cm' and (amount < 150 or amount > 193)):
                        is_valid = False
                elif w == 'hcl' and not re.match(r'#[a-f0-9]{6}', val):
                    is_valid = False
                elif w == 'ecl' and val not in ['amb','brn','blu','gry','grn','hzl','oth']:
                    is_valid = False
                elif w == 'pid' and (not val.isdigit() or len(val) != 9):
                    is_valid = False
                elif w not in fields:
                    is_valid = False
                if not is_valid:
                    break
                passport.add(w)
            if not is_valid:
                break
        if is_valid and (passport == fields or len(passport) == len(fields) - 1 and 'cid' not in passport):
            valid_passports += 1
        lines = lines[end + 1:]
print(valid_passports)