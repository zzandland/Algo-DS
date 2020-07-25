class Solution:
    """
    >>> s1 = Solution(5)
    >>> s1.insert(2)
    >>> s1.insert(2)
    >>> s1.insert(2)
    >>> s1.insert(4)
    >>> s1.insert(1)
    1

    >>> s2 = Solution(33)
    >>> s2.insert(3)
    >>> s2.insert(8)
    >>> s2.insert(15)
    >>> s2.insert(8)
    >>> s2.insert(15)
    15
    >>> s2.insert(18)
    >>> s2.insert(14)
    >>> s2.insert(22)
    >>> s2.insert(10)
    >>> s2.insert(21)
    """
    def __init__(self, target: int):
        self.st = set()
        self.target = target
        self.found = False

    def insert(self, num: int):
        if not self.found and self.target - num in self.st:
            self.found = True
            return num
        for n in list(self.st):
            self.st.add(n + num)
        self.st.add(num)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
