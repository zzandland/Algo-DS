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
var detectCycle = function(head) {
  if (!head || !head.next) {
    return null;
  }
  var fast, slow;
  var isCircular = false;
  slow = fast = head;
  while (fast && fast.next && !isCircular) {
    fast = fast.next.next;
    slow = slow.next;
    if (fast === slow) {
      slow = head;
      isCircular = true;
    }
  }
  if (!isCircular) {
    return null;
  } else {
    while (fast !== slow) {
      fast = fast.next;
      slow = slow.next;
    }
    return fast;
  }
};