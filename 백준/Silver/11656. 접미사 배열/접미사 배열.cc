#include <iostream>
#include <algorithm>
using namespace std;

int main(){
  string s;
  cin >> s;
  string str[s.length()];
  for(int i=0 ; i<s.length() ; i++){
    str[i] = s.substr(i,s.length()-i);
  }
  sort(str,str+s.length());

  for(int i=0 ; i<s.length() ; i++){
    cout << str[i] << "\n";
  }
  return 0;
}