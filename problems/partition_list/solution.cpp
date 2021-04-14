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
    ListNode* partition(ListNode* head, int x) {
        ListNode *lh = new ListNode(), *rh = new ListNode();
        ListNode *l = lh, *r = rh, *cur = head;
        while (cur) {
            ListNode* tmp = cur->next;
            if (cur->val < x) {
                l->next = cur;
                l = cur;
            } else {
                r->next = cur;
                r = cur;
            }
            cur = tmp;
        }
        l->next = rh->next;
        r->next = nullptr;
        return lh->next;
    }
};