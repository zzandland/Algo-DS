"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        idx = {e.id: e for e in employees}
        st = [idx[id]]
        res = 0
        while st:
            e = st.pop()
            res += e.importance
            st += [idx[id] for id in e.subordinates]
        return res