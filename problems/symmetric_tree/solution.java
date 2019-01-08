/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class MyQueue {
  private static class QueueNode<TreeNode> {
    private TreeNode data;
    private QueueNode<TreeNode> next;
    public QueueNode(TreeNode data) {
      this.data = data;
    }
  }  
  
  private QueueNode<TreeNode> first;
  private QueueNode<TreeNode> last;
  private int size = 0;

  public void enqueue(TreeNode node) {
    size++;
    QueueNode<TreeNode> t = new QueueNode<TreeNode>(node);
    if (last != null) last.next = t;
    last = t;
    if (first == null) first = last;
  }

  public TreeNode dequeue() {
    size--;
    TreeNode item = first.data;
    first = first.next;
    if (first == null) last = null;
    return item;
  }
  
  public boolean isEmpty() {
    return first == null;
  }
  
  public int getSize() {
    return size;
  }
}

class Solution {
  public boolean isPalindrome(ArrayList<TreeNode> list) {
    for (int i = 0; i < list.size() / 2; i++) {
      if (list.get(i) == null && list.get(list.size() - 1 - i) == null) continue;
      if ((list.get(i) == null || list.get(list.size() - 1 - i) == null)
        || list.get(i).val != list.get(list.size() - 1 - i).val) return false;
    }
    return true;
  }

  public boolean isSymmetric(TreeNode root) {
    if (root == null) return true;
    MyQueue queue = new MyQueue();
    ArrayList<TreeNode> list;
    TreeNode item;
    queue.enqueue(root);
    while (!queue.isEmpty()) {
      list = new ArrayList<TreeNode>();
      int size = queue.getSize();
      for (int i = 0; i < size; i++) {
        item = queue.dequeue();
        list.add(item);
        if (item != null) queue.enqueue(item.left);
        if (item != null) queue.enqueue(item.right);
      }
      if (!isPalindrome(list)) {
        return false;
      } 
    }
    return true;
  }
}