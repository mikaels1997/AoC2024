import re
from math import prod

rs = list(map(re.compile(r'-?\d+').findall, 
                open("data/input14.txt").readlines()))
res, w, h = [0, 0, 0, 0], 101, 103

for i in range(int(1e6)):
    cnts = {c: 0 for c in range(w+h)}
    for r in rs:
        x, y, v1, v2 = map(int, r)
        x, y = (x + v1 * i) % w, (y + v2 * i) % h
        if i == 100 and x != w // 2 and y != h // 2:
            res[2* (y > (h//2)) + (x > (w//2))] += 1
        cnts[x] += 1; cnts[w+y] += 1
    if sum([v >= 30 for v in cnts.values()]) >= 4:
        print([prod(res), i])
        break