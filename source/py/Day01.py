import numpy as np

def solve(path, second_part = False):
    data = [*map(str.split, open(path).readlines())]
    left = np.array(sorted([int(d[0]) for d in data]))
    right = np.array(sorted([int(d[1]) for d in data]))
    return sum(abs(left - right)) if not second_part else sum([n * sum(right == n) for n in left])
    
print("Part 1 solution: ", solve("data/input01.txt", False))
print("Part 2 solution: ", solve("data/input01.txt", True))