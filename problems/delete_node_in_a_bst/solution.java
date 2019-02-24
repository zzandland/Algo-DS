/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;zx
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
  public TreeNode deleteNode(TreeNode root, int key) {
    if (root == null) return root;
    if (root.val == key) {
      // if target has both child
      if (root.left != null && root.right != null) {
        TreeNode next = findSuccessor(root.right);
        root.val = next.val;
        root.right = deleteNode(root.right, next.val);
        return root;
      }
      // if target has left branch
      if (root.left != null) {
        return root.left;
      }  
      // if target has right branch
      if (root.right != null) {
        return root.right;
      }
      // if node is a leaf
      return null;
    }
    if (root.val > key) root.left = deleteNode(root.left, key);
    else root.right = deleteNode(root.right, key);
    
    return root;
  }  
  
  private TreeNode findSuccessor(TreeNode root) {
    if (root.left != null) return findSuccessor(root.left);
    return root;
  }
}