#include <bits/stdc++.h>
using namespace std;
const int N = 1e2 + 10;
int a[N];
int cnt[N];
bool reponce(int n, int a0[]) {
    int len = -1;
    for (int i = 1; i <= n; i++) {
        if (n % i == 0) {
            bool ok = true;
            for (int j = i + 1; j <= n; j++)
                if (a0[j] != a0[j - i]) {
                    ok = false;
                    break;
                }
            if (ok) {
                len = i;
                break;
            }
        }
    }
    cnt[1] = cnt[2] = cnt[3] = 0;
    int num = 0;
    for (int i = 1; i <= len; i++) {
        cnt[a[i]]++;
        num += cnt[a[i]] == 1;
    }
    if (num == 1)
        return true;
    if (num == 2) {
        int changed = 0;
        for (int i = 2; i <= len; i++) {
            changed += a[i] != a[i - 1];
        }

    }

}
int main() {
    int t; cin >> t;
    while (t--) {
        int n, k; 
        cin >> n >> k;
        for (int i = 1; i <= n; i++)
            cin >> a[i];
        int best = -1;
        for (int s = 1; s <= n; s++) {
            if (n % s == 0) {
                bool ok = true;
                for (int j = s + 1; j <= n; j++)
                    if (a[j] != a[j - s]) {
                        ok = false;
                        break;
                    }
                if (ok) {
                    best = s;
                    break;
                }
            }
        }
        // 1231233
        cnt[1] = cnt[2] = cnt[3] = 0;
        int num = 0;
        for (int i = 1; i <= best; i++) {
            cnt[a[i]]++;
            num += cnt[a[i]] == 1;
        }
        if (num == 1) {
            cout << "YES" << endl;
            continue;
        }
        if (num == 2) {

        }
    }
    return 0;
}