#include <iostream>
#include <set>
using namespace std;

int main() {
  set<int> s;
  int n,tmp;
  cin >> n;
  for(int i=0 ; i<n ; i++){
    cin >> tmp;
    s.insert(tmp);
  }
  for (typename std::set<int>::iterator itr = s.begin(); itr != s.end(); ++itr) {
    cout << *itr << " ";
  }
  return 0;
}