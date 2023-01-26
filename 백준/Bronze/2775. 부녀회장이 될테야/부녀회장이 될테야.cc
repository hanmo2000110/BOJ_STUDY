#include <iostream>

using namespace std;

int main() { 
  int n[15][15]={ 0, };
  int t,x,y;
  for(int i=0 ; i<15 ; i++){
    n[0][i] = i+1;
  }

  for(int i=1 ; i<15 ; i++){
    for(int j=0 ; j<15 ; j++){
      for(int k=0 ; k<j+1 ; k++){
        n[i][j] += n[i-1][k];
      }
    }
  }
  cin >> t;
  for(int i=0 ; i<t ; i++){
    cin >> x >> y;
    cout << n[x][y-1] << endl;
  }
  return 0; 
}