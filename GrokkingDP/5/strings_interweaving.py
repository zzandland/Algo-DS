#  Problem Statement #
#  Give three strings ‘m’, ‘n’, and ‘p’, write a method to find out if ‘p’ has been formed by interleaving ‘m’ and ‘n’. ‘p’ would be considered interleaving ‘m’ and ‘n’ if it contains all the letters from ‘m’ and ‘n’ and the order of letters is preserved too.

#  Example 1:

#  Input: m="abd", n="cef", p="abcdef"
#  Output: true
#  Explanation: 'p' contains all the letters from 'm' and 'n' and preserves their order too.

#  Example 2:

#  Input: m="abd", n="cef", p="adcbef"
#  Output: false
#  Explanation: 'p' contains all the letters from 'm' and 'n' but does not preserve the order.

#  Example 3:

#  Input: m="abc", n="def", p="abdccf"
#  Output: false
#  Explanation: 'p' does not contain all the letters from 'm' and 'n'.

#  Example 4:

#  Input: m="abcdef", n="mnop", p="mnaobcdepf"
#  Output: true
#  Explanation: 'p' contains all the letters from 'm' and 'n' and preserves their order too.

t1 = ['abd', 'cef', 'abcdef']
t2 = ['abd', 'cef', 'abcbef']
t3 = ['abc', 'def', 'abdccf']
t4 = ['abcdef', 'mnop', 'mnaobcdepf']

def td(m: str, n: str, p: str) -> bool:
    """
    >>> td(*t1)
    True
    >>> td(*t2)
    False
    >>> td(*t3)
    False
    >>> td(*t4)
    True
    """
    M, N, P = len(m), len(n), len(p)
    dp = [[[None] * P for _1 in range(N)] for _2 in range(M)]
    def fn(i: int, j: int, k: int) -> bool:
        if i == M and j == N and k == P: return True
        if p == P: return False
        if i == M: return n[j:] == p[k:]
        if j == N: return m[i:] == p[k:]
        if dp[i][j][k] is None:
            a = fn(i+1, j, k+1) if p[k] == m[i] else False
            b = fn(i, j+1, k+1) if p[k] == n[j] else False
            dp[i][j][k] = a or b
        return dp[i][j][k]
    return fn(0, 0, 0)

def bu(m: str, n: str, p: str) -> bool:
    """
    >>> bu(*t1)
    True
    >>> bu(*t2)
    False
    >>> bu(*t3)
    False
    >>> bu(*t4)
    True
    """
    M, N, P = len(m), len(n), len(p)
    i = j = k = 0
    while k < P:
        if i < M and m[i] == p[k]: i += 1
        elif j < N and n[j] == p[k]: j += 1
        k += 1
    return i == M and j == N

if __name__ == '__main__':
    import doctest
    doctest.testmod()
