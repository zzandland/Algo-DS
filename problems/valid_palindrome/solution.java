class Solution {
  public boolean isPalindrome(String s) {
    s = s.replaceAll("\\W", "");
    for (int i = 0; i < s.length() / 2; i++) {
      if (Character.toLowerCase(s.charAt(i)) != Character.toLowerCase(s.charAt(s.length() - 1 - i))) return false;
    }
    return true;
  }
}