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
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode *run = head;
        int freq[201];
        for (int i = 0; i < 201; ++i) freq[i] = 0;
        while (run) {
            freq[run->val + 100]++;
            run = run->next;
        }
        
        ListNode *dummy = new ListNode();
        dummy->next = head;
        ListNode *prev = dummy;
        run = head;
        while (run) {
            if (freq[run->val + 100] != 1) {
                prev->next = run->next;
            } else {
                prev = run;
            }
            run = run->next;
        }
        return dummy->next;
    }
};