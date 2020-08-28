# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        sm = 40
        while sm >= 40:
            sm = (rand7()-1) * 7 + rand7() - 1
        return sm % 10 + 1