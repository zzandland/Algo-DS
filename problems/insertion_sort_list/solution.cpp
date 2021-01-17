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
    ListNode* insertionSortList(ListNode* head) {
        ListNode *res = new ListNode(INT_MIN), *run = head;
        while (run) {
            ListNode *tmp = res;
            while (tmp->next && tmp->next->val < run->val) {
                tmp = tmp->next;
            }
            ListNode *next = run->next;
            run->next = tmp->next;
            tmp->next = run;
            run = next;
        }
        return res->next;
    }
};