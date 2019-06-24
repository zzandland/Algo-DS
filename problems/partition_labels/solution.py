class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        output = []
        if len(S) == 0:
            return output
        interval_map = {}
        for i, c in enumerate(S):
            if c not in interval_map:
                interval_map[c] = [i, i]        
            else:
                if interval_map[c][1] < i:
                    interval_map[c][1] = i
        sorted_intervals = sorted(interval_map.values(), key=lambda x: x[0])                
        curr = sorted_intervals[0]
        for k in range(1, len(sorted_intervals)):
            interval = sorted_intervals[k]
            if curr[1] > interval[0]:
                curr[1] = max(curr[1], interval[1])
            else:
                output.append(curr[1] - curr[0] + 1)
                curr = interval
        output.append(curr[1] - curr[0] + 1)        
        return output