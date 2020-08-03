class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        N = len(A)
        def get_next(order: List[int]) -> List[int]:
            st = []
            res = [-1]*N
            for n in order:
                while st and st[-1] < n: res[st.pop()] = n
                st.append(n)
            return res
        I = sorted(range(N), key=lambda x: A[x])
        odd_next = get_next(I)
        I.sort(key=lambda x: -A[x])
        even_next = get_next(I)
        odd, even = [False]*N, [False]*N
        odd[-1] = even[-1] = True
        res = 1
        for i in range(N-2, -1, -1):
            if odd_next[i] != -1 and even[odd_next[i]]: odd[i] = True
            if even_next[i] != -1 and odd[even_next[i]]: even[i] = True
            if odd[i]: res += 1
        return res