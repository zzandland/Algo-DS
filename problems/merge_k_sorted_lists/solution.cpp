#include <climits>
#include <iostream>

/*
 * @lc app=leetcode id=23 lang=cpp
 *
 * [23] Merge k Sorted Lists
 *
 * https://leetcode.com/problems/merge-k-sorted-lists/description/
 *
 * algorithms
 * Hard (33.81%)
 * Total Accepted:    369.9K
 * Total Submissions: 1.1M
 * Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
 *
 * Merge k sorted linked lists and return it as one sorted list. Analyze and
 * describe its complexity.
 *
 * Example:
 *
 *
 * Input:
 * [
 * 1->4->5,
 * 1->3->4,
 * 2->6
 * ]
 * Output: 1->1->2->3->4->4->5->6
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
  ListNode* mergeKLists(std::vector<ListNode*>& lists) {
    if (lists.size() == 0) return nullptr;
    ListNode* output = lists[0];
    for (size_t i = 1; i < lists.size(); ++i)
      output = MergeList(output, lists[i]);
    return output;
  }

 private:
  ListNode* MergeList(ListNode*& output, ListNode*& n) {
    ListNode* merged = nullptr;
    ListNode* head = nullptr;
    while (output != nullptr && n != nullptr) {
      ListNode* temp = nullptr;
      if (output->val < n->val) {
        if (head == nullptr) {
          head = merged = output;
          continue;
        }
        temp = output;
        output = output->next;
        merged->next = temp;
      } else {
        if (head == nullptr) {
          head = merged = n;
          continue;
        }
        temp = n;
        n = n->next;
        merged->next = temp;
      }
      merged = merged->next;
    }
    if (merged == nullptr) {
      if (output == nullptr && n == nullptr)
        return nullptr;
      else if (output == nullptr)
        return n;
      else if (n == nullptr)
        return output;
    }
    if (output == nullptr)
      merged->next = n;
    else
      merged->next = output;
    return head;
  }
};
