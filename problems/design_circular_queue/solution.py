class MyCircularQueue:

    def __init__(self, k: int):
        self.arr = [-1] * k
        self.head = self.tail = 0
        
    def _prev(self, i: int):
        return (i - 1) % len(self.arr)

    def _next(self, i: int):
        return (i + 1) % len(self.arr)
        
    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        self.arr[self.tail] = value
        self.tail = self._next(self.tail)
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        self.arr[self.head] = -1
        self.head = self._next(self.head)
        return True

    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.arr[self.head]

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.arr[self._prev(self.tail)]

    def isEmpty(self) -> bool:
        return self.head == self.tail and self.arr[self.head] == -1

    def isFull(self) -> bool:
        return self.head == self.tail and self.arr[self.head] != -1

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()