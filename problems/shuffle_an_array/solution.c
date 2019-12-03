typedef struct {
  int* arr;
  int* originalArr;   
  int size;
} Solution;

Solution* solutionCreate(int* nums, int numsSize) {
  Solution* solution = (Solution*)malloc(sizeof(Solution));
  solution->arr = (int*)malloc(numsSize * sizeof(int));
  solution->originalArr = (int*)malloc(numsSize * sizeof(int));
  solution->size = numsSize;
  for (int i = 0; i < numsSize; ++i) {
    solution->arr[i] = nums[i];
    solution->originalArr[i] = nums[i];
  }
  return solution;
}

/** Resets the array to its original configuration and return it. */
int* solutionReset(Solution* obj, int* retSize) {
  *retSize = obj->size;
  for (int i = 0; i < obj->size; ++i) {
    obj->arr[i] = obj->originalArr[i];
  }
  return obj->arr;
}

/** Returns a random shuffling of the array. */
int* solutionShuffle(Solution* obj, int* retSize) {
  *retSize = obj->size;
  for (int i = 0; i < obj->size - 1; ++i) {
    int j = i + rand() / (RAND_MAX / (obj->size - i) + 1);
    int tmp = obj->arr[j];
    obj->arr[j] = obj->arr[i];
    obj->arr[i] = tmp;
  }
  return obj->arr;
}

void solutionFree(Solution* obj) {
  free(obj->arr);
  free(obj->originalArr);
  free(obj);
}

/**
 * Your Solution struct will be instantiated and called as such:
 * Solution* obj = solutionCreate(nums, numsSize);
 * int* param_1 = solutionReset(obj, retSize);
 
 * int* param_2 = solutionShuffle(obj, retSize);
 
 * solutionFree(obj);
*/