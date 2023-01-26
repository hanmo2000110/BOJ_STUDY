#include<bits/stdc++.h>
using namespace std;

int main()
{
  float a,b,n,min;
  scanf("%f %f",&a,&b);
  min = a/b;
  scanf("%f",&n);
  for(int i=0 ; i<n ; i++){
    scanf("%f %f",&a,&b);
    if(min > a/b) min = a/b;
  }
  printf("%.2f",min*1000);
	return 0;
}