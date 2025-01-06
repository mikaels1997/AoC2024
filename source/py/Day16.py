import heapq
from itertools import count

G = {complex(r_i, c_i): c 
       for r_i, r in enumerate(open("data/input16.txt").readlines()) 
       for c_i, c in enumerate(r) if c != "#"}
ns, ct = [-1, 1j, 1, -1j], count()
st = [x for x in G if G[x] == "S"][0]

paths = [(0, next(ct), [st - 1j, st])]
node_costs = {c: {n: float('inf') for n in ns} for c in G}
lowest, p2 = float('inf'), set()

while len(paths) > 0:
    c, _, p = heapq.heappop(paths)
    for n in ns:
        ne = p[-1] + n
        new_c = c + 1 + 1000 * (p[-1] - p[-2] != n)
        if ne in G and new_c <= node_costs[ne][n]:
            node_costs[ne][n] = new_c
            if G[ne] == "E":
                lowest = min(new_c, lowest)
                if new_c <= lowest:
                    p2.update(p + [ne])
            elif new_c <= lowest:
                heapq.heappush(paths, (new_c, next(ct), p + [ne]))
            
print(lowest, len(p2) - 1)