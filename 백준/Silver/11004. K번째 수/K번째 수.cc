#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
bool compare(int x, int y) {
	return x < y;
}
int main(void) {
	int N, K;
	scanf("%d %d", &N, &K);
	vector<int> v(N, 0);
	for (int i = 0; i < N; i++) {
		scanf("%d", &v[i]);
	}
	sort(v.begin(), v.end(), compare);
	
	printf("%d\n", v[K-1]);
}