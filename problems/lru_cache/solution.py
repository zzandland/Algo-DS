from typing import Any

class CacheQueue:
    class Node:
        def __init__(self, data: Any):
            self.data = data
            self.next = None
            self.prev = None
            
    def __init__(self, capacity: int):
        self.least = None
        self.most = None
        self.q_map = {}
        
    def enque(self, key: int) -> None:
        node = self.Node(key)
        self.q_map[key] = node
        node.prev = self.most
        if self.most:
            self.most.next = node 
        self.most = node    
        if not self.least:
            self.least = node
            
    def deque(self) -> int:
        out = self.least
        self.least = self.least.next
        if self.least:
            self.least.prev = None
        else:
            self.most = None
        del self.q_map[out.data]
        return out.data
    
    def update_q(self, key: int) -> None:
        node = self.q_map[key]
        if node is self.least:
            self.deque()
            self.enque(node.data)
        elif node is not self.most:    
            node.next.prev = node.prev
            node.prev.next = node.next
            self.enque(node.data)
        
        
class LRUCache:

    def __init__(self, capacity: int):
        self.data_map = {}
        self.q = CacheQueue(capacity)
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key in self.data_map:
            self.q.update_q(key)
            return self.data_map[key]
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key not in self.data_map:
            if self.size == self.capacity:
                del self.data_map[self.q.deque()]
                self.q.enque(key)
            else:
                self.size += 1
                self.q.enque(key)    
        self.data_map[key] = value
        self.q.update_q(key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)