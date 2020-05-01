#  Problem Statement #
#  Given an array of positive numbers, where each element represents the max number of jumps that can be made forward from that element, write a program to find the minimum number of jumps needed to reach the end of the array (starting from the first element). If an element is 0, then we cannot move through that element.

#  Example 1:

#  Input = {2,1,1,1,4}
#  Output = 3
#  Explanation: Starting from index '0', we can reach the last index through: 0->2->3->4
#  Example 2:

#  Input = {1,1,3,6,9,3,0,1,3}
#  Output = 4
#  Explanation: Starting from index '0', we can reach the last index through: 0->1->2->3->8

from typing import List

def bu(nums: List[int]) -> int:
    """
    >>> bu([2,1,1,1,4])
    3
    >>> bu([1,1,3,6,9,3,0,1,3])
    4
    """
    N = len(nums)
    dp = [0] + [float('inf')]*(N-1)
    for i in range(N):
        for j in range(1, nums[i]+1):
            nxt = j+i
            if nxt >= N: break
            dp[nxt] = min(dp[nxt], dp[i]+1)
    return dp[-1]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
