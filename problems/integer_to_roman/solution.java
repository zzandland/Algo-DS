import java.util.Hashtable;

class Solution {
  public String intToRoman(int num) {
    int[] ints = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
    String[] romans = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
    StringBuilder build = new StringBuilder();
    for (int i = 0; i < ints.length; i++) {
      while (num >= ints[i]) {
        num -= ints[i];
        build.append(romans[i]);
      }
    }
    return build.toString();
  }
}