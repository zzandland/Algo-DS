# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 0, n
        while l < r:
            m = l + (r-l)//2
            tmp = isBadVersion(m)
            if not tmp:
                if isBadVersion(m+1): return m+1
                l = m+1
            else: r = m
        return l+1