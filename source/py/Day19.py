avail, seqs = [*open("data/input19.txt").read().split("\n\n")]

poss, total = 0, 0
avail = [*map(str.strip, avail.split(','))]
for seq in seqs.split():
    d = {seq[:i]: 0 for i in range(1, len(seq)+1)}
    for i in range(len(seq)):
        for a in avail:
            if not seq[i:].startswith(a): continue
            d[seq[:i]+a] += d[seq[:i]] if i > 0 else 1
    poss += 1 if d[seq] > 0 else 0
    total += d[seq]

print(poss, total)