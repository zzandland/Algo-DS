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
var reverse = function(head) {
  var curr = head;
  var p;
  while (head.next) {
    p = head.next;
    head.next = p.next;
    p.next = curr;
    curr = p;
  }
  return curr;
}

var isPalindrome = function(head) {
  if (!head || !head.next) {
    return true;
  } else if (!head.next.next) {
    return head.val === head.next.val;
  }
  var runner, mid;
  runner = mid = head;
  while (runner && runner.next && runner.next.next) {
    runner = runner.next.next;
    mid = mid.next;
  }
  mid.next = reverse(mid.next);
  var check = mid.next;
  runner = head;
  while (check) {
    if (runner.val !== check.val) {
      return false;
    }
    check = check.next;
    runner = runner.next;
  }
  mid.next = reverse(mid.next);
  return true;
};