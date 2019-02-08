import java.util.HashSet;

class Solution {
  public int singleNumber(int[] nums) {
    HashSet<Integer> set = new HashSet<Integer>();
    for (int num : nums) {
      if (set.contains(num)) set.remove(num);      
      else set.add(num);
    }
    Iterator<Integer> ite = set.iterator();
    int output = ite.next();
    return output;
  }
}