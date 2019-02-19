class Solution {
  public String longestCommonPrefix(String[] strs) {
    if (strs.length <= 0) return "";
    StringBuilder output = new StringBuilder();
    String smallest = getSmallestLen(strs);
    char cha;
    boolean matched = true;
    for (int i = 0; matched && i < smallest.length(); i++) {
      cha = smallest.charAt(i);
      if (checkCharMatch(strs, i, cha)) output.append(cha);
      else matched = false;
    }
    return output.toString();
  }
  
  private boolean checkCharMatch(String strs[], int index, char cha) {
    for (String str : strs) {
      if (str.charAt(index) != cha) return false; 
    }
    return true;
  }
  
  private String getSmallestLen(String strs[]) {
    String smallest = strs[0];
    for (int i = 0; i < strs.length; i++) {
      if (strs[i].length() < smallest.length()) smallest = strs[i];
    }
    return smallest;
  }
}