import re
from collections import Counter
from math import prod

def solve(path, w, h):
    rs = list(map(re.compile(r'-?\d+').findall, 
                   open(path).read().splitlines()))
    res = [0, 0, 0, 0]
    for i in range(int(1e6)):
        cs = []
        for r in rs:
            x, y, v1, v2 = map(int, r)
            x = (x + v1 * i) % w
            y = (y + v2 * i) % h
            if i == 100 and x != w // 2 and y != h // 2:
                res[2* (y > (h//2)) + (x > (w//2))] += 1
            cs.append((x, y))
        cnt = [Counter([c[i] for c in cs]) for i in [0,1]]
        if sum([co >= 30 for co in cnt[0].values()]) >= 2:
            if sum([co >= 30 for co in cnt[1].values()]) >= 2:
                return [prod(res), i]

print(solve("data/input14.txt", 101, 103))