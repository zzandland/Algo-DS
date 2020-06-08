class MyQueue:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.inst = []
        self.outst = []
        
    def _move(self) -> None:
        while self.inst:
            self.outst.append(self.inst.pop())

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.inst.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.outst:
            self._move()
        return self.outst.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.outst:
            self._move()
        return self.outst[-1]
        
    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.inst and not self.outst

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()