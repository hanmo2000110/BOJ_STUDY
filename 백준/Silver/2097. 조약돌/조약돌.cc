#include<iostream>
#include<cstdio>
#include<cmath>
using namespace std;
typedef long long ll;
int n;	int idx=1;
int main() {
	scanf("%d", &n);
    if(n < 4) {
        cout << 4 << endl;
        return 0;
    }
	while (idx++) {
		ll temp = idx*idx;
		if (temp >= n) {
			ll t = (idx - 1)*(idx - 1);
			if (n <= t+idx - 1) {
				cout << (idx - 2) * 4 + 2 << endl;
			}
			else {
				cout << (idx - 2) * 4 + 4 << endl;
			}
			return 0;
		}
	}
	


	return 0;
}