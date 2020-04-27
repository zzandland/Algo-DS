import sys
readline = sys.stdin.readline
flush = sys.stdin.flush

T = int(readline())

for t in range(1, T+1):
    N = int(readline())
    H = [int(p) for p in readline().split()]
    ans = 0
    for i in range(1, N-1):
        if H[i-1] < H[i] and H[i] > H[i+1]:
            ans += 1
    print("Case #%d: %d" % (t, ans))
