class Node:
    
    def __init__(self, lst: [int]):
        self.lst = lst
        self.next = None

class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        lsts = [v1, v2]
        head = run = None
        for lst in lsts:
            tmp = Node(lst[::-1])
            if run: run.next = tmp
            run = tmp
            if not head: head = run
        run.next = head
        self.p = run

    def next(self) -> int:
        return self.p.lst.pop()

    def hasNext(self) -> bool:
        self.p = self.p.next
        while self.p and not self.p.lst:
            if self.p.next == self.p: return False
            self.p.lst = self.p.next.lst
            self.p.next = self.p.next.next
        return self.p and self.p.lst

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())