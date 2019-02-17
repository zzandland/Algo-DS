class Solution {
  public String countAndSay(int n) {
    String str = "1";
    while (n > 1) {
      StringBuilder build = new StringBuilder(); 
      int count = 1;
      for (int i = 0; i < str.length(); i++) {
        if (str.length() > i + 1 && str.charAt(i) == str.charAt(i + 1)) {
          count++;
          continue;
        } 
        build.append(count);
        build.append(str.charAt(i));
        count = 1;
      }
      str = build.toString();
      n--;
    }
    return str;
  }
}