/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
    if (head->next == NULL)
        return NULL;
    struct ListNode *front, *back;
    back = front = head;
    for (int i = 0; i < n; ++i)
        front = front->next;
    if (front == head->next) {
        while (front->next != NULL) {
            front = front->next;
            back = back->next;
        }
        free(back->next);
        back->next = NULL;
    } else {
        while (front != NULL) {
            front = front->next;
            back = back->next;
        }
        struct ListNode* tmp = back->next;
        back->val = tmp->val;
        back->next = tmp->next;
        free(tmp);
    }
    return head;
}