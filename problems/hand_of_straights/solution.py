from collections import defaultdict

class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        hand.sort()
        dic = defaultdict(list)
        for n in hand:
            found = False
            for i in range(len(dic[n])):
                if n - dic[n][i] < W:
                    dic[n][i], dic[n][-1] = dic[n][-1], dic[n][i]
                    dic[n+1].append(dic[n].pop())
                    break
            else:
                dic[n+1].append(n)
                
        for n, lst in dic.items():
            for nn in lst:
                if n - nn != W: return False
                
        return True