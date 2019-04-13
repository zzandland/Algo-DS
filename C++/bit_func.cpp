#include "bit_func.h"

// Get bit at ith position in num
bool GetBit(int num, int i) {
  /*
   * 1. Left shift 1 with i
   * 2. Bitwise AND operation with num
   * 3. If bit at the ith position is not zero, it will be greater than 0
   */
  return (num & (1 << i)) != 0;
}

// Set bit at ith position in num to 1
int SetBit(int num, int i) {
  /*
   * 1. Left shift 1 with i
   * 2. Bitwise OR operation with num (since other than ith position is 0, they
   * won't be affected
   */
  return num | (1 << i);
}

// Clear bit at ith position in num to 0
int ClearBit(int num, int i) {
  /*
   * 1. Left shift 1 with i
   * 2. Reverse the shifted i
   * 3. Bitwise AND operation with num
   */
  return num & (~(1 << i));
}

// Clear bits from the most significant bit (highest) to i (inclusive)
int ClearBitsMSBthrouthI(int num, int i) {
  /*
   * 1. Left shift 1 with i
   * 2. Minus 1 to generate a sequence of 0s followed by i 1s.
   * 3. Bitwise AND operation with num (Since every digit from the most
   * significant to the ith pos is 0, they are all cleared)
   */
  return num & ((1 << i) - 1);
}

// Clear bits from i to 0 (inclusive)
int ClearBitsIthrough0(int num, int i) {
  /*
   * 1. Left shift -1 (all 1s) with i + 1 (generate a sequence of 1s followed by
   * i + 1 0s)
   * 2. Bitwise AND operation with num
   */
  return num & (-1 << (i + 1));
}

// Update ith bit with desired value
int UpdateBit(int num, int i, bool bit_is_1) {
  int value = bit_is_1 ? 1 : 0;
  int deleted = num & ~(1 << i);
  return deleted | (value << i);
}
