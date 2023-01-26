#include <stdio.h>

int main(){
    int x=0,y;
    scanf("%d %d",&x,&y);
    printf("%d\n",(x+y));
    printf("%d\n",(x-y));
    printf("%d\n",(x*y));
    printf("%d\n",(x/y));
    printf("%d",(int)x%(int)y);
}