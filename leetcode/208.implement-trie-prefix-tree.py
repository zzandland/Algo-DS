#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#
# https://leetcode.com/problems/implement-trie-prefix-tree/description/
#
# algorithms
# Medium (43.70%)
# Likes:    2438
# Dislikes: 44
# Total Accepted:    247.6K
# Total Submissions: 559.6K
# Testcase Example:  '["Trie","insert","search","search","startsWith","insert","search"]\n[[],["apple"],["apple"],["app"],["app"],["app"],["app"]]'
#
# Implement a trie with insert, search, and startsWith methods.
#
# Example:
#
#
# Trie trie = new Trie();
#
# trie.insert("apple");
# trie.search("apple");   // returns true
# trie.search("app");     // returns false
# trie.startsWith("app"); // returns true
# trie.insert("app");
# trie.search("app");     // returns true
#
#
# Note:
#
#
# You may assume that all inputs are consist of lowercase letters a-z.
# All inputs are guaranteed to be non-empty strings.
#
#
#

# @lc code=start
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        def helper(trie, i: int) -> None:
            if i == len(word):
                trie.add('*', {});
                return
            if word[i] not in trie:
                trie.add(word[i], {});
            helper(trie[word[i]], i+1)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        n = self.trie
        for c in word:
            if c not in n:
                return False
            n = n[c]
        return '*' in n


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        n = self.trie
        for c in prefix:
            if c not in n:
                return False
            n = n[c]
        return True



# Your Trie object will be instantiated and called as such:
#  obj = Trie()
#  obj.insert(word)
#  param_2 = obj.search(word)
#  param_3 = obj.startsWith(prefix)
# @lc code=end
