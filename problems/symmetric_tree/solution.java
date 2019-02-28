import java.util.ArrayList;

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
  public boolean isSymmetric(TreeNode root) throws IllegalStateException {
    if (root == null) return true;
    MyQueue<TreeNode> q = new MyQueue<TreeNode>();
    q.enqueue(root.left);
    q.enqueue(root.right);
    while (!q.isEmpty()) {
      TreeNode left = q.dequeue();
      TreeNode right = q.dequeue();
      if (left == null && right == null) continue;
      if (left == null || right == null) return false;
      if (left.val != right.val) return false;
      q.enqueue(left.left);
      q.enqueue(right.right);
      q.enqueue(left.right);
      q.enqueue(right.left);
    }    
    return true;
  }
}

class MyQueue<T> {
  private static class QueueNode<T> {
    T data;
    QueueNode<T> next;
    public QueueNode(T data) { this.data = data; }
  }
  
  private QueueNode<T> head = null;
  private QueueNode<T> tail = null;
  int size = 0;
  
  public void enqueue(T data) {
    QueueNode<T> node = new QueueNode<T>(data);
    if (tail != null) tail.next = node;
    tail = node;
    if (head == null) head = tail;
    size++;
  }
  
  public T dequeue() throws IllegalStateException {
    if (isEmpty()) throw new IllegalStateException("The queue is empty");
    QueueNode<T> temp = head;
    head = head.next;
    if (head == null) tail = null;
    size--;
    return temp.data;
  }
  
  public T peek() throws IllegalStateException { 
    if (isEmpty()) throw new IllegalStateException("The queue is empty");
    return head.data; 
  }
  
  public boolean isEmpty() { return head == null; }
}