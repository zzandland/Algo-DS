class Solution {
  public int[] plusOne(int[] digits) {
    boolean lifted = false;
    int onesIndex = digits.length - 1;
    digits[onesIndex]++;
    if (digits[onesIndex] == 10) {
      digits[onesIndex] = 0;
      lifted = true;
    }
    if (lifted) {
      for (int i = digits.length - 2; i >= 0; i--) {
        digits[i]++;
        if (digits[i] == 10) {
          digits[i] = 0;
        } else {
          lifted = false;
          break;
        }
      }
    }
    if (lifted) {
      int[] oneMore = new int[digits.length + 1];
      oneMore[0] = 1;
      for (int j = 0; j < digits.length; j++) {
        oneMore[j + 1] = digits[j];
      }
      return oneMore;
    } else {
      return digits;
    }
  }
}