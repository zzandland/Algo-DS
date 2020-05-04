#  Problem Statement #
#  Given a number sequence, find the minimum number of elements that should be deleted to make the remaining sequence sorted.

#  Example 1:

#  Input: {4,2,3,6,10,1,12}
#  Output: 2
#  Explanation: We need to delete {4,1} to make the remaing sequence sorted {2,3,6,10,12}.

#  Example 2:

#  Input: {-4,10,3,7,15}
#  Output: 1
#  Explanation: We need to delete {10} to make the remaing sequence sorted {-4,3,7,15}.

#  Example 3:

#  Input: {3,2,1,0}
#  Output: 3
#  Explanation: Since the elements are in reverse order, we have to delete all except one to get a
#  sorted sequence. Sorted sequences are {3}, {2}, {1}, and {0}

from typing import List

def bu(nums: List[int]) -> int:
    """
    >>> bu([4,2,3,6,10,1,12])
    2
    >>> bu([-4,10,3,7,15])
    1
    >>> bu([3,2,1,0])
    3
    """
    N, mx = len(nums), 1
    dp = [1] * N
    for i in range(1, N):
        for j in range(i):
            if nums[i] > nums[j] and dp[i] <= dp[j]: dp[i] += 1
        mx = max(mx, dp[i])
    return N-mx

if __name__ == '__main__':
    import doctest
    doctest.testmod()
