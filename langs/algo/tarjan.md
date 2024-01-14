## 缩点（有向图找强连通分量（互通块））

https://www.luogu.com.cn/problem/P3387

```cpp
#include <bits/stdc++.h>
using namespace std;
const int N = 1e4 + 10, E = 2e5 + 10;
int n, m;
struct A {
	int first[N], to[E], nxt[E], cnt;
	void adde(int u, int v) {
		++cnt;
		to[cnt] = v;
		nxt[cnt] = first[u];
		first[u] = cnt;
	}
} o, asd; int w[N];
queue<int> q;
int dfn[N], id, low[N], insta[N], sta[N], top;
int col[N], colcnt, colw[N];
int f[N], in[N];
void dfs(int u) {
	dfn[u] = low[u] = ++id;
	sta[++top] = u; insta[u] = 1;
	for (int p = o.first[u]; p; p = o.nxt[p]) {
		int v = o.to[p];
		if (dfn[v] == 0) {
			dfs(v);
            // v 在搜索树上搜完了
            // low[u] 的定义：搜索树上 u 的子树最多经过一条后向边能到达的时间戳
			low[u] = min(low[u], low[v]);
		}
		else {
			if (insta[v])
				low[u] = min(low[u], dfn[v]);
            // 注意！这里 insta 不是搜索栈，而是未确定强连通块的点的栈
            // 为什么这里是 insta 才更新呢？
            // 如果不 insta[v]，注意此时 dfn[v] != 0 说明 v 已经访问过了，然而这说明访问 v 所在强连通块并不包含 u
            // 如果 insta[v]，就很抽象了，我也不好说，你自己记住吧
		}
	}
	if (low[u] == dfn[u]) {
		++colcnt;
		do {
			col[sta[top]] = colcnt;
			colw[colcnt] += w[sta[top]];
			insta[sta[top]] = 0; 
		} while (sta[top--] != u);
	}
}
int main() {
	ios::sync_with_stdio(0); cin >> n >> m;
	for (int i = 1; i <= n; ++i) {
		cin >> w[i];
	} for (int i = 1; i<= m; ++i) {
		int u, v; cin >> u >> v; o.adde(u, v);
	}
	for (int i = 1; i <= n; ++i) {
		if (not dfn[i])
			dfs(i);
	}
	for (int u = 1; u <= n; ++u) for (int p = o.first[u]; p; p = o.nxt[p]) 
	{
		int v = o.to[p];
		if (col[u] != col[v])
			asd.adde(col[u], col[v]), ++in[col[v]];
	}
	int ans = 0;
	for (int i = 1; i <= colcnt; ++i)
		if (in[i] == 0) q.push(i);
	while (not q.empty()) {
		int u = q.front(); q.pop();
		f[u] += colw[u];
		if (f[u] > ans) ans = f[u];
		for (int p = asd.first[u]; p ; p= asd.nxt[p]) {
			int v = asd.to[p];
			if (f[u] > f[v])
				f[v] = f[u];
			--in[v];
			if (in[v] == 0)	q.push(v);
		}
	}
	cout << ans << endl;
	return 0;
}
```
