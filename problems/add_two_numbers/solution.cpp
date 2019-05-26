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
  ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
    bool roof = false;
    ListNode *r1 = l1, *r2 = l2, *r = nullptr, *head = nullptr;
    while (r1 != nullptr || r2 != nullptr) {
      int val1 = 0, val2 = 0, up = roof ? 1 : 0;
      if (r1 != nullptr) {
        val1 = r1->val;
        r1 = r1->next;
      }
      if (r2 != nullptr) {
        val2 = r2->val;
        r2 = r2->next;
      }
      int total = val1 + val2 + up;
      if (total < 10)
        roof = false;
      else {
        roof = true;
        total -= 10;
      }
      ListNode* tmp = new ListNode(total);
      if (r != nullptr) {
        r->next = tmp;
      }
      r = tmp;
      if (head == nullptr) head = r;
    }
    if (roof) r->next = new ListNode(1);
    return head;
  }
};