#include <iostream>
#include <set>
#include <cmath>

typedef long long ll;

using namespace std;

int main() {
	ll k, x, y;
	cin >> k >> x >> y;

	ll m = 1e+18;
	
	ll arr[k];
	for (int i = 0; i < k; ++i)
		arr[i] = x + i;

	set <ll> arr1 = {0};

	while (arr1.size() > 0) {
		set<ll> arr2 = {};
		for (ll a : arr1) {
			for (ll b : arr) {
				if (a + b >= y) {
					m = min(m, a + b);
					// cout << "m = " << m << " a + b = " << a + b << endl; 
				} else {
					arr2.insert(a + b);
				}
			}
		}

		// for (auto ii  : arr2)
		// 	cout << ii << ' ';
		// cout << endl;

		arr1 = arr2;

	}

	cout << m << endl;

}