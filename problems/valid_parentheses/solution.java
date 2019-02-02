class MyStack<T> {
  static class StackNode<T> {
    T data;
    StackNode<T> next;
    
    StackNode(T data) { this.data = data; }
  }
  
  StackNode<T> top;
  
  void push(T data) {
    StackNode<T> newNode = new StackNode<T>(data);
    if (top != null) newNode.next = top;
    top = newNode;
  }
  
  T pop() {
    StackNode<T> output = top;
    top = top.next;
    return output.data;
  }
  
  T peek() { return top.data; }
  
  boolean empty() { return top == null; }
}

class Solution {
  public boolean isValid(String s) {
    MyStack<Character> stack = new MyStack<Character>();
    char[] chars = s.toCharArray();
    
    for (char ch : chars) {
      if (ch == ')' || ch == ']' || ch == '}') {
        if (!checkStack(ch, stack)) return false;
      } else {
        stack.push(ch);    
      }
    }
    return stack.empty();
  }
  
  private boolean checkStack(char ch, MyStack<Character> s) {
    if (s.empty()) return false;
    char popChar = s.pop();
    switch (ch) {
      case ')':
        return popChar == '(';
      case ']':
        return popChar == '[';
      case '}':
        return popChar == '{';
    }
    return true;
  }
}