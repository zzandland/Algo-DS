import java.util.*;

class Solution {
  public void rotate(int[] nums, int k) {
    List<Integer> numsList = new ArrayList<Integer>(nums.length);
    for (int i = 0; i < nums.length; i++) {
      numsList.add(nums[i]);
    }
    System.out.println(numsList);
    for (int j = 0 ; j < k; j++) {
      int temp = numsList.remove(numsList.size() - 1);
      numsList.add(0, temp);
    }
    for (int l = 0; l < nums.length; l++) {
      nums[l] = numsList.get(l);
    }
  }
}