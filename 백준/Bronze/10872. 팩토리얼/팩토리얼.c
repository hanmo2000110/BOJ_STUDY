#include <stdio.h>
int main(){int n=0;int pac(int n);scanf("%d",&n);n=pac(n);printf("%d",n);}int pac(n){if(n==0) return 1;return n*pac(n-1);}