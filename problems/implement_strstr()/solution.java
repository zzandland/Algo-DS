import java.util.regex.*;

class Solution {
  public int strStr(String haystack, String needle) {
    if (needle.length() == 0) return 0;
    Matcher m = Pattern.compile(needle).matcher(haystack);
    if (m.find()) {
      return m.start();
    }
    return -1;
  }
}