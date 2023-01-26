#include <iostream>
using namespace std;

int main() {
    string s;
    int n,answer=0,level=0;

    cin >> n;
    for(int i=0 ; i<n ; i++){
        cin >> s;
        level = 0;
        answer = 0;
        for(int j=0 ; j<s.length() ; j++){
            if(s[j] == 'O'){
                level++;
                answer += level;
            }
            else if(s[j] == 'X'){
                level = 0;
            }
        }
        cout << answer << endl;
    }
    return 0;
}