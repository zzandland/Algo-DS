/*
 * @lc app=leetcode id=61 lang=cpp
 *
 * [61] Rotate List
 *
 * https://leetcode.com/problems/rotate-list/description/
 *
 * algorithms
 * Medium (28.86%)
 * Likes:    888
 * Dislikes: 951
 * Total Accepted:    239.7K
 * Total Submissions: 830.4K
 * Testcase Example:  '[1,2,3,4,5]\n2'
 *
 * Given a linked list, rotate the list to the right by k places, where k is
 * non-negative.
 * 
 * Example 1:
 * 
 * 
 * Input: 1->2->3->4->5->NULL, k = 2
 * Output: 4->5->1->2->3->NULL
 * Explanation:
 * rotate 1 steps to the right: 5->1->2->3->4->NULL
 * rotate 2 steps to the right: 4->5->1->2->3->NULL
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: 0->1->2->NULL, k = 4
 * Output: 2->0->1->NULL
 * Explanation:
 * rotate 1 steps to the right: 2->0->1->NULL
 * rotate 2 steps to the right: 1->2->0->NULL
 * rotate 3 steps to the right: 0->1->2->NULL
 * rotate 4 steps to the right: 2->0->1->NULL
 * 
 */

// @lc code=start
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
// @lc code=end
