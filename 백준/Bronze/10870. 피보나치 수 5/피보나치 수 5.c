#include <stdio.h>

int main(){
 int n;
 int pab(int n);
    scanf("%d",&n);
    n=pab(n);
    printf("%d",n);
}
 
int pab(int n){
    if(n==0) return 0;
    if(n==1) return 1;
    return pab(n-1)+pab(n-2);
}