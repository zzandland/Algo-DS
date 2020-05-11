class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        st = set()
        for num in arr:
            if num*2 in st or num/2 in st: return True
            st.add(num)
        return False    