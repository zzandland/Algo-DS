class MyCircularQueue {
    int storage[];
    int size;
    int head, tail;
  
    /** Initialize your data structure here. Set the size of the queue to be k. */
    public MyCircularQueue(int k) {
      storage = new int[k];
      size = k;
      head = tail = -1;
    }
    
    /** Insert an element into the circular queue. Return true if the operation is successful. */
    public boolean enQueue(int value) {
      if (isFull()) return false;
      if (isEmpty()) {
        head = tail = 0;
      } else {
        head = ++head % size;
      }
      storage[head] = value;
      return true;
    }
    
    /** Delete an element from the circular queue. Return true if the operation is successful. */
    public boolean deQueue() {
      if (isEmpty()) return false; 
      tail = ++tail % size;
      if ((head + 1) % size == tail) head = tail = -1;
      return true;
    }
  
    /** Get the front item from the queue. */
    public int Front() {
      return (tail == -1) ? -1 : storage[tail];
    }
    
    /** Get the last item from the queue. */
    public int Rear() {
      return (head == -1) ? -1 : storage[head];        
    }
    
    /** Checks whether the circular queue is empty or not. */
    public boolean isEmpty() {
      return head == -1 && tail == -1;
    }
    
    /** Checks whether the circular queue is full or not. */
    public boolean isFull() {
      return !isEmpty() && (head + 1) % size == tail;    
    }
}

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue obj = new MyCircularQueue(k);
 * boolean param_1 = obj.enQueue(value);
 * boolean param_2 = obj.deQueue();
 * int param_3 = obj.Front();
 * int param_4 = obj.Rear();
 * boolean param_5 = obj.isEmpty();
 * boolean param_6 = obj.isFull();
 */