#  Problem Statement #
#  Given a string, find the length of its Longest Palindromic Substring (LPS). In a palindromic string, elements read the same backward and forward.

#  Example 1:

#  Input: "abdbca"
#  Output: 3
#  Explanation: LPS is "bdb".

#  Example 2:

#  Input: = "cddpd"
#  Output: 3
#  Explanation: LPS is "dpd".

#  Example 3:

#  Input: = "pqr"
#  Output: 1
#  Explanation: LPS could be "p", "q" or "r".

def bu(s: str) -> int:
    """
    >>> bu('abdbca')
    3
    >>> bu('cddpd')
    3
    >>> bu('pqr')
    1
    """
    S, mx = len(s), 1
    dp = [[True if r == c else False for c in range(S)] for r in range(S)]
    for i in range(S-1, -1, -1):
        for j in range(i+1, S):
            if s[i] == s[j] and dp[i+1][j-1]:
                dp[i][j] = True
                mx = max(mx, j-i+1)
    return mx

if __name__ == '__main__':
    import doctest
    doctest.testmod()
