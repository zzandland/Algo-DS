import java.util.*;
import java.io.*;

public class Main {
  public static void main(String[] args) {
    java.util.Random rand = new java.util.Random();
int count = 0;
int totalCount = 0;
int roulette = 0;
int target = 37;
int sampleSize = 100;
for (int i = 0; i < sampleSize; i++) {
  while (roulette != target) {
    roulette = rand.nextInt(1000);
    count++;
  }
  System.out.println(String.format("Landed on %d after %d spins", target, count));
  totalCount += count;
  roulette = 0;
  count = 0;
}
System.out.println(String.format("On average, it takes about %d spins to land on %d with sample size of %d", totalCount / sampleSize, target, sampleSize));
  }
}
