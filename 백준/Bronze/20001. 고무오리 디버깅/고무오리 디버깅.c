#include <stdio.h>
#include <string.h>

int main(){
  int ex=0;
  int gomu=0;
  char start[100]={"고무오리 디버깅 시작"};
  char end[100]={"고무오리 디버깅 끝"};
  char scan[100];
  char gomuo[20]={"고무오리"};
  char mon[20]={"문제"};

  fgets(scan,100,stdin);
  scan[strlen(scan)-1]='\0';

  if(strcmp(start,scan)==0){
    while(1){
      fgets(scan,100,stdin);
      scan[strlen(scan)-1]='\0';
      if(strcmp(scan,mon)==0){
        ex++;
      }
      else if(strcmp(scan,gomuo)==0){
        if(ex>0){
          ex--;
        }
        else {
          ex+=2;
        }
      }
      if(strcmp(scan,end)==0)
        break;
    }
  
  if(ex!=0)
    printf("힝구");
  else 
    printf("고무오리야 사랑해");

  }



  return 0;
}