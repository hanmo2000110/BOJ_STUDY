#include <iostream>
#include <map>
#define MAX 500001
using namespace std;
typedef long long ll;

map<ll, ll> m;
ll list[MAX];
int N, K;

ll getDis(ll idx, ll value) {
	ll ret = 0;
	map<ll, ll>::iterator next = m.lower_bound(value);
	map<ll, ll>::iterator pre = --m.lower_bound(value);

	if (next == m.begin()) {
		ret = abs(idx - (*next).second);
	}
	else if (next == m.end()) {
		ret = abs(idx - (*pre).second);
	}
	else {
		ret = -abs((*pre).second - (*next).second);
		ret += (abs(idx - (*pre).second) + abs(idx - (*next).second));
	}

	return ret;
}

void func() {
	if (K == 1) {
		cout << "0\n";
		return;
	}

	ll ans = 0;
	m.insert({ list[0], 0LL });
	for (int i = 1; i < K; i++) {
		ans += getDis((ll)i, list[i]);
		m.insert({ list[i], (ll)i });
	}

	ll sum = ans;
	for (int i = K; i < N; i++) {
		m.erase(list[i - K]);
		sum -= getDis((ll)(i - K), list[i - K]);

		sum += getDis((ll)i, list[i]);
		m.insert({ list[i], (ll)i });

		ans = min(ans, sum);
	}

	cout << ans << '\n';
}

void input() {
	cin >> N >> K;
	for (int i = 0; i < N; i++) {
		cin >> list[i];
	}
}

int main() {
	cin.tie(NULL); cout.tie(NULL);
	ios::sync_with_stdio(false);

	input();
	func();

	return 0;
}