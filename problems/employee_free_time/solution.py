"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        output, cur, schedules = [], None, [[s.start, s.end] for e in schedule for s in e]
        for bg, end in sorted(schedules, key=lambda s: s[0]):
            if not cur: cur = bg
            elif cur > end: continue    
            elif bg > cur: output.append(Interval(cur, bg))
            cur = end
        return output    