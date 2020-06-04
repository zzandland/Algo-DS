/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} k
 * @return {ListNode}
 */
var rotateRight = function(head, k) {
    if (!head) return null;
    let len = 0, run = head;
    while (run.next) {
        len += 1;
        run = run.next;
    }
    const last = run
    run = head;
    k %= (len+1);
    if (k === 0) return head;
    for (let i = 0; i < len-k; i++) {
        run = run.next;
    }
    const res = run.next;
    last.next = head;
    run.next = null;
    return res
};