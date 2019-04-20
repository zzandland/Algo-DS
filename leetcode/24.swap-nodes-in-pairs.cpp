/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
 public:
  ListNode* swapPairs(ListNode* head) {
    if (head == nullptr || head->next == nullptr) return head;
    ListNode *n1, *n2, *node, *prev;
    n1 = n2 = prev = nullptr;
    node = head;
    bool first = true;
    while (node != nullptr && node->next != nullptr) {
      n1 = node;
      n2 = node->next;
      node = node->next->next;
      if (prev != nullptr) prev->next = n2;
      if (first) {
        head = n2;
        first = false;
      }
      n2->next = n1;
      prev = n1;
    }
    n1->next = node;
    return head;
  }
};
