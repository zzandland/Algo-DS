class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        st = set()
        for num in nums: 
            if num in st: st.remove(num)
            else: st.add(num)
        return list(st)[0]