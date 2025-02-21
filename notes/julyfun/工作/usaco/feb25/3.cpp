#include <bits/stdc++.h>
using namespace std;
const int N = 1e2 + 10;
int cnt[N];
bool check(int n, int a0[], int k) {
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
        cnt[a0[i]]++;
        num += cnt[a0[i]] == 1;
    }
    if (num == 1)
        return true;
    // 如果循环节内部有 2 种数字，则需要分类讨论。
    // 如果 K = 3，则可能有 1212222 这种形式（即包含两个循环节 12 和额外输出的 222，这也满足 3 个 PRINT）。
    if (num == 2) {
        if (k == 3) {
            // 暴力删除连续 1 或 2 的前缀或后缀，再递归判断剩下部分即可。
            for (int i = 1; i <= len; i++) {
                if (!(i == 1 || a0[i] == a0[i - 1]))
                    break;
                if (check(len - i, a0 + i, 2))
                    return true;
            }
            for (int i = len; i >= 1; i--) {
                if (!(i == len || a0[i] == a0[i + 1]))
                    break;
                if (check(i - 1, a0, 2))
                    return true;
            }
        }
        // 如果 K = 2，则 S 必然是 111222... 或者 222111.. 这种形式。
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
    if (l != -1 && check(len - l, a0 + l, 2)) return true;
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
    if (r != -1 && check(r - 1, a0, 2)) return true;
    return false;
}

int a[N];
int main() {
    int t; cin >> t;
    while (t--) {
        // cout << "------" << endl;
        int n, k; 
        cin >> n >> k;
        for (int i = 1; i <= n; i++)
            cin >> a[i];
        if (check(n, a, k))
            cout << "YES" << endl;
        else
            cout << "NO" << endl;
    }
    return 0;
}