package heaps;

import java.util.ArrayList;

public class HeapSort {
  private static int parent(int i) { return (i - 1) / 2; }

  private static int left(int i) { return 2 * i + 1; }

  private static int right(int i) { return 2 * i + 2; }

  private static void swap(int[] arr, int a, int b) {
    int temp = arr[a];
    arr[a] = arr[b];
    arr[b] = temp;
  }

  private static void swap(ArrayList<Integer> list, int a, int b) {
    int temp = list.get(a);
    list.set(a, list.get(b));
    list.set(b, temp);
  }

  private static void maxHeapify(int[] arr, int size) {
    for (int i = 0; i < size; i++) {
      while (i > 0 && arr[i] > arr[parent(i)]) {
        swap(arr, i, parent(i));
        i = parent(i);
      }
    }
  } 

  private static void maxHeapify(ArrayList<Integer> list, int size) {
    for (int i = 0; i < size; i++) {
      while (i > 0 && list.get(i) > list.get(parent(i))) {
        swap(list, i, parent(i));
        i = parent(i);
      }
    }
  }

  public static void heapSort(int[] arr) {
    int size = arr.length;
    maxHeapify(arr, size);
    while (size > 1) {
      swap(arr, 0, size - 1);
      maxHeapify(arr, --size);
    }
  }

  public static void heapSort(ArrayList<Integer> list) {
    int size = list.size();
    maxHeapify(list, size);
    while (size > 1) {
      swap(list, 0, size - 1);
      maxHeapify(list, --size);
    }
  }
}
