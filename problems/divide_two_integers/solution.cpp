#include <climits>
#include <cmath>
#include <iostream>
#include <list>

/*
 * @lc app=leetcode id=29 lang=cpp
 *
 * [29] Divide Two Integers
 *
 * https://leetcode.com/problems/divide-two-integers/description/
 *
 * algorithms
 * Medium (16.15%)
 * Total Accepted:    189.9K
 * Total Submissions: 1.2M
 * Testcase Example:  '10\n3'
 *
 * Given two integers dividend and divisor, divide two integers without using
 * multiplication, division and mod operator.
 *
 * Return the quotient after dividing dividend by divisor.
 *
 * The integer division should truncate toward zero.
 *
 * Example 1:
 *
 *
 * Input: dividend = 10, divisor = 3
 * Output: 3
 *
 * Example 2:
 *
 *
 * Input: dividend = 7, divisor = -3
 * Output: -2
 *
 * Note:
 *
 *
 * Both dividend and divisor will be 32-bit signed integers.
 * The divisor will never be 0.
 * Assume we are dealing with an environment which could only store integers
 * within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of
 * this problem, assume that your function returns 231 − 1 when the division
 * result overflows.
 *
 *
 */
class Solution {
 public:
  int divide(int dividend, int divisor) {
    if (dividend == INT_MIN && divisor == -1) return INT_MAX;
    bool negative = false;
    if ((dividend < 0 || divisor < 0) && !(dividend < 0 && divisor < 0))
      negative = true;
    long dividend_abs = std::abs((long)dividend);
    long divisor_abs = std::abs((long)divisor);
    std::list<bool> dividend_arr = MakeBinary(dividend_abs);
    long dividend_bin = 0;
    long quotient = 0;
    for (bool digit : dividend_arr) {
      dividend_bin += digit;
      if (dividend_bin >= divisor_abs) {
        ++quotient;
        dividend_bin -= divisor_abs;
      }
      dividend_bin <<= 1;
      quotient <<= 1;
    }
    long output = quotient >> 1;
    return negative ? output * -1 : output;
  }

  std::list<bool> MakeBinary(long dividend) {
    std::list<bool> dividend_arr;
    while (dividend > 0) {
      if ((dividend & 1) == 1)
        dividend_arr.push_front(1);
      else
        dividend_arr.push_front(0);
      dividend >>= 1;
    }
    return dividend_arr;
  }
};
