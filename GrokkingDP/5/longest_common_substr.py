#  Problem Statement #
#  Given two strings ‘s1’ and ‘s2’, find the length of the longest substring which is common in both the strings.

#  Example 1:

#  Input: s1 = "abdca"
#  s2 = "cbda"
#  Output: 2
#  Explanation: The longest common substring is "bd".

#  Example 2:

#  Input: s1 = "passport"
#  s2 = "ppsspt"
#  Output: 3
#  Explanation: The longest common substring is "ssp".

def td(s1: str, s2: str) -> int:
    """
    >>> td('abdca', 'cbda')
    2
    >>> td('passport', 'ppsspt')
    3
    """
    A, B = len(s1), len(s2)
    dp = {}
    def fn(i: int, j: int, l: int) -> int:
        if i == A or j == B: return l
        key = '{}:{}:{}'.format(i, j, l)
        if key not in dp:
            if s1[i] == s2[j]: l = dp[key] = fn(i+1, j+1, l+1)
            dp[key] = max(l, max(fn(i+1, j, 0), fn(i, j+1, 0)))
        return dp[key]
    return fn(0, 0, 0)

def bu(s1: str, s2: str) -> int:
    """
    >>> bu('abdca', 'cbda')
    2
    >>> bu('passport', 'ppsspt')
    3
    """
    A, B, mx = len(s1), len(s2), 0
    if B > A: A, B = B, A
    dp = [0] * (B+1)
    for i in range(A):
        for j in range(B, 0, -1):
            if s1[i] == s2[j-1]: dp[j] = 1+dp[j-1]
            else: dp[j] = 0
            mx = max(mx, dp[j])
    return mx

if __name__ == '__main__':
    import doctest
    doctest.testmod()
