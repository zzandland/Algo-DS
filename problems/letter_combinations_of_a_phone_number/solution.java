class Solution {
  public List<String> letterCombinations(String digits) {
    List<String> output = new ArrayList<String>();
    if (digits.equals("")) return output;
    StringBuilder build = new StringBuilder();
    char[][] map = {
      {},
      {},
      {'a', 'b', 'c'},
      {'d', 'e', 'f'},
      {'g', 'h', 'i'},
      {'j', 'k', 'l'},
      {'m', 'n', 'o'},
      {'p', 'q', 'r', 's'},
      {'t', 'u', 'v'},
      {'w', 'x', 'y', 'z'}
    };
    helper(output, digits, build, map, 0);
    return output;
  }
  
  private void helper(List<String> output, String digits, StringBuilder build, char[][] map, int index) {
    if (index == digits.length()) {
      output.add(build.toString());
      return;
    }
    char[] chars = map[Character.getNumericValue(digits.charAt(index))];
    for (char cha : chars) {
      build.append(cha);
      index++;
      helper(output, digits, build, map, index);
      build.deleteCharAt(build.length() - 1);
      index--;
    }
  }
}