#
# @lc app=leetcode id=30 lang=python
#
# [30] Substring with Concatenation of All Words
#
# https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/
#
# algorithms
# Hard (24.73%)
# Likes:    730
# Dislikes: 1123
# Total Accepted:    163.2K
# Total Submissions: 658.2K
# Testcase Example:  '"barfoothefoobarman"\n["foo","bar"]'
#
# You are given a string, s, and a list of words, words, that are all of the
# same length. Find all starting indices of substring(s) in s that is a
# concatenation of each word in words exactly once and without any intervening
# characters.
#
#
#
# Example 1:
#
#
# Input:
# ⁠ s = "barfoothefoobarman",
# ⁠ words = ["foo","bar"]
# Output: [0,9]
# Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar"
# respectively.
# The output order does not matter, returning [9,0] is fine too.
#
#
# Example 2:
#
#
# Input:
# ⁠ s = "wordgoodgoodgoodbestword",
# ⁠ words = ["word","good","best","word"]
# Output: []
#
#
#

# @lc code=start
from collections import defaultdict
import itertools

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if len(s) == 0 or len(words) == 0: return []
        st = {s[i] + s[i+1] for i in range(0, len(s)-1)}
        valid_st = set()
        for i in range(0, len(words)):
            word1 = words[i]
            for j in range(i + 1, len(words)):
                word2 = words[j]
                comb1, comb2 = word1[-1] + word2[0], word2[-1] + word1[0]
                if comb1 in st or comb2 in st:
                    valid_st.add(word1)
                    valid_st.add(word2)
        perm = {''.join(list(i)) for i in itertools.permutations(filter(lambda x:x in valid_st, words) or words)}
        permLen = len(''.join(words))
        return [i for i in range(0, len(s) - permLen+1) if s[i:i+permLen] in perm]
# @lc code=end
