package heaps;

import java.util.ArrayList;

public class MinHeap {
  private ArrayList<Integer> heap = new ArrayList<Integer>();

  private int getLast() { return heap.size() - 1; }

  private int getParent(int index) { return (index - 1) / 2; }

  private int getLeft(int index) { return 2 * index + 1; }

  private int getRight(int index) { return 2 * index + 2; }

  private void swap(int parent, int child) {
    int temp = heap.get(parent);
    heap.set(parent, heap.get(child));
    heap.set(child, temp);
  }

  private void minHeapify(int index) {
    int left = getLeft(index), right = getRight(index), temp;
    if (getRight(index) >= heap.size()) {
      if (heap.get(index) < heap.get(left)) return;
      temp = left;
    } else {
      if ( heap.get(index) < heap.get(left) && heap.get(index) < heap.get(right)) return; 
      temp = (heap.get(left) < heap.get(right)) ? left : right;
    }
    swap(index, temp);
    if (getLeft(temp) < heap.size()) minHeapify(temp);
  }

  private void decreaseKey(int index, int newVal) {
    heap.set(index, newVal);
    int parentIdx = getParent(index);
    while (index > 0 && heap.get(parentIdx) > heap.get(index)) {
      swap(parentIdx, index);
      index = parentIdx;
      parentIdx = getParent(index);
    }
  }

  public ArrayList<Integer> getHeap() { return heap; }

  public int getMin() {
    return heap.get(0);
  }

  public int extractMin() { 
    int min = heap.get(0);
    int last = getLast();
    int temp = heap.get(last);
    heap.set(0, heap.get(last));
    heap.remove(last);
    minHeapify(0);
    return min;
  }

  public void insert(int val) {
    heap.add(val);
    int last = getLast();
    int parent = getParent(last);
    while (last != 0 && val < heap.get(parent)) {
      swap (parent, last);
      last = parent;
      parent = getParent(last);
    }
  }

  public void delete(int index) {
    decreaseKey(index, Integer.MIN_VALUE);
    extractMin();
  }
}
