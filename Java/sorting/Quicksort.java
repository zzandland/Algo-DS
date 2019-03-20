package sorting;

import java.util.List;

public class Quicksort {
  public static void sort(List<Integer> arr) {
    quicksort(arr, 0, arr.size() - 1);
  }

  private static void quicksort(List<Integer> arr, int left, int right) {
    if (right > left) {
      int pi = partition(arr, left, right);

      quicksort(arr, left, pi - 1);
      quicksort(arr, pi + 1, right);
    }    
  }

  private static int partition(List<Integer> arr, int left, int right) {
    int pivot = arr.get(right);
    int i = left - 1;

    for (int j = left; j < right; j++) {
      if (arr.get(j) < pivot) {
        swap(arr, j, ++i);
      }
    }
    swap(arr, ++i, right);
    return i;
  }

  private static void swap(List<Integer> arr, int left, int right) {
    int temp = arr.get(left);
    arr.set(left, arr.get(right));
    arr.set(right, temp);
  }
}
