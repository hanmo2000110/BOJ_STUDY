#include <stdio.h>
#include <string.h>

int main(){

  int num;
  int len;
  char str[100001];
  char stack[100001];
  int count=0,cnt=0;
  scanf("%d",&num);
  for(int i=0;i<num;i++){
    scanf("%s",str);
    len=strlen(str);
    count=0;
    for(int j=0;j<len;j++){
      if(count==0){
        stack[count]=str[j];
        count++;
      }
      else if(stack[count-1]!=str[j]){
        stack[count]=str[j];
        count++;
      }
      else{
        count--;
      }
    }
    if(count==0)
      cnt++;
  }
  printf("%d",cnt);

  return 0;
}