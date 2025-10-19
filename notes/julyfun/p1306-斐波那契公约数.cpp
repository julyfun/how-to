#include <bits/stdc++.h>
using namespace std;
int f[1010];
int gcd(int a, int b) {
    return b == 0 ? a : gcd(b, a % b);
}
const int N = 80;
int main() {
    f[1] = f[0] = 1;
    for (int i = 2; i <= N; i++) {
        f[i] = (f[i - 1] + f[i - 2]) % int(1e8);
    }
    puts("");
    for (int i = 1; i <= N; i++, puts("")) {
        printf("%3d", i);
        for (int j = 1; j <= i; j++) {
            int g = gcd(f[i], f[j]);
            if (g % 5 == 0)
                printf("*");
            else
                printf(" ");
            // printf("%6d", gcd(f[i], f[j]) == 2 ? 2 : 0);
            // printf
        }
    }
    return 0;
}
