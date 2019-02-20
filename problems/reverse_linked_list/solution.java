/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
  public ListNode reverseList(ListNode head) {
    if (head == null) return null;
    if (head.next == null) return head;
    ListNode node, next;
    node = next = reverseList(head.next);
    while (next.next != null) next = next.next;
    next.next = head;
    head.next = null;
    return node;
  }
}