#  Problem Statement #
#  Given a sequence, find the length of its Longest Palindromic Subsequence (LPS). In a palindromic subsequence, elements read the same backward and forward.

#  A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

#  Example 1:

#  Input: "abdbca"
#  Output: 5
#  Explanation: LPS is "abdba".

#  Example 2:

#  Input: = "cddpd"
#  Output: 3
#  Explanation: LPS is "ddd".
#  Example 3:

#  Input: = "pqr"
#  Output: 1
#  Explanation: LPS could be "p", "q" or "r".

def td(s: str) -> int:
    """
    >>> td('abdbca')
    5
    >>> td('cddpd')
    3
    >>> td('pqr')
    1
    """
    S = len(s)
    dp = [[None for _ in range(S)] for _ in range(S)]
    def fn(l: int, r: int) -> int:
        if l == r: return 1
        if l > r: return 0
        if dp[l][r] == None:
            if s[l] == s[r]: dp[l][r] = 2 + fn(l+1, r-1)
            else: dp[l][r] = max(fn(l+1, r), fn(l, r-1))
        return dp[l][r]
    return fn(0, S-1)

def bu(s: str) -> int:
    """
    >>> bu('abdbca')
    5
    >>> bu('cddpd')
    3
    >>> bu('pqr')
    1
    """
    S, mx = len(s), 0
    dp = [[1 if c == r else 0 for c in range(S)] for r in range(S)]
    for i in range(S-1, -1, -1):
        for j in range(i+1, S):
            if s[i] == s[j]: dp[i][j] = dp[i+1][j-1] + 2
            else: dp[i][j] = max(dp[i+1][j], dp[i][j-1])
            mx = max(mx, dp[i][j])
    return mx

if __name__ == '__main__':
    import doctest
    doctest.testmod()
