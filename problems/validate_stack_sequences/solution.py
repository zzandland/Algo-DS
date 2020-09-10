class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        st = []
        pushed.reverse()
        popped.reverse()
        while pushed or popped:
            if st and st[-1] == popped[-1]:
                popped.pop()
                st.pop()
            else:
                if not pushed: return False
                st.append(pushed.pop())
        return not st