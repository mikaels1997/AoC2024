import itertools

def solve(path):
    grid = {complex(r_i, c_i): c 
            for r_i, r in enumerate(open(path).read().splitlines()) 
            for c_i, c in enumerate(r)}
    an, found = set([x[0] for x in grid.items() if x[1] != "."]), set()
    for a in set(grid.values()) - set("."):
        cs = [c[0] for c in grid.items() if c[1] == a]
        for p in list(itertools.combinations(cs, 2)):      
            diff = p[0] - p[1]
            while p[0] + diff in grid.keys() or p[1] - diff in grid.keys():
                found |= set([p[0] + diff, p[1] - diff])
                diff += p[0] - p[1]
    return [len((x).intersection(grid.keys())) for x in [found, found | an]]

print(solve("data/input08.txt"))