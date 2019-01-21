class Solution {
  public int romanToInt(String s) {
    int sum = 0;
    if (s.indexOf("IV") != -1) sum -= 2;
    if (s.indexOf("IX") != -1) sum -= 2;
    if (s.indexOf("XL") != -1) sum -= 20;
    if (s.indexOf("XC") != -1) sum -= 20;
    if (s.indexOf("CD") != -1) sum -= 200;
    if (s.indexOf("CM") != -1) sum -= 200;
    for (int i = 0; i < s.length(); i++) {
      switch (s.charAt(i)) {
        case 'M': sum += 1000;
          break;
        case 'D': sum += 500;
          break;
        case 'C': sum += 100;
          break;
        case 'L': sum += 50;
          break;
        case 'X': sum += 10;
          break;
        case 'V': sum += 5;
          break;
        case 'I': sum += 1;
          break;
      }
    }
    return sum;
  }
}