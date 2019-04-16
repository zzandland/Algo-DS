package heaps;

import java.util.ArrayList;
import java.util.Arrays;

public class KthLargest {
  private int[] heap;
  private int size = 0;

  public kthLargest(int[] arr, int k) {
    heap = new int[arr.length];
    for (int e : arr) {
      insert(e);
    }
    getKthLargest(k);
  }


  private int parent(int i) { return (i - 1) / 2; }

  private int left(int i) { return 2 * i + 1; }
  
  private int right(int i) { return 2 * i + 2; }

  private void swap(int a, int b) {
    int temp = heap[a];
    heap[a] = heap[b];
    heap[b] = temp;
  }

  private void maxHeapify(int i) {
    int largest = i;
    if (left(i) < size && heap[left(i)] > heap[i]) largest = left(i);
    if (right(i) < size && heap[right(i)] > heap[largest]) largest = right(i);
    if (largest != i) {
      swap(i , largest);
      maxHeapify(largest);
    }
  }
  
  public void getKthLargest(int k) {
    for (int i = 0; i < k; i++) {
      System.out.println(extractMax());
    }
  }

  public void insert(int val) {
    int i = size;
    heap[i] = val;
    size++;
    while (i > 0 && heap[i] > heap[parent(i)]) {
      swap(i, parent(i));
      i = parent(i);
    }
  }

  public int extractMax() {
    int max = heap[0];
    size--;
    heap[0] = heap[size];
    maxHeapify(0);
    return max;
  }
}
