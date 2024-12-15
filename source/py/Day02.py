import numpy as np

def solve(path, second_part = False):
    data = [*map(str.split, open(path).readlines())]
    nums = [[*map(int, d)] for d in data]
    diffs = lambda x: [np.array(n) - np.array([*n[1:], n[-1]]) for n in x]
    valid_count = lambda x: sum([max(abs(d)) <=3 and (np.all(d[:-1]>0) or np.all(d[:-1]<0)) for d in x])
    if not second_part:
        return valid_count(diffs(nums))
    return sum([valid_count(diffs([d[:i] + d[i+1:] for i in range(len(d))])) > 0 for d in nums])

print("Part 1 solution: ", solve("data/input02.txt", False))
print("Part 2 solution: ", solve("data/input02.txt", True))