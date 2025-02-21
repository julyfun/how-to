#include <bits/stdc++.h>
using namespace std;
const int N = 1e2 + 10;
int a[N];
int last_cont_start[N];
int main() {
    int t; cin >> t;
    while (t--) {
        int n, k; 
        cin >> n >> k;
        for (int i = 1; i <= n; i++)
            cin >> a[i];
        for (int i = 1; i <= k; i++)
            last_cont_start[i] = 0;
        bool ok = true;
        int p = 1;
        while (p <= n && ok) {
            if (p >= 2 && a[p] == a[p - 1]) {
                p++;
                continue;
            }
            int x = last_cont_start[a[p]];
            if (x != 0) {
                int rep = p - x;
                for (int i = 1; i <= rep; i++) {
                    if (a[p] != a[p - rep] || p > n) {
                        ok = false;
                        break;
                    }
                    p++;
                }
            }
            last_cont_start[a[p]] = p;
            p++;
        }
        if (ok)
            cout << "YES" << endl;
        else
            cout << "NO" << endl;
    }

    return 0;
}