#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;

const int N = 1e5 + 10;
int n, m, a[N];
int f[N][20];
int main() {
    scanf("%d %d", &n, &m);
    for (int i = 1; i <= n; i++) {
        scanf("%d", &a[i]);
        f[i][0] = a[i];
    }
    // 1: 0, 2: 1, 3: 1, 4: 2
    for (int t = 1; t <= 19; t++) {
        for (int i = 1; i + (1 << t) - 1 <= n; i++) {
            f[i][t] =
                max(f[i][t - 1], f[i + (1 << (t - 1))][t - 1]);
        }
    }
    while (m--) {
        int l, r;
        scanf("%d%d", &l, &r);
        int len = r - l + 1;
        int t = log2(len);
        printf("%d\n",
             max(f[l][t], f[r - (1 << t) + 1][t]));
    }

    return 0;
}
