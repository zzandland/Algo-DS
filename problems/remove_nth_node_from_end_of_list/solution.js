/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function(head, n) {
    let a = head, b = head, i = 0;
    while (a) {
        a = a.next;
        if (i === n+1) b = b.next;
        else i++;
    }
    if (i == n) return head.next
    b.next = b.next.next;
    return head;
};