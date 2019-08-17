#include <queue>

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Compare {
public:
  bool operator() (ListNode* a, ListNode* b) {
    if (a == NULL) return false;
    if (b == NULL) return true;
    return a->val > b->val;
  }
};

class Solution {
public:
  ListNode* mergeKLists(vector<ListNode*>& lists) {
    priority_queue<ListNode*,vector<ListNode*>,Compare> min_node_heap;
    ListNode *res, *res_head, *n, *tmp;
    res = res_head = n = tmp = NULL;
    for (ListNode* list : lists) {
      if (list != NULL)
        min_node_heap.push(list);
    }
    
    while (!min_node_heap.empty()) {
      n = min_node_heap.top();
      min_node_heap.pop();
      if (n != NULL) {
        tmp = n;
        n = n->next;
        min_node_heap.push(n);
        if (res != NULL)
          res->next = tmp;
        res = tmp;
        if (res_head == NULL)
          res_head = res;
      }
    }
    
    return res_head;
  }
};