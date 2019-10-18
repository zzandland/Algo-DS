import java.util.ArrayList;
import java.util.List;
import sorting.*;

public class Main {
  public static void main(String[] args) {
    List<Integer> arr = new ArrayList<Integer>();

    int length = (int) (30 + (Math.random() * 150));

    System.out.println("The length is: " + length);

    for (int i = 0; i < length; i++) {
      int number = (int) (Math.random() * 10000);
      arr.add(number);
    }

    List<Integer> copy = new ArrayList<Integer>(arr);

    // System.out.println("Before heapsort: " + copy.toString());

    long start = System.nanoTime();
    sorting.Heapsort.sort(copy);
    long elapsed = System.nanoTime() - start;

    // System.out.println("After heapsort: " + copy.toString());

    System.out.println("The process took: " + elapsed + " nanosecond.");

    copy = new ArrayList<Integer>(arr);

    // System.out.println("Before quicksort: " + copy.toString());

    start = System.nanoTime();
    sorting.Quicksort.sort(copy);
    elapsed = System.nanoTime() - start;

    // System.out.println("After quicksort: " + copy.toString());

    System.out.println("The process took: " + elapsed + " nanosecond.");
  }
}
