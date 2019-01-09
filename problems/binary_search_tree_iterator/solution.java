import java.util.Stack;
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class BSTIterator {
  private Stack<TreeNode> stack = new Stack<TreeNode>();
    
  public BSTIterator(TreeNode root) {
    while (root != null) {
      stack.push(root);
      root = root.left;
    }  
  }
  
  /** @return the next smallest number */
  public int next() {
    TreeNode item = stack.pop();
    if (item.right != null) {
      TreeNode right = item.right;
      while (right != null) {
        stack.push(right);
        right = right.left;
      }
    }
    return item.val;
  }

  /** @return whether we have a next smallest number */
  public boolean hasNext() {
    return !stack.empty();
  }
}

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator obj = new BSTIterator(root);
 * int param_1 = obj.next();
 * boolean param_2 = obj.hasNext();
 */