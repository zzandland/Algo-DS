import sys

def func(n: int, k: int) -> int:
    if k == 0:
        return 0
    mem = [0]
    for x in range(1, n + 1):
        start = x - k
        if start < 1:
            start = 1
        cum = 0
        if x <= k:
            cum += 1
        for y in range(start, x):
            cum += mem[y]
        mem.append(cum)
    return mem[-1]

print(func(int(sys.argv[1]), int(sys.argv[2])))
