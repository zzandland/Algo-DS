/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
  public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
    ListNode head, node;
    head = node = null;
    while (l1 != null && l2 != null) {
      ListNode smaller = (l1.val > l2.val) ? l2 : l1;
      if (head == null) {
        head = node = smaller;
      }  else {
        node.next = smaller;
        node = node.next;
      } 
      if (smaller == l2) l2 = l2.next;
      else l1 = l1.next;
    }
    if (head == null) return (l1 != null) ? l1 : l2;
    if (l1 != null) node.next = l1;
    else if (l2 != null) node.next = l2;
    return head;
  }
}