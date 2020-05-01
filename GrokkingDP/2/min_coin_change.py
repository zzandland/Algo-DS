#  Introduction #
#  Given an infinite supply of ‘n’ coin denominations and a total money amount, we are asked to find the minimum number of coins needed to make up that amount.

#  Example 1:

#  Denominations: {1,2,3}
#  Total amount: 5
#  Output: 2
#  Explanation: We need minimum of two coins {2,3} to make a total of '5'

#  Example 2:

#  Denominations: {1,2,3}
#  Total amount: 11
#  Output: 4
#  Explanation: We need minimum four coins {2,3,3,3} to make a total of '11'

#  Problem Statement #
#  Given a number array to represent different coin denominations and a total amount ‘T’, we need to find the minimum number of coins needed to make change for ‘T’. We can assume an infinite supply of coins, therefore, each coin can be chosen multiple times.
from typing import List

def bu(denoms: List[int], T: int) -> int:
    """
    >>> bu([1,2,3], 5)
    2
    >>> bu([1,2,3], 11)
    4
    """
    dp = [0] + [float('inf')]*T
    for denom in denoms:
        for i in range(denom, T+1):
            dp[i] = min(dp[i], dp[i-denom]+1)
    return dp[-1]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
