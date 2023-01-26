#include <iostream>
using namespace std;

int main() {
    int num,first;

    cin >> num;
    cin >> first;
    if(num > 5) cout << "Love is open door" << endl;
    else {
        for(int i=0 ; i < num-1 ; i++){
            first ^= 1;
            cout << first << endl;
        } 
    }
    
    return 0;
}