#  Given a list of positive integers nums and an int target, return indices of the two numbers such that they add up to a target - 30.

#  Conditions:

#  You will pick exactly 2 numbers.
#  You cannot pick the same element twice.
#  If you have muliple pairs, select the pair with the largest number.

def pair_sum(nums, target):
    dc, max_, pair = {}, float('-inf'), []
    for i, num in enumerate(nums):
        rem = target-num-30
        print(i, num, rem, dc)
        if rem in dc and (num > max_ or rem > max_):
            pair = [dc[rem], i]
            max_ = max(num, rem)
        dc[num] = i
    return pair

nums = [20, 50, 40, 25, 30, 10]
target = 90
print(pair_sum(nums, target))
