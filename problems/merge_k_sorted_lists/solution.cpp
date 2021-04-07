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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        auto cmp = [&](const ListNode* a, const ListNode* b) {
            return a->val > b->val;
        };
        priority_queue<ListNode*, vector<ListNode*>, decltype(cmp)>pq(cmp);
        for (ListNode* a : lists) if (a) pq.push(a);
        ListNode* dmy = new ListNode(0);
        ListNode* run = dmy;
        while (!pq.empty()) {
            ListNode* tmp = pq.top();
            pq.pop();
            run->next = tmp;
            run = run->next;
            tmp = tmp->next;
            if (tmp) pq.push(tmp);
        }
        return dmy->next;
    }
};