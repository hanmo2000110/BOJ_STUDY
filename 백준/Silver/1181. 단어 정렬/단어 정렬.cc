#include<bits/stdc++.h>
using namespace std;

struct Compare {
	bool operator() (const string &a, const string &b) const{
		if (a.size() == b.size())
			return a < b;
		else
			return a.size() < b.size();
	}
};

int main(){
  ios::sync_with_stdio(0);
	cin.tie(0);
  set<string, Compare> sets;
  int n;
  string tmp;
  cin >> n;
  for(int i=0 ; i<n ; i++){
    cin >> tmp;
    sets.insert(tmp);
  }
  for(auto i : sets){
    cout << i << "\n";
  }
	return 0;
}