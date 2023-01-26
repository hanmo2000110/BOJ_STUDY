#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int N,n;
    double m[4],h=0,s=0,tmp1,tmp2;

    cin >> N >> n;
    cin >> m[0] >> m[1] >> m[2] >> m[3];

    if(n == 1){
      h = m[2];
      s = m[3];
    }
    else if(n == 0){
      h = m[0];
      s = m[1];
    }

    for(int i=0 ; i < N-1 ; i++){
      tmp1 = h*m[0] + s*m[2];
      tmp2 = s*m[3] + h*m[1];
      h = tmp1;
      s = tmp2;
    } 

    h = h*1000;
    s = s*1000;
    
    cout << (int)ceil(h*10)/10 << endl;
    cout << (int)ceil(s*10)/10 << endl;
    return 0;
}