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
    let f, s;
    f = s = head;
    while (--n >= 0) f = f.next;
    
    const dmy = new ListNode(0);
    dmy.next = head;
    let prev = dmy;
    while (f) {
        prev = s;
        s = s.next;
        f = f.next;
    }
    
    prev.next = prev.next.next;
    return dmy.next;
};