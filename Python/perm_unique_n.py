# Output all the permutations of a string of unique characters given length N
# so (2, 'ab') => ['ab', 'aa', 'bb', 'ba']

def permN(n, s):
    def fn(prev):
        if len(prev) == n:
            return [prev]
        o = []
        for c in s:
            o.extend(fn(prev + c))
        return o
    return fn('')

print(permN(3, 'azb'))
