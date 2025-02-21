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
    int empty = 0;
    for (int i = 0; i <= n; i++) {
        cout << max(cnt[i], empty);
        if (cnt[i] == 0)
            empty++;
    }
    return 0;
}