#include <bits/stdc++.h>
using namespace std;
const int N = 2010;
int sharp[N][N];
char c[N][N];
int n, m;
int close(int x) {
    if (x <= 2)
        return x;
    return 4 - x;
}
int main() {
    cin >> n >> m;
    int ans = 0;
    for (int i = 1; i <= n; i++) {
        cin >> (c[i] + 1);
        for (int j = 1; j <= n; j++) {
            int x = i > n / 2 ? n - i + 1 : i, y = j > n / 2 ? n - j + 1 : j;
            sharp[x][y] += c[i][j] == '#';
        }
    }
    for (int i = 1; i <= n / 2; i++)
        for (int j = 1; j <= n / 2; j++)
            ans += close(sharp[i][j]);
    cout << ans << endl;
    for (int i = 1; i <= m; i++) {
        int p, q; cin >> p >> q;
        int x = p > n / 2 ? n - p + 1 : p, y = q > n / 2 ? n - q + 1 : q;
        ans -= close(sharp[x][y]);
        if (c[p][q] == '#') {
            sharp[x][y]--;
            c[p][q] = '.';
        } else {
            sharp[x][y]++;
            c[p][q] = '#';
        }
        ans += close(sharp[x][y]);
        cout << ans << endl;
    }
    return 0;
}