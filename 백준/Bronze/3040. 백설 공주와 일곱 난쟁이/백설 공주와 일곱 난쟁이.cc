#include<bits/stdc++.h>
using namespace std;

int main()
{
	int n[9],sum=0;
  for(int i=0 ; i<9 ; i++){
    scanf("%d",&n[i]);
    sum += n[i];
  }

  int x,y,flag=0;

  for(int i=0 ; i<9 ; i++){
    for(int j=0 ; j<9 ; j++){
      if(i == j || ((sum-n[i]-n[j]) != 100)) continue;
      flag = 1;
      x = i;
      y = j;
      break;
    }
    if(flag == 1) break;
  }

  for(int i=0 ; i<9 ; i++){
    if(i != x && i != y)
      printf("%d\n",n[i]);
  }

	return 0;
}