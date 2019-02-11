class Solution {
  public int reverse(int x) {
    try {
      boolean negative = false;
      if (x < 0) {
        negative = true;
        x *= -1;
      }
      StringBuilder build = new StringBuilder(String.valueOf(x));
      int reversed = Integer.parseInt(build.reverse().toString());
      return (negative) ? -1 * reversed : reversed;
    } catch (NumberFormatException e) {
      return 0;
    }
  }
}