#include <bits/stdc++.h>
using namespace std;
int a[100010];
int main() {
	// 先读入 n，再读入 n 个数 
	int n;
	cin >> n;
	for (int i = 1; i <= n; i++) {
		cin >> a[i];
	}
	// 读入 x，并寻找 x 在 a 数组中第一次出现的位置
	int x, flag = 0;
	cin >> x;
	for (int i = 1; i <= n; i++) {
		if (x == a[i]) {
			cout << i << endl;
			flag = 1;
			break;
		}
	}
	if (flag == 0) {
		cout << "-1";
	}
	return 0;
}
