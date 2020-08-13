class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.s = characters
        self.st = []
        self.len = combinationLength
        self.end = False
        for i in range(self.len):
            self.st.append(i)

    def next(self) -> str:
        tmp = ''.join([self.s[i] for i in self.st])
        for i in range(self.len):
            if self.st[-1] == len(self.s)-i-1: self.st.pop()
            else: break
        if not self.st:
            self.end = True
        else:
            self.st[-1] += 1
            while len(self.st) < self.len:
                self.st.append(self.st[-1]+1)
        return tmp

    def hasNext(self) -> bool:
        return not self.end

# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()