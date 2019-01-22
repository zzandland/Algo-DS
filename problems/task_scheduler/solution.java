class Solution {
  public int leastInterval(char[] tasks, int n) {
    int[] map = new int[26];
    for (char cha : tasks) {
      map[cha - 'A']++;
    }
    int max = 0;
    for (int freq : map) {
      if (freq > max) max = freq;
    }
    int count = 0;
    for (int freq : map) {
      if (freq == max) count++;
    }
    return Math.max((n + 1) * (max - 1) + count, tasks.length);
  }
}