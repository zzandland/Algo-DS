class Solution {
  public String addBinary(String a, String b) {
    char[] aArr = a.toCharArray();
    char[] bArr = b.toCharArray();
    StringBuilder output = new StringBuilder();
    int aLen = aArr.length - 1, bLen = bArr.length - 1, sum, lifted = 0;
    while (aLen >= 0 || bLen >= 0) {
      sum = lifted;
      if (aLen >= 0) sum += aArr[aLen--] - '0';
      if (bLen >= 0) sum += bArr[bLen--] - '0';
      output.insert(0, sum % 2);
      lifted = sum / 2;
    }
    if (lifted == 1) output.insert(0, lifted);
    return output.toString();
  }
}