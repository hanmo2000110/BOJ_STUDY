#include <iostream>
using namespace std;

int main() {
    int answer = 0;
    int n,flag=0,count = 0;
    cin >> n;
    string name[n];
    for(int i = 0 ; i < n ; i++){
      cin >> name[i];
    }
    for(int i = 0 ; i < 26 ; i++ ){
        count = 0;
        for(int j = 0 ; j < n ; j++ ){
            if(name[j][0] == 'a' + i){
                count++;
            }
        }
        if(count >= 5) {
          flag = 1;
          cout << (char)('a' + i) ;
        }
    }

    if(flag == 0) cout << "PREDAJA";
    return 0;
}