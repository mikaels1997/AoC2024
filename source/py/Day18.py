s, bytes = 71, [tuple(map(int, l.split(",")))
     for l in open("data/input18.txt").read().split()]

def bfs(lim):
    Q, p, vis = [(0, 0)], {}, set([(0, 0)] + bytes[0:lim])
    while len(Q) > 0:
        v = Q.pop(0)
        if v == (s, s):
            n, d = p[(s, s)], 1
            while n != (0, 0): n, d = p[n], d+1 
            return d
        for n in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
            ne = (v[0] + n[0], v[1] + n[1])
            if ne not in vis and all(0 <= c <= s for c in ne):
                p[ne] = v
                vis.add(ne); Q.append(ne)

a, t, vis = len(bytes) // 2, len(bytes) // 4, []
while a not in vis:
    vis.append(a)
    a += t if bool(bfs(a)) else -t
    if t != 1: t //= 2

print(bfs(1024), ','.join(map(str, bytes[a])))