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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode *pre = head;
        while (--n >= 0) pre = pre->next;
        ListNode *cur = head, *prev = nullptr;
        while (pre) {
            prev = cur;
            cur = cur->next;
            pre = pre->next;
        }
        if (!prev) return head->next;
        prev->next = cur->next;
        return head;
    }
};