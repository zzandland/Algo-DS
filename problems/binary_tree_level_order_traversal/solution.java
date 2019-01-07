/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

class TreeNodeQueue {
  private static class QueueNode {
    private TreeNode data;
    private QueueNode next;
    public QueueNode(TreeNode node) {
      this.data = node;
    }
  }
  private QueueNode first;
  private QueueNode last;
  private int size = 0;
  
  public void enqueue(TreeNode node) {
    size++;
    QueueNode t = new QueueNode(node);
    if (last != null) last.next = t;
    last = t;
    if (first == null) first = last;
  }
  
  public TreeNode dequeue() {
    size--;
    TreeNode n = first.data;
    first = first.next;
    if (first == null) last = null; 
    return n;
  }
  
  public boolean isEmpty() {
    return first == null;
  }
  
  public int size() {
    return size;
  }
}

class Solution {
  public List<List<Integer>> levelOrder(TreeNode root) {
    List<List<Integer>> output = new ArrayList<List<Integer>>();
    if (root == null) return output;
    TreeNodeQueue queue = new TreeNodeQueue();
    queue.enqueue(root);
    while (!queue.isEmpty()) {
      List<Integer> level = new ArrayList<Integer>();
      int size = queue.size();
      for (int i = 0; i < size; i++) {
        TreeNode node = queue.dequeue();
        level.add(node.val);
        if (node.left != null) queue.enqueue(node.left);
        if (node.right != null) queue.enqueue(node.right);
      }
      output.add(level);
    }
    return output;
  }
}