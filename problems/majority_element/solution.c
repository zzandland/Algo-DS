

int majorityElement(int* nums, int numsSize){
    int candidate;
    int freq = 0;
    for (int i = 0; i < numsSize; ++i) {
        if (freq == 0) {
            candidate = nums[i];
            freq = 1;
        } else {
            freq += (nums[i] == candidate ? 1 : -1);
        }
    }
    return candidate;
}