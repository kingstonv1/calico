#include <bits/stdc++.h>
using namespace std;


int solve(int length, int jump, string course) {
    if (length <= jump) {
        return -1;
    }

    int low = 0;
    int spcmax = 0;
    int cur_spc = 0;
    jump++;

    for (int i = 0; i < jump; i++) {
        if (course[i] == '-') {
            cur_spc++;
        }

        spcmax = max(cur_spc, spcmax);
    }

    for (int i = jump; i < length; i++) {
        if (course[i] == '-') { cur_spc++; }
        if (course[i - jump] == '-') { cur_spc--; }
        spcmax = max(cur_spc, spcmax);
    }

    return jump - spcmax;
}


int main() {
    int n; cin >> n;

    for (int i = 0; i < n; i++) {
        int length; int jump;
        string course;
        cin >> length >> jump;
        cin >> course;
        cout << solve(length, jump, course) << endl;
    }

    return 0;
}
