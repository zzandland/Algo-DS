#  Problem Statement #
#  Given a string, find the total number of palindromic substrings in it. Please note we need to find the total number of substrings and not subsequences.

#  Example 1:

#  Input: "abdbca"
#  Output: 7
#  Explanation: Here are the palindromic substrings, "a", "b", "d", "b", "c", "a", "bdb".

#  Example 2:

#  Input: = "cddpd"
#  Output: 7
#  Explanation: Here are the palindromic substrings, "c", "d", "d", "p", "d", "dd", "dpd".

#  Example 3:

#  Input: = "pqr"
#  Output: 3
#  Explanation: Here are the palindromic substrings,"p", "q", "r".

def bu(s: str) -> int:
    """
    >>> bu('abdbca')
    7
    >>> bu('cddpd')
    7
    >>> bu('pqr')
    3
    """
    S = cnt = len(s)
    dp = [[True if r == c else False for c in range(S)] for r in range(S)]
    for i in range(S-1, -1, -1):
        for j in range(i+1, S):
            if s[i] == s[j] and (j-i == 1 or dp[i+1][j-1]):
                dp[i][j] = True
                cnt += 1
    return cnt

if __name__ == '__main__':
    import doctest
    doctest.testmod()
