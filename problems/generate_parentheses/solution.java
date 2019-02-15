import java.util.ArrayList;
import java.util.HashMap;

class Solution {
  private static class Bracket {
    int open = 0;
    int close = 0;
  }
  
  static List<String> output = new ArrayList<String>();
  static StringBuilder build = new StringBuilder();
  
  public List<String> generateParenthesis(int n) {
    Bracket bracket = new Bracket();
    List<String> output = new ArrayList<String>();
    StringBuilder build = new StringBuilder();
    helper(n, bracket, output, build);
    return output;
  }
  
  private void helper(int nPair, Bracket bracket, List<String> output, StringBuilder build) {
    if (bracket.open == nPair && bracket.close == nPair) {
      output.add(build.toString()) ;
      return;
    }
    if (bracket.open < nPair) {
      build.append('(');
      bracket.open++;
      helper(nPair, bracket, output, build);
      build.deleteCharAt(build.length() - 1);
      bracket.open--;
    }
    if (bracket.close < bracket.open) {
      build.append(')');
      bracket.close++;
      helper(nPair, bracket, output, build);
      build.deleteCharAt(build.length() - 1);
      bracket.close--;
    }
  }
}