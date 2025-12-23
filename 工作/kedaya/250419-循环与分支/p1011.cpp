// ac, t2
#include <bits/stdc++.h>
using namespace std;
int main() {
    int n, x;
    cin >> n >> x;
    for (int i = 1; i <= n; i++) {
        if (i % x != 0)
            cout << i << " ";
    }
    return 0;
}
