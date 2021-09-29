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
    vector<ListNode*> splitListToParts(ListNode* head, int k) {
        vector<ListNode*> res(k, nullptr);
        size_t len = 0;
        ListNode *cur = head, *prev = head;
        while (cur) {
            ++len;
            cur = cur->next;
        }
        int each = len / k, left = len % k;
        cur = head;
        for (int i = 0; i < k; ++i) {
            size_t t = each + (int)(left-- > 0);
            if (t == 0) continue;
            for (int j = 0; j < t - 1; ++j) {
                cur = cur->next;
            }
            ListNode *tmp = prev;
            res[i] = tmp;
            prev = cur->next;
            cur->next = nullptr;
            cur = prev;
        }
        return res;
    }
};