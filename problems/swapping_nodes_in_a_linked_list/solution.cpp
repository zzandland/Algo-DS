/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* swapNodes(ListNode* head, int k) {
        ListNode* a, *b, *c;
        a = b = c = head;
        while (c) {
            if (k > 1) a = a->next;
            if (k <= 0) b = b->next;
            c = c->next;
            k--;
        }
        int tmp = a->val;
        a->val = b->val;
        b->val = tmp;
        return head;
    }
};