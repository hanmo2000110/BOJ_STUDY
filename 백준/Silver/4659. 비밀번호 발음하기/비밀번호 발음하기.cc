#include <iostream>
using namespace std;

bool test1(string s);//모음 포함하고 있는지 판별
bool test2(string s);//모음 자음 세개 연속으로 오는지 판별
bool test3(string s);//같은 글자가 두번 연속으로 오는지 판별 ee와 oo는 허용

int main() {
    string s;
    while(1){
        cin >> s;
        if(s == "end") break;
        if(test1(s) != true){
          cout << "<" << s << "> is not acceptable." << endl;
          continue;
        }
        if(test2(s) != true){
          cout << "<" << s << "> is not acceptable." << endl;
          continue;
        } 
        if(test3(s) != true) {
          cout << "<" << s << "> is not acceptable." << endl;
          continue;
        }
        cout << "<" << s << "> is acceptable." << endl;
    }
    return 0;
}

bool test1(string s){
    if(s.find('a') != string::npos) return true;
    else if(s.find('e') != string::npos) return true;
    else if(s.find('i') != string::npos) return true;
    else if(s.find('o') != string::npos) return true;
    else if(s.find('u') != string::npos) return true;  
    return false;
}

bool test2(string s){
    int m=0,j=0;

    for(int i = 0 ; i < s.length() ; i++){
        if(s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' || s[i] == 'u'){
            if(j != 0) j = 0;
            m++;
        }
        else {
            if(m != 0) m = 0;
            j++;
        }
        if(m >= 3 || j >= 3) return false;
    }

    return true;
}

bool test3(string s){
    char c,tmp;
    c = s[0];
    for(int i=1 ; i<s.length() ; i++){
        tmp = s[i];
        if(tmp != 'e' && tmp != 'o'){
            if(tmp == c) return false;
        }
        c = tmp; 
    }
    return true;
}