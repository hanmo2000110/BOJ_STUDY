#include <iostream>
using namespace std;

int main(){
    int nt;
    float sum=0, count=0;
    int n;

    cin >> nt;

    cout << fixed;
    cout.precision(3);

    for(int i = 0 ; i < nt ; i++){
        cin >> n;
        int tmp[n];
        count = 0;

        for(int j = 0 ; j < n ; j++){
            cin >> tmp[j];
            sum += tmp[j];
        }

        for(int j = 0 ; j < n ; j++){
            if( sum/n < tmp[j]) count++;
        }
        
        
        cout << (count/n)*100 << "%" << endl;
        sum = 0;
    }

}
