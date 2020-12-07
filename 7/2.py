import re

lines = open("input.txt").readlines()
rules = map(lambda line: re.match(r"^(.+)\s+bags\s+contain\s+(?:(\d+.+bags?)|no\s*other\s*bags)\.$", line), lines)
rules = list(rules)

assert len(list(filter(lambda rule: rule is None, rules))) == 0


def split_content(content):
    if content is None:
        return []

    content = content.split(",")
    content = map(str.strip, content)
    content = map(lambda bag: re.match(r"^(\d+)\s+(.*)\s+bags?$", bag), content)

    return [{
        "count": int(bag.group(1)),
        "color": bag.group(2),
    } for bag in content]


def structify_rule(rule):
    return {
        "color": rule.group(1),
        "content": split_content(rule.group(2))
    }


rules = map(structify_rule, rules)
rules = list(rules)

rules = {rule["color"]: {bag["color"]: bag["count"] for bag in rule["content"]} for rule in rules}



def content_size(color):
    total = 0
    for color, count in rules[color].items():
        total += count * (content_size(color) + 1)
    return total


print(content_size("shiny gold"))
