#include <iostream>
#include <algorithm>
using namespace std;
bool comp(int a,int b){
  return a > b;
}
int main(){
  string s;
  cin >> s;
  int arr[s.length()];

  for(int i=0 ; i<s.length() ; i++){
    arr[i] = s[i] - '0';
  }

  sort(arr,arr+s.length(),comp);
  for(int i=0 ; i<s.length() ; i++){
    cout << arr[i];
  }
  return 0;
}