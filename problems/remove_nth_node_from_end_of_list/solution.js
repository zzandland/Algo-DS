/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function(head, n) {
  if (!head || !head.next) {
    return null;
  }
  var runner = head;
  var target = head;
  while (n > 0 && runner) {
    runner = runner.next;
    n--;
  }
  while (runner && runner.next) {
    runner = runner.next;
    target = target.next;
  }
  if (!runner) {
    head = head.next;
  } else {
    target.next = target.next.next;
  }
  return head;
};