import java.util.ArrayList;
import java.util.Queue;

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
  public List<List<Integer>> levelOrder(TreeNode root) {
    List<List<Integer>> output = new ArrayList<List<Integer>>();
    if (root == null) return output;
    Queue<TreeNode> q = new LinkedList<TreeNode>();
    
    q.add(root);
    while (!q.isEmpty()) {
      int size = q.size();
      List<Integer> sub = new ArrayList<Integer>();
      for (int i = 0; i < size; i++) {
        TreeNode node = q.poll();
        sub.add(node.val);
        if (node.left != null) q.add(node.left);
        if (node.right != null) q.add(node.right);
      }
      output.add(sub);
    }
    return output;
  }
}