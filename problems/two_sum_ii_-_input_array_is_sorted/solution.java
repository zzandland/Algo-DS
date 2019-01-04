class Solution {
  public int[] twoSum(int[] numbers, int target) {
    int left = 0, right = numbers.length - 1, sum;
    int[] output = new int[2];
    while (right > left) {
      sum = numbers[left] + numbers[right];
      if (sum == target) {
        output[0] = left + 1;
        output[1] = right + 1;
        return output;
      }
      if (sum > target) {
        right--;
      } else {
        left++;
      }
    }
    return null;
  }
}