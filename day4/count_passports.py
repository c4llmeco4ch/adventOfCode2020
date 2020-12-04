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
        else:
            print(f'Invalid passport: {lines[:end]}\nMissing: {fields.difference(passport)}')
        lines = lines[end + 1:]

print(valid_passports)

# PART 2
import re
fields = [r'byr:(19[2-9][0-9]|200[0-2])', r'iyr:20(1[0-9]|20)', r'eyr:20(2[0-9]|30)',
          r'hgt:(1([5-8][0-9]|9[0-3])cm|[59|6[0-9]|7[0-6]]in)', r'hcl:#[0-9a-f]{6}', r'ecl:[amb|brn|blu|gry|grn|hzl|oth]',
          r'pid:[0-9]{9}']
valid_passports = 0
with open('passports.txt') as f:
    lines = f.readlines()
    while len(lines) > 1:
        try:
            end = lines.index('\n')
        except ValueError:
            end = len(lines)
        passport = [False] * len(fields)
        p_values = ''.join(lines[:end])
        for pos, val in enumerate(fields):
            if pos == 0:
                print(f'attempting to find byr in {p_values[:-1]}')
            if re.match(val, p_values):
                print('got it\n')
                passport[pos] = True
        if all(passport):
            passport += 1
        lines = lines[end + 1:]
print(valid_passports)