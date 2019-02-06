import java.util.HashSet;

class Solution {
  HashSet dup = new HashSet();
  public boolean containsDuplicate(int[] nums) {
    for (int num : nums) {
      if (dup.contains(num)) return true;
      dup.add(num);
    }
    return false;
  }
}