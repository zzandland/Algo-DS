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
        auto comp = [&](ListNode *a, ListNode *b) -> bool { return a->val > b->val; };
        priority_queue<ListNode*, vector<ListNode*>, decltype(comp)> pq(comp);
        
        for (auto l : lists) if (l) pq.emplace(l);
        ListNode *dum = new ListNode();
        ListNode *tmp, *run = dum;
        while (!pq.empty()) {
            tmp = pq.top();
            pq.pop();
            run->next = tmp;
            tmp = tmp->next;
            run = run->next;
            if (tmp) pq.emplace(tmp);
        }
        run->next = nullptr;
        return dum->next;
    }
};