class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        return sum([1 for st, et in zip(startTime, endTime) if st <= queryTime <= et])