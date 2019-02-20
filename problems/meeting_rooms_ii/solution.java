/**
 * Definition for an interval.
 * public class Interval {
 *     int start;
 *     int end;
 *     Interval() { start = 0; end = 0; }
 *     Interval(int s, int e) { start = s; end = e; }
 * }
 */
class Solution {
  public int minMeetingRooms(Interval[] intervals) {
    int time[] = new int[1000000];
    for (Interval intr : intervals) {
      for (int i = intr.start; i < intr.end; i++) {
        time[i]++;
      }
    }
    int most = 0;
    for (int j = 0; j < time.length; j++) {
      if (time[j] > most) most = time[j];
    }
    return most;
  }
}