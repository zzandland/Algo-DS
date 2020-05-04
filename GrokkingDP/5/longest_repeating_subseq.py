#  Problem Statement #
#  Given a sequence, find the length of its longest repeating subsequence (LRS). A repeating subsequence will be the one that appears at least twice in the original sequence and is not overlapping (i.e. none of the corresponding characters in the repeating subsequences have the same index).

#  Example 1:

#  Input: “t o m o r r o w”
#  Output: 2
#  Explanation: The longest repeating subsequence is “or” {tomorrow}.

#  Example 2:

#  Input: “a a b d b c e c”
#  Output: 3
#  Explanation: The longest repeating subsequence is “a b c” {a a b d b c e c}.

#  Example 3:

#  Input: “f m f f”
#  Output: 2
#  Explanation: The longest repeating subsequence is “f f” {f m f f, f m f f}. Please note the second last character is shared in LRS.
s1, s2, s3 = 'tomorrow', 'aabdbcec', 'fmff'

def td(s: str) -> int:
    """
    >>> td(s1)
    2
    >>> td(s2)
    3
    >>> td(s3)
    2
    """
    S = len(s)
    dp = [[None for _ in range(S)] for _ in range(S)]
    def fn(i: int, j: int) -> int:
        if i == S or j == S: return 0
        if dp[i][j] == None:
            if i != j and s[i] == s[j]: dp[i][j] = 1 + fn(i+1, j+1)
            else: dp[i][j] = max(fn(i+1, j), fn(i, j+1))
        return dp[i][j]
    return fn(0, 0)

def bu(s: str) -> int:
    """
    >>> bu(s1)
    2
    >>> bu(s2)
    3
    >>> bu(s3)
    2
    """
    S = len(s)
    dp = [0] * S
    for i in range(1, S):
        for j in range(i):
            dp[i] = max(dp[i], dp[j])
            if s[i] == s[j]: dp[i] += 1
    return dp[-1]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
