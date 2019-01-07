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
  public List<Integer> preorderTraversal(TreeNode root) {
    List<Integer> output = new ArrayList<Integer>();
    if (root == null) return output;
    preorderTraversalRecurse(root, output);
    return output;
  }
  
  public void preorderTraversalRecurse(TreeNode node, List<Integer> list) {
    list.add(node.val);
    if (node.left != null) preorderTraversalRecurse(node.left, list);
    if (node.right != null) preorderTraversalRecurse(node.right, list);
  }
}