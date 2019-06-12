from typing import List


def sort_A_as_B(A: List[int], B: List[int]) -> List[int]:
    """
    >>> sort_A_as_B([24, 56, 74, -23, 87, 91], [2, 3, 4, 1, 5, 6])
    [-23, 24, 56, 74, 87, 91]
    >>> sort_A_as_B([], [3, 1, 2])
    []
    >>> sort_A_as_B([5, 23, 7], [3, 2, 1, 4])
    [5, 23, 7]
    """

    if not A or len(A) != len(B):
        return A

    i = 0

    while i < len(A):
        j = B[i] - 1

        if i != j:
            A[i], A[j] = A[j], A[i]
            B[i], B[j] = B[j], B[i]
        else:
            i += 1

    return A


if __name__ == "__main__":
    import doctest
    doctest.testmod()
