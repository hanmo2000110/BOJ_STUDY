#include <iostream>
using namespace std;

int main(){
    int M,N;
    int answer[5] = {0};

    cin >> M;
    cin >> N;
    string arr[5*M + 1];

    for(int i=0 ; i < (5*M+1) ; i++){
        cin >> arr[i];
    }

    for(int i=0 ; i<M ; i++){
        for(int j=0 ; j<N ; j++){
            if( arr[1 + i*5][1 + j*5] == '.' ) answer[0]++;
            else if(arr[2 + i*5][1 + j*5] == '.') answer[1]++;
            else if(arr[3 + i*5][1 + j*5] == '.') answer[2]++;
            else if(arr[4 + i*5][1 + j*5] == '.') answer[3]++;
            else answer[4]++;
        }
    }
    for(int i=0 ; i<5 ; i++)
        cout << answer[i] << " " ;
}