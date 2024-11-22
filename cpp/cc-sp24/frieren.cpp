#include <bits/stdc++.h>
using ll = long long;
using namespace std;

ll solve(ll b, ll l, ll e) {
    ll fs = (e + b) % 50;

    if (fs > l) {
        return 0;
    }

    ll ans = (l - fs) / 50;
    return ans + 1;
}

int main() {
    int n; cin >> n;

    for (int i = 0; i < n; i++) {
        ll b; ll l; ll e;
        cin >> b >> l >> e;

        cout << solve(b, l, e) << endl;
    }

    return 0;
}
