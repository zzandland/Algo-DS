/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* genListNode(int val) {
    struct ListNode* out = (struct ListNode*)malloc(sizeof(struct ListNode));
    out->val = val;
    out->next = NULL;
    return out;
}

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode *head, *merged;
    head = merged = NULL;
    int lift, sum;
    lift = sum = 0;
    while (l1 != NULL || l2 != NULL) {
        sum = lift;
        if (l1 != NULL) {
            sum += l1->val;
            l1 = l1->next;
        }
        if (l2 != NULL) {
            sum += l2->val;
            l2 = l2->next;
        }
        if (sum > 9) {
            lift = 1;
            sum -= 10;
        } else {
            lift = 0;
        }
        struct ListNode* tmp = genListNode(sum);
        if (merged != NULL)
            merged->next = tmp;
        merged = tmp;
        if (head == NULL)
            head = merged;
    }
    if (lift == 1) {
        struct ListNode* tmp = genListNode(1);
        merged->next = tmp;
    }
    return head;
}