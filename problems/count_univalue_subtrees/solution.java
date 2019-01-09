/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
  public int countUnivalSubtrees(TreeNode root) {
    if (root == null) return 0;
    ArrayList<Integer> list = new ArrayList<Integer>();
    recurse(root, list);
    return list.size();
  }
  
  public boolean recurse(TreeNode node, ArrayList<Integer> list) {
    if (node.left == null && node.right == null) {
      list.add(1);
      return true;
    }
    boolean left = true;
    boolean right = true;
    if (node.left != null) left = recurse(node.left, list);
    if (node.right != null) right = recurse(node.right, list);
    if (!left || !right) {
      return false;
    } else {
      if (
        (node.left != null && node.left.val != node.val)
        || (node.right != null && node.right.val != node.val)
      ) {
        return false;
      }  
      list.add(1);
      return true;
    }
  }
}
