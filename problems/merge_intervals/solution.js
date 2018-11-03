/**
 * Definition for an interval.
 * function Interval(start, end) {
 *     this.start = start;
 *     this.end = end;
 * }
 */
/**
 * @param {Interval[]} intervals
 * @return {Interval[]}
 */
var merge = function(intervals) {
  if (intervals.length === 1) {
    return intervals;
  }
  var start, target, min, max, newI;
  var set = new Set();
  for (var i = 0; i < intervals.length; i++) {
    start = intervals[i];
    for (var j = i + 1; j < intervals.length; j++) {
      target = intervals[j];
      if ((start.end >= target.start && start.start <= target.end)
         || (start.end <= target.start && start.start >= target.end)) {
        min = Math.min(start.start, target.start);
        max = Math.max(start.end, target.end);
        newI = new Interval(min, max);
        intervals.splice(j, 1);
        start = newI;
        j--;
      }
    }
    if (!set.has(newI)) {
      intervals.splice(i, 1, newI || start);
      set.add(newI);
      i = -1;
    }
  }
  return intervals;
};