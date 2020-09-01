class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        check_col = lambda a, b: a > 0 and b < 0
        st = []
        for size in asteroids:
            while st and check_col(st[-1], size) and st[-1] + size < 0:
                st.pop()
            if not st or not check_col(st[-1], size):
                st.append(size)
            elif st[-1] + size == 0: st.pop()
        return st