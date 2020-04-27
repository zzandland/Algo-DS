import sys
from collections import deque
readline = sys.stdin.readline

T = int(readline())
N = 10**9
for t in range(1, T+1):
    q = deque(list(readline()))
    def fn(w, h):
        while q:
            print(w, h, q)
            c = q.popleft()
            if c == ')':
                return [w, h]
            elif c.isdigit():
                q.popleft()
                w2, h2 = fn(0, 0)
                w += int(c) * w2
                h += int(c) * h2
            elif c == 'N': h -= 1
            elif c == 'S': h += 1
            elif c == 'E': w += 1
            elif c == 'W': w -= 1
        return [w, h]
    ow, oh = fn(1, 1)
    ow %= N
    if ow == 0: ow = N
    oh %= N
    if oh == 0: oh = N
    print('Case #%d: %d %d' % (t, ow, oh))
