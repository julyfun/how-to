#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <cstring>
#define init(x) memset (x,0,sizeof (x))
#define ll long long
#define ull unsigned long long
#define INF 0x3f3f3f3f
using namespace std;
const int MAX = 5e5 + 5,M = 5e6 + 500;
const int MOD = 1e9 + 7;
inline int read ();
int t,n,ok,times,cnt,a[MAX],vis[M + 5],p[MAX];
int main ()
{
	//freopen (".in","r",stdin);
	//freopen (".out","w",stdout);
	for (int i = 2;i <= M;++i)
	{
		if (!vis[i]) p[++cnt] = i;
		for (int j = 1;j <= cnt;++j)
		{
			if (i * p[j] > M) break;
			vis[i * p[j]] = 1;
			if (i % p[j] == 0) break;
		}
	}
	p[0] = 1;
	t = read ();
	while (t--)
	{
		n = read ();
		ok = 1;times = INF;
		for (int i = 1;i <= n;++i) a[i] = read ();
		for (int i = 1;i <= n;++i) 
		{
			if (a[i] % 2 == 0 && times > a[i] / 4) ok = (a[i] % 4 != 0),times = a[i] / 4;
			if (a[i] & 1)
			{
				int x = upper_bound (p,p + 1 + cnt,a[i]) - p - 1;
				while (~x)
				{
					if ((a[i] - p[x]) % 4 == 0)
					{
						if (times > (a[i] - p[x]) / 4) ok = 1,times = (a[i] - p[x]) / 4;
						break;
					} 
					--x;
				}
			}
		}
		puts (ok ? "Farmer John" : "Farmer Nhoj");
	}
	return 0;
}
inline int read ()
{
    int s = 0;int f = 1;
    char ch = getchar ();
    while ((ch < '0' || ch > '9') && ch != EOF)
	{
        if (ch == '-') f = -1;
        ch = getchar ();
    }
    while (ch >= '0' && ch <= '9')
	{
        s = s * 10 + ch - '0';
        ch = getchar ();
    }
    return s * f;
}
