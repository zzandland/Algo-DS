from collections import deque

class Solution:
    def simplifyPath(self, path: str) -> str:
        if not path: return ''
        res = []
        for p in path.split('/'):
            if p and p != '.':
                if p == '..': 
                    if res: res.pop()
                else: res.append(p)    
        return '/' + '/'.join(res)            