

void dfs(int i, int* nums, int numsSize) {
    if (i <= 0 || i > numsSize) return;
    int val = nums[i-1];
    if (val == i) return;
    nums[i-1] = i;
    dfs(val, nums, numsSize);
}

int firstMissingPositive(int* nums, int numsSize) {
    for (int i = 0; i < numsSize; ++i) {
        dfs(nums[i], nums, numsSize);
    }
    
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] != i+1) return i+1;
    }
    return numsSize + 1;
}