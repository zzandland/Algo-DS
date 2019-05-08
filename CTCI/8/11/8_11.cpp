#include <climits>
#include <iostream>
#include <vector>

int Coins(std::vector<int>& denoms, int sum, size_t i);
int BU(std::vector<int>& denoms, int sum);
void Heapsort(std::vector<int>& arr);
void Heapify(std::vector<int>& arr, size_t i, size_t limit);
void Quicksort(std::vector<int>& arr, int left, int right);
int Partition(std::vector<int>& arr, int left, int right);
void Mergesort(std::vector<int>& arr, int left, int right);
void Merge(std::vector<int>& arr, int left, int mid, int right);

int main(void) {
  std::vector<int> denoms = {25, 10, 5, 1};
  // std::vector<int> denoms = {25, 10, 5, 1,234,2,1234,65,1,34,61,234,1265,2341,2562,757,56432,567,325};
  std::cout << BU(denoms, 3980);
  return 0;
}

int Coins(std::vector<int>& denoms, int sum, size_t i) {
  if (i == denoms.size()) return 0;
  if (sum == 0) return 1;
  int s1 = 0;
  if (sum >= denoms[i]) s1 = Coins(denoms, sum - denoms[i], i);
  int s2 = Coins(denoms, sum, i + 1);
  return s1 + s2;
}

int BU(std::vector<int>& denoms, int sum) {
  Mergesort(denoms, 0, denoms.size() - 1);
  std::vector<std::vector<int>> dp(denoms.size(), std::vector<int>(sum + 1));
  for (size_t i = 0; i < denoms.size(); ++i) dp[i][0] = 1;
  for (int j = 1; j <= sum; ++j)
    if (j >= denoms[0]) dp[0][j] = 1;
  for (size_t i = 1; i < denoms.size(); ++i) {
    for (int j = 1; j <= sum; ++j) {
      if (j >= denoms[i])
        dp[i][j] = dp[i - 1][j] + dp[i][j - denoms[i]];
      else
        dp[i][j] = dp[i - 1][j];
    }
  }
  return dp[denoms.size() - 1][sum];
}

void Heapsort(std::vector<int>& arr) {
  for (int i = arr.size() / 2 - 1; i >= 0; --i) Heapify(arr, i, arr.size());

  int right = arr.size();
  while (right > 0) {
    std::swap(arr[0], arr[--right]);
    Heapify(arr, 0, right);
  }
}

void Heapify(std::vector<int>& arr, size_t i, size_t limit) {
  size_t left = 2 * i + 1;
  size_t right = 2 * i + 2;
  if (left < limit && arr[i] < arr[left]) {
    std::swap(arr[i], arr[left]);
    Heapify(arr, left, limit);
  }
  if (right < limit && arr[i] < arr[right]) {
    std::swap(arr[i], arr[right]);
    Heapify(arr, right, limit);
  }
}

void Quicksort(std::vector<int>& arr, int left, int right) {
  if (right > left) {
    int pivot = Partition(arr, left, right);
    Quicksort(arr, left, pivot - 1);
    Quicksort(arr, pivot + 1, right);
  }
}

int Partition(std::vector<int>& arr, int left, int right) {
  int i = left - 1;
  for (int j = left; j < right; ++j)
    if (arr[j] < arr[right]) std::swap(arr[++i], arr[j]);
  std::swap(arr[++i], arr[right]);
  return i;
}

void Mergesort(std::vector<int>& arr, int left, int right) {
  if (right > left) {
    int mid = left + ((right - left) / 2);
    Mergesort(arr, left, mid);
    Mergesort(arr, mid + 1, right);
    int tmp[right - mid];
    for (int i = 0; i < right - mid; ++i)
      tmp[i] = arr[mid + 1 + i];
    int p1 = mid, p2 = right - mid - 1, p3 = right;
    while (p1 >= left || p2 >= 0) {
      int left_val = (p1 >= left) ? arr[p1] : INT_MIN;
      int right_val = (p2 >= 0) ? tmp[p2] : INT_MIN;
      if (left_val < right_val)
        arr[p3--] = tmp[p2--];
      else 
        arr[p3--] = arr[p1--];
    }
  }
}

void Merge(std::vector<int>& arr, int left, int mid, int right) {
  int tmp[right - left + 1];
  int p1 = left, p2 = mid + 1, p3 = 0;
  std::cout << p1 << ":" << p2 << std::endl;
  while (p1 <= mid || p2 <= right) {
    int left_val = (p1 <= mid) ? arr[p1] : INT_MAX;
    int right_val = (p2 <= right) ? arr[p2] : INT_MAX;
    if (left_val < right_val)
      tmp[p3++] = arr[p1++];
    else
      tmp[p3++] = arr[p2++];
  }
  for (size_t i = 0; i < right - left + 1; ++i) arr[left + i] = tmp[i];
}
