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
      ArrayList<Integer> output = new ArrayList<Integer>();
      Stack<TreeNode> stack = new Stack<TreeNode>();
      TreeNode node = root;
      while (node != null || stack.size() != 0) {
        while (node != null) {
          stack.push(node);
          node = node.left;
        }        
        node = stack.pop();
        output.add(node.val);
        node = node.right;
      }
      return output;
    }
}