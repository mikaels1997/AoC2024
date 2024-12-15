import re

def solve(path, second_part = False):
    matches = re.findall(r"(do)\(\)|(don't)\(\)|mul\((\d+),(\d+)\)", open(path).read())
    enabled = True
    res = 0
    for d, dnt, x, y in matches:
        changed = (d != "" or dnt != "")
        enabled = d != "" if changed and second_part else enabled
        res += int(x) * int(y) if enabled and not changed else 0
    return res
 
print("Part 1 solution: ", solve("data/input03.txt", False))
print("Part 2 solution: ", solve("data/input03.txt", True))