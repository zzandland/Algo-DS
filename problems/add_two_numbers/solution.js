/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
  var head, node, sum;
  var lifted = 0;
  while (!(l1 === null && l2 === null) || lifted === 1) {
    sum = lifted;
    if (l1 !== null) {
      sum += l1.val;  
      l1 = l1.next;
    }
    if (l2 !== null) {
      sum += l2.val;  
      l2 = l2.next;
    } 
    if (sum > 9) {
      sum -= 10;
      lifted = 1;
    } else {
      lifted = 0;
    }
    if (node === undefined) {
      node = new ListNode(sum);
      head = node;
    } else {
      node.next = new ListNode(sum);
      node = node.next;
    }
  }
  return head;
};