typedef struct Node {
  int val;
  struct Node* next;
} Node;

Node* nodeCreate(int x) {
  Node* n = (Node*)malloc(sizeof(Node));
  n->val = x;
  n->next = NULL;
  return n;
}

void nodeFree(Node* obj) {
  free(obj->next);
  free(obj);
}

typedef struct {
  Node* top;
} Stack;

Stack* stackCreate() {
  Stack* s = (Stack*)malloc(sizeof(Stack));
  s->top = NULL;
  return s;
}

void stackPush(Stack* obj, int x) {
  Node* n = nodeCreate(x);
  if (obj->top != NULL) {
    n->next = obj->top;
  }
  obj->top = n;
}

void stackPop(Stack* obj) {
  Node* tmp = obj->top;
  obj->top = obj->top->next;
  free(tmp);
}

int stackTop(Stack* obj) {
  return obj->top->val;
}

int stackEmpty(Stack* obj) {
  return obj->top == NULL;
}

void stackFree(Stack* obj) {
  free(obj->top);  
  free(obj);
}

typedef struct {
  Stack* s;
  Stack* m;
} MinStack;

/** initialize your data structure here. */

MinStack* minStackCreate() {
  MinStack* ms = (MinStack*)malloc(sizeof(MinStack));
  ms->s = stackCreate();
  ms->m = stackCreate();
  return ms;
}

void minStackPush(MinStack* obj, int x) {
  stackPush(obj->s, x);
  if (!stackEmpty(obj->m)) {
    int curMin = stackTop(obj->m);
    if (curMin < x) {
      stackPush(obj->m, curMin);
      return;
    }
  } 
  stackPush(obj->m, x);
}

void minStackPop(MinStack* obj) {
  stackPop(obj->s);
  stackPop(obj->m);
}

int minStackTop(MinStack* obj) {
  return stackTop(obj->s);  
}

int minStackGetMin(MinStack* obj) {
  return stackTop(obj->m); 
}

void minStackFree(MinStack* obj) {
  free(obj->s);
  free(obj->m);
  free(obj);
}

/**
 * Your MinStack struct will be instantiated and called as such:
 * MinStack* obj = minStackCreate();
 * minStackPush(obj, x);
 
 * minStackPop(obj);
 
 * int param_3 = minStackTop(obj);
 
 * int param_4 = minStackGetMin(obj);
 
 * minStackFree(obj);
*/