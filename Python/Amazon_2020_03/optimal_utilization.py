#  Given 2 lists a and b. Each element is a pair of integers where the first integer represents the unique id and the second integer represents a value. Your task is to find an element from a and an element form b such that the sum of their values is less or equal to target and as close to target as possible. Return a list of ids of selected elements. If no pair is possible, return an empty list.

#  Example 1:

#  Input:
a1 = [[1, 2], [2, 4], [3, 6]]
b1 = [[1, 2]]
target1 = 7

#  Output: [[2, 1]]

#  Explanation:
#  There are only three combinations [1, 1], [2, 1], and [3, 1], which have a total sum of 4, 6 and 8, respectively.
#  Since 6 is the largest sum that does not exceed 7, [2, 1] is the optimal pair.
#  Example 2:

#  Input:
a2 = [[1, 3], [2, 5], [3, 7], [4, 10]]
b2= [[1, 2], [2, 3], [3, 4], [4, 5]]
target2 = 10

#  Output: [[2, 4], [3, 2]]

#  Explanation:
#  There are two pairs possible. Element with id = 2 from the list `a` has a value 5, and element with id = 4 from the list `b` also has a value 5.
#  Combined, they add up to 10. Similarily, element with id = 3 from `a` has a value 7, and element with id = 2 from `b` has a value 3.
#  These also add up to 10. Therefore, the optimal pairs are [2, 4] and [3, 2].
#  Example 3:

#  Input:
a3 = [[1, 8], [2, 7], [3, 14]]
b3 = [[1, 5], [2, 10], [3, 14]]
target3 = 20

#  Output: [[3, 1]]
#  Example 4:

#  Input:
a4 = [[1, 8], [2, 15], [3, 9]]
b4 = [[1, 8], [2, 11], [3, 12]]
target4 = 20

#  Output: [[1, 3], [3, 2]]

#  from typing import List
#  from collections import defaultdict
#  import sys

#  class Solution:
    #  def binarySearch(self, a: List[int], b: List[int], target: int) -> List[int]:
        #  A, B = sorted(a, key=lambda x: x[1]), sorted(b, key=lambda x: x[1])
        #  if len(A) < len(B): short, long = A, B
        #  else: short, long = B, A
        #  def bs(nums: List[int], rem: int) -> int:
            #  left, right = 0, len(nums)-1
            #  while left < right:
                #  mid = left + (right-left)//2
                #  if nums[mid][1] == rem or (nums[mid+1][1] > rem and nums[mid][1] < rem):
                    #  return mid
                #  if nums[mid][1] < rem: left = mid+1
                #  else: right = mid
            #  return left if nums[left][1] < rem else left-1
        #  d = defaultdict(list)
        #  for i, sn in enumerate(short):
            #  j = bs(long, target-sn[1])
            #  if j != -1:
                #  pair = [sn[0], long[j][0]] if short == A else [long[j][0], sn[0]]
                #  d[sn[1]+long[j][1]].append(pair)
        #  return sorted(d[max(d.keys())], key=lambda x:x[0])

    #  def twoPointers(self, a: List[int], b: List[int], target: int) -> List[int]:
        #  A, B = sorted(a, key=lambda x: x[1]), sorted(b, key=lambda x: x[1])
        #  M, N = len(A), len(B)
        #  m, n, max_, output = 0, N-1, -sys.maxsize-1, []
        #  while m < M and n >= 0:
            #  sum_ = A[m][1] + B[n][1]
            #  print()
            #  if sum_ > target: n-=1
            #  else:
                #  if sum_ > max_:
                    #  max_ = sum_
                    #  output = []
                #  output.append([A[m][0], B[n][0]])
                #  cnt = n
                #  while cnt >= 1 and B[cnt][1] == B[cnt-1][1]:
                    #  output.append([A[m][0], B[cnt-1][0]])
                    #  cnt-=1
                #  m+=1
        #  return output

#  def main():
    #  res = Solution().twoPointers(a, b, target)
    #  print(res)

from typing import List
import bisect

def brute_force(a: List[List[int]], b: List[List[int]], target: int) -> List[List[int]]:
    """
    >>> brute_force(a1, b1, target1)
    [[2, 1]]
    >>> brute_force(a2, b2, target2)
    [[2, 4], [3, 2]]
    >>> brute_force(a3, b3, target3)
    [[3, 1]]
    >>> brute_force(a4, b4, target4)
    [[1, 3], [3, 2]]
    """
    # organize pairs by sum -> exclude sums over the target O(a*b) O(max(a, b))
    res = []
    seen = set()
    mxSum = float('-inf')
    for i, n1 in a:
        for j, n2 in b:
            sm = n1 + n2
            if sm <= target and (i, j) not in seen:
                if sm > mxSum:
                    seen.clear()
                    res.clear()
                    mxSum = sm
                if sm == mxSum:
                    res.append([i, j])
                    seen.add((j, i))

    # return the array from the biggest sum within the target val
    return res

def binary_search(a: List[List[int]], b: List[List[int]], target: int) -> List[List[int]]:
    '''
    >>> brute_force(a1, b1, target1)
    [[2, 1]]
    >>> brute_force(a2, b2, target2)
    [[2, 4], [3, 2]]
    >>> brute_force(a3, b3, target3)
    [[3, 1]]
    >>> brute_force(a4, b4, target4)
    [[1, 3], [3, 2]]
    '''
    # make sure that b is longer than a
    if len(a) > len(b): a, b = b, a

    # sort b to use binary search on it O(b log b)
    b.sort(key=lambda x: x[1])

    res = []
    seen = set()
    mxSum = float('-inf')
    # iterate a O(a) -> O(a log b)
    tmp = [val for _, val in b]
    for i, n in a:
        rest = target - n
        # binary search for b ele equal or smaller than target - O(log b)
        idx = bisect.bisect_left(b, tmp)
        if tmp[idx] > mxSum:
            res.clear()
            seen.clear()
            mxSum = tmp[idx]
        j = b[idx][0]
        if tmp[idx] == mxSum and (i, j) not in seen:
            res.append([i, j])
            seen.append((j, i))
    return res

if __name__ == '__main__':
    import doctest
    doctest.testmod()
