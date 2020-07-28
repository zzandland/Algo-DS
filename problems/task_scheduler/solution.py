from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = Counter(tasks)
        mx_freq, mx_arr = 0, []
        for task, freq in c.items():
            if mx_freq < freq:
                mx_arr.clear()
                mx_freq = freq
            if mx_freq == freq:
                mx_arr.append(task)
        return max(len(tasks), mx_freq * (n+1) - (n+1-len(mx_arr)))