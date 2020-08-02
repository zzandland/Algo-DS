class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if not nums: return False
        mn = [nums[0]]
        for n in nums[1:]:
            mn.append(min(mn[-1], n))
        st = []
        for mn, n in zip(mn[::-1], nums[::-1]):
            if mn < n:
                while st and st[-1] <= mn:
                    st.pop()
                if st and st[-1] < n and st[-1] > mn: return True
                st.append(n)
        return False