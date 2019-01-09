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
  public boolean isValidBST(TreeNode root) {
    if (root == null) return true;
    boolean output = true;
    if (root.left != null) {
      output = root.val > root.left.val 
        && helper(root.left, Long.MIN_VALUE, root.val)
        && output;
    }
    if (root.right != null) {
      output = root.val < root.right.val
        && helper(root.right, root.val, Long.MAX_VALUE)
        && output;
    }
    return output;
  }
  
  public boolean helper(TreeNode node, long low, long high) {
    if (node.left == null && node.right == null) return true;
    boolean left = true, right = true;
    if (node.left != null) {
      left = node.val > node.left.val 
        && node.left.val > low
        && helper(node.left, low, node.val); 
    }
    if (node.right != null) {
      right = node.val < node.right.val 
        && node.right.val < high 
        && helper(node.right, node.val, high);
    } 
    return left && right;
  }
}