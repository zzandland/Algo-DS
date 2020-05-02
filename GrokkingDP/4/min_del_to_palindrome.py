#  Problem Statement #
#  Given a string, find the minimum number of characters that we can remove to make it a palindrome.

#  Example 1:

#  Input: "abdbca"
#  Output: 1
#  Explanation: By removing "c", we get a palindrome "abdba".

#  Example 2:

#  Input: = "cddpd"
#  Output: 2
#  Explanation: Deleting "cp", we get a palindrome "ddd".

#  Example 3:

#  Input: = "pqr"
#  Output: 2
#  Explanation: We have to remove any two characters to get a palindrome, e.g. if we
#  remove "pq", we get palindrome "r".

def bu(s: str) -> int:
    """
    >>> bu('abdbca')
    1
    >>> bu('cddpd')
    2
    >>> bu('pqr')
    2
    """
    S, mx = len(s), 1
    dp = [[1 if r == c else 0 for c in range(S)] for r in range(S)]
    for i in range(S-1, -1, -1):
        for j in range(i+1, S):
            if s[i] == s[j]: dp[i][j] = dp[i+1][j-1] + 2
            else: dp[i][j] = max(dp[i+1][j], dp[i][j-1])
            mx = max(mx, dp[i][j])
    return S - mx

if __name__ == '__main__':
    import doctest
    doctest.testmod()
