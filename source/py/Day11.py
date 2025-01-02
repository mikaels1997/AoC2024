from functools import cache

@cache
def blink(val, d, sec):
    if d == 25 if not sec else d == 75: return 1
    if len(str(val)) % 2 == 0:
        exp = 10 ** (len(str(val)) // 2)
        return blink(val//exp, d+1, sec) + blink(val%exp, d+1, sec)
    else:
        return blink((2024*val if val != 0 else 1), d+1, sec)

vals = [*map(int, open("data/input11.txt").read().split())]
print(((sum(blink(x, 0, False) for x in vals)), (sum(blink(x, 0, True) for x in vals))))