

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* majorityElement(int* nums, int numsSize, int* returnSize){
    int can1, can2, freq1, freq2;
    can1 = can2 = 1 << 30;
    freq1 = freq2 = 0;
    
    for (int i = 0; i < numsSize; ++i) {
        int val = nums[i];
        if (val == can1) {
            freq1 += 1;
        } else if (val == can2) {
            freq2 += 1;
        } else if (freq1 == 0) {
            can1 = val;
            freq1 = 1;
        } else if (freq2 == 0) {
            can2 = val;
            freq2 = 1;
        } else {
            freq1 -= 1;
            freq2 -= 1;
        }
    }
    
    freq1 = freq2 = 0;
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] == can1) freq1 += 1;
        else if (nums[i] == can2) freq2 += 1;
    }
    
    int threshold = numsSize / 3;
    int* out = (int*) malloc(sizeof(int) * 2);
    int i = 0;
    if (freq1 > threshold) {
        out[i] = can1;
        i += 1;
    }
    if (freq2 > threshold) {
        out[i] = can2;
        i += 1;
    }
    *returnSize = i;
    return out;
}