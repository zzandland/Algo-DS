/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var mergeTwoLists = function(l1, l2) {
    const dmy = new ListNode(0);
    let run = dmy;
    while (l1 && l2) {
        let tmp;
        if (l1.val < l2.val) {
            tmp = l1;
            l1 = l1.next;
        } else {
            tmp = l2;
            l2 = l2.next;
        }
        run.next = tmp;
        run = tmp;
    }
    if (l1) run.next = l1;
    if (l2) run.next = l2;
    return dmy.next;
};