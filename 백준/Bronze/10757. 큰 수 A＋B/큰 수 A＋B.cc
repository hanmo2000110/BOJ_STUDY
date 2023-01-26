#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <string>
using namespace std;
char c; 

int main() { 
  string tmp1="",tmp2="",tmp,s1="0",s2="0";
  int overflow = 0,a,b;

  cin >> tmp1 >> tmp2;

  if(tmp1.length() < tmp2.length() ){
    tmp = tmp1;
    tmp1 = tmp2;
    tmp2 = tmp;
  }
  for(int i=0 ; i<tmp1.length()-tmp2.length() ; i++){
    s2 += "0"; 
  }
  s1 += tmp1;
  s2 += tmp2;
  tmp = "";
  for(int i=0 ; i<s1.length() ; i++){
    a = s1[s1.length() - 1 - i] - '0';
    b = s2[s2.length() - 1 - i] - '0';
    if( a + b + overflow >= 10){
      tmp += a + b + overflow - 10 + '0';
      overflow = 1;
    }
    else {
      tmp += a + b + overflow + '0';
      overflow = 0; 
    }
  }
  reverse(tmp.begin(),tmp.end());
  if(tmp[0] == '0') tmp.erase(0,1);
  cout << tmp << endl;
  
  return 0; 
}
