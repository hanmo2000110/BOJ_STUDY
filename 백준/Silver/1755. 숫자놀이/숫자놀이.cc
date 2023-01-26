#include <iostream>
#include <algorithm>
using namespace std;
string num[10] = {"zero","one","two","three","four","five","six","seven","eight","nine"};
bool comp(pair<string,int> p1,pair<string,int> p2){
  return p1.first < p2.first;
}
int main(){
  string s;
  int n1=4,n2=6;
  cin >> n1 >> n2;
  int n = n2 - n1 + 1;
  pair<string,int> str[n];

  for(int i = n1 ; i <= n2 ; i++){
    s = to_string(i); 
    str[i-n1].first="";
    str[i-n1].second = i;
    for(int j=0 ; j<s.length() ; j++){
      str[i-n1].first += num[(int)(s[j]-'0')] + " ";
    }
  }
  sort(str,str+n,comp);

  for(int i=0 ; i<n ; i++){
    cout << str[i].second << "\n";
  }
  return 0;
}