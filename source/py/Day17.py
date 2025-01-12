import re

reg, insts = list(map(re.compile(r'-?\d+').findall, 
                open("data/input17.txt").read().split("\n\n")))
reg, insts = list(map(int, reg)), list(map(int, insts))
cmbs = lambda x, r: x if 0 <= x <= 3 else r[x-4]

def process(r, trgs, a, sec):
    head, output = 0, ""
    while head < len(insts):
        i, op = insts[head], cmbs(insts[head+1], r)
        match i:
            case 0: r[0] = r[0] // 2**op
            case 1: r[1] = r[1] ^ insts[head+1]
            case 2: r[1] = op % 8
            case 3:
                if sec: break
                head = len(insts) if r[0] == 0 else insts[head+1] - 2
            case 4: r[1] = r[1] ^ r[2]
            case 5:
                if op % 8 == trgs[0] and sec:
                    if len(trgs) == 1: return a
                    for n in range(8):
                        f = process([a*8+n, *r[1:]], trgs[1:], a*8+n, sec)
                        if f: return f
                output = "".join(output + str(op % 8))
            case 6: r[1] = r[0] // 2**op
            case 7: r[2] = r[0] // 2**op
        head += 2
    if not sec: print(",".join(map(str, output)))
    return 0

process(reg, insts, 0, False)

targets = list(reversed(insts))
print(sum(process([nn, 0, 0], targets, nn, True) for nn in range(8)))