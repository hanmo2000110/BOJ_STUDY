#include <iostream>
using namespace std;

int main() {
    string s;
    int answer = 0;
    cin >> s;
    answer = s.length() * 2;

    for(int i = 0 ; i < s.length() ; i++){
        if(s[i] <= 'C') answer++;
        else if(s[i] <= 'F')answer += 2;
        else if(s[i] <= 'I')answer += 3;
        else if(s[i] <= 'L')answer += 4;
        else if(s[i] <= 'O')answer += 5;
        else if(s[i] <= 'S')answer += 6;
        else if(s[i] <= 'V')answer += 7;
        else if(s[i] <= 'Z')answer += 8;
    }
    cout << answer;
    return 0;
}