class Solution {
  public int totalFruit(int[] tree) {
    int max = -1;
    int lastFruit = -1;
    int dic[] = {-1, -1};
    int size = 0;
    int left = 0;
    int index = 0;
    
    for (int i = 0; i < tree.length; i++) {
      if (dic[0] == -1) {
        dic[0] = tree[i]; 
      } else if (dic[0] != tree[i] && dic[1] == -1) {
        dic[1] = tree[i];
      } else if (dic[0] != tree[i] && dic[1] != tree[i]) {
        size = i - left;
        if (size > max) max = size;
        dic[0] = tree[i - 1];
        dic[1] = tree[i];
        left = index;
      }
      if (tree[i] != lastFruit) {
        index = i; 
        lastFruit = tree[i];
      }
    }
    size = tree.length - left;
    if (size > max) max = size;
    return max;
  }
}