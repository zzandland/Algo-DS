/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} headA
 * @param {ListNode} headB
 * @return {ListNode}
 */
var getIntersectionNode = function(headA, headB) {
  if (!headA || !headB) { 
    return null;
  }
  var pA = headA;
  var pB = headB;
  var counter = 0;
  while (pA !== pB && counter < 3) {
    pA = pA.next;
    pB = pB.next;
    if (!pA) {
      pA = headB;
      counter++;
    }
    if (!pB) {
      pB = headA;
      counter++;
    }
  }
  return pA === pB ? pA : null
};