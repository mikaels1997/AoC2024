vecs = [(0, 1), (1, 1), (1,0), (1, -1), (0, -1), (-1,-1), (-1,0), (-1, 1)]

def solve(path, second_part = False):
    mat = open(path).read().splitlines() 
    total = 0
    for r_i, r in enumerate(mat):
        for c_i, c in enumerate(r):
            if c != "X" and not second_part or c != "A" and second_part:
                continue
            ws = []
            for v in vecs:
                w_length = 2 if second_part else 4
                found = [""] * w_length
                for i in range(w_length):
                    if 0 <= r_i + v[0] * i < len(mat) and 0 <= c_i + v[1] * i < len(r):
                        found[i] = mat[r_i + v[0] * i][c_i + v[1] * i]
                ws.append(found)
                total += 1 if found == ["X", "M", "A", "S"] and not second_part else 0
            if second_part and ws[1][1] + ws[3][1] + ws[5][1] + ws[7][1] in ("SSMM", "MSSM", "SMMS", "MMSS"):
                total += 1
    return total

print("Part 1 solution: ", solve("data/input04.txt", False))
print("Part 2 solution: ", solve("data/input04.txt", True))