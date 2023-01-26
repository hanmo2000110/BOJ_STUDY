#include <stdio.h>

int main(){
    int num=0;
    int x=0;
    int y=0;
    scanf("%d",&num);
    x=num%3;
    y=num%2;
    if(y==0 )
      printf("CY");
    else if(y==1)
      printf("SK");

  return 0;
}