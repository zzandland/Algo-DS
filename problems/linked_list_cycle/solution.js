/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {boolean}
 */
var hasCycle = function(head) {
  if (!head || !head.next) {
    return false;
  }
  var fast = head.next.next;
  var slow = head.next;
  while (fast && fast.next) {
    if (fast.val === slow.val) {
      return true;
    }
    fast = fast.next.next;
    slow = slow.next;
  }
  return false;
};