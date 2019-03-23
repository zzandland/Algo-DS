import java.util.NoSuchElementException;

public class Stack<T> {
  private Node<T> top;

  public void push(T data) {
    Node<T> dataNode = new Node<T>(data);
    if (top != null) dataNode.setNext(top);
    top = dataNode;
  }

  public T pop() {
    if (empty()) throw new NoSuchElementException();
    T data = top.getData();
    top = top.getNext();
    return data;
  }

  public T peek() {
    if (empty()) throw new NoSuchElementException();
    return top.getData();
  }

  public boolean empty() {
    return top == null;
  }
}
