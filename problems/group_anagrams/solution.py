from collections import defaultdict

class Solution:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    dic = defaultdict(list);
    for word in strs:
      lst = [0] * 27
      for c in word:
        lst[ord(c) - ord('a')] += 1
      dic[str(lst)].append(word)
    output = []  
    for _, v in dic.items():
      output.append(v)
    return output  