#include <iostream>
using namespace std;
int main() {
    int n, l, r;
    cin >> n >> l >> r;
    int best = r - r % n - 1;
    if (best < l)
        cout << r % n;
    else
        cout << n - 1;
    return 0;
}
