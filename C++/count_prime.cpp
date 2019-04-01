#include <iostream>
#include <vector>
#include <math.h>

class CountPrime
{
public:
  static int Legendre(size_t n);

private:
  static int Phi(size_t n, int a, std::vector<int> &primes);
  static std::vector<int> GetNthPrime(int n);
};

int CountPrime::Legendre(size_t n) {
  int a = std::sqrt(n);
  std::vector<int> primes = GetNthPrime(a);
  std::cout << primes.size();
  return a + Phi(n, a, primes) - 1;
}

int CountPrime::Phi(size_t n, int a, std::vector<int> &primes) {
  if (a == 1)
    return (n + 1) / 2;
  return Phi(n, a - 1, primes) - Phi(n / primes[a - 1], a - 1, primes);
}

std::vector<int> CountPrime::GetNthPrime(int n) {
  std::vector<int> output = {2};
  for (int i = 3, j = 1; j < n; i += 2) {
    bool isPrime = true;
    for (size_t k = 0; k < output.size(); ++k) {
      if (i % output[k] == 0) {
        isPrime = false;
        break;
      }
    }
    if (isPrime) {
      output.push_back(i);
      j++;
    }
  } 
  return output;
}
