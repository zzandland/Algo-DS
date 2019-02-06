class Solution {
  public void rotate(int[] nums, int k) {
    if (k == 0) return;
    k %= nums.length;
    int count = 0;
    for (int start = 0; count < nums.length; start++) {
      int pos = start;
      int prev = nums[start];
      do {
        int next = (pos + k) % nums.length;
        int save = nums[next];
        nums[next] = prev;
        pos = next;
        prev = save;
        count++;
      } while (pos != start);
    }
  }
}