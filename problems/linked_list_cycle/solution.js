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
  var nodeSeen = new Set();
  while (head) {
    if (nodeSeen.has(head)) {
      return true;
    } else {
      nodeSeen.add(head);
      head = head.next;
    }
  }
  return false;
};