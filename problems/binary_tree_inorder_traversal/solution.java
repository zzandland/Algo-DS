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
  public List<Integer> inorderTraversal(TreeNode root) {
    List<Integer> output = new ArrayList<Integer>();
    if (root == null) return output;
    this.inorderTraversalRecurse(root, output);
    return output;
  }
  
  private void inorderTraversalRecurse(TreeNode node, List<Integer> list) {
    if (node.left != null) inorderTraversalRecurse(node.left, list);
    list.add(node.val);
    if (node.right != null) inorderTraversalRecurse(node.right, list);
  }
}