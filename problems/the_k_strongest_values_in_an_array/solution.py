class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        N, res = len(arr), []
        arr.sort()
        med, l, r = arr[(N-1)//2], 0, N-1
        while len(res) < k:
            rd, ld = abs(arr[r] - med), abs(arr[l] - med)
            if rd == ld:
                if arr[r] > arr[l]:
                    res.append(arr[r])
                    r -= 1
                else:
                    res.append(arr[l])    
                    l += 1
            elif rd > ld:
                res.append(arr[r])
                r -= 1
            else:
                res.append(arr[l])    
                l += 1
        return res