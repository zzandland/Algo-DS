from collections import defaultdict

class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lst = []
        self.idx = defaultdict(set)

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        res = bool(self.idx[val])
        self.lst.append(val)
        self.idx[val].add(len(self.lst) - 1)
        return not res

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if not self.idx[val]: return False
        i = next(iter(self.idx[val]))
        self.idx[val].remove(i)
        if i != len(self.lst) - 1:
            last = self.lst[-1]
            self.idx[last].remove(len(self.lst) - 1)
            self.idx[last].add(i)
            self.lst[i] = last
        self.lst.pop()
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return random.choice(self.lst)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()