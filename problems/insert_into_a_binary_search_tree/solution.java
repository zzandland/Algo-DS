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
  public TreeNode insertIntoBST(TreeNode root, int val) {
    TreeNode target = new TreeNode(val);
    if (root == null) root = target;
    else {
      TreeNode node = root;
      boolean isFound = false;
      while (!isFound) {
        if (node.val > val) {
          if (node.left != null) node = node.left;
          else {
            node.left = target;
            isFound = true;
          }
        } else {
          if (node.right != null) node = node.right;
          else {
            node.right = target;
            isFound = true;
          }
        }
      }  
    } 
    return root;
  }
}