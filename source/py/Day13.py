import re
import sympy as sp

def solve(path, a):
    res, x, y = 0, *sp.symbols('x y')
    for eq in list(map(re.compile(r'\d+').findall, 
                   open(path).read().split("\n\n"))):
        a1, a2, b1, b2, c1, c2 = map(int, eq)
        e1, e2 = sp.Eq(a1*x + b1*y, c1+a), sp.Eq(a2*x + b2*y, c2+a)
        sol = sp.solve([e1, e2], [x, y])
        found = int(sol[x].is_Integer and sol[y].is_Integer)
        res += found * (sol[x] * 3 + sol[y])
    return res

print([solve("data/input13.txt", i) for i in [0, int(1e13)]])