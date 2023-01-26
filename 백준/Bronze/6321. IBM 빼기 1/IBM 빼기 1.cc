#include <iostream>
using namespace std;

int main() {
    int n;
    string s;

    cin >> n;
    for(int i=0 ; i < n ; i++){
        cin >> s;
        cout << "String #" << i+1 << endl;
        for(int j=0 ; j<s.length() ; j++){
            if(s[j] != 'Z')
              s[j] = (char)(s[j] + 1);
            else s[j] = 'A';
        }
        cout << s << "\n" << endl;
    }

    return 0;
}