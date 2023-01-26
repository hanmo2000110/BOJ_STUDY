#include <stdio.h>

int main(void) {
  int x=0,y=0,z=0,count=0;

  scanf("%d %d %d",&x,&y,&z);

  count=(z-x)/(x-y);

  if((z-x)%(x-y)>0)
    count+=2;
  else
    count++;

  printf("%d",count);
  return 0;
}