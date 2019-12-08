uint32_t reverseBits(uint32_t n) {
  uint32_t output = 0;
  for (int i = 0; i < 31; ++i) {
    output += n & 1;
    n >>= 1;
    output <<= 1;
  }
  output += n & 1;
  return output;
}