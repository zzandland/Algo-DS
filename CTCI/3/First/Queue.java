import java.util.NoSuchElementException;

public class Queue<T> {
  Node<T> first, last;

  public void enqueue(T data) {
    Node<T> dataNode = new Node<T>(data);
    if (last != null) last.setNext(dataNode);
    last = dataNode;
    if (first == null) first = last;
  }

  public T dequeue() {
    if (empty()) throw new NoSuchElementException();
    T data = first.getData();
    first = first.getNext();
    if (first == null) last = null;
    return data;
  }

  public T peek() {
    if (empty()) throw new NoSuchElementException();
    return first.getData();
  }

  public boolean empty() {
    return first == null;
  }
}
