__author__ = '31351'

#include <stdio.h>

int creat_prime(int prime[],int n,int total)
{
　　　　register　　　　int　　　　i;
　　　　register　　　　int　　　　j;
　　　　register　　　　int　　　　gab=2;
　　　　register　　　　int　　　　count;
　　　　for(i=7;i<=n;i+=gab)
　　　　{
　　　　　　　　count=1;
　　　　　　　　gab=6-gab;
　　　　　　　　for(j=0;prime[j]*prime[j]<=i;j++)
　　　　　　　　{
　　　　　　　　　　　　if(i%prime[j]==0)
　　　　　　　　　　　　{
　　　　　　　　　　　　　　　　count=0;
　　　　　　　　　　　　　　　　break;
　　　　　　　　　　　　}
　　　　　　　　}
　　　　　　　　if(count)
　　　　　　　　{
　　　　　　　　　　　　prime[total]=i;
　　　　　　　　　　　　total++;
　　　　　　　　}
　　　　}

　　　　return total;
}

int main(void)
{
　　　　int　　　　prime[30000]={2,3,5};
　　　　int　　　　total=3;　　　　//孀欺殆方議倖方
　　　　int　　　　i;
　　　　int　　　　n=200000;　　　　//勣臥孀議袈律(>=6)

　　　　total=creat_prime(prime,n,total);
　　　　for(i=0;i<total;i++)
　　　　{
　　　　　　　　printf("%d ",prime[i]);
　　　　　　　　if(i && !(i%10))
　　　　　　　　　　　　putchar('\n');
　　　　}
　　　　putchar('\n');
}