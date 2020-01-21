class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    a = b = -1
    st = set()
    mx = 0
    while b < len(s) - 1:
      b += 1
      if s[b] in st:
        a += 1
        while s[a] != s[b]:
          st.remove(s[a])
          a += 1
      else:
        st.add(s[b])
      if b - a > mx:
        mx = b - a    
    return mx    