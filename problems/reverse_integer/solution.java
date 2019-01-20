class Solution {
    public int reverse(int x) {
      int output = 0, temp, sign;
      if (x < 0) {
        sign = -1;
        x *= -1;
      } else {
        sign = 1;
      }
      while (x > 0) {
        temp = output * 10 + x % 10;
        if (temp / 10 != output) return 0;
        output = temp;
        x /= 10;
      }
      return output * sign;
    }
}