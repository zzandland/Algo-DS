class Solution {
    public String longestCommonPrefix(String[] strs) {
      if (strs.length == 0) return "";
      StringBuilder output = new StringBuilder();
      int min = strs[0].length();
      boolean isSame = true;
      for (String str : strs) {
        if (str.length() < min) min = str.length();
      }
      for (int i = 0; i < min && isSame; i++) {
        char common = strs[0].charAt(i);
        for (int j = 1; j < strs.length; j++) {
          if (strs[j].charAt(i) != common) {
            isSame = false;
            break;
          } 
        }
        if (isSame) output.append(common);
      }
      return output.toString();
    }
}