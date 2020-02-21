// *
// Definition for singly-linked list.
// struct ListNode {
    // int val;
    // ListNode *next;
    // ListNode(int x) : val(x), next(nullptr) {}
// };
#include <iostream>
using namespace std;

class Solution {
public:
  ListNode* rotateRight(ListNode* head, int k) {
    if (!k || !head) return head;
    ListNode *tail, *newTail, *newHead, *runner;
    tail = newTail = newHead = runner = nullptr;
    runner = head;
    int len = 0;
    while (runner) {
      len += 1;
      tail = runner;
      runner = runner->next;
    }
    int iterLen = len - (k % len);
    if (iterLen == len) return head;
    runner = head;
    for (int i = 0; i < iterLen; ++i) {
      newTail = runner;
      runner = runner->next;
    }
    newHead = newTail->next;
    newTail->next = nullptr;
    tail->next = head;
    return newHead;
  }
};