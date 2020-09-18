from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.q = OrderedDict()
        self.c = capacity

    def get(self, key: int) -> int:
        if key not in self.q: return -1
        val = self.q.pop(key)
        self.q[key] = val
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.q: self.q.pop(key)
        self.q[key] = value
        if len(self.q) > self.c: self.q.popitem(last=False)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)