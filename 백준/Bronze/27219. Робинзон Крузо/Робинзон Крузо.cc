#include <bits/stdc++.h>

using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int n; cin >> n;

  int cntV = n / 5, cntI = n % 5;

  for (int i = 0; i < cntV; i++)
    cout << "V";
  for (int i = 0; i < cntI; i++)
    cout << "I";
  cout << "\n";

  return 0;
}