/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
  private static class Stack {
    private static class StackNode {
      ListNode data;
      StackNode next;
      
      public StackNode(ListNode data) {
        this.data = data;
      }
    }
    
    private StackNode top;
    
    public void push(ListNode node) {
      StackNode newTop = new StackNode(node);
      if (top != null) newTop.next = top;
      top = newTop;
    }
    
    public ListNode pop() throws Exception {
      if (isEmpty()) throw new Exception("Stack is empty");
      StackNode prevTop = top;
      top = top.next;
      return prevTop.data;
    }
    
    public ListNode peek() {
      return top.data;
    }
    
    public boolean isEmpty() {
      return top == null;
    }
  }
  
  public boolean isPalindrome(ListNode head) {
    try {
      Stack s = new Stack();
      ListNode p = head;
      
      while (p != null) {
        s.push(p);
        p = p.next;
      }
      
      p = head;
      while (p != null) {
        if (s.pop().val != p.val) return false;
        p = p.next;
      }
      
      return true;
    } catch (Exception e) {
      return false;
    }    
  }
}