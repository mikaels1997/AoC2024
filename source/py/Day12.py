def solve(path):
    dic = {}
    for r_i, r in enumerate(open(path).read().splitlines()):
        for c_i, c in enumerate(r):
            if c not in dic: dic[c] = [complex(r_i, c_i)]
            else: dic[c].append(complex(r_i, c_i))
    ans = sum([sym_val(dic[v]) for v in dic.keys()])
    return int(ans.real), int(ans.imag)

def sym_val(crds):
    res = 0 + 0j
    while len(crds) > 0:
        vis, p1, p2 = bfs(crds, crds[0])
        res += complex(len(vis) * p1, len(vis) * p2)
        crds = [c for c in crds if c not in vis]
    return res

def bfs(G, root):
    expl, Q = [root], [root]
    sides = {n: [] for n in [1, -1, 1j, -1j]}
    while len(Q) > 0:
        v = Q.pop(0)
        for n in sides.keys():
            ne = v + n
            if ne not in expl and ne in G:
                expl.append(ne) 
                Q.append(ne)
            elif ne not in G:
                sides[n].append(ne)
    sds = sum(ss - (1j if s.real else 1) not in v 
        for s, v in sides.items() for ss in v)
    return expl, sum([len(s) for s in sides.values()]), sds

print(solve("data/input12.txt"))