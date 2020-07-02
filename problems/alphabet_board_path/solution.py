class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        res = []
        coords = {}
        alpha, ai = string.ascii_lowercase, 0
        for y in range(0, 6):
            for x in range(0, 5):
                if ai == len(alpha): break
                coords[alpha[ai]] = (y, x)
                ai += 1
        y = x = 0
        for c in target:
            tmp = []
            ty, tx = coords[c]
            dy, dx = ty-y, tx-x
            v, h = '', ''
            if dy > 0: v = 'D'*dy
            elif dy < 0: v = 'U'*abs(dy)
            if dx > 0: h = 'R'*dx
            elif dx < 0: h = 'L'*abs(dx)
            if c == 'z':
                res.append('%s%s!' % (h, v))
            else:
                res.append('%s%s!' % (v, h))
            y, x = ty, tx
        return ''.join(res)