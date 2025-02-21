#include <bits/stdc++.h>    
using namespace std;
const int N = 2e5 + 10;
int a[N];
int cnt[N];
int main() {
    int n; cin >> n;
    for (int i = 1; i <= n; i++) {
        cin >> a[i];
        if (a[i] <= n)
            cnt[a[i]]++;
    }
    // 我们统计 0 ~ i - 1 中有几个数没有出现过（表示有几个空位需要填），
    // 再统计 i 出现了几次（这几个 i 都必须修改为其他数）
    int empty = 0;
    for (int i = 0; i <= n; i++) {
        cout << max(cnt[i], empty) << endl;
        if (cnt[i] == 0)
            empty++;
    }
    return 0;
}