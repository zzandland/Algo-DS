from typing import List
from heapq import heappush, heappop, heapify

def min_cost_to_connect_ropes(ropes: List[int]) -> int:
    '''
    >>> min_cost_to_connect_ropes([8, 4, 6, 12])
    58
    >>> min_cost_to_connect_ropes([20, 4, 8, 2])
    54
    >>> min_cost_to_connect_ropes([1, 2, 5, 10, 35, 89])
    224
    >>> min_cost_to_connect_ropes([2, 2, 3, 3])
    20
    '''
    # heapify the ropes O(ropes)
    heapify(ropes)

    # take out shortest two ropes and tie them until there's only one rope left O(n log n)
    cost = 0
    while len(ropes) > 1:
        a, b = heappop(ropes), heappop(ropes)
        cost += a + b
        heappush(ropes, a + b)
    return cost

if __name__ == '__main__':
    import doctest
    doctest.testmod()
