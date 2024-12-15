order_dic = {}

def solve(path, second_part = False):
    data = open(path).read().splitlines()
    result = 0
    for d in data:
        nums = d.split("|")
        if len(nums) > 1:
            if int(nums[0]) in order_dic:
                order_dic[int(nums[0])].append(int(nums[1]))
            else:
                order_dic[int(nums[0])] = [int(nums[1])]
            continue
        nums = [*map(int, d.split(","))] if d != "" else []
        if check_validity(nums, second_part):
            result += int(nums[len(nums) // 2]) if not second_part else 0
            continue
        while second_part and nums != []:
            if check_validity(nums, second_part):
                result += int(nums[len(nums) // 2])
                break
    return result

def check_validity(nums, correction=False):
    for i in range(len(nums)-1):
        if nums[i] in order_dic and nums[i+1] not in order_dic[nums[i]]:
            if correction:
                nums[i], nums[i+1] = nums[i+1], nums[i]
            return False
        if nums[i] not in order_dic and len(set(nums[i+1:])) > 0:
            if correction:
                nums[i], nums[i+1] = nums[i+1], nums[i]
            return False
        elif i == len(nums) - 2:
            continue
    return nums != []

print("Part 1 solution: ", solve("data/input05.txt", False))
print("Part 2 solution: ", solve("data/input05.txt", True))