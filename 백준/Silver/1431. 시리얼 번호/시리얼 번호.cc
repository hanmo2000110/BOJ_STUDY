#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <string>
using namespace std;

bool comp(string s1,string s2){
  int n1=0,n2=0;
  
  if(s1.length() == s2.length() ){
    for(int i=0 ; i<s1.length() ; i++){
      //toupper(s1[i]);
      if( isdigit(s1[i]) != 0) n1 += s1[i]-'0';
      if( isdigit(s2[i]) != 0) n2 += s2[i]-'0';
    }
    // cout << n1 << " " << n2 << endl;
    if(n1 == n2){
       return s1 < s2;
    }
    else return n1 < n2;
  }
  return s1.length() < s2.length();
}

int main() {
  int n;
  cin >> n;
  string tmp[n];
  for(int i=0 ; i<n ; i++){
    cin >> tmp[i];
  }
  sort(tmp,tmp+n ,comp);
  for(int i=0 ; i<n ; i++){
    cout << tmp[i] << endl;
  }
  return 0;
}