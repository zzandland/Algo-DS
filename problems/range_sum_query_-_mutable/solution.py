class Node:
    def __init__(self, l: int, r: int, val: int):
        self.l = l
        self.r = r
        self.val = val
        self.left = self.right = None

class NumArray:
    def __init__(self, nums: List[int]):
        run, tmp = 0, [0]
        for n in nums:
            run += n
            tmp.append(run)
        def build(l: int, r: int) -> Node:
            n = Node(l, r, tmp[r+1]-tmp[l])
            if l < r:
                m = l + (r-l)//2
                n.left, n.right = build(l, m), build(m+1, r)
            return n
        self.root = build(0, len(nums)-1)
        
    def update(self, i: int, val: int) -> None:
        n, st = self.root, []
        while n.l != i or n.r != i:
            st.append(n)
            m = n.l + (n.r-n.l)//2
            if m >= i:
                n = n.left
            else:
                n = n.right
        diff = n.val - val
        n.val = val
        while st:
            n = st.pop()
            n.val -= diff

    def sumRange(self, i: int, j: int) -> int:
        def fn(n: Node, l: int, r: int) -> int:
            if n.l == l and n.r == r:
                return n.val
            m = n.l + (n.r-n.l)//2
            if r <= m:
                return fn(n.left, l, r)
            elif l > m:
                return fn(n.right, l, r)
            else:
                return fn(n.left, l, m) + fn(n.right, m+1, r)
        return fn(self.root, i, j)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)