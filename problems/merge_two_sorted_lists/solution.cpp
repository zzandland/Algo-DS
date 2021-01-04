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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode* tmp = new ListNode();
        ListNode* run = tmp;
        while (l1 && l2) {
            if (l1->val < l2->val) {
                run->next = l1;
                l1 = l1->next;
            } else {
                run->next = l2;
                l2 = l2->next;
            }
            run = run->next;
        }
        if (l1) run->next = l1;
        if (l2) run->next = l2;
        return tmp->next;
    }
};