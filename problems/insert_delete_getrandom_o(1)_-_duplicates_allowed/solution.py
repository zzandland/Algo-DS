import random

class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lst = []
        self.mp = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.lst.append(val)
        if val not in self.mp:
            uniq = True
            self.mp[val] = set()
        else: uniq = False    
        self.mp[val].add(len(self.lst)-1)
        return uniq

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if val not in self.mp: return False
        i = self.mp[val].pop()
        if not self.mp[val]: del self.mp[val]
        if i != len(self.lst)-1:
            self.lst[i], self.lst[-1] = self.lst[-1], self.lst[i]
            swap = self.lst[i]
            self.mp[swap].remove(len(self.lst)-1)
            self.mp[swap].add(i)
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