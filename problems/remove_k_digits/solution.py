from heapq import heapify, heappop

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st = []
        for i in range(len(num)):
            n = int(num[i])
            while k > 0 and st and n < st[-1]:
                st.pop()
                k -= 1
            st.append(n)
            
        st = st[:-k] if k else st
        return ''.join(map(str, st)).lstrip('0') or '0'