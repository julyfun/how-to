#include <iostream>
using namespace std;
int w[10];
int main() {
    long long x, n, cnt = 0;
    cin >> x >> n;
    for (int i = 1; i <= 7; i++) {
        cin >> w[i];
        if (w[i] == x)
            cnt++;
    }
    long long day = (n - 1) / cnt * 7;
    n -= (n - 1) / cnt * cnt;
    for (int i = 1; i <= 7; i++) {
        day++;
        if (w[i] == x) {
            n--;
            if (n == 0)
                break;
        }
    }
    cout << day << endl;
    return 0;
}

