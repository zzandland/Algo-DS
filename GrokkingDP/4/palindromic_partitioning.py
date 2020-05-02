#  Problem Statement #
#  Given a string, we want to cut it into pieces such that each piece is a palindrome. Write a function to return the minimum number of cuts needed.

#  Example 1:

#  Input: "abdbca"
#  Output: 3
#  Explanation: Palindrome pieces are "a", "bdb", "c", "a".

#  Example 2:

#  Input: = "cddpd"
#  Output: 2
#  Explanation: Palindrome pieces are "c", "d", "dpd".

#  Example 3:

#  Input: = "pqr"
#  Output: 2
#  Explanation: Palindrome pieces are "p", "q", "r".

#  Example 4:

#  Input: = "pp"
#  Output: 0
#  Explanation: We do not need to cut, as "pp" is a palindrome.

def td(s: str) -> int:
    """
    >>> td('abdbca')
    3
    >>> td('cddpd')
    2
    >>> td('pqr')
    2
    >>> td('pp')
    0
    """
    S = len(s)
    dp = [[None for _ in range(S)] for _ in range(S)]
    def fn(l: int, r: int) -> int:
        if l >= r: return 0
        if s[l] == s[r] and fn(l+1, r-1) == 0: return 0
        if dp[l][r] == None: dp[l][r] = 1 + min(fn(l+1, r), fn(l, r-1))
        return dp[l][r]
    return fn(0, S-1)

def bu(s: str) -> int:
    """
    >>> bu('abdbca')
    3
    >>> bu('cddpd')
    2
    >>> bu('pqr')
    2
    >>> bu('pp')
    0
    """
    S = len(s)
    dp = [[0 for _ in range(S)] for _ in range(S)]
    for i in range(S-1, -1, -1):
        for j in range(i+1, S):
            if s[i] == s[j] and dp[i+1][j-1] == 0: dp[i][j] = 0
            else: dp[i][j] = 1 + min(dp[i+1][j], dp[i][j-1])
    return dp[0][-1]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
