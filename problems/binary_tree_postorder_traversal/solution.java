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
  public List<Integer> postorderTraversal(TreeNode root) {
    List<Integer> output = new ArrayList<Integer>();
    if (root == null) return output;
    this.postorderTraversalRecurse(root, output);
    return output;
  }
  

  private void postorderTraversalRecurse(TreeNode node, List<Integer> list) {
    if (node.left != null) postorderTraversalRecurse(node.left, list);
    if (node.right != null) postorderTraversalRecurse(node.right, list);
    list.add(node.val);
  }
}