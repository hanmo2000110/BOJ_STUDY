#include <iostream>
using namespace std;

int main() { 
  int answer[3];
  cin >> answer[0] >> answer[1] >> answer[2];
  int e=1,s=1,m=1;
  int count = 1;
  while(count++){
    if((e == answer[0]) && (s == answer[1]) && (m == answer[2]) ) {
      cout << count-1 << endl;  
      break;
    }
    if(++e > 15) e = 1;
    if(++s > 28) s = 1;
    if(++m > 19) m = 1;
  }
  return 0; 
}
