class Solution {
  public String addBinary(String a, String b) {
    int aIdx = a.length() - 1;
    int bIdx = b.length() - 1;
    int sum = 0;
    int lift = 0;
    StringBuilder build = new StringBuilder();
    while (aIdx >= 0 || bIdx >= 0) {
      if (aIdx >= 0) {
        sum += a.charAt(aIdx) - '0'; 
        aIdx--;
      }
      if (bIdx >= 0) {
        sum += b.charAt(bIdx) - '0'; 
        bIdx--;
      }
      if (sum > 1) {
        sum -= 2;
        lift = 1;
      } else {
        lift = 0;
      }
      build.append(sum);
      sum = lift;
    }
    if (sum == 1) build.append(sum);
    return build.reverse().toString();
  }
}