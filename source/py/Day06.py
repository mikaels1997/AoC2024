def solve(path):
    data = open(path).read().splitlines()
    start = [complex(x, y) for x, li in enumerate(data) 
             for y, val in enumerate(li) if val=="^"]
    return move(start[0], -1, data)

def move(coord, vec, grid,):
    vis = {k: set() for k in (1, -1, 1j, -1j)}
    asd, obs = project(coord, vec, grid, vis, 0, -1, set())
    return len(set().union(*asd.values())) + 1, len(obs)

def project(coord, dir, grid, vis, d, o, obs):
    start = coord
    is_in = lambda c: (0 <= c.real < len(grid) and 0 <= c.imag < len(grid[0]))
    while is_in(coord + dir):
        if coord in vis[dir]:
            obs.add(o)
            return
        vis[dir].add(coord)
        ne = grid[int(coord.real + dir.real)][int(coord.imag + dir.imag)]
        while ne == "#"  or (coord + dir == o):
            dir *= -1j
            vis[dir].add(coord)
            ne = grid[int(coord.real + dir.real)][int(coord.imag + dir.imag)]
        coord += dir
        if d == 0:
            project(start, -1, grid, {k: set() for k in (1, -1, 1j, -1j)}, d+1, coord, obs)
    return vis, obs
    
print(solve("data/input06.txt"))