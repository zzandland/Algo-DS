/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function(head) {
  if (!head) {
    return null;
  }
  var curr, p;
  curr = head;
  while (head.next) {
    p = head.next;
    head.next = p.next;
    p.next = curr;
    curr = p;
  }
  return curr;
};