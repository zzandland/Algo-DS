class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        i = j = 0
        st, T, mx = set(), len(tree), 0
        while i < T:
            st.add(tree[i])
            if len(st) > 2:
                j, st = i, set([tree[i]])
                while len(st) <= 2:
                    j -= 1
                    st.add(tree[j])
                st.remove(tree[j])    
                j += 1
            i += 1
            mx = max(mx, i-j)
        return mx  