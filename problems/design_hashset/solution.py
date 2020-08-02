class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1000003 # smallest prime number greater than 1 million
        self.arr = [-1]*self.size
        
    def add(self, key: int) -> None:
        idx = hash(str(key)) % self.size
        while self.arr[idx] != -1: idx = (idx+1) % self.size
        self.arr[idx] = key

    def remove(self, key: int) -> None:
        idx = hash(str(key)) % self.size
        while self.arr[idx] not in (key, -1): idx = (idx+1) % self.size
        self.arr[idx] = -1

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        idx = hash(str(key)) % self.size
        while self.arr[idx] not in (key, -1): idx = (idx+1) % self.size
        return self.arr[idx] != -1

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)