class Solution:
    def nextClosestTime(self, time: str) -> str:
        t = [int(c) for c in filter(lambda x: x != ':', list(time))]
        ts = sorted(t)
        combs = []
        def fil(t: List[int]) -> bool:
            if t[0] > 2:
                return False
            if t[0] == 2 and t[1] > 4:
                return False
            if t[2] > 5:
                return False
            return True
        def fn(i: int, run: List[int]) -> None:
            if i == 4:
                combs.append(run[:])
                return
            for t in ts:
                fn(i+1, run + [t])
        fn(0, [])
        combs = sorted(list(set([''.join(map(str, x)) for x in filter(fil, combs)])))
        idx = combs.index(''.join(map(str, t)))
        if idx == len(combs)-1:
            return combs[0][:2] + ':' + combs[0][2:]
        return combs[idx+1][:2] + ':' + combs[idx+1][2:]