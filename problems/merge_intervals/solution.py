class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        output = []        
        time_dict = {}
        for interval in intervals:
            start, end = interval
            if start not in time_dict:
                time_dict[start] = 0
            time_dict[start] += 1
            if end not in time_dict:
                time_dict[end] = 0
            time_dict[end] -= 1
        diff, start = 0, -1
        for num, weight in sorted(time_dict.items()):
            if start == -1:
                start = num
            diff += weight
            if diff == 0:
                output.append([start, num])
                start = -1
        return output        