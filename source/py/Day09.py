class Mem:
    def __init__(s, id, pos, len): s.id = id; s.pos = pos; s.len = len
    def val(s): return sum([s.id*i for i in range(s.pos, s.pos+s.len)])

def solve(path, sec):
    data = [*map(int, open(path).read().strip())]
    mems, pos = [], 0
    for i in range(len(data)):
        if i % 2 == 0 and not sec:
            mems.extend([Mem(i//2, pos+j, 1) for j in range(data[i])])
        elif i % 2 == 0 and sec: mems.append(Mem(i//2, pos, data[i]))
        pos += data[i]
    for to_move in reversed(mems[:]):
        for i in range(len(mems)-1):
            if mems[i].pos < to_move.pos and mems[i+1].pos - (mems[i].pos + mems[i].len) >= to_move.len:
                to_move.pos = mems[i].pos + mems[i].len
                mems.remove(to_move)
                mems.insert(i+1, to_move)
                break
    return sum([x.val() for x in mems])

print(solve("data/input09.txt", False))
print(solve("data/input09.txt", True))
