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
      ArrayList<Integer> output = new ArrayList<Integer>();
      Stack<TreeNode> stack = new Stack<TreeNode>();
      TreeNode node = root;
      while (node != null) {
        output.add(node.val);
        if (node.right != null) {
          stack.push(node.right);
        }
        node = node.left;
        if (node == null && stack.size() != 0) {
          node = stack.pop();
        }
      }
      return output;
    }
}