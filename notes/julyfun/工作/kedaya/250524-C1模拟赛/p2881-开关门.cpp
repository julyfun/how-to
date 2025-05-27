#include <iostream>
using namespace std;
int n;
bool a[2010];
int main() {
    cin >> n;
    for (int i = 1; i <= n; i++)
        for (int j = i; j <= 2 * n; j += i)
            a[j] = !a[j];
    int cnt = 0;
    for (int i = 1; i <= 2 * n; i++)
        cnt += a[i];
    cout << cnt << endl;
    return 0;
}
