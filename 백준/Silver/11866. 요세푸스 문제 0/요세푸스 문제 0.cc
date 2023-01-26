#include <iostream>
using namespace std;

int main() {
    int n,k,count=0;
    cin >> n;
    cin >> k;
    int arr[n];
    int c=k,i=k-1;

    for(int j=0 ; j<n ; j++) arr[j] = j+1;

    cout << "<";
    while(count < n){
      if(arr[i] == 0){
        i = (i+1)%n;
      }
      else if(c != k){
        i = (i+1)%n;
        c++;
      }
      else{
        cout << arr[i];
        if(count != n-1) cout << ", ";
        arr[i] = 0;
        count++;
        c=1;
      }
    }
    cout << ">";
    
    return 0;
}