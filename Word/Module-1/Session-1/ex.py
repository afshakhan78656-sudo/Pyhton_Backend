def num():
    nums=[2,7,11,15]
    target=9

    for i in range(len(nums)):
        if nums[i]==target:
            return nums[0]+nums[1]

        else:
            return "not in target"

    return target

print(num())        