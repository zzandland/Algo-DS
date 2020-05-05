class Node:
    def __init__(self, key:int, val: int):
        self.key = key
        self.val = val
        self.prev = self.next = None
        
class DLL:
    def __init__(self):
        self.head = self.tail = None
        
    def appendLeft(self, n: Node) -> None:
        if self.head: self.head.prev, n.next = n, self.head
        if self.tail == n: self.tail = self.head    
        self.head = n    
        if not self.tail: self.tail = n    
        
    def pop(self) -> Node:
        n = self.tail
        if self.tail:
            self.tail.prev.next = None
            self.tail = self.tail.prev
        n.prev = None    
        return n
    
    def popInside(self, n: Node) -> Node:
        if n.prev: n.prev.next = n.next
        else: self.head = self.head.next    
        if n.next: n.next.prev = n.prev
        else: self.tail = self.tail.prev    
        n.next = n.prev = None    
        return n

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = 0
        self.max = capacity
        self.dic = {}
        self.dll = DLL()
        
    def get(self, key: int) -> int:
        if key not in self.dic: return -1
        n = self.dll.popInside(self.dic[key])
        self.dll.appendLeft(n)
        return n.val

    def put(self, key: int, val: int) -> None:
        if key not in self.dic:
            n = Node(key, val)
            self.dic[key] = n
            self.dll.appendLeft(n)
            if self.capacity == self.max:
                l = self.dll.pop()
                del self.dic[l.key]
            else: self.capacity += 1    
        else:
             self.dic[key].val = val       
             self.get(key)   

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)