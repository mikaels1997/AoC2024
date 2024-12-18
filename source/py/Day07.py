from itertools import product

def solve(path, ops):
    data = {int(l.split(": ")[0]): l.split(": ")[1].split() 
            for l in open(path).read().splitlines()}
    sol = 0
    for goal, nums in data.items():
        seqs = [*product(ops, repeat=len(nums)-1)]
        for seq in seqs:
            res = int(nums[0])
            for n_i, o in enumerate(seq):
                if o == "+":
                    res += int(nums[n_i+1])
                elif o == "*":
                    res *= int(nums[n_i+1])
                elif o == "||":
                    res = int(str(res) + nums[n_i+1])
            if res == goal:
                sol += res
                break
    return sol

    
print(solve("data/input07.txt", ["+", "*"]))
print(solve("data/input07.txt", ["+", "*", "||"]))