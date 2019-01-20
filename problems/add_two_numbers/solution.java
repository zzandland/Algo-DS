/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
  public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
    int lift = 0, sum = 0;;
    ListNode output = null, node = null;
    while (l1 != null || l2 != null || sum == 1) {
      if (l1 != null) {
        sum += l1.val; 
        l1 = l1.next;
      }
      if (l2 != null) {
        sum += l2.val; 
        l2 = l2.next;
      }
      if (sum > 9) {
        sum -= 10;
        lift = 1;
      } else {
        lift = 0;
      }
      if (output == null) {
        node = new ListNode(sum);
        output = node;
      } else {
        node.next = new ListNode(sum);
        node = node.next;
      }
      sum = lift;
    }
    return output;
  }
}