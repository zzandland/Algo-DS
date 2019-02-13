class Solution {
  public String licenseKeyFormatting(String S, int K) {
    StringBuilder build = new StringBuilder();
    S = S.replaceAll("-", "");
    for (int i = S.length() - 1, j = 1; i >= 0; i--, j++) {
      char cha = S.charAt(i);
      if (cha - 'Z' > 0) build.append(Character.toUpperCase(cha));
      else build.append(cha);
      if (j % K == 0 && i > 0) build.append('-');
    }
    return build.reverse().toString();
  }
}