#  Given a word of length n and n six-sided dice with a character in each side. Find out if this word can be constructed by the set of given dice.

#  Example 1:

#  Input:
#  word = "hello"
#  dice = [[a, l, c, d, e, f], [a, b, c, d, e, f], [a, b, c, h, e, f], [a, b, c, d, o, f], [a, b, c, l, e, f]]
#  Output: true
#  Explanation: dice[2][3] + dice[1][4] + dice[0][1] + dice[4][3] + dice[3][4]

#  Example 2:

#  Input:
#  word = "hello"
#  dice = [[a, b, c, d, e, f], [a, b, c, d, e, f], [a, b, c, d, e, f], [a, b, c, d, e, f], [a, b, c, d, e, f]]
#  Output: false

#  Example 3:

#  Input:
#  word = "aaaa"
#  dice = [[a, a, a, a, a, a], [b, b, b, b, b, b], [a, b, c, d, e, f], [a, b, c, d, e, f]]
#  Output: false

from typing import *
from collections import defaultdict

dice1 = [
    ['a', 'l', 'c', 'd', 'e', 'f'],
    ['a', 'b', 'c', 'd', 'e', 'f'],
    ['a', 'b', 'c', 'h', 'e', 'f'],
    ['a', 'b', 'c', 'd', 'o', 'f'],
    ['a', 'b', 'c', 'l', 'e', 'f']
]

dice2 = [
    ['a', 'b', 'c', 'd', 'e', 'f'],
    ['a', 'b', 'c', 'd', 'e', 'f'],
    ['a', 'b', 'c', 'd', 'e', 'f'],
    ['a', 'b', 'c', 'd', 'e', 'f'],
    ['a', 'b', 'c', 'd', 'e', 'f']
]

dice3 = [
    ['a', 'a', 'a', 'a', 'a', 'a'],
    ['b', 'b', 'b', 'b', 'b', 'b'],
    ['a', 'b', 'c', 'd', 'e', 'f'],
    ['a', 'b', 'c', 'd', 'e', 'f']
]

def can_construct(dice: List[List[str]], word: str) -> bool:
    """
    >>> can_construct(dice1, 'hello')
    True
    >>> can_construct(dice2, 'hello')
    False
    >>> can_construct(dice3, 'aaaa')
    False
    """
    dic = defaultdict(set)
    for i, face in enumerate(dice):
        for c in face:
            dic[c].add(i)
    seen = set()
    def dfs(i: int) -> bool:
        if i == len(word): return True
        for j in dic[word[i]]:
            if j not in seen:
                seen.add(j)
                if dfs(i+1): return True
                seen.remove(j)
        return False
    return dfs(0)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
