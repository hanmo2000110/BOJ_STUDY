#include <stdio.h>
int main(){
    int num=0;
    int x=1;
    scanf("%d",&num);

    for(int i=1;i<=num;i++){
      x++;
      if(x>6)
        x=0;


    }

    if(x==1 || x==3)
      printf("CY");
    else 
      printf("SK");



  return 0;
}