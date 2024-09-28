#include <iostream>
using namespace std;
const int N=5e6+5;
bool isprime[N];
int prime[N];
int n,cnt;
int s[4];//统计格式为4k+1,4k+2,4k+3的最大质数
int ans[N];
int t;
void euler()//欧拉筛
{
    int i,j;
    isprime[1]=true;
    ans[1]=1;
    s[1]=1;
    for(i=2; i<=N; i++)
    {
        if(!isprime[i])
        {
            prime[++cnt]=i;
            if(i%4!=0)
                s[i%4]=i;//更新最大质数数组
        }
        for(j=1; j<=cnt && i*prime[j]<=N; j++)
        {
            isprime[i*prime[j]]=true;
            if(i%prime[j]==0)
                break;
        }
        if(i%4==0)
            ans[i]=i/4+1;//套公式
        else
            ans[i]=(i-s[i%4])/4+1;//套公式
    }
}
int main()
{
    int i;
    euler();
    cin>>t;
    while(t--)
    {
        cin>>n;
        int minx1=1e9,mark1;
        int minx2=1e9,mark2;
        for(i=1; i<=n; i++)//不多解释了，作者的代码很烂，不一定要学习我的，自己写也行
        {
            int temp;
            cin>>temp;
            if(temp%4==0)
            {
                if(minx2>ans[temp])
                {
                    minx2=ans[temp];
                    mark2=i;
                }
            }
            else
            {
                if(minx1>ans[temp])
                {
                    minx1=ans[temp];
                    mark1=i;
                }
            }
        }
        if(minx1<minx2)
            cout<<"Farmer John"<<endl;
        else if(minx1>minx2)
            cout<<"Farmer Nhoj"<<endl;
        else
        {
            if(mark1<mark2)
                cout<<"Farmer John"<<endl;
            else
                cout<<"Farmer Nhoj"<<endl;
        }
    }
    return 0;
}
