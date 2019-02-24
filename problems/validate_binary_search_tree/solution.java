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
  public boolean isValidBST(TreeNode root) {
    if (root == null) return true;
    return helper(root, Long.MIN_VALUE, Long.MAX_VALUE);
  }
  
  public boolean helper(TreeNode root, long minLimit, long maxLimit) {
    if (root.left != null) {
      if (!
        (root.val > root.left.val 
          && minLimit < root.left.val 
          && helper(root.left, minLimit, root.val)
        )
      ) return false;      
    }
    if (root.right != null) {
      if (!
        (root.val < root.right.val 
          && maxLimit > root.right.val 
          && helper(root.right, root.val, maxLimit)
        ) 
      ) return false;
    }
    return true;
  }
}