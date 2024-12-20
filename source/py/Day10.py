def solve(path):
    G = {complex(i, j): int(v) 
         for i, r in enumerate(open(path).readlines()) 
            for j, v in enumerate(r[:-1])}
    res = sum([(dfs(G, s, set(), []))
         for s in [n[0] for n in G.items() if n[1] == 0]])
    return int(res.real), int(res.imag)

def dfs(G, v, vis, f):
    vis.add(v)
    for n in [v-e for e in [1, 1j, -1, -1j]]:
        if n in set(G) - vis and G[n] - G[v] == 1: 
            if G[n] == 9: f.append(n)
            dfs(G, n, vis.copy(), f)
    return complex(len(set(f)), len(f))

print(solve("data/input10.txt"))