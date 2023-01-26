#include <stdio.h>

int main(){
    int num1,num2;
    scanf("%d%d",&num1,&num2);
    
    num2-=45;
    if(num2<0){
        num2=60+num2;
        num1-=1;
        if(num1<0)
            num1=23;
    }  
    printf("%d %d",num1,num2);
}