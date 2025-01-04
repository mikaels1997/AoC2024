dirs = {"<": -1j, "^": -1, ">": 1j, "v": 1}
p2_map = {"#": "##", "O": "[]", ".": "..", "@": "@."}

class Tile:
    def __init__(s, v, c): s.v = v; s.c = complex(c[0], c[1])
    def move(s, d, g):
        to_move = s.check(d, g, set())
        if all(to_move):
            for t in to_move: t.c += d
    def check(s, d, g, to_move):
        nxt = next((x for x in G if x.c == s.c + d), None)
        to_move.add(s if (not nxt or nxt.v != "#") else 0)
        if nxt and nxt.v in "O[]":
            nxt.check(d, g, to_move)
        if nxt and nxt.v in "[]" and d.real:
            b_dir = -1j if nxt.v == "]" else 1j
            other = next(x for x in G if x.c == s.c + d + b_dir)
            other.check(d, g, to_move)
        return to_move
    def val(s): 
        return int(s.v in "O[") * (100 * s.c.real + s.c.imag) 

l1, l2 = open("data/input15.txt").read().split("\n\n")
ds = [dirs[d] for d in "".join(l2.split("\n"))]

for p in [0, 1]:
    line = lambda x: x if not p else x.translate(x.maketrans(p2_map))
    G = [Tile(v, [i, j])
            for i, r in enumerate(l1.split("\n")) 
                for j, v in enumerate(line(r)) if v in "@#O[]"]
    r = next(x for x in G if x.v == "@")
    for d in ds: r.move(d, G)
    print(int(sum([g.val() for g in G])))