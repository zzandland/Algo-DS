import java.util.regex.*;

class Solution {
    public int myAtoi(String str) {
      Pattern regex = Pattern.compile("^(\\s*)([+-]?\\d+)");
      Matcher match = regex.matcher(str);
      if (match.find()) {
        Double val = Double.parseDouble(match.group(2));
        if (val < Integer.MIN_VALUE) return Integer.MIN_VALUE;
        if (val > Integer.MAX_VALUE) return Integer.MAX_VALUE;
        return val.intValue();
      } else {
        return 0;
      }
    }
}