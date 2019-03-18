import java.util.regex.*;

class Solution {
  public String reverseWords(String s) {
    Pattern p = Pattern.compile("\\S+");
    Matcher m = p.matcher(s);
    StringBuilder build = new StringBuilder();
    while (m.find()) {
      build.insert(0, m.group(0));
      build.insert(0, ' ');
    }
    return build.toString().trim();
  }
}