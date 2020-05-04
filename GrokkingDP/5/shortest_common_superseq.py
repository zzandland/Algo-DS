#  Problem Statement #
#  Given two sequences ‘s1’ and ‘s2’, write a method to find the length of the shortest sequence which has ‘s1’ and ‘s2’ as subsequences.

#  Example 1:

#  Input: s1: "abcf" s2:"bdcf"
#  Output: 5
#  Explanation: The shortest common super-sequence (SCS) is "abdcf".
#  Example 2:

#  Input: s1: "dynamic" s2:"programming"
#  Output: 15
#  Explanation: The SCS is "dynprogrammicng".

def bu(s1: str, s2: str) -> int:
    """
    >>> bu('abcf', 'bdcf')
    5
    >>> bu('dynamic', 'programming')
    15
    """
    A, B = len(s1), len(s2)
    if B > A:
        A, B = B, A
        s1, s2 = s2, s1
    dp = [[0 for _ in range(B)] for _ in range(2)]
    for i in range(A):
        for j in range(B):
            if s1[i] == s2[j]: dp[1][j] = dp[0][j-1] + 1
            else: dp[1][j] = max(dp[0][j], dp[1][j-1])
        dp[0] = dp[1][:]
    return A + B - dp[1][-1]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
