class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic = {}
        output = ''
        for i in range(len(s)):
          if s[i] not in dic:
            dic[s[i]] = [i]
            if output == '':
              output = s[i]
          else:
            dic[s[i]].append(i)
            for j in range(len(dic[s[i]]) - 1):
              substr = s[dic[s[i]][j]:i + 1]
              if len(substr) > len(output):
                if substr == substr[::-1]:
                  output = substr
        return output
