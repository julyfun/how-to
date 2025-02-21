#include <bits/stdc++.h>
using namespace std;
const int N = 2010;
int sharp[N][N];
char c[N];
int n, m;
int close(int x) {
    if (x <= 2)
        return x;
    return 4 - x;
}
int main() {
    cin >> n;
    int ans = 0;
    for (int i = 1; i <= n; i++) {
        cin >> (c + 1);
        for (int j = 1; j <= n; j++) {
            int x = i > n / 2 ? n - i + 1 : i, y = j > n / 2 ? n - j + 1 : j;
            sharp[x][y] += c[j] == '#';
            ans += close(sharp[x][y]);
        }
    }
    return 0;
}