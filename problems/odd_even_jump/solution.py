class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        if not A: return 0
        L = len(A)
        odds, evens = [False]*L, [False]*L
        odds[-1] = evens[-1] = True
        def make(N: List[int]) -> List[int]:
            output = [None]*L
            s = []
            for i in N:
                while s and s[-1] < i:
                    output[s.pop()] = i
                s.append(i)
            return output    
        B = sorted(range(L), key=lambda i: A[i])
        oddNext = make(B)
        B.sort(key=lambda i: -A[i])
        evenNext = make(B)
        for i in range(L-2, -1, -1):
            if oddNext[i] != None: odds[i] = evens[oddNext[i]]
            if evenNext[i] != None: evens[i] = odds[evenNext[i]]
        return sum(odds)