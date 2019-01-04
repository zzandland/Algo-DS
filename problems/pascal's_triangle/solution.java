import java.util.*;

class Solution {
  public List<List<Integer>> generate(int numRows) {
    List<List<Integer>> output = new ArrayList<List<Integer>>();
    if (numRows == 0) return output; 
    List<Integer> first = new ArrayList<Integer>();
    first.add(1);
    output.add(first);
    for (int i = 0; i < numRows - 1; i++) {
      output = this.generateNextRow(output.get(i), output);
    }    
    return output;
  }
  
  public List<List<Integer>> generateNextRow(List<Integer> row, List<List<Integer>> output) {
    List<Integer> nextRow = new ArrayList<Integer>();
    for (int i = 0; i <= row.size(); i++) {
      if (i == 0) nextRow.add(1);
      else if (i == row.size()) nextRow.add(1);
      else nextRow.add(row.get(i - 1) + row.get(i));
    }
    output.add(nextRow);
    return output;
  }
}