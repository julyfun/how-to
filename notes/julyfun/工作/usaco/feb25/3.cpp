#include <bits/stdc++.h>
using namespace std;
const int N = 1e2 + 10;
int cnt[N];
bool check(int n, int a0[]) {
    // cout << "---" << endl;
    // cout << n << endl;
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
    // cout << "len: " << len << endl;
    cnt[1] = cnt[2] = cnt[3] = 0;
    int num = 0;
    for (int i = 1; i <= len; i++) {
        cnt[a0[i]]++;
        num += cnt[a0[i]] == 1;
    }
    if (num == 1)
        return true;
    if (num == 2) {
        int changed = 0;
        for (int i = 2; i <= len; i++) {
            changed += a0[i] != a0[i - 1];
        }
        return changed == 1;
    }
    // 1, 2, 3 中必须有一个数只在前面或者只在后面，将其排除
    int l = -1;
    for (int i = 2; ; i++) {
        if (a0[i] != a0[i - 1]) {
            l = i - 1;
            for (int j = i; j <= len; j++) {
                if (a0[j] == a0[1]) {
                    l = -1;
                    break;
                }
            }
            break;
        }
    }
    if (l != -1) return check(len - l, a0 + l);
    // cout << "not L" << endl;
    int r = -1;
    for (int i = len - 1; ; i--) {
        if (a0[i] != a0[i + 1]) {
            r = i + 1;
            for (int j = i; j >= 1; j--) {
                if (a0[j] == a0[len]) {
                    r = - 1;
                    break;
                }
            }
            break;
        }
    }
    if (r != -1) return check(r - 1, a0);
    // cout << "not R" << endl;
    return false;
}

int a[N];
int main() {
    int t; cin >> t;
    while (t--) {
        cout << "------" << endl;
        int n, k; 
        cin >> n >> k;
        for (int i = 1; i <= n; i++)
            cin >> a[i];
        if (check(n, a))
            cout << "YES" << endl;
        else
            cout << "NO" << endl;
    }
    return 0;
}