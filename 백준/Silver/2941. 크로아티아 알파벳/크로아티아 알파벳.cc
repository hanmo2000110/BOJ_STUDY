#include <iostream>
#include <string>
using namespace std;

int iscroi(string s){
  string croi[8] = {"c=","c-","dz","d-","lj","nj","s=","z="};
  for(int i=0 ; i<8 ; i++){
    if(s == croi[i]){
      if(s == "dz") return 2;
      else return 1;
    }
  }
  return 0;
}

int main() { 
  int count = 0;
  string s;
  cin >> s;
  for(int i=0 ; i<s.length() ; i++){
    if(iscroi(s.substr(i,2)) > 0 ){
      if(iscroi(s.substr(i,2)) == 1) i++;
      else if(s[i+2] == '=') i+=2;
    } 
    count++;
  }
  cout << count;
  return 0; 
}
