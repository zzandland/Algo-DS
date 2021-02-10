/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution 
{
public:
    Node* copyRandomList(Node* head) 
    {
        Node *run = head;
        while (run) {
            Node *nxt = run->next;
            run->next = new Node(run->val);
            run->next->next = nxt;
            run = nxt;
        }
        run = head;
        while (run) {
            if (run->random) run->next->random = run->random->next;
            run = run->next->next;
        }
        run = head;
        Node *cpyhead = new Node(0);
        Node *cpyrun = cpyhead;
        while (run) {
            cpyrun->next = run->next;
            run->next = run->next->next;
            cpyrun = cpyrun->next;
            run = run->next;
        }
        return cpyhead->next;
    }
};