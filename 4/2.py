import re

text = open("input.txt").read()
passports = text.split("\n\n")
passports = map(str.strip, passports)
passports = list(passports)


def structify(passport):
    ms = list(re.finditer(r"(\w{3}):([^\s\n]+)", passport))
    ms = map(re.Match.groups, ms)
    ms = list(ms)
    return ms


passports = map(structify, passports)
passports = list(passports)

fields = sorted(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])


def get_passport_fields(passport):
    return list(map(lambda field: field[0], passport))


def check_height(height):
    m = re.match(r"^(\d+)(cm|in)$", height)

    if m is None:
        return False

    height = int(m.group(1))

    if m.group(2) == "in":
        return 59 <= height <= 76
    else:
        return 150 <= height <= 193


check_fns = {
    "byr": (lambda value: re.match(r"^\d{4}$", value) is not None and 1920 <= int(value) <= 2002),
    "iyr": (lambda value: re.match(r"^\d{4}$", value) is not None and 2010 <= int(value) <= 2020),
    "eyr": (lambda value: re.match(r"^\d{4}$", value) is not None and 2020 <= int(value) <= 2030),
    "hgt": check_height,
    "hcl": (lambda value: re.match(r"^#[0-9a-f]{6}$", value) is not None),
    "ecl": (lambda value: value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]),
    "pid": (lambda value: re.match(r"^\d{9}$", value) is not None),
    "cid": (lambda value: True),
}


def check(passport):
    passport_fields = get_passport_fields(passport)

    if "cid" in passport_fields:
        passport_fields.remove("cid")
    passport_fields.sort()

    if not (passport_fields == fields):
        return False

    for field, value in passport:
        if not check_fns[field](value):
            return False

    return True


passports = map(lambda passport: int(check(passport)), passports)
passports = list(passports)

print(sum(passports))
