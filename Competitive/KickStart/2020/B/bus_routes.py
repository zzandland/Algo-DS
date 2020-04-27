import sys
readline = sys.stdin.readline

T = int(readline())

for t in range(1, T+1):
    N, D = [int(x) for x in readline().split()]
    X, out = [int(x) for x in readline().split()], D
    for i in range(N-1, -1, -1):
        out = X[i] * (out//X[i])
    print("Case #%d: %d" % (t, out))
