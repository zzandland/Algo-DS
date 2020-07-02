class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        N = len(A)
        odds, evens = [False]*N, [False]*N
        odds[-1] = evens[-1] = True
        oddNext, evenNext = [-1]*N, [-1]*N
        B = sorted(range(N), key=lambda x: A[x])
        st = []
        for n in B:
            while st and st[-1] < n:
                oddNext[st.pop()] = n
            st.append(n)
        st = []    
        B.sort(key=lambda x: -A[x])
        for n in B:
            while st and st[-1] < n:
                evenNext[st.pop()] = n
            st.append(n)
        res = 1
        for i in range(N-1, -1, -1):
            if oddNext[i] != -1:
                odds[i] = evens[oddNext[i]]
                if odds[i]: res += 1
            if evenNext[i] != -1:
                evens[i] = odds[evenNext[i]]
        return res