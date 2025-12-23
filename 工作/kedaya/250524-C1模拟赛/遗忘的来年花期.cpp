#include <iostream>
using namespace std;

int a[100010];
int main() {
    int n, cnt = 0;
    cin >> n;
    for (int i = 1; i <= n; i++)
        cin >> a[i];
    for (int i = 2; i <= n - 1; i++)
        if (a[i] >= a[i - 1] && a[i] >= a[i + 1])
            cnt++;
    cout << cnt << endl;
    return 0;
}

