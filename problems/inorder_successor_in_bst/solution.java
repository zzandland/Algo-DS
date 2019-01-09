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
  public TreeNode inorderSuccessor(TreeNode root, TreeNode p) {
    ArrayList<TreeNode> list = new ArrayList<TreeNode>();
    inorder(root, list);
    for (int i = 0; i < list.size() - 1; i++) {
      if (list.get(i).val == p.val) return list.get(i + 1);
    }
    return null;
  }
  
  public void inorder(TreeNode node, ArrayList<TreeNode> list) {
    if (node.left != null) inorder(node.left, list);
    list.add(node);
    if (node.right != null) inorder(node.right, list);
  }
}