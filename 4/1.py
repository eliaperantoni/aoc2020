import re

text = open("input.txt").read()
passports = text.split("\n\n")
passports = map(str.strip, passports)
passports = list(passports)


def structify(passport):
    ms = re.findall(r"(\w{3}):[^\s\n]+", passport)
    return ms


passports = map(structify, passports)
passports = list(passports)

fields = sorted(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])


def check(passport):
    if "cid" in passport:
        passport.remove("cid")
    passport.sort()
    return int(passport == fields)


passports = map(check, passports)
passports = list(passports)

print(sum(passports))
