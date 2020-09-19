class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lst = []
        self.idx = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.idx: return False
        self.lst.append(val)
        self.idx[val] = len(self.lst) - 1
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.idx: return False
        last = self.lst[-1]
        self.lst[self.idx[val]] = last
        self.idx[last] = self.idx[val]
        del self.idx[val]
        self.lst.pop()
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.lst)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()