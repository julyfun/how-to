// Translated from Python to C++ for a prime number calculation and game logic
#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    const int N = static_cast<int>(5e6);
    std::vector<bool> isPrime(N + 1, true);
    std::vector<int> primeNumbers;

    for (int i = 2; i <= N; ++i) {
        if (isPrime[i]) {
            primeNumbers.push_back(i);
        }
        for (size_t j = 0; j < primeNumbers.size(); ++j) {
            int currentPrime = primeNumbers[j];
            if (currentPrime * i > N) {
                break;
            }
            isPrime[currentPrime * i] = false;
            if (i % currentPrime == 0) {
                break;
            }
        }
    }

    int largestM3 = 3; // largest 4i + 3 prime
    int largestM1 = 1;
    std::vector<int> toWin(N + 10, 0);
    toWin[0] = 0; 
    toWin[1] = 1; 
    toWin[2] = 1; 
    toWin[3] = 1; 

    for (int i = 4; i <= N; ++i) {
        if (i % 2 == 0) {
            toWin[i] = i / 2;
        } else if (i % 4 == 1) {
            if (isPrime[i]) {
                largestM1 = i;
                toWin[i] = 1;
            } else {
                toWin[i] = (i - largestM1) / 2 + 1;
            }
        } else if (i % 4 == 3) {
            if (isPrime[i]) {
                largestM3 = i;
                toWin[i] = 1;
            } else {
                toWin[i] = (i - largestM3) / 2 + 1;
            }
        }
    }

    int testCases;
    std::cin >> testCases;
    for (int t = 0; t < testCases; ++t) {
        int n;
        std::cin >> n;
        std::vector<int> a(n + 1);
        for (int i = 1; i <= n; ++i) {
            std::cin >> a[i];
        }
        int firstMinRound = 1e9, win = 0;
        for (int i = 1; i <= n; ++i) {
            if (toWin[a[i]] / 2 + 1 < firstMinRound) {
                firstMinRound = toWin[a[i]] / 2 + 1;
                win = toWin[a[i]] % 2;
            }

        }
        if (win == 1) {
            std::cout << "Farmer John" << std::endl;
        } else {
            std::cout << "Farmer Nhoj" << std::endl;
        }
    }

    return 0;
}
