#  Given a list of positive integers nums and an int target, return indices of the two numbers such that they add up to a target - 30.

#  Conditions:

#  You will pick exactly 2 numbers.
#  You cannot pick the same element twice.
#  If you have muliple pairs, select the pair with the largest number.

def pair_sum(nums, target):
    '''
    >>> pair_sum([1, 10, 25, 35, 60], 90)
    [2, 3]
    >>> pair_sum([20, 50, 40, 25, 30, 10], 90)
    [1, 5]
    '''
    seen = {}
    res = []

    # iterate the nums and update repetitively as soon as target - 30 is found O(n)
    for i, n in enumerate(nums):
        rest = target - 30 - n
        if rest in seen: res = [seen[rest], i]
        seen[n] = i

    return res

if __name__ == '__main__':
    import doctest
    doctest.testmod()
