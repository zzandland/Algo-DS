package trees;

import nodes.BinaryCountNode;

public class BSTWithCount extends BinarySearchTree {
  private BinaryCountNode root;

  public BSTWithCount(int val) {
    super(val);
    root = new BinaryCountNode(val); 
  }

  public void addNode(int val) { root = addNodeHelper(root, val); }

  public BinaryCountNode getKthLargest(int k) { return getKthLargestHelper(root, k); }

  private BinaryCountNode addNodeHelper(BinaryCountNode root, int val) {
    if (root == null) return new BinaryCountNode(val);
    if (root.getData() > val) root.setLeft(addNodeHelper(root.getLeft(), val));
    else root.setRight(addNodeHelper(root.getRight(), val));
    root.setCount(root.getCount() + 1);
    return root;
  }

  private BinaryCountNode getKthLargestHelper(BinaryCountNode root, int k) {
    int m = (root.getRight() == null) ? 0 : root.getRight().getCount();
    if (m + 1 == k) return root;
    if (k > m) return getKthLargestHelper(root.getLeft(), k - m - 1);
    else return getKthLargestHelper(root.getRight(), k);
  }
}
