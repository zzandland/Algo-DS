class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.next = self.prev = None
        
class LRUQueue:
    def __init__(self):
        self.head = self.tail = None        
        self.size = 0
        
    def enqueue(self, n: Node) -> None:
        if self.head: n.next, self.head.prev = self.head, n
        self.head = n
        if not self.tail: self.tail = n
        self.size += 1    
            
    def dequeue(self) -> Node:
        t = self.tail
        if self.tail != self.head:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            self.tail = self.head = None
        t.next = t.prev = None
        self.size -= 1    
        return t
        
    def remove(self, n: Node) -> Node:
        if self.tail == n: return self.dequeue()
        self.size -= 1
        if self.head == n: self.head = n.next
        if n.prev: n.prev.next = n.next
        if n.next: n.next.prev = n.prev    
        n.next = n.prev = None
        return n
        
class LRUCache:
    def __init__(self, capacity: int):
        self.q = LRUQueue()        
        self.dic = {}
        self.capacity = capacity
        
    def get(self, key: int) -> int:
        if key in self.dic: 
            n = self.q.remove(self.dic[key])
            self.q.enqueue(n)
            return n.val
        return -1

    def put(self, key: int, val: int) -> None:
        n = Node(key, val)
        if key in self.dic: self.q.remove(self.dic[key])        
        self.dic[key] = n
        self.q.enqueue(n)
        if self.capacity < self.q.size: 
            d = self.q.dequeue()
            del self.dic[d.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)