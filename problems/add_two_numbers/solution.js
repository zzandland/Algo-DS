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
  var output = new ListNode(0);
  var sumNodes = function(first, second, sum) {
    if (first === null) {
      first = new ListNode(0);
    }
    if (second === null) {
      second = new ListNode(0);
    }
    var value = first.val + second.val;
    sum.val += value;
    if (first.next === null && second.next === null && sum.val < 10) {
      return;
    }
    if (sum.val >= 10) {
      sum.val -= 10;
      sum.next = new ListNode(1);
    } else {
      sum.next = new ListNode(0);
    }
    sumNodes(first.next, second.next, sum.next);
  }
  sumNodes(l1, l2, output);
  return output;
};