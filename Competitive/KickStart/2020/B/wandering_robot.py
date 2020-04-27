dir_ = [(1, 0), (0, 1)]

def cnt(x, y, w, h):
    if x > w or y > h: return 0
    if x == w and y == h: return 1
    return sum([cnt(x+r, y+c, w, h) for r, c in dir_])

print(cnt(0, 0, 1, 1))
print(cnt(0, 0, 2, 1))
print(cnt(0, 0, 1, 2))
print(cnt(0, 0, 2, 2))
print(cnt(0, 0, 2, 3))
print(cnt(0, 0, 3, 3))
