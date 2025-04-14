#include <bits/stdc++.h>

using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int n; cin >> n;

  vector<int> numbers(n);

  int evenCount = 0;
  for (int i = 0; i < n; ++i) {
    cin >> numbers[i];
    if (numbers[i] % 2 == 0)
      evenCount++;
  }

  if (evenCount > n / 2) cout << "Happy\n";
  else cout << "Sad\n";

  return 0;
}