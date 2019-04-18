/*
 * @lc app=leetcode id=25 lang=cpp
 *
 * [25] Reverse Nodes in k-Group
 *
 * https://leetcode.com/problems/reverse-nodes-in-k-group/description/
 *
 * algorithms
 * Hard (35.94%)
 * Total Accepted:    177.1K
 * Total Submissions: 492.7K
 * Testcase Example:  '[1,2,3,4,5]\n2'
 *
 * Given a linked list, reverse the nodes of a linked list k at a time and
 * return its modified list.
 *
 * k is a positive integer and is less than or equal to the length of the
 * linked list. If the number of nodes is not a multiple of k then left-out
 * nodes in the end should remain as it is.
 *
 *
 *
 *
 * Example:
 *
 * Given this linked list: 1->2->3->4->5
 *
 * For k = 2, you should return: 2->1->4->3->5
 *
 * For k = 3, you should return: 3->2->1->4->5
 *
 * Note:
 *
 *
 * Only constant extra memory is allowed.
 * You may not alter the values in the list's nodes, only nodes itself may be
 * changed.
 *
 *
 */
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
  ListNode* reverseKGroup(ListNode* head, int k) {
    if (head == nullptr) return head;
    ListNode *tail, *prev_tail, *prev, *curr, *next, *output;
    int cnt = 0;
    curr = head;
    tail = prev_tail = next = output = nullptr;
    while (curr != nullptr) {
      prev = nullptr;
      prev_tail = tail;
      tail = curr;
      if (remainingLessThanK(curr, k)) {
        if (prev_tail != nullptr) prev_tail->next = tail;
        return output == nullptr ? curr : output;
      }
      while (cnt < k && curr != nullptr) {
        next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
        ++cnt;
      }
      if (prev_tail != nullptr) prev_tail->next = prev;
      if (output == nullptr) output = prev;
      cnt = 0;
    }
    return output;
  }

  bool remainingLessThanK(ListNode* head, int k) {
    int cnt = 1;
    while (head != nullptr && cnt <= k) {
      head = head->next;
      ++cnt;
    }
    return cnt <= k;
  }
};
