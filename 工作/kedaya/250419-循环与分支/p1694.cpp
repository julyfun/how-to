// ac, t3
#include <bits/stdc++.h>
using namespace std;
int cnt[11];
int main() {
    int n; cin >> n;
    for (int i = 1; i <= n; i++) {
        int x; cin >> x;
        cnt[x]++;
    }
    cout << cnt[1] << endl << cnt[5] << endl << cnt[10] << endl;
    return 0;
}
