class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        output, stack, sub = [0 for _ in range(n)], [], [0 for _ in range(n)]
        for id_, met, t in [log.split(':') for log in logs]:
            stack.append((int(id_), met, int(t)))
            if met == 'end':
                id1, met1, t1 = stack.pop()
                _, met2, t2 = stack.pop()
                diff = t1 - t2 + 1
                if stack: sub[stack[-1][0]] += diff
                output[id1] += diff - sub[id1]
                sub[id1] = 0
        return output        