package sorting;

import java.util.List;

public class Heapsort {
  public static void sort(List<Integer> arr) {
    int len = arr.size();

    for (int i = len / 2 - 1; i >= 0; i--) {
      heapify(arr, i, len);
    }

    for (int i = len - 1; i >= 0; i--) {
      swap(arr, 0, i);
      heapify(arr, 0, i);
    }
  }

  private static void heapify(List<Integer> arr, int index, int delimiter) {
    int left = 2 * index + 1;
    int right = 2 * index + 2;
    int largest = index;

    if (left < delimiter && arr.get(left) > arr.get(largest)) largest = left;

    if (right < delimiter && arr.get(right) > arr.get(largest)) largest = right;

    if (index != largest) {
      swap(arr, index, largest);
      heapify(arr, largest, delimiter);
    }
  }

  private static void swap(List<Integer> arr, int left, int right) {
    int temp = arr.get(left);
    arr.set(left, arr.get(right));
    arr.set(right, temp);
  };
}
