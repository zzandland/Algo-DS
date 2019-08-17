char * multiply(char * num1, char * num2){
  if (num1[0] == '0' || num2[0] == '0') return "0";
  int total_len = strlen(num1) + strlen(num2);
  int sums[total_len];
  char chars[total_len+1];
  int i, j, sum, lift;
  for (i = 0; i < total_len; ++i)
    sums[i] = 0;
  for (i = strlen(num2)-1; i >= 0; --i) {
    for (j = strlen(num1)-1; j >= 0; --j) {
      sum = ((int)num1[j] - '0') * ((int)num2[i] - '0');
      sums[i+j+1] += sum;
    }
  }
  lift = 0;
  for (i = total_len-1; i >= 0; --i) {
    sums[i] += lift;
    lift = sums[i] / 10;
    sums[i] %= 10;
  }
  int ignore = 0;
  for (i = 0; i < total_len; ++i) {
    if (i == 0 && sums[i] == 0) {
      ignore = 1;
      continue;
    }
    if (ignore)
      chars[i-1] = sums[i] + '0';
    else
      chars[i] = sums[i] + '0';
  }
  if (ignore)
    chars[total_len-1] = '\0';
  else
    chars[total_len] = '\0';
  char* res = &chars[0];
  return res;
}