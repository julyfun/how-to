// t4
#include <bits/stdc++.h>
using namespace std;
int a[100010];
int main() {
    int n; cin >> n;
    for (int i = 1; i <= n; i++)
        cin >> a[i];
    int t;
    cin >> t;
    for (int i = 1; i <= n; i++) {
        if (a[i] == t) {
            cout << i << endl;
            break;
        }
    }
    cout << -1 << endl;
    return 0;
}
