class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not newInterval: return intervals
        intervals.sort()
        N, output, inserted = len(intervals), [], False
        for i in range(N):
            cur = intervals[i]
            if cur[1] < newInterval[0]: output.append(cur)
            elif cur[0] > newInterval[1]:
                if not inserted:
                    output.append(newInterval)
                    inserted = True
                output.append(cur)    
            else: 
                print(i, min(cur[0], newInterval[0]))
                newInterval = [min(newInterval[0], cur[0]), max(newInterval[1], cur[1])]    
        if not inserted: output.append(newInterval)        
        return output