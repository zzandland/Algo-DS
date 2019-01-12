class KthLargest {
  private static class Node {
    private int val;
    private int count = 1;
    private Node left, right;
    
    public Node(int val) {
      this.val = val;
    }
    
    public int getVal() {
      return val;
    }
    
    public int getCount() {
      return count;
    }
    
    public void incrementCount() {
      count++;
    }
  }
  
  private Node root;
  private int kth;
  
  public KthLargest(int k, int[] nums) {
    kth = k;
    for (int i = 0; i < nums.length; i++) {
      root = insertNode(root, nums[i]);
    }
  }
  
  public int add(int val) {
    root = insertNode(root, val);    
    return searchKth(root, kth).getVal();
  }
  
  private Node insertNode(Node node, int val) {
    if (node == null) return new Node(val);
    if (node.getVal() > val) node.left = insertNode(node.left, val);
    else node.right = insertNode(node.right, val);
    node.incrementCount();
    return node;
  }
  
  public Node searchKth(Node root, int k) {
    int m = (root.right != null) ? root.right.count : 0;
    if (m + 1 == k) return root;
    if (m < k) return searchKth(root.left, k - m - 1);
    else return searchKth(root.right, k);
  }
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest obj = new KthLargest(k, nums);
 * int param_1 = obj.add(val);
 */