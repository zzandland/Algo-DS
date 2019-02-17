import java.util.regex.*;

class Solution {
  public int myAtoi(String str) {
    Pattern p = Pattern.compile("^(\\s*)([+-]?\\d+)(.*)");
    Matcher m = p.matcher(str);
    if (m.matches()) {
      double num = Double.parseDouble(m.group(2));
      if (num > Integer.MAX_VALUE) return Integer.MAX_VALUE;
      else if (num < Integer.MIN_VALUE) return Integer.MIN_VALUE;
      else return (int) num;
    }
    return 0;
  }
}