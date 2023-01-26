#include <iostream>
using namespace std;

int main() {
    int n,flag=0,answer=0;
    cin >> n;
    string s[n],tmp="";
    char c;
    for(int i = 0 ; i < n ; i++){
        cin >> s[i];
    }


    for(int i = 0 ; i < n ; i++){
        c = s[i][0];
        flag = 0;
        tmp = "";
        for(int j = 1 ; j < s[i].length() ; j++){
            if( s[i][j] != c ){
                if( tmp.find(s[i][j]) == string::npos ){
                    tmp += c;
                    c = s[i][j];
                }
                else {
                  flag = 1;
                }
            }
            else {
                c = s[i][j];
            }
        }   
        if(flag == 0) {
          answer++;
        }
    }
    cout << answer;
    return 0;
}