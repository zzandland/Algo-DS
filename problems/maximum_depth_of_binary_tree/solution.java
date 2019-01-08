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
  public int maxDepth(TreeNode root) {
    int output = 0;
    if (root == null) return output;
    return traversal(root, 1, output);
  }
  
  public int traversal(TreeNode node, int depth, int max) {
    max = Math.max(depth, max);
    if (node.left != null) {
      max = traversal(node.left, ++depth, max);
      depth--;
    }
    if (node.right != null) {
      max = traversal(node.right, ++depth, max);  
      depth--;
    }
    return max;
  }
}