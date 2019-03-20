/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;

    Node() {}

    Node(int _val, Node* _left, Node* _right) {
        val = _val;
        left = _left;
        right = _right;
    }
};
*/
class Solution {
public:
  Node* treeToDoublyList(Node* root) {
    if (root == nullptr) return nullptr;
    stack<Node*> s;
    Node* n;
    Node *prev, *head, *tail;
    prev = head = tail = nullptr;
    n = root;
    
    do {
      if (n == nullptr) {
        n = s.top();
        s.pop();
      } else {
        while (n->left != nullptr) {
          s.push(n);
          n = n->left;
        }
      }
      
      if (head == nullptr) {
        head = prev = n;  
      } else {
        prev->right = n;
        n->left = prev;
        prev = n;
      }  
      tail = n;
      n = n->right;
    } while (n != nullptr || !s.empty());
    
    head->left = tail;
    tail->right = head;
    
    return head;
  }
};