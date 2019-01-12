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
  public boolean isBalanced(TreeNode root) {
    if (root == null) return true;
    boolean left = true, right = true;
    if (root.left != null) left = isBalanced(root.left);
    if (root.right != null) right = isBalanced(root.right);
    return Math.abs(getHeight(root.left) - getHeight(root.right)) <= 1 && left && right;
  }
  
  public int getHeight(TreeNode root) {
    if (root == null) return 0;
    int left = 1, right = 1;
    if (root.left != null) left = 1 + getHeight(root.left);
    if (root.right != null) right = 1 + getHeight(root.right);
    return Math.max(left, right); 
  }
}