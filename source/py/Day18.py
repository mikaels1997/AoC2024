bytes = [complex(*map(int, l.split(","))) 
     for l in open("data/input18.txt").read().split()]
grid = [complex(x, y) for y in range(71) for x in range(71)]
s, g = grid[0], grid[-1]

def bfs(G, root, goal):
    Q, vis, p = [root], [root], {}
    while len(Q) > 0:
        v = Q.pop(0)
        if v == goal:
            node, d = p[goal], 1
            while node != root:
                node = p[node]
                d += 1 
            return d
        for n in [1, 1j, -1, -1j]:
            ne = v + n
            if ne not in vis + G and ne in grid:
                p[ne] = v
                vis.append(ne)
                Q.append(ne)

a, t, expl = len(bytes) // 2, len(bytes) // 4, []
while a not in expl:
    expl.append(a)
    a += t if bool(bfs(bytes[0:a], s, g)) else -t
    if t != 1: t //= 2

print(bfs(bytes[0: 1024], s, g))
print(f'{str(int(bytes[a].real))},{str(int(bytes[a].imag))}')