#include <iostream>
#include <cctype>
using namespace std;

int main() {
    string s;
    int flag = 0,max,index;
    cin >> s;
    int n[26] = {0};
    
    for(int i=0 ; i<s.length() ; i++ ){
        s[i] = toupper(s[i]);
        n[ s[i] - 'A' ]++;
    }
    max = n[0];
    index = 0;
    for(int i=1 ; i<26 ; i++ ){
        if(n[i] > max){
            flag = 0;
            max = n[i];
            index = i;
        }
        else if(n[i] == max) flag = 1;
    }
    if(flag == 0)
        cout << (char)('A' + index);
    else cout << "?";
    return 0;
}